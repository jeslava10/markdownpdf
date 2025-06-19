#!/usr/bin/env python3
"""
Script de prueba para la validación avanzada de Markdown
"""

import sys
from pathlib import Path

# Agregar el directorio actual al path para importar módulos
sys.path.insert(0, str(Path(__file__).parent))

from core.config_manager import ConfigManager
from core.validator import MarkdownValidator


def create_test_files():
    """Crear archivos de prueba con diferentes problemas"""
    
    test_dir = Path("conversion/test_validation")
    test_dir.mkdir(exist_ok=True)
    
    # Archivo perfecto
    perfect_content = """---
title: "Documento Perfecto"
author: "Usuario Test"
date: 2024-12-19
description: "Un documento sin problemas"
---

# Título Principal

## Sección 1

Este es un documento perfecto sin problemas.

### Subsección 1.1

- Lista bien formateada
- Con elementos válidos
- Y estructura correcta

## Sección 2

![Imagen válida](image.png)

[Enlace válido](documento.md)

\`\`\`python
# Código bien formateado
print("Hello World")
\`\`\`
"""
    
    # Archivo con problemas
    problematic_content = """# Título sin metadatos

## Sección 1

Esta línea es extremadamente larga y debería generar una advertencia porque excede el límite de caracteres recomendado para una línea de Markdown, lo cual puede causar problemas de legibilidad y formato.

### Subsección 1.1

- Elemento de lista vacío

![Imagen faltante](imagen_inexistente.jpg)

[Enlace roto](archivo_inexistente.md)

## Sección 1

Heading duplicado que debería generar advertencia.

### Sub-subsección

#### Sub-sub-subsección

Saltando niveles de heading.

\`\`\`python
# Bloque de código sin cerrar
print("Código sin cerrar")
"""
    
    # Archivo vacío
    empty_content = ""
    
    # Archivo con YAML inválido
    invalid_yaml_content = """---
title: "Documento con YAML Inválido"
author: "Usuario Test"
date: 2024-12-19
description: "Documento con problemas en YAML"
invalid_yaml: [un, array, sin, cerrar
---

# Contenido normal

Este documento tiene YAML inválido.
"""
    
    # Archivo con caracteres problemáticos
    chars_content = """---
title: "Documento con Caracteres Problemáticos"
author: "Usuario Test"
date: 2024-12-19
---

# Título con caracteres especiales

Esta línea tiene tabs	que pueden causar problemas.

Caracteres Unicode problemáticos: 🚀💻📱

Línea con caracteres de control invisibles: 

## Sección con problemas

- Elemento de lista con tab	al inicio
- Otro elemento normal
"""
    
    # Crear archivos
    files = {
        "perfecto.md": perfect_content,
        "problematico.md": problematic_content,
        "vacio.md": empty_content,
        "yaml_invalido.md": invalid_yaml_content,
        "caracteres_problematicos.md": chars_content
    }
    
    for filename, content in files.items():
        file_path = test_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"✅ Archivos de prueba creados en {test_dir}")
    return test_dir

def test_validation():
    """Probar la validación avanzada"""
    
    print("🧪 Probando Validación Avanzada de Markdown")
    print("=" * 60)
    
    # Crear archivos de prueba
    test_dir = create_test_files()
    
    # Cargar configuración
    config_manager = ConfigManager("config.yaml")
    validation_config = config_manager.get_validation_config()
    
    # Crear validador
    validator = MarkdownValidator(validation_config)
    
    # Validar directorio de prueba
    print(f"\n🔍 Validando archivos en: {test_dir}")
    validation_results = validator.validate_directory(test_dir)
    
    # Mostrar reporte detallado
    validator.print_validation_report(validation_results, verbose=True)
    
    # Análisis específico por tipo de problema
    print("\n📊 ANÁLISIS POR TIPO DE PROBLEMA:")
    summary = validator.get_summary(validation_results)
    
    issues_by_type = summary['issues_by_type']
    for issue_type, count in issues_by_type.items():
        print(f"   {issue_type}: {count}")
    
    # Verificar que se detectaron los problemas esperados
    expected_issues = [
        'empty_file',
        'invalid_yaml', 
        'line_too_long',
        'missing_image',
        'broken_link',
        'duplicate_headings',
        'inconsistent_headings',
        'tab_characters',
        'no_metadata'
    ]
    
    detected_issues = set(issues_by_type.keys())
    print(f"\n✅ PROBLEMAS DETECTADOS:")
    for issue in expected_issues:
        if issue in detected_issues:
            print(f"   ✅ {issue}: {issues_by_type[issue]}")
        else:
            print(f"   ❌ {issue}: No detectado")
    
    # Limpiar archivos de prueba
    print(f"\n🧹 Limpiando archivos de prueba...")
    for file_path in test_dir.glob("*.md"):
        file_path.unlink()
    test_dir.rmdir()
    
    print("✅ Pruebas de validación completadas")

def test_validation_modes():
    """Probar diferentes modos de validación"""
    
    print("\n🔧 Probando Diferentes Modos de Validación")
    print("=" * 50)
    
    # Crear un archivo de prueba simple
    test_file = Path("conversion/test_simple.md")
    test_content = """---
title: "Test Simple"
author: "Usuario"
date: 2024-12-19
---

# Título

## Sección

Contenido normal.

![Imagen](image.png)
"""
    
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    # Cargar configuración
    config_manager = ConfigManager("config.yaml")
    validation_config = config_manager.get_validation_config()
    validator = MarkdownValidator(validation_config)
    
    # Probar validación de archivo individual
    print("\n📄 Validación de archivo individual:")
    result = validator.validate_file(test_file)
    print(f"   Archivo: {test_file.name}")
    print(f"   Válido: {result.valid}")
    print(f"   Problemas: {len(result.issues)}")
    print(f"   Headings: {result.heading_count}")
    print(f"   Enlaces: {result.link_count}")
    print(f"   Imágenes: {result.image_count}")
    print(f"   Metadatos: {result.metadata_present}")
    
    # Limpiar
    test_file.unlink()
    
    print("✅ Pruebas de modos completadas")

def main():
    """Función principal de pruebas"""
    
    print("🚀 Iniciando pruebas de Validación Avanzada")
    print("=" * 60)
    
    try:
        # Probar validación básica
        test_validation()
        
        # Probar diferentes modos
        test_validation_modes()
        
        print("\n" + "=" * 60)
        print("🎉 ¡Todas las pruebas de validación pasaron exitosamente!")
        return 0
        
    except Exception as e:
        print(f"\n❌ Error durante las pruebas: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 