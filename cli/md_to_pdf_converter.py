#!/usr/bin/env python3
"""
Script para convertir archivos Markdown a PDF con estilos CSS personalizados
Autor: Generado automáticamente
Fecha: 2024
"""

import argparse
import logging
import re
import sys
import glob
import os
from pathlib import Path
from typing import Any, Dict, Optional

import markdown
import yaml
from colorama import Fore, Style, init as colorama_init
import difflib

from core.config_manager import ConfigManager, ConversionConfig
from core.exporter import export_pdf
from core.parser import extract_metadata
from core.renderer import (insert_automatic_toc, markdown_to_html,
                           safe_update_metadata)
from core.validator import MarkdownValidator
from core.image_processor import process_html_images

colorama_init(autoreset=True)

class MarkdownToPDFConverter:
    """Clase principal para convertir archivos Markdown a PDF"""
    
    def __init__(self, config: ConversionConfig, config_manager: Optional[ConfigManager] = None):
        self.config = config
        self.config_manager = config_manager
        self.input_dir = Path(config.input_dir)
        self.output_dir = Path(config.output_dir)
        self.style_file = Path(config.style_file) if config.style_file is not None else None
        
        # Configurar logging
        self._setup_logging()
        
        # Crear directorio de salida si no existe
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Configurar markdown con extensiones completas para soporte total de Markdown Guide
        self.md = markdown.Markdown(extensions=[
            # Sintaxis básica (ya soportada por defecto)
            # - Headings (# ## ###)
            # - Paragraphs
            # - Line breaks
            # - Emphasis (bold, italic)
            # - Links
            # - Images
            # - Escaping characters
            
            # Extensiones para sintaxis extendida
            'markdown.extensions.tables',           # Tablas
            'markdown.extensions.fenced_code',      # Bloques de código con ```
            'markdown.extensions.codehilite',       # Resaltado de sintaxis
            'markdown.extensions.toc',              # Tabla de contenidos
            'markdown.extensions.attr_list',        # Atributos HTML
            'markdown.extensions.def_list',         # Listas de definición
            'markdown.extensions.footnotes',        # Notas al pie
            'markdown.extensions.md_in_html',       # Markdown dentro de HTML
            'markdown.extensions.nl2br',            # Saltos de línea
            'markdown.extensions.sane_lists',       # Listas mejoradas
            'markdown.extensions.smarty',           # Comillas inteligentes
            'markdown.extensions.abbr',             # Abreviaciones
            'markdown.extensions.admonition',       # Advertencias/notas
            'markdown.extensions.legacy_attrs',     # Atributos legacy
            'markdown.extensions.legacy_em',        # Énfasis legacy
            'markdown.extensions.meta',             # Metadatos
            'markdown.extensions.wikilinks',        # Enlaces tipo wiki
        ], extension_configs={
            'codehilite': {
                'css_class': 'highlight',
                'use_pygments': True,
                'noclasses': True,
                'linenums': False,
                'guess_lang': True,
            },
            'toc': {
                'title': 'Tabla de Contenidos',
                'anchorlink': True,
                'permalink': True,
                'baselevel': 1,
            },
            'footnotes': {
                'PLACE_MARKER': '///Footnotes Go Here///',
            },
            'smarty': {
                'smart_angled_quotes': True,
                'smart_quotes': True,
                'smart_dashes': True,
                'smart_ellipses': True,
            },
        })
    
    def _setup_logging(self):
        """Configurar el sistema de logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(sys.stdout),
                logging.FileHandler('conversion.log')
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def _extract_metadata(self, content: str) -> tuple[Dict[str, Any], str]:
        """Extraer metadatos YAML del contenido"""
        metadata = {}
        
        # Buscar YAML front matter
        yaml_pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.search(yaml_pattern, content, re.DOTALL)
        
        if match:
            try:
                yaml_content = match.group(1)
                metadata = yaml.safe_load(yaml_content) or {}
                
                # Remover YAML del contenido
                content = re.sub(yaml_pattern, '', content, count=1)
                
            except yaml.YAMLError as e:
                self.logger.warning(f"Error al parsear YAML: {e}")
        
        return metadata, content
    
    def _get_default_css(self) -> str:
        """Retorna CSS por defecto si no se proporciona archivo de estilos"""
        return f"""
        <style>
        body {{
            font-family: {self.config.font_family};
            line-height: 1.6;
            margin: {self.config.margins};
            color: #333;
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            color: #2c3e50;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
        }}
        
        h1 {{ font-size: 2.2em; border-bottom: 3px solid #3498db; padding-bottom: 0.3em; }}
        h2 {{ font-size: 1.8em; border-bottom: 2px solid #ecf0f1; padding-bottom: 0.2em; }}
        h3 {{ font-size: 1.4em; }}
        h4 {{ font-size: 1.2em; }}
        
        p {{ margin-bottom: 1em; }}
        
        ul, ol {{ margin-bottom: 1em; padding-left: 2em; }}
        
        li {{ margin-bottom: 0.3em; }}
        
        code {{
            background-color: #f8f9fa;
            padding: 0.2em 0.4em;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
        
        pre {{
            background-color: #f8f9fa;
            padding: 1em;
            border-radius: 5px;
            border-left: 4px solid #3498db;
        }}
        
        pre code {{
            background-color: transparent;
            padding: 0;
        }}
        
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }}
        
        th, td {{
            border: 1px solid #ddd;
            padding: 8px 12px;
            text-align: left;
        }}
        
        th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}
        
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        
        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 1em auto;
        }}
        
        blockquote {{
            border-left: 4px solid #3498db;
            margin: 1em 0;
            padding-left: 1em;
            color: #666;
            font-style: italic;
        }}
        
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        hr {{
            border: none;
            border-top: 2px solid #ecf0f1;
            margin: 2em 0;
        }}
        
        @page {{
            margin: {self.config.margins};
            size: {self.config.page_size};
            @bottom-center {{
                content: counter(page);
                font-size: 0.8em;
            }}
        }}
        </style>
        """
    
    def _read_css_file(self) -> str:
        """Lee el archivo CSS proporcionado"""
        if self.style_file and self.style_file.exists():
            try:
                with open(self.style_file, 'r', encoding='utf-8') as f:
                    return f.read()
            except Exception as e:
                self.logger.warning(f"No se pudo leer el archivo CSS {self.style_file}: {e}")
                return self._get_default_css()
        else:
            self.logger.info("No se proporcionó archivo CSS, usando estilos por defecto")
            return self._get_default_css()
    
    def _convert_markdown_to_html(self, markdown_content: str, metadata: Optional[Dict[str, Any]] = None, toc_levels: int = 3, number_headings: bool = False, toc: bool = False, debug_filename: str = "", max_image_width: int = 800, max_image_height: int = 600, image_quality: int = 85, download_remote_images: bool = False, embed_images: bool = False) -> str:
        """Convertir contenido Markdown a HTML con soporte completo"""
        print(f"[DEBUG] _convert_markdown_to_html: toc={toc} archivo={debug_filename}")
        doc_metadata, clean_content = extract_metadata(markdown_content)
        doc_metadata = safe_update_metadata(doc_metadata, metadata)
        html_content = markdown_to_html(clean_content)
        html_content = insert_automatic_toc(html_content, toc_levels=toc_levels, number_headings=number_headings) if toc else html_content
        
        # Procesar imágenes si se solicita
        if download_remote_images or embed_images:
            base_path = Path(self.input_dir)
            html_content = process_html_images(
                html_content, 
                base_path,
                max_width=max_image_width,
                max_height=max_image_height,
                quality=image_quality,
                embed_images=embed_images
            )
        
        css_content = self._read_css_file() if self.style_file and self.style_file.exists() else self._get_default_css()
        
        # Crear HTML completo con soporte para SVG y emojis
        full_html = f"""
        <!DOCTYPE html>
        <html lang="{self.config.language}">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{doc_metadata.get('title', 'Documento Markdown')}</title>
            <style>
                {css_content}
                
                /* Soporte mejorado para SVG */
                svg {{
                    max-width: 100%;
                    height: auto;
                    display: block;
                    margin: 1em auto;
                }}
                
                /* Soporte para emojis */
                @font-face {{
                    font-family: 'EmojiFont';
                    src: local('Apple Color Emoji'),
                         local('Segoe UI Emoji'),
                         local('Noto Color Emoji'),
                         local('Android Emoji'),
                         local('EmojiSymbols');
                    unicode-range: U+1F600-1F64F, U+1F300-1F5FF, U+1F680-1F6FF, U+1F1E0-1F1FF, U+2600-26FF, U+2700-27BF;
                }}
                
                body {{
                    font-family: {self.config.font_family}, 'EmojiFont', sans-serif;
                }}
                
                /* Mejoras para contenido técnico */
                .svg-container {{
                    text-align: center;
                    margin: 1.5em 0;
                    padding: 1em;
                    background-color: #f8f9fa;
                    border-radius: 8px;
                    border: 1px solid #e9ecef;
                }}
                
                .svg-container svg {{
                    margin: 0;
                }}
                
                .emoji {{
                    font-family: 'EmojiFont', sans-serif;
                    font-size: 1.2em;
                    vertical-align: middle;
                }}
                
                /* Mejoras para diagramas SVG */
                .diagram {{
                    background-color: white;
                    border: 2px solid #dee2e6;
                    border-radius: 8px;
                    padding: 1em;
                    margin: 1.5em 0;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
                
                .diagram svg {{
                    margin: 0;
                }}
                
                /* Responsive para SVG */
                @media print {{
                    svg {{
                        page-break-inside: avoid;
                    }}
                    
                    .svg-container {{
                        page-break-inside: avoid;
                    }}
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        return full_html
    
    def _validate_markdown_file(self, file_path: Path) -> bool:
        """Valida que el archivo Markdown tenga contenido"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if not content:
                    self.logger.warning(f"Archivo vacío: {file_path}")
                    return False
                return True
        except Exception as e:
            self.logger.error(f"Error al leer archivo {file_path}: {e}")
            return False
    
    def convert_file(self, markdown_file: Path, toc: bool = False, toc_levels: int = 3, number_headings: bool = False, max_image_width: int = 800, max_image_height: int = 600, image_quality: int = 85, download_remote_images: bool = False, embed_images: bool = False) -> bool:
        """Convierte un archivo Markdown específico a PDF"""
        try:
            # Validar archivo
            if not self._validate_markdown_file(markdown_file):
                return False
            
            # Leer contenido Markdown
            with open(markdown_file, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
            
            # Extraer metadatos
            metadata, markdown_content = extract_metadata(markdown_content)
            
            # Convertir a HTML
            html_content = self._convert_markdown_to_html(
                markdown_content,
                metadata,
                toc_levels=toc_levels,
                number_headings=number_headings,
                toc=toc,
                max_image_width=max_image_width,
                max_image_height=max_image_height,
                image_quality=image_quality,
                download_remote_images=download_remote_images,
                embed_images=embed_images
            )
            
            # Generar nombre del archivo PDF
            pdf_filename = markdown_file.stem + '.pdf'
            pdf_path = self.output_dir / pdf_filename
            
            # Exportar PDF
            style_path = Path(self.style_file or 'style/light.css')
            export_pdf(html_content, pdf_path, markdown_file.parent, style_path)
            
            self.logger.info(f"✅ Convertido exitosamente: {markdown_file.name} -> {pdf_filename}")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Error al convertir {markdown_file.name}: {e}")
            return False
    
    def convert_all_files(self, specific_file: Optional[str] = None, toc: bool = False, toc_levels: int = 3, number_headings: bool = False, max_image_width: int = 800, max_image_height: int = 600, image_quality: int = 85, download_remote_images: bool = False, embed_images: bool = False) -> dict:
        """Convierte todos los archivos Markdown en el directorio de entrada o uno específico"""
        if not self.input_dir.exists():
            self.logger.error(f"El directorio de entrada no existe: {self.input_dir}")
            return {"success": 0, "failed": 0, "total": 0}
        
        if specific_file:
            markdown_files = [self.input_dir / specific_file]
            if not markdown_files[0].exists():
                self.logger.error(f"El archivo especificado no existe: {markdown_files[0]}")
                return {"success": 0, "failed": 1, "total": 1}
        else:
            markdown_files = list(self.input_dir.glob("*.md"))
        
        if not markdown_files:
            self.logger.warning(f"No se encontraron archivos .md en {self.input_dir}")
            return {"success": 0, "failed": 0, "total": 0}
        
        self.logger.info(f"Encontrados {len(markdown_files)} archivos Markdown para convertir")
        
        success_count = 0
        failed_count = 0
        
        for md_file in markdown_files:
            if self.convert_file(md_file, toc=toc, toc_levels=toc_levels, number_headings=number_headings, max_image_width=max_image_width, max_image_height=max_image_height, image_quality=image_quality, download_remote_images=download_remote_images, embed_images=embed_images):
                success_count += 1
            else:
                failed_count += 1
        
        return {
            "success": success_count,
            "failed": failed_count,
            "total": len(markdown_files)
        }

def print_error(msg):
    print(f"{Fore.RED}❌ {msg}{Style.RESET_ALL}")

def print_warning(msg):
    print(f"{Fore.YELLOW}⚠️  {msg}{Style.RESET_ALL}")

def print_success(msg):
    print(f"{Fore.GREEN}✅ {msg}{Style.RESET_ALL}")

def main():
    """Función principal del script"""
    parser = argparse.ArgumentParser(
        description="""
        📝 Convierte archivos Markdown a PDF con estilos CSS profesionales y validación avanzada.
        
        Herramienta ideal para documentación técnica, reportes, presentaciones y contenido académico.
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos prácticos:
  # Convertir todos los archivos Markdown de la carpeta por defecto
  python md_to_pdf_converter.py

  # Convertir todos los archivos de una carpeta específica
  python md_to_pdf_converter.py --input ./conversion --output ./output

  # Convertir un archivo específico
  python md_to_pdf_converter.py --file documento.md

  # Usar un estilo CSS personalizado
  python md_to_pdf_converter.py --style ./style/light.css

  # Validar todos los archivos antes de convertir
  python md_to_pdf_converter.py --validate

  # Validar con información detallada
  python md_to_pdf_converter.py --validate --verbose

  # Listar templates disponibles
  python md_to_pdf_converter.py --list-templates

Solución de problemas:
  - Si tienes errores de validación, usa --validate --verbose para ver detalles.
  - Si no se genera el PDF, revisa el log conversion.log.
  - Para ayuda completa, ejecuta: python md_to_pdf_converter.py --help
        """
    )
    
    parser.add_argument(
        '--input', '-i',
        help='Directorio que contiene los archivos Markdown (.md). Por defecto: ./conversion'
    )
    parser.add_argument(
        '--output', '-o',
        help='Directorio donde se guardarán los archivos PDF generados. Por defecto: ./output'
    )
    parser.add_argument(
        '--style', '-s',
        help='Archivo CSS personalizado para estilizar el PDF (opcional)'
    )
    parser.add_argument(
        '--file', '-f',
        nargs='*',
        help='Uno o varios archivos .md a convertir (puede usar patrones tipo "*.md")'
    )
    parser.add_argument(
        '--template', '-t',
        help='Template predefinido (tecnico, oscuro). Por defecto: tecnico'
    )
    parser.add_argument(
        '--dark-theme',
        action='store_true',
        help='Activar tema oscuro (equivalente a --template oscuro)'
    )
    parser.add_argument(
        '--config', '-c',
        help='Archivo de configuración personalizado (opcional)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Mostrar información detallada durante la conversión'
    )
    parser.add_argument(
        '--validate', '-V',
        action='store_true',
        help='Validar archivos antes de convertir'
    )
    parser.add_argument(
        '--list-templates',
        action='store_true',
        help='Listar templates disponibles'
    )
    parser.add_argument(
        '--theme',
        choices=['light', 'dark', 'auto'],
        default='auto',
        help='Tema visual: light, dark o auto (por defecto: auto/light)'
    )
    parser.add_argument(
        '--pdf',
        action='store_true',
        help='Generar archivo PDF'
    )
    parser.add_argument(
        '--html',
        action='store_true',
        default=False,
        help='Generar archivo HTML además del PDF para previsualización rápida'
    )
    parser.add_argument(
        '--toc-levels',
        type=int,
        default=3,
        help='Niveles máximos de encabezado a incluir en la tabla de contenidos (por defecto: 3, es decir, h1-h3)'
    )
    parser.add_argument(
        '--number-headings',
        action='store_true',
        help='Numerar automáticamente los headings en el documento y la TOC'
    )
    parser.add_argument(
        '--toc',
        action='store_true',
        help='Incluir tabla de contenidos automática (TOC) en el documento'
    )
    parser.add_argument(
        '--max-image-width',
        type=int,
        default=800,
        help='Ancho máximo para redimensionar imágenes automáticamente (por defecto: 800px)'
    )
    parser.add_argument(
        '--max-image-height',
        type=int,
        default=600,
        help='Alto máximo para redimensionar imágenes automáticamente (por defecto: 600px)'
    )
    parser.add_argument(
        '--image-quality',
        type=int,
        default=85,
        help='Calidad de compresión de imágenes (1-100, por defecto: 85)'
    )
    parser.add_argument(
        '--download-remote-images',
        action='store_true',
        help='Descargar y procesar imágenes remotas automáticamente'
    )
    parser.add_argument(
        '--embed-images',
        action='store_true',
        help='Embeber imágenes como base64 en el HTML (aumenta el tamaño del archivo)'
    )
    args = parser.parse_args()

    # Cargar configuración
    try:
        config_manager = ConfigManager(args.config if args.config else "config.yaml")
    except Exception as e:
        print(f"❌ Error al cargar la configuración: {e}")
        print("💡 Sugerencia: Verifica que el archivo config.yaml existe y es válido. Usa --help para más información.")
        sys.exit(1)

    # Listar templates si se solicita
    if args.list_templates:
        templates = config_manager.list_templates()
        print("\n📋 Templates disponibles:")
        for template in templates:
            print(f"   - {template}")
        print("\n💡 Usa --template <nombre> para seleccionar un template al convertir.")
        return

    # Obtener configuración de conversión
    try:
        # Si se especifica --dark-theme, usar template oscuro
        template_name = args.template
        if args.dark_theme:
            template_name = "oscuro"
            if args.template and args.template != "oscuro":
                print("⚠️  Advertencia: --dark-theme sobrescribe --template")
        
        conversion_config = config_manager.get_conversion_config(template_name)
    except Exception as e:
        print(f"❌ Error al cargar la configuración de conversión: {e}")
        print("💡 Sugerencia: Revisa tu archivo config.yaml o el nombre del template.")
        sys.exit(1)

    # Sobrescribir con argumentos de línea de comandos
    if args.input:
        conversion_config.input_dir = args.input
    if args.output:
        conversion_config.output_dir = args.output
    if args.style:
        conversion_config.style_file = args.style
    if args.verbose:
        conversion_config.verbose = True

    # Configurar nivel de logging
    if conversion_config.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Validar archivos si se solicita
    if args.validate:
        print("\n🔍 Iniciando validación avanzada de archivos Markdown...")
        validator = MarkdownValidator(config_manager.get_validation_config())
        validation_results = validator.validate_directory(Path(conversion_config.input_dir))
        validator.print_validation_report(validation_results, verbose=args.verbose)
        summary = validator.get_summary(validation_results)
        if summary['invalid_files'] > 0:
            print(f"\n❌ Se encontraron {summary['invalid_files']} archivos con errores críticos.")
            print("💡 Sugerencia: Corrige los errores antes de convertir. Usa --validate --verbose para más detalles.")
            if not args.verbose:
                print("💡 Usa --verbose para ver detalles completos de cada problema.")
            if not sys.stdin.isatty():
                print("🔄 Continuando con la conversión (modo no interactivo)...")
            else:
                try:
                    response = input("\n¿Deseas continuar con la conversión? (s/N): ").strip().lower()
                    if response not in ['s', 'si', 'sí', 'y', 'yes']:
                        print("❌ Conversión cancelada por el usuario.")
                        sys.exit(0)
                except KeyboardInterrupt:
                    print("\n❌ Conversión cancelada por el usuario.")
                    sys.exit(0)
        elif summary['total_issues'] > 0:
            print(f"\n⚠️  Todos los archivos son válidos, pero hay {summary['total_issues']} advertencias/sugerencias.")
            print("💡 Sugerencia: Usa --verbose para ver todas las recomendaciones de mejora.")
        else:
            print(f"\n✅ ¡Todos los archivos son perfectos! No se encontraron problemas.")

    # Lógica de selección de tema
    if args.theme:
        if args.theme == 'dark':
            conversion_config.style_file = 'style/dark.css'
        else:  # 'light' o 'auto'
            conversion_config.style_file = 'style/light.css'
        # Ignorar --style y --dark-theme si --theme está presente
        args.style = None
        args.dark_theme = False

    # Expansión de archivos si se pasan varios o patrones
    files_to_convert = []
    if args.file:
        for pattern in args.file:
            files_to_convert.extend(glob.glob(os.path.join(conversion_config.input_dir, pattern)))
        files_to_convert = [Path(f) for f in files_to_convert if Path(f).is_file()]
        if not files_to_convert:
            all_md_files = [f.name for f in Path(conversion_config.input_dir).glob('*.md')]
            for pattern in args.file:
                suggestion = difflib.get_close_matches(pattern, all_md_files, n=1)
                if suggestion:
                    print_error(f"No se encontró '{pattern}'. ¿Quizás quisiste decir: '{suggestion[0]}'?")
                else:
                    print_error(f"No se encontró '{pattern}' y no hay archivos similares.")
            if all_md_files:
                print_warning("Archivos disponibles: " + ", ".join(all_md_files))
            else:
                print_warning("No hay archivos .md disponibles en el directorio de entrada.")
            print_warning("Usa --input para cambiar la carpeta de entrada o revisa los patrones.")
            sys.exit(1)

    # Verificar existencia de carpeta de entrada
    if not Path(conversion_config.input_dir).exists():
        print_error(f"El directorio de entrada no existe: {conversion_config.input_dir}")
        print_warning("Crea la carpeta o revisa la ruta con --input")
        sys.exit(1)
    # Verificar existencia de carpeta de salida
    if not Path(conversion_config.output_dir).exists():
        print_error(f"El directorio de salida no existe: {conversion_config.output_dir}")
        print_warning("Crea la carpeta o revisa la ruta con --output")
        sys.exit(1)
    # Verificar permisos de escritura en la carpeta de salida
    if not os.access(conversion_config.output_dir, os.W_OK):
        print_error(f"No tienes permisos de escritura en la carpeta de salida: {conversion_config.output_dir}")
        print_warning("Cambia los permisos o elige otra carpeta con --output")
        sys.exit(1)

    # Crear convertidor
    try:
        converter = MarkdownToPDFConverter(conversion_config, config_manager)
    except Exception as e:
        print(f"❌ Error al inicializar el convertidor: {e}")
        print("💡 Sugerencia: Revisa la configuración y los permisos de los directorios de entrada/salida.")
        sys.exit(1)

    # Ejecutar conversión
    print("\n🚀 Iniciando conversión de Markdown a PDF...")
    print(f"📁 Entrada: {conversion_config.input_dir}")
    print(f"📁 Salida: {conversion_config.output_dir}")
    if conversion_config.style_file:
        print(f"🎨 Estilos: {conversion_config.style_file}")
    if args.file:
        print(f"📄 Archivos específicos: {', '.join([str(f) for f in files_to_convert])}")
    if args.template:
        print(f"📋 Template: {args.template}")
    print("-" * 50)

    try:
        if files_to_convert:
            results = {'success': 0, 'failed': 0, 'total': len(files_to_convert)}
            for md_file in files_to_convert:
                pdf_filename = md_file.stem + '.pdf'
                html_filename = md_file.stem + '.html'
                pdf_path = Path(conversion_config.output_dir) / pdf_filename
                html_path = Path(conversion_config.output_dir) / html_filename
                # PDF: solo aquí se inserta la TOC si se solicita
                if args.pdf:
                    success = converter.convert_file(
                        md_file,
                        toc=args.toc,
                        toc_levels=args.toc_levels,
                        number_headings=args.number_headings,
                        max_image_width=args.max_image_width,
                        max_image_height=args.max_image_height,
                        image_quality=args.image_quality,
                        download_remote_images=args.download_remote_images,
                        embed_images=args.embed_images
                    )
                    if success:
                        results['success'] += 1
                    else:
                        results['failed'] += 1
                    results['total'] += 1
                # HTML: nunca insertar TOC
                if args.html:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        markdown_content = f.read()
                    html_content = converter._convert_markdown_to_html(
                        markdown_content,
                        metadata=None,
                        toc=False,  # Nunca TOC en HTML
                        toc_levels=args.toc_levels,
                        number_headings=args.number_headings,
                        debug_filename=md_file.name,
                        max_image_width=args.max_image_width,
                        max_image_height=args.max_image_height,
                        image_quality=args.image_quality,
                        download_remote_images=args.download_remote_images,
                        embed_images=args.embed_images
                    )
                    with open(html_path, 'w', encoding='utf-8') as f:
                        f.write(html_content)
                    print_success(f"HTML generado: {md_file} -> {html_path}")
        else:
            results = converter.convert_all_files(toc=args.toc, toc_levels=args.toc_levels, number_headings=args.number_headings, max_image_width=args.max_image_width, max_image_height=args.max_image_height, image_quality=args.image_quality, download_remote_images=args.download_remote_images, embed_images=args.embed_images)
    except Exception as e:
        print_error(f"Error durante la conversión: {e}")
        print_warning("Revisa el log conversion.log para más detalles.")
        print_warning("Sugerencia: Usa --validate para verificar la calidad de tus documentos o --verbose para más detalles.")
        sys.exit(1)

    print("-" * 50)
    print("📊 Resumen de conversión:")
    print(f"   Total de archivos: {results['total']}")
    print(f"   ✅ Exitosos: {results['success']}")
    print(f"   ❌ Fallidos: {results['failed']}")

    if results['failed'] > 0:
        print("\n❌ Algunos archivos no se pudieron convertir.")
        print("💡 Sugerencia: Revisa el log conversion.log o ejecuta --validate --verbose para identificar problemas.")
        sys.exit(1)
    else:
        print("\n🎉 ¡Conversión completada exitosamente!")
        if results['total'] > 0:
            print("\n💡 Consejos:")
            print("   - Usa --validate para verificar la calidad de tus documentos")
            print("   - Agrega metadatos YAML a tus archivos para mejores resultados")
            print("   - Personaliza los estilos con --style o --template")
            print("   - Consulta el README para más opciones y ejemplos")
        sys.exit(0)


if __name__ == "__main__":
    main() 