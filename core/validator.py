#!/usr/bin/env python3
"""
Validador avanzado de documentos Markdown con mensajes claros y sugerencias
"""

import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml


@dataclass
class ValidationIssue:
    """Problema encontrado durante la validación"""
    type: str
    message: str
    line: Optional[int] = None
    file: Optional[str] = None
    severity: str = "warning"
    code: str = ""
    suggestion: str = ""
    context: str = ""


@dataclass
class ValidationResult:
    """Resultado de la validación"""
    valid: bool
    issues: List[ValidationIssue]
    file_path: str
    file_size: int
    line_count: int
    heading_count: int = 0
    link_count: int = 0
    image_count: int = 0
    metadata_present: bool = False


class MarkdownValidator:
    """Validador avanzado de documentos Markdown con mensajes claros"""
    
    def __init__(self, config):
        self.config = config
        self.image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.bmp', '.tiff'}
        self.video_extensions = {'.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm'}
        
        # Códigos de error con mensajes claros
        self.error_codes = {
            'FILE_NOT_FOUND': 'E001',
            'FILE_TOO_LARGE': 'E002', 
            'EMPTY_FILE': 'E003',
            'BROKEN_LINK': 'E004',
            'MISSING_IMAGE': 'E005',
            'UNSUPPORTED_FORMAT': 'E006',
            'INVALID_METADATA': 'E007',
            'NO_TITLE': 'E008',
            'LINE_TOO_LONG': 'E009',
            'TAB_CHARACTERS': 'E010',
            'INVALID_DATE': 'E011',
            'MISSING_METADATA': 'E012',
            'INVALID_YAML': 'E013',
            'NO_HEADINGS': 'E014',
            'INCONSISTENT_HEADINGS': 'E015',
            'LARGE_IMAGE': 'E016',
            'UNSAFE_LINK': 'E017',
            'DUPLICATE_HEADINGS': 'E018',
            'MISSING_ALT_TEXT': 'E019',
            'INVALID_CHARACTERS': 'E020',
            'TOO_MANY_EMOJIS': 'E021',
            'EMOJI_IN_TITLE': 'E022',
            'TITLE_CHARS': 'E023',
            'LIST_NO_SPACE': 'E024',
            'NUMBERED_LIST_NO_SPACE': 'E025'
        }
    
    def validate_file(self, file_path: Path) -> ValidationResult:
        """Validar un archivo Markdown con mensajes claros y sugerencias"""
        issues = []
        
        try:
            # Verificar que el archivo existe
            if not file_path.exists():
                issues.append(ValidationIssue(
                    type="file_not_found",
                    message=f"❌ El archivo no existe: {file_path.name}",
                    code=self.error_codes['FILE_NOT_FOUND'],
                    suggestion="Verifica que el archivo existe en la ruta especificada",
                    severity="error"
                ))
                return ValidationResult(False, issues, str(file_path), 0, 0)
            
            # Verificar tamaño del archivo
            file_size = file_path.stat().st_size
            max_size = self.config.max_file_size_mb * 1024 * 1024
            
            if file_size > max_size:
                issues.append(ValidationIssue(
                    type="file_too_large",
                    message=f"⚠️  El archivo es muy grande: {file_size / 1024 / 1024:.2f}MB (máximo {self.config.max_file_size_mb}MB)",
                    code=self.error_codes['FILE_TOO_LARGE'],
                    suggestion="Considera dividir el documento en archivos más pequeños",
                    severity="warning"
                ))
            
            # Leer contenido del archivo
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            line_count = len(content.splitlines())
            
            # Verificar archivo vacío
            if self.config.check_empty_files and not content.strip():
                issues.append(ValidationIssue(
                    type="empty_file",
                    message="❌ El archivo está completamente vacío",
                    code=self.error_codes['EMPTY_FILE'],
                    suggestion="Agrega contenido al archivo o elimínalo si no es necesario",
                    severity="error"
                ))
            
            # Contar elementos del documento
            heading_count = len(re.findall(r'^#{1,6}\s+', content, re.MULTILINE))
            link_count = len(re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content))
            image_count = len(re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content))
            metadata_present = bool(re.search(r'^---\s*\n', content, re.MULTILINE))
            
            # Validar contenido
            content_issues = self._validate_content(content, file_path)
            issues.extend(content_issues)
            
            # Verificar enlaces rotos
            if self.config.check_broken_links:
                link_issues = self._validate_links(content, file_path)
                issues.extend(link_issues)
            
            # Verificar imágenes faltantes
            if self.config.check_missing_images:
                image_issues = self._validate_images(content, file_path)
                issues.extend(image_issues)
            
            # Verificar metadatos YAML
            metadata_issues = self._validate_metadata(content)
            issues.extend(metadata_issues)
            
            # Validaciones adicionales
            additional_issues = self._validate_additional(content, file_path)
            issues.extend(additional_issues)
            
            # Determinar si el archivo es válido
            valid = not any(issue.severity == "error" for issue in issues)
            
            return ValidationResult(
                valid, issues, str(file_path), file_size, line_count,
                heading_count, link_count, image_count, metadata_present
            )
            
        except Exception as e:
            issues.append(ValidationIssue(
                type="validation_error",
                message=f"❌ Error inesperado durante la validación: {str(e)}",
                code="E999",
                suggestion="Verifica que el archivo no esté corrupto y sea un Markdown válido",
                severity="error"
            ))
            return ValidationResult(False, issues, str(file_path), 0, 0)
    
    def _validate_content(self, content: str, file_path: Path) -> List[ValidationIssue]:
        """Validar contenido del archivo con mensajes claros"""
        issues = []
        
        lines = content.splitlines()
        
        # Verificar si hay headings
        headings = re.findall(r'^#{1,6}\s+', content, re.MULTILINE)
        if not headings:
            issues.append(ValidationIssue(
                type="no_headings",
                message="⚠️  No se encontraron headings (títulos) en el documento",
                code=self.error_codes['NO_HEADINGS'],
                suggestion="Agrega títulos usando # para H1, ## para H2, etc.",
                severity="warning"
            ))
        else:
            # Verificar estructura de headings
            heading_structure = self._analyze_heading_structure(content)
            if heading_structure['inconsistent']:
                issues.append(ValidationIssue(
                    type="inconsistent_headings",
                    message="⚠️  Estructura de headings inconsistente detectada",
                    code=self.error_codes['INCONSISTENT_HEADINGS'],
                    suggestion="Usa una jerarquía consistente: H1 → H2 → H3, sin saltar niveles",
                    context=f"Headings encontrados: {heading_structure['summary']}",
                    severity="warning"
                ))
            
            # Verificar headings duplicados
            duplicate_headings = self._find_duplicate_headings(content)
            for heading, line_numbers in duplicate_headings.items():
                issues.append(ValidationIssue(
                    type="duplicate_headings",
                    message=f"⚠️  Heading duplicado: '{heading}'",
                    code=self.error_codes['DUPLICATE_HEADINGS'],
                    suggestion="Considera usar headings únicos o agregar sufijos para diferenciarlos",
                    context=f"Aparece en líneas: {', '.join(map(str, line_numbers))}",
                    severity="warning"
                ))
        
        for i, line in enumerate(lines, 1):
            # Verificar líneas muy largas
            if len(line) > 120:
                issues.append(ValidationIssue(
                    type="line_too_long",
                    message=f"📏 Línea {i} es muy larga ({len(line)} caracteres)",
                    line=i,
                    code=self.error_codes['LINE_TOO_LONG'],
                    suggestion="Considera dividir la línea para mejor legibilidad",
                    context=f"Línea: {line[:50]}...",
                    severity="warning"
                ))
            
            # Verificar caracteres especiales problemáticos
            if '\t' in line:
                issues.append(ValidationIssue(
                    type="tab_characters",
                    message=f"🔤 Línea {i} contiene caracteres tab",
                    line=i,
                    code=self.error_codes['TAB_CHARACTERS'],
                    suggestion="Reemplaza los tabs con espacios para mejor compatibilidad",
                    severity="warning"
                ))
            
            # Verificar caracteres inválidos
            invalid_chars = self._find_invalid_characters(line)
            if invalid_chars:
                issues.append(ValidationIssue(
                    type="invalid_characters",
                    message=f"🔤 Línea {i} contiene caracteres potencialmente problemáticos",
                    line=i,
                    code=self.error_codes['INVALID_CHARACTERS'],
                    suggestion="Revisa y corrige los caracteres especiales",
                    context=f"Caracteres: {invalid_chars}",
                    severity="warning"
                ))
        
        return issues
    
    def _validate_links(self, content: str, file_path: Path) -> List[ValidationIssue]:
        """Validar enlaces con mensajes claros"""
        issues = []
        
        # Patrón para enlaces Markdown
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        
        for match in re.finditer(link_pattern, content):
            link_text = match.group(1)
            link_url = match.group(2)
            
            # Verificar enlaces locales
            if not link_url.startswith(('http://', 'https://', 'mailto:', '#')):
                local_path = file_path.parent / link_url
                
                if not local_path.exists():
                    issues.append(ValidationIssue(
                        type="broken_link",
                        message=f"🔗 Enlace roto: '{link_text}' → {link_url}",
                        code=self.error_codes['BROKEN_LINK'],
                        suggestion="Verifica que el archivo referenciado existe en la ruta correcta",
                        severity="error"
                    ))
            
            # Verificar enlaces potencialmente inseguros
            elif link_url.startswith('http://'):
                issues.append(ValidationIssue(
                    type="unsafe_link",
                    message=f"🔒 Enlace HTTP (no seguro): '{link_text}'",
                    code=self.error_codes['UNSAFE_LINK'],
                    suggestion="Considera usar HTTPS para mayor seguridad",
                    severity="warning"
                ))
        
        return issues
    
    def _validate_images(self, content: str, file_path: Path) -> List[ValidationIssue]:
        """Validar imágenes y archivos multimedia"""
        issues = []
        
        # Buscar imágenes en Markdown
        image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        images = re.findall(image_pattern, content)
        
        for alt_text, image_path in images:
            # Validar ruta de imagen
            if image_path.startswith('http'):
                # URL externa - verificar formato
                if not any(ext in image_path.lower() for ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp']):
                    issues.append(ValidationIssue(
                        type="WARNING",
                        code="IMG_FORMAT",
                        message=f"Formato de imagen no estándar: {image_path}",
                        suggestion="Usar formatos estándar: PNG, JPG, SVG, GIF, WebP",
                        line=self.find_line_number(content, image_path)
                    ))
            else:
                # Ruta local
                image_file = file_path.parent / image_path
                if not image_file.exists():
                    issues.append(ValidationIssue(
                        type="ERROR",
                        code="IMG_MISSING",
                        message=f"Imagen no encontrada: {image_path}",
                        suggestion=f"Verificar que el archivo existe en: {image_file}",
                        line=self.find_line_number(content, image_path)
                    ))
                else:
                    # Validar formato de archivo
                    file_extension = image_file.suffix.lower()
                    if file_extension not in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp']:
                        issues.append(ValidationIssue(
                            type="WARNING",
                            code="IMG_FORMAT",
                            message=f"Formato de imagen no estándar: {file_extension}",
                            suggestion="Usar formatos estándar: PNG, JPG, SVG, GIF, WebP",
                            line=self.find_line_number(content, image_path)
                        ))
                    
                    # Validaciones específicas para SVG
                    if file_extension == '.svg':
                        svg_issues = self._validate_svg_file(image_file)
                        issues.extend(svg_issues)
                    
                    # Verificar tamaño de archivo
                    file_size = image_file.stat().st_size
                    if file_size > 5 * 1024 * 1024:  # 5MB
                        issues.append(ValidationIssue(
                            type="WARNING",
                            code="IMG_SIZE",
                            message=f"Imagen muy grande: {image_path} ({file_size / 1024 / 1024:.1f}MB)",
                            suggestion="Optimizar imagen para reducir tamaño",
                            line=self.find_line_number(content, image_path)
                        ))
        
        return issues
    
    def _validate_svg_file(self, svg_file: Path) -> List[ValidationIssue]:
        """Validar archivo SVG específicamente"""
        issues = []
        
        try:
            with open(svg_file, 'r', encoding='utf-8') as f:
                svg_content = f.read()
            
            # Verificar que es un SVG válido
            if not svg_content.strip().startswith('<svg'):
                issues.append(ValidationIssue(
                    type="ERROR",
                    code="SVG_INVALID",
                    message=f"Archivo SVG inválido: {svg_file.name}",
                    suggestion="Verificar que el archivo contiene código SVG válido",
                    line=1
                ))
                return issues
            
            # Verificar elementos básicos
            if '<svg' not in svg_content:
                issues.append(ValidationIssue(
                    type="ERROR",
                    code="SVG_MISSING_ROOT",
                    message=f"Falta elemento raíz <svg> en: {svg_file.name}",
                    suggestion="Asegurar que el archivo tiene un elemento <svg> válido",
                    line=1
                ))
            
            # Verificar viewBox (importante para escalado)
            if 'viewBox=' not in svg_content and 'width=' not in svg_content:
                issues.append(ValidationIssue(
                    type="WARNING",
                    code="SVG_NO_VIEWBOX",
                    message=f"SVG sin viewBox o dimensiones: {svg_file.name}",
                    suggestion="Añadir viewBox para mejor escalado en PDF",
                    line=1
                ))
            
            # Verificar si es muy grande
            if len(svg_content) > 100000:  # 100KB
                issues.append(ValidationIssue(
                    type="WARNING",
                    code="SVG_SIZE",
                    message=f"SVG muy grande: {svg_file.name} ({len(svg_content) / 1024:.1f}KB)",
                    suggestion="Optimizar SVG para mejor rendimiento",
                    line=1
                ))
                
        except Exception as e:
            issues.append(ValidationIssue(
                type="ERROR",
                code="SVG_READ_ERROR",
                message=f"Error al leer SVG: {svg_file.name}",
                suggestion=f"Verificar que el archivo es legible: {str(e)}",
                line=1
            ))
        
        return issues
    
    def _validate_metadata(self, content: str) -> List[ValidationIssue]:
        """Validar metadatos YAML con mensajes claros"""
        issues = []
        
        # Verificar si hay YAML front matter
        yaml_pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.search(yaml_pattern, content, re.DOTALL)
        
        if match:
            yaml_content = match.group(1)
            
            try:
                # Intentar parsear YAML
                metadata = yaml.safe_load(yaml_content)
                if metadata is None:
                    metadata = {}
            except yaml.YAMLError as e:
                issues.append(ValidationIssue(
                    type="invalid_yaml",
                    message=f"📋 Error en formato YAML: {str(e)}",
                    code=self.error_codes['INVALID_YAML'],
                    suggestion="Verifica la sintaxis YAML en los metadatos",
                    severity="error"
                ))
                return issues
            
            # Validar campos recomendados
            recommended_fields = ['title', 'author', 'date', 'description']
            for field in recommended_fields:
                if field not in metadata:
                    issues.append(ValidationIssue(
                        type="missing_metadata",
                        message=f"📋 Campo de metadatos recomendado faltante: {field}",
                        code=self.error_codes['MISSING_METADATA'],
                        suggestion=f"Agrega el campo '{field}' a los metadatos para mejor documentación",
                        severity="info"
                    ))
            
            # Validar formato de fecha
            if 'date' in metadata:
                date_value = metadata['date']
                if isinstance(date_value, str):
                    try:
                        datetime.strptime(date_value, '%Y-%m-%d')
                    except ValueError:
                        issues.append(ValidationIssue(
                            type="invalid_date_format",
                            message=f"📅 Formato de fecha inválido: {date_value}",
                            code=self.error_codes['INVALID_DATE'],
                            suggestion="Usa el formato YYYY-MM-DD (ejemplo: 2024-12-19)",
                            severity="warning"
                        ))
        else:
            issues.append(ValidationIssue(
                type="no_metadata",
                message="📋 No se encontraron metadatos YAML",
                code="I001",
                suggestion="Considera agregar metadatos para mejor documentación del archivo",
                severity="info"
            ))
        
        return issues
    
    def _validate_additional(self, content: str, file_path: Path) -> List[ValidationIssue]:
        """Validaciones adicionales específicas"""
        issues = []
        
        # Validar emojis
        emoji_issues = self._validate_emojis(content)
        issues.extend(emoji_issues)
        
        # Validar caracteres especiales en títulos
        title_issues = self._validate_title_characters(content)
        issues.extend(title_issues)
        
        # Validar estructura de listas
        list_issues = self._validate_list_structure(content)
        issues.extend(list_issues)
        
        return issues
    
    def _validate_emojis(self, content: str) -> List[ValidationIssue]:
        """Validar uso de emojis"""
        issues = []
        
        # Patrón para detectar emojis Unicode
        emoji_pattern = r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\U00002600-\U000027BF]'
        emojis = re.findall(emoji_pattern, content)
        
        if emojis:
            # Verificar si hay demasiados emojis
            if len(emojis) > 20:
                issues.append(ValidationIssue(
                    type="too_many_emojis",
                    message=f"🎭 Demasiados emojis encontrados ({len(emojis)})",
                    code=self.error_codes.get('TOO_MANY_EMOJIS', 'EMOJI_OVERUSE'),
                    suggestion="Considera reducir el uso de emojis para un tono más profesional",
                    severity="warning"
                ))
            
            # Verificar emojis en títulos (puede ser problemático)
            lines = content.split('\n')
            for i, line in enumerate(lines, 1):
                if line.strip().startswith('#') and re.search(emoji_pattern, line):
                    issues.append(ValidationIssue(
                        type="emoji_in_title",
                        message=f"📝 Emoji encontrado en título (línea {i})",
                        line=i,
                        code=self.error_codes.get('EMOJI_IN_TITLE', 'EMOJI_TITLE'),
                        suggestion="Los emojis en títulos pueden causar problemas en algunos sistemas",
                        severity="info"
                    ))
        
        return issues
    
    def _validate_title_characters(self, content: str) -> List[ValidationIssue]:
        """Validar caracteres especiales en títulos"""
        issues = []
        
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if line.strip().startswith('#'):
                # Verificar caracteres problemáticos en títulos
                problematic_chars = ['<', '>', '&', '"', "'", '|', '\\', '/', ':', '*', '?']
                found_chars = [char for char in problematic_chars if char in line]
                
                if found_chars:
                    issues.append(ValidationIssue(
                        type="problematic_title_chars",
                        message=f"🔤 Caracteres problemáticos en título (línea {i}): {', '.join(found_chars)}",
                        line=i,
                        code=self.error_codes.get('PROBLEMATIC_TITLE_CHARS', 'TITLE_CHARS'),
                        suggestion="Evita caracteres especiales en títulos para mejor compatibilidad",
                        severity="warning"
                    ))
        
        return issues
    
    def _validate_list_structure(self, content: str) -> List[ValidationIssue]:
        """Validar estructura de listas"""
        issues = []
        
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            
            # Verificar listas sin espacio después del marcador
            if re.match(r'^[-*+]\S', stripped):
                issues.append(ValidationIssue(
                    type="list_no_space",
                    message=f"📋 Lista sin espacio después del marcador (línea {i})",
                    line=i,
                    code=self.error_codes.get('LIST_NO_SPACE', 'LIST_FORMAT'),
                    suggestion="Añade un espacio después del marcador de lista: '- ' en lugar de '-'",
                    severity="warning"
                ))
            
            # Verificar listas numeradas inconsistentes
            if re.match(r'^\d+\.\S', stripped):
                issues.append(ValidationIssue(
                    type="numbered_list_no_space",
                    message=f"📋 Lista numerada sin espacio después del punto (línea {i})",
                    line=i,
                    code=self.error_codes.get('NUMBERED_LIST_NO_SPACE', 'LIST_FORMAT'),
                    suggestion="Añade un espacio después del punto: '1. ' en lugar de '1.'",
                    severity="warning"
                ))
        
        return issues
    
    def _analyze_heading_structure(self, content: str) -> Dict[str, Any]:
        """Analizar la estructura de headings"""
        lines = content.splitlines()
        heading_levels = []
        current_level = 0
        
        for line in lines:
            match = re.match(r'^(#{1,6})\s+', line)
            if match:
                level = len(match.group(1))
                heading_levels.append(level)
                
                # Verificar saltos de nivel
                if level > current_level + 1:
                    return {
                        'inconsistent': True,
                        'summary': f"H{current_level} → H{level} (salto de nivel)"
                    }
                current_level = level
        
        return {
            'inconsistent': False,
            'summary': f"Total: {len(heading_levels)} headings"
        }
    
    def _find_duplicate_headings(self, content: str) -> Dict[str, List[int]]:
        """Encontrar headings duplicados"""
        lines = content.splitlines()
        headings = {}
        
        for i, line in enumerate(lines, 1):
            match = re.match(r'^#{1,6}\s+(.+)$', line)
            if match:
                heading_text = match.group(1).strip()
                if heading_text in headings:
                    headings[heading_text].append(i)
                else:
                    headings[heading_text] = [i]
        
        return {k: v for k, v in headings.items() if len(v) > 1}
    
    def _find_invalid_characters(self, line: str) -> str:
        """Encontrar caracteres potencialmente problemáticos"""
        invalid_chars = []
        for char in line:
            if ord(char) > 127 and char not in 'áéíóúñüÁÉÍÓÚÑÜ':
                invalid_chars.append(char)
        return ''.join(set(invalid_chars))
    
    def validate_directory(self, directory: Path) -> Dict[str, ValidationResult]:
        """Validar todos los archivos Markdown en un directorio"""
        results = {}
        
        if not directory.exists():
            return results
        
        for file_path in directory.glob("*.md"):
            results[str(file_path)] = self.validate_file(file_path)
        
        return results
    
    def get_summary(self, results: Dict[str, ValidationResult]) -> Dict[str, Any]:
        """Obtener resumen detallado de validación"""
        total_files = len(results)
        valid_files = sum(1 for r in results.values() if r.valid)
        total_issues = sum(len(r.issues) for r in results.values())
        
        # Estadísticas por tipo de problema
        issues_by_type = {}
        issues_by_severity = {'error': 0, 'warning': 0, 'info': 0}
        
        for result in results.values():
            for issue in result.issues:
                if issue.type not in issues_by_type:
                    issues_by_type[issue.type] = 0
                issues_by_type[issue.type] += 1
                issues_by_severity[issue.severity] += 1
        
        # Estadísticas del contenido
        total_headings = sum(r.heading_count for r in results.values())
        total_links = sum(r.link_count for r in results.values())
        total_images = sum(r.image_count for r in results.values())
        files_with_metadata = sum(1 for r in results.values() if r.metadata_present)
        
        return {
            'total_files': total_files,
            'valid_files': valid_files,
            'invalid_files': total_files - valid_files,
            'total_issues': total_issues,
            'issues_by_type': issues_by_type,
            'issues_by_severity': issues_by_severity,
            'content_stats': {
                'total_headings': total_headings,
                'total_links': total_links,
                'total_images': total_images,
                'files_with_metadata': files_with_metadata
            }
        }
    
    def print_validation_report(self, results: Dict[str, ValidationResult], verbose: bool = False):
        """Imprimir reporte de validación con formato claro"""
        summary = self.get_summary(results)
        
        print("\n" + "="*60)
        print("📋 REPORTE DE VALIDACIÓN DE MARKDOWN")
        print("="*60)
        
        # Resumen general
        print(f"\n📊 RESUMEN GENERAL:")
        print(f"   📄 Archivos analizados: {summary['total_files']}")
        print(f"   ✅ Archivos válidos: {summary['valid_files']}")
        print(f"   ❌ Archivos con errores: {summary['invalid_files']}")
        print(f"   ⚠️  Total de problemas: {summary['total_issues']}")
        
        # Estadísticas de contenido
        stats = summary['content_stats']
        print(f"\n📈 ESTADÍSTICAS DE CONTENIDO:")
        print(f"   📝 Total de headings: {stats['total_headings']}")
        print(f"   🔗 Total de enlaces: {stats['total_links']}")
        print(f"   🖼️  Total de imágenes: {stats['total_images']}")
        print(f"   📋 Archivos con metadatos: {stats['files_with_metadata']}")
        
        # Problemas por severidad
        severity = summary['issues_by_severity']
        if severity['error'] > 0:
            print(f"\n❌ ERRORES CRÍTICOS: {severity['error']}")
        if severity['warning'] > 0:
            print(f"⚠️  ADVERTENCIAS: {severity['warning']}")
        if severity['info'] > 0:
            print(f"ℹ️  SUGERENCIAS: {severity['info']}")
        
        # Detalles por archivo
        if verbose:
            print(f"\n📄 DETALLES POR ARCHIVO:")
            for file_path, result in results.items():
                file_name = Path(file_path).name
                status = "✅ VÁLIDO" if result.valid else "❌ CON PROBLEMAS"
                print(f"\n   {file_name} - {status}")
                
                if result.issues:
                    for issue in result.issues:
                        severity_icon = {
                            'error': '❌',
                            'warning': '⚠️',
                            'info': 'ℹ️'
                        }.get(issue.severity, '❓')
                        
                        print(f"      {severity_icon} {issue.message}")
                        if issue.suggestion:
                            print(f"         💡 {issue.suggestion}")
                        if issue.context:
                            print(f"         📝 {issue.context}")
                        if issue.line:
                            print(f"         📍 Línea: {issue.line}")
        
        # Recomendaciones
        print(f"\n💡 RECOMENDACIONES:")
        if summary['invalid_files'] > 0:
            print("   🔧 Corrige los errores críticos antes de convertir")
        if severity['warning'] > 0:
            print("   📝 Revisa las advertencias para mejorar la calidad")
        if stats['files_with_metadata'] < summary['total_files']:
            print("   📋 Considera agregar metadatos a todos los archivos")
        if stats['total_headings'] == 0:
            print("   📝 Agrega headings para mejor estructura del documento")
        
        print("\n" + "="*60)
    
    def find_line_number(self, content: str, search: str) -> int:
        """Devuelve el número de línea donde aparece el texto buscado, o -1 si no se encuentra."""
        for i, line in enumerate(content.splitlines(), 1):
            if search in line:
                return i
        return -1 