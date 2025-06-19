# 🔍 Guía Completa de Validación

El sistema de validación avanzada detecta automáticamente problemas en tus documentos Markdown antes de la conversión, asegurando PDFs de alta calidad.

## ✨ Características del Sistema de Validación

- ✅ **20+ tipos** de problemas detectados
- ✅ **3 niveles** de severidad (error, warning, info)
- ✅ **Códigos específicos** para cada problema (E001-E020)
- ✅ **Sugerencias automáticas** de solución
- ✅ **Reportes detallados** con estadísticas
- ✅ **Validación interactiva** con confirmación del usuario

## 🚀 Uso Básico

### Validación Simple
```bash
# Validar todos los archivos
python md_to_pdf_converter.py --validate

# Validar archivo específico
python md_to_pdf_converter.py --validate --file documento.md

# Validar con información detallada
python md_to_pdf_converter.py --validate --verbose
```

### Validación con Conversión
```bash
# Validar y convertir en un solo comando
python md_to_pdf_converter.py --validate --file documento.md

# Validar y convertir con confirmación interactiva
python md_to_pdf_converter.py --validate --verbose
```

## 📋 Tipos de Validación

### ❌ Errores Críticos (Impiden la conversión)

| Código | Problema | Descripción | Solución |
|--------|----------|-------------|----------|
| E001 | Archivo no encontrado | El archivo referenciado no existe | Verificar ruta y nombre del archivo |
| E003 | Archivo vacío | El documento no tiene contenido | Agregar contenido o eliminar archivo |
| E004 | Enlace roto | Enlace a archivo local inexistente | Corregir ruta o eliminar enlace |
| E005 | Imagen faltante | Imagen referenciada no existe | Verificar ruta de la imagen |
| E007 | YAML inválido | Sintaxis incorrecta en metadatos | Revisar sintaxis YAML entre `---` |
| E013 | YAML inválido | Error al parsear front matter | Corregir sintaxis YAML |

### ⚠️ Advertencias (Afectan la calidad)

| Código | Problema | Descripción | Solución |
|--------|----------|-------------|----------|
| E009 | Línea muy larga | Línea excede 120 caracteres | Dividir en múltiples líneas |
| E010 | Caracteres problemáticos | Tabs o caracteres especiales | Usar espacios en lugar de tabs |
| E015 | Estructura inconsistente | Saltos en jerarquía de headings | Usar H1 → H2 → H3 sin saltar |
| E016 | Imagen muy grande | Archivo de imagen pesado | Comprimir imagen |
| E017 | Enlace HTTP | Enlace no seguro | Usar HTTPS |
| E018 | Headings duplicados | Títulos repetidos | Usar títulos únicos |
| E019 | Texto alternativo faltante | Imagen sin descripción | Agregar `![descripción](imagen.png)` |

### ℹ️ Sugerencias (Mejoras recomendadas)

| Código | Problema | Descripción | Solución |
|--------|----------|-------------|----------|
| E008 | Sin título | Documento sin heading principal | Agregar `# Título Principal` |
| E012 | Metadatos faltantes | Campos YAML importantes faltantes | Agregar `title`, `author`, `date` |
| E014 | Sin headings | Documento sin estructura | Agregar headings para organización |

## 📊 Reporte de Validación

### Salida Básica
```bash
python md_to_pdf_converter.py --validate
```

**Ejemplo de salida:**
```
🔍 Iniciando validación avanzada de archivos Markdown...
✅ documento1.md: Válido (0 problemas)
❌ documento2.md: 2 problemas encontrados
   - E004: Enlace roto en línea 15: [Manual](manual.pdf)
   - W009: Línea muy larga en línea 8 (150 caracteres)
⚠️ documento3.md: 1 advertencia
   - I012: Metadatos faltantes: considera agregar 'author' y 'date'

📊 Resumen de validación:
   Total de archivos: 3
   ✅ Válidos: 1
   ❌ Inválidos: 1
   ⚠️ Con advertencias: 1
   📝 Total de problemas: 3
```

### Salida Detallada
```bash
python md_to_pdf_converter.py --validate --verbose
```

**Ejemplo de salida detallada:**
```
🔍 Iniciando validación avanzada de archivos Markdown...

📄 documento1.md (2.3KB, 45 líneas)
✅ Válido - No se encontraron problemas

📄 documento2.md (1.8KB, 32 líneas)
❌ 2 problemas encontrados:

   ❌ E004: Enlace roto en línea 15
       Problema: [Manual](manual.pdf) - El archivo 'manual.pdf' no existe
       Sugerencia: Verifica que el archivo existe o corrige la ruta
       Contexto: ...ver el [Manual](manual.pdf) para más detalles...

   ⚠️ W009: Línea muy larga en línea 8
       Problema: Línea de 150 caracteres (máximo recomendado: 120)
       Sugerencia: Divide la línea en múltiples líneas para mejor legibilidad
       Contexto: Esta es una línea muy larga que debería ser dividida...

📄 documento3.md (3.1KB, 67 líneas)
⚠️ 1 advertencia encontrada:

   ℹ️ I012: Metadatos faltantes
       Problema: Campos importantes faltantes en YAML front matter
       Sugerencia: Agrega 'author' y 'date' para mejor documentación
       Ejemplo:
       ---
       title: "Mi Documento"
       author: "Tu Nombre"
       date: 2024-06-18
       ---

📊 Estadísticas de contenido:
   📝 Total de headings: 12
   🔗 Total de enlaces: 8
   🖼️ Total de imágenes: 3
   📋 Archivos con metadatos: 2
```

## 🎯 Códigos de Error Detallados

### E001-E010: Errores de Archivo y Sintaxis
- **E001**: Archivo no encontrado
- **E002**: Archivo muy grande (>10MB)
- **E003**: Archivo vacío
- **E004**: Enlace roto
- **E005**: Imagen faltante
- **E006**: Formato no soportado
- **E007**: Metadatos inválidos
- **E008**: Sin título principal
- **E009**: Línea muy larga
- **E010**: Caracteres problemáticos

### E011-E020: Errores de Estructura y Contenido
- **E011**: Fecha inválida
- **E012**: Metadatos faltantes
- **E013**: YAML inválido
- **E014**: Sin headings
- **E015**: Estructura inconsistente
- **E016**: Imagen muy grande
- **E017**: Enlace HTTP no seguro
- **E018**: Headings duplicados
- **E019**: Texto alternativo faltante
- **E020**: Caracteres inválidos

## 🔧 Configuración de Validación

### Archivo de Configuración (`config.yaml`)
```yaml
validation:
  check_broken_links: true
  check_missing_images: true
  check_empty_files: true
  max_file_size_mb: 10
  max_line_length: 120
  allowed_image_formats: ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp']
  max_image_size_mb: 5
  require_https_links: true
  require_alt_text: true
```

### Personalizar Validación
```bash
# Usar configuración personalizada
python md_to_pdf_converter.py --config mi_config.yaml --validate

# Validar con configuración específica
python md_to_pdf_converter.py --validate --verbose --config proyecto.yaml
```

## 💡 Mejores Prácticas

### Antes de Convertir
1. **Siempre valida** tus documentos
2. **Corrige errores críticos** primero
3. **Revisa advertencias** para mejorar calidad
4. **Usa metadatos YAML** para mejor documentación

### Estructura Recomendada
```markdown
---
title: "Título del Documento"
author: "Tu Nombre"
date: 2024-06-18
description: "Descripción breve del documento"
---

# Título Principal

## Sección 1

Contenido con líneas de máximo 120 caracteres para mejor legibilidad.

### Subsección

- Lista con elementos claros
- Enlaces a archivos que existen
- Imágenes con texto alternativo

![Descripción de la imagen](imagen.png)
```

## 🐛 Solución de Problemas

### Errores Comunes

| Problema | Causa | Solución |
|----------|-------|----------|
| "Enlace roto" | Archivo no existe | Verificar ruta y nombre |
| "YAML inválido" | Sintaxis incorrecta | Revisar sintaxis entre `---` |
| "Línea muy larga" | Línea >120 caracteres | Dividir en múltiples líneas |
| "Imagen faltante" | Imagen no existe | Verificar ruta de imagen |

### Debugging
```bash
# Ver todos los detalles
python md_to_pdf_converter.py --validate --verbose

# Validar configuración
python md_to_pdf_converter.py --config config.yaml --validate

# Revisar logs
cat conversion.log
```

## 📈 Beneficios de la Validación

### Para el Usuario
- **Confianza**: Saber que los documentos son válidos
- **Calidad**: Identificar y corregir problemas
- **Eficiencia**: Evitar conversiones fallidas
- **Aprendizaje**: Sugerencias para mejorar

### Para el Proyecto
- **Consistencia**: Documentos con formato uniforme
- **Mantenibilidad**: Detección automática de problemas
- **Profesionalismo**: PDFs de alta calidad
- **Escalabilidad**: Sistema extensible

## Validación de SVG y Emojis

El sistema valida automáticamente:

- **SVG**:
  - Estructura XML válida
  - Tamaño de archivo razonable
  - Presencia de viewBox o dimensiones
  - Accesibilidad y compatibilidad
- **Emojis**:
  - Sobreuso de emojis (más de 20 por documento)
  - Emojis en títulos (pueden causar problemas en algunos sistemas)
  - Compatibilidad Unicode

**Recomendación:** Usa SVG optimizados y emojis con moderación para mantener la profesionalidad y compatibilidad del PDF.

---

**¿Necesitas más ayuda?** Consulta las otras guías o ejecuta `python md_to_pdf_converter.py --help` 