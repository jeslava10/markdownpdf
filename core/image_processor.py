#!/usr/bin/env python3
"""
Procesador de imágenes y SVG para el convertidor Markdown a PDF
"""

import os
import re
import urllib.request
import urllib.parse
from pathlib import Path
from typing import Optional, Tuple, Union
from PIL import Image
import requests
from io import BytesIO
import base64
import mimetypes
import logging

logger = logging.getLogger(__name__)

class ImageProcessor:
    """Procesador de imágenes con soporte para redimensionamiento, descarga remota y optimización"""
    
    def __init__(self, max_width: int = 800, max_height: int = 600, quality: int = 85):
        self.max_width = max_width
        self.max_height = max_height
        self.quality = quality
        self.supported_formats = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg'}
        
    def process_image_tag(self, img_tag: str, base_path: Path) -> str:
        """Procesa una etiqueta de imagen y retorna la versión optimizada"""
        try:
            # Extraer atributos de la imagen
            src_match = re.search(r'src=["\']([^"\']+)["\']', img_tag)
            if not src_match:
                return img_tag
                
            src = src_match.group(1)
            alt_match = re.search(r'alt=["\']([^"\']*)["\']', img_tag)
            alt = alt_match.group(1) if alt_match else ""
            
            # Procesar la imagen
            processed_src = self.process_image_src(src, base_path)
            
            # Reconstruir la etiqueta con atributos optimizados
            new_img_tag = self.build_optimized_img_tag(img_tag, processed_src, alt)
            
            return new_img_tag
            
        except Exception as e:
            logger.warning(f"Error procesando imagen {img_tag}: {e}")
            return img_tag
    
    def process_image_src(self, src: str, base_path: Path) -> str:
        """Procesa la fuente de una imagen (local o remota)"""
        # Verificar si es una URL remota
        if self.is_remote_url(src):
            return self.download_and_process_remote_image(src, base_path)
        
        # Procesar imagen local
        return self.process_local_image(src, base_path)
    
    def is_remote_url(self, src: str) -> bool:
        """Verifica si la fuente es una URL remota"""
        return src.startswith(('http://', 'https://', '//'))
    
    def download_and_process_remote_image(self, url: str, base_path: Path) -> str:
        """Descarga y procesa una imagen remota"""
        try:
            # Crear directorio para imágenes descargadas
            images_dir = base_path / "downloaded_images"
            images_dir.mkdir(exist_ok=True)
            
            # Generar nombre de archivo único
            filename = self.generate_filename_from_url(url)
            local_path = images_dir / filename
            
            # Descargar imagen
            logger.info(f"Descargando imagen remota: {url}")
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # Guardar imagen
            with open(local_path, 'wb') as f:
                f.write(response.content)
            
            # Procesar imagen descargada
            processed_path = self.process_local_image(str(local_path), base_path)
            
            return processed_path
            
        except Exception as e:
            logger.error(f"Error descargando imagen {url}: {e}")
            return url  # Retornar URL original si falla
    
    def process_local_image(self, src: str, base_path: Path) -> str:
        """Procesa una imagen local"""
        try:
            # Resolver ruta relativa
            if not os.path.isabs(src):
                image_path = base_path / src
            else:
                image_path = Path(src)
            
            if not image_path.exists():
                logger.warning(f"Imagen no encontrada: {image_path}")
                return src
            
            # Verificar si es SVG
            if image_path.suffix.lower() == '.svg':
                return self.process_svg(image_path, base_path)
            
            # Procesar imagen raster
            return self.process_raster_image(image_path, base_path)
            
        except Exception as e:
            logger.error(f"Error procesando imagen local {src}: {e}")
            return src
    
    def process_svg(self, svg_path: Path, base_path: Path) -> str:
        """Procesa un archivo SVG"""
        try:
            # Crear directorio para SVGs procesados
            processed_dir = base_path / "processed_images"
            processed_dir.mkdir(exist_ok=True)
            
            # Leer contenido SVG
            with open(svg_path, 'r', encoding='utf-8') as f:
                svg_content = f.read()
            
            # Optimizar SVG (remover comentarios, espacios extra, etc.)
            optimized_svg = self.optimize_svg(svg_content)
            
            # Guardar SVG optimizado
            processed_path = processed_dir / f"{svg_path.stem}_optimized.svg"
            with open(processed_path, 'w', encoding='utf-8') as f:
                f.write(optimized_svg)
            
            return str(processed_path.relative_to(base_path))
            
        except Exception as e:
            logger.error(f"Error procesando SVG {svg_path}: {e}")
            return str(svg_path)
    
    def process_raster_image(self, image_path: Path, base_path: Path) -> str:
        """Procesa una imagen raster (redimensionar, optimizar)"""
        try:
            # Crear directorio para imágenes procesadas
            processed_dir = base_path / "processed_images"
            processed_dir.mkdir(exist_ok=True)
            
            # Abrir imagen
            with Image.open(image_path) as img:
                # Convertir a RGB si es necesario
                if img.mode in ('RGBA', 'LA', 'P'):
                    img = img.convert('RGB')
                
                # Redimensionar si es necesario
                new_size = self.calculate_optimal_size(img.size)
                if new_size != img.size:
                    img = img.resize(new_size, Image.Resampling.LANCZOS)
                
                # Guardar imagen optimizada
                processed_path = processed_dir / f"{image_path.stem}_optimized{image_path.suffix}"
                
                # Determinar formato de salida
                if image_path.suffix.lower() in ('.jpg', '.jpeg'):
                    img.save(processed_path, 'JPEG', quality=self.quality, optimize=True)
                elif image_path.suffix.lower() == '.png':
                    img.save(processed_path, 'PNG', optimize=True)
                else:
                    img.save(processed_path, optimize=True)
                
                return str(processed_path.relative_to(base_path))
            
        except Exception as e:
            logger.error(f"Error procesando imagen raster {image_path}: {e}")
            return str(image_path)
    
    def calculate_optimal_size(self, original_size: Tuple[int, int]) -> Tuple[int, int]:
        """Calcula el tamaño óptimo para la imagen"""
        width, height = original_size
        
        # Si la imagen es más pequeña que el máximo, mantener tamaño original
        if width <= self.max_width and height <= self.max_height:
            return original_size
        
        # Calcular proporción
        ratio = min(self.max_width / width, self.max_height / height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        
        return (new_width, new_height)
    
    def optimize_svg(self, svg_content: str) -> str:
        """Optimiza contenido SVG"""
        # Remover comentarios
        svg_content = re.sub(r'<!--.*?-->', '', svg_content, flags=re.DOTALL)
        
        # Remover espacios extra
        svg_content = re.sub(r'\s+', ' ', svg_content)
        
        # Remover espacios al inicio y final
        svg_content = svg_content.strip()
        
        return svg_content
    
    def generate_filename_from_url(self, url: str) -> str:
        """Genera un nombre de archivo único basado en la URL"""
        parsed = urllib.parse.urlparse(url)
        filename = os.path.basename(parsed.path)
        
        if not filename or '.' not in filename:
            # Generar nombre basado en la URL
            filename = f"image_{hash(url) % 10000}"
            # Intentar determinar extensión
            content_type = self.get_content_type_from_url(url)
            if content_type:
                ext = mimetypes.guess_extension(content_type)
                if ext:
                    filename += ext
            else:
                filename += '.jpg'  # Por defecto
        
        return filename
    
    def get_content_type_from_url(self, url: str) -> Optional[str]:
        """Obtiene el tipo de contenido de una URL"""
        try:
            response = requests.head(url, timeout=10)
            return response.headers.get('content-type')
        except:
            return None
    
    def build_optimized_img_tag(self, original_tag: str, new_src: str, alt: str) -> str:
        """Construye una etiqueta de imagen optimizada"""
        # Mantener atributos existentes pero actualizar src y alt
        tag = original_tag
        
        # Actualizar src
        tag = re.sub(r'src=["\'][^"\']*["\']', f'src="{new_src}"', tag)
        
        # Asegurar que tenga alt
        if 'alt=' not in tag:
            tag = tag.replace('>', f' alt="{alt}">')
        
        # Agregar atributos de optimización
        if 'style=' not in tag:
            tag = tag.replace('>', ' style="max-width: 100%; height: auto;">')
        
        return tag
    
    def embed_image_as_base64(self, image_path: Path) -> str:
        """Convierte una imagen a base64 para embebido directo"""
        try:
            with open(image_path, 'rb') as f:
                image_data = f.read()
            
            # Determinar tipo MIME
            mime_type = mimetypes.guess_type(str(image_path))[0]
            if not mime_type:
                mime_type = 'image/jpeg'
            
            # Codificar en base64
            base64_data = base64.b64encode(image_data).decode('utf-8')
            
            return f"data:{mime_type};base64,{base64_data}"
            
        except Exception as e:
            logger.error(f"Error embebiendo imagen {image_path}: {e}")
            return str(image_path)

def process_html_images(html_content: str, base_path: Path, 
                       max_width: int = 800, max_height: int = 600, 
                       quality: int = 85, embed_images: bool = False) -> str:
    """Procesa todas las imágenes en el contenido HTML"""
    processor = ImageProcessor(max_width, max_height, quality)
    
    # Encontrar todas las etiquetas de imagen
    img_pattern = r'<img[^>]+>'
    
    def replace_img(match):
        img_tag = match.group(0)
        return processor.process_image_tag(img_tag, base_path)
    
    # Procesar todas las imágenes
    processed_html = re.sub(img_pattern, replace_img, html_content)
    
    return processed_html 