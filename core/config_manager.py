#!/usr/bin/env python3
"""
Gestor de configuración para el conversor de Markdown a PDF
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

import yaml


@dataclass
class ConversionConfig:
    """Configuración para la conversión de documentos"""
    input_dir: str
    output_dir: str
    style_file: Optional[str]
    page_size: str
    margins: str
    font_family: str
    language: str
    verbose: bool


@dataclass
class ValidationConfig:
    """Configuración para la validación de documentos"""
    check_broken_links: bool
    check_missing_images: bool
    check_empty_files: bool
    max_file_size_mb: int


@dataclass
class MetadataConfig:
    """Configuración para metadatos por defecto"""
    default_author: str
    default_title: str
    default_date_format: str
    include_creation_date: bool
    include_modification_date: bool


class ConfigManager:
    """Gestor de configuración del proyecto"""
    
    def __init__(self, config_file: str = "config.yaml"):
        self.config_file = Path(config_file)
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Cargar configuración desde archivo YAML"""
        if not self.config_file.exists():
            return self._get_default_config()
        
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Error al cargar configuración: {e}")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Configuración por defecto"""
        return {
            'default': {
                'input_dir': './conversion',
                'output_dir': './output',
                'style_file': './style/bootstrap.css',
                'page_size': 'A4',
                'margins': '2cm',
                'font_family': 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif',
                'language': 'es',
                'verbose': False
            },
            'templates': {
                'report': {
                    'style_file': './style/report.css',
                    'page_size': 'A4',
                    'margins': '2.5cm',
                    'font_family': 'Times New Roman, serif',
                    'language': 'es'
                },
                'presentation': {
                    'style_file': './style/presentation.css',
                    'page_size': 'A4',
                    'margins': '1.5cm',
                    'font_family': 'Arial, sans-serif',
                    'language': 'es'
                }
            },
            'logging': {
                'level': 'INFO',
                'file': 'conversion.log',
                'format': '%(asctime)s - %(levelname)s - %(message)s'
            },
            'validation': {
                'check_broken_links': True,
                'check_missing_images': True,
                'check_empty_files': True,
                'max_file_size_mb': 10
            },
            'metadata': {
                'default_author': 'Usuario',
                'default_title': 'Documento Markdown',
                'default_date_format': '%Y-%m-%d',
                'include_creation_date': True,
                'include_modification_date': True
            }
        }
    
    def get_conversion_config(self, template: Optional[str] = None) -> ConversionConfig:
        """Obtener configuración de conversión"""
        if template and template in self.config.get('templates', {}):
            config = self.config['templates'][template]
        else:
            config = self.config.get('default', {})
        
        return ConversionConfig(
            input_dir=config.get('input_dir', './conversion'),
            output_dir=config.get('output_dir', './output'),
            style_file=config.get('style_file'),
            page_size=config.get('page_size', 'A4'),
            margins=config.get('margins', '2cm'),
            font_family=config.get('font_family', 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif'),
            language=config.get('language', 'es'),
            verbose=config.get('verbose', False)
        )
    
    def get_validation_config(self) -> ValidationConfig:
        """Obtener configuración de validación"""
        validation = self.config.get('validation', {})
        return ValidationConfig(
            check_broken_links=validation.get('check_broken_links', True),
            check_missing_images=validation.get('check_missing_images', True),
            check_empty_files=validation.get('check_empty_files', True),
            max_file_size_mb=validation.get('max_file_size_mb', 10)
        )
    
    def get_metadata_config(self) -> MetadataConfig:
        """Obtener configuración de metadatos"""
        metadata = self.config.get('metadata', {})
        return MetadataConfig(
            default_author=metadata.get('default_author', 'Usuario'),
            default_title=metadata.get('default_title', 'Documento Markdown'),
            default_date_format=metadata.get('default_date_format', '%Y-%m-%d'),
            include_creation_date=metadata.get('include_creation_date', True),
            include_modification_date=metadata.get('include_modification_date', True)
        )
    
    def get_logging_config(self) -> Dict[str, Any]:
        """Obtener configuración de logging"""
        return self.config.get('logging', {
            'level': 'INFO',
            'file': 'conversion.log',
            'format': '%(asctime)s - %(levelname)s - %(message)s'
        })
    
    def list_templates(self) -> list:
        """Listar templates disponibles"""
        return list(self.config.get('templates', {}).keys())
    
    def create_template(self, name: str, config: Dict[str, Any]) -> bool:
        """Crear nuevo template"""
        try:
            if 'templates' not in self.config:
                self.config['templates'] = {}
            
            self.config['templates'][name] = config
            self._save_config()
            return True
        except Exception as e:
            print(f"Error al crear template: {e}")
            return False
    
    def _save_config(self) -> bool:
        """Guardar configuración en archivo"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                yaml.dump(self.config, f, default_flow_style=False, allow_unicode=True)
            return True
        except Exception as e:
            print(f"Error al guardar configuración: {e}")
            return False 