#!/usr/bin/env python3
"""
Script de prueba para la funcionalidad de Tabla de Contenidos Automática
"""

import sys
import unittest
from pathlib import Path

# Agregar el directorio actual al path para importar módulos
sys.path.insert(0, str(Path(__file__).parent))

from cli.md_to_pdf_converter import MarkdownToPDFConverter
from core.config_manager import ConfigManager


class TestTOC(unittest.TestCase):
    def setUp(self):
        self.config_manager = ConfigManager("config.yaml")
        self.conversion_config = self.config_manager.get_conversion_config("tecnico")
        self.converter = MarkdownToPDFConverter(self.conversion_config)
        Path("output").mkdir(exist_ok=True)

    def test_toc_functionality(self):
    test_files = [
        "conversion/documento_con_toc.md",
        "conversion/test_toc_simple.md"
    ]
    for test_file in test_files:
        file_path = Path(test_file)
            self.assertTrue(file_path.exists(), f"Archivo no encontrado: {test_file}")
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                import re
                headings = re.findall(r'^#{1,6}\s+', content, re.MULTILINE)
            self.assertGreater(len(headings), 0, f"No se encontraron headings en {test_file}")
            result = self.converter.convert_file(file_path)
            self.assertTrue(result, f"Conversión fallida para {test_file}")
                    pdf_path = Path("output") / f"{file_path.stem}.pdf"
            self.assertTrue(pdf_path.exists(), f"PDF no generado para {test_file}")

    def test_toc_styles(self):
        css_file = Path("style/light.css")
        self.assertTrue(css_file.exists(), "Archivo CSS no encontrado")
    with open(css_file, 'r', encoding='utf-8') as f:
        css_content = f.read()
    toc_styles = [
        '.toc {',
        '.toc::before {',
        '.toc ul {',
        '.toc li {',
        '.toc a {',
        '.toc a:hover {'
    ]
    for style in toc_styles:
            self.assertIn(style, css_content, f"Falta el estilo: {style}")

def main():
    """Función principal de pruebas"""
    
    print("🚀 Iniciando pruebas de Tabla de Contenidos Automática")
    print("=" * 60)
    
    # Crear directorio de salida si no existe
    Path("output").mkdir(exist_ok=True)
    
    # Ejecutar pruebas
    unittest.main()

if __name__ == "__main__":
    sys.exit(main()) 