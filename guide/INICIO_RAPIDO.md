# 🚀 Guía de Inicio Rápido - Conversor Markdown a PDF

¡Bienvenido al conversor Markdown a PDF más avanzado! Esta guía te ayudará a comenzar en menos de 5 minutos.

## 📋 Requisitos Previos

- ✅ Python 3.7 o superior
- ✅ Dependencias instaladas (`pip install -r requirements.txt`)
- ✅ Conversor instalado (`./install.sh`)

## ⚡ Instalación Rápida

```bash
# 1. Clonar o descargar el proyecto
git clone <tu-repositorio>
cd renderizador_mardown

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar script de instalación
./install.sh
```

## 🎯 Primeros Pasos (2 minutos)

### **Paso 1: Crear tu primer documento**
```bash
# Crear directorio de trabajo
mkdir -p conversion output

# Crear archivo de ejemplo
cat > conversion/mi_primer_documento.md << 'EOF'
---
title: "Mi Primer Documento"
author: "Tu Nombre"
date: 2024-12-19
---

# Introducción

Este es mi primer documento con el conversor avanzado.

## Características

### ✅ Funcionalidades Principales
- Conversión Markdown a PDF
- Estilos CSS profesionales
- Tabla de contenidos automática
- Validación de documentos

### 🖼️ Soporte de Imágenes
![Ejemplo](image.png)

## Código de Ejemplo

```python
print("¡Hola Mundo!")
```

## Lista de Tareas

- [x] Instalar conversor
- [x] Crear primer documento
- [ ] Personalizar estilos
- [ ] Generar PDF final
EOF
```

### **Paso 2: Convertir a PDF**
```bash
# Conversión básica
python cli/md_to_pdf_converter.py

# O convertir archivo específico
python cli/md_to_pdf_converter.py --file conversion/mi_primer_documento.md
```

### **Paso 3: Verificar resultado**
```bash
# Ver archivos generados
ls -la output/
```

## 🚀 Comandos Esenciales

### **Conversión Básica**
```bash
# Convertir todos los archivos .md
python cli/md_to_pdf_converter.py

# Convertir archivo específico
python cli/md_to_pdf_converter.py --file documento.md

# Usar tema oscuro
python cli/md_to_pdf_converter.py --dark-theme
```

### **Validación de Documentos**
```bash
# Validar antes de convertir
python cli/md_to_pdf_converter.py --validate

# Validar con detalles completos
python cli/md_to_pdf_converter.py --validate --verbose
```

### **Personalización**
```bash
# Usar CSS personalizado
python cli/md_to_pdf_converter.py --style mi_estilo.css

# Usar template específico
python cli/md_to_pdf_converter.py --template dark

# Listar templates disponibles
python cli/md_to_pdf_converter.py --list-templates
```

## 🎨 Funcionalidades Avanzadas

### **📋 Tabla de Contenidos Automática**
```bash
# Incluir TOC automática
python cli/md_to_pdf_converter.py --toc

# Configurar niveles de TOC (1-6)
python cli/md_to_pdf_converter.py --toc --toc-levels 4

# Numerar headings automáticamente
python cli/md_to_pdf_converter.py --number-headings
```

### **🖼️ Procesamiento de Imágenes**
```bash
# Redimensionar imágenes automáticamente
python cli/md_to_pdf_converter.py --max-image-width 1200 --max-image-height 800

# Descargar imágenes remotas
python cli/md_to_pdf_converter.py --download-remote-images

# Embeber imágenes como base64
python cli/md_to_pdf_converter.py --embed-images

# Configurar calidad de imagen (1-100)
python cli/md_to_pdf_converter.py --image-quality 95
```

### **📄 Generación de HTML**
```bash
# Generar HTML para previsualización
python cli/md_to_pdf_converter.py --html

# Generar solo HTML (sin PDF)
python cli/md_to_pdf_converter.py --html --pdf
```

## 📊 Ejemplos Prácticos

### **Documentación Técnica**
```bash
# Documento técnico con TOC y validación
python cli/md_to_pdf_converter.py \
  --file manual_tecnico.md \
  --toc \
  --toc-levels 4 \
  --number-headings \
  --validate \
  --verbose
```

### **Reporte Ejecutivo**
```bash
# Reporte con tema oscuro y imágenes optimizadas
python cli/md_to_pdf_converter.py \
  --file reporte.md \
  --dark-theme \
  --max-image-width 1000 \
  --image-quality 90 \
  --download-remote-images
```

### **Presentación**
```bash
# Presentación con HTML para revisión rápida
python cli/md_to_pdf_converter.py \
  --file presentacion.md \
  --html \
  --style style/presentation.css
```

## 🔧 Configuración Rápida

### **Archivo de Configuración (`config.yaml`)**
```yaml
default:
  input_dir: "./conversion"
  output_dir: "./output"
  style_file: "./style/light.css"
  page_size: "A4"
  margins: "2cm"
  font_family: "Roboto, Helvetica Neue, Segoe UI, Arial, sans-serif"
  language: "es"
  verbose: false
  
  # Configuración de imágenes
  max_image_width: 800
  max_image_height: 600
  image_quality: 85
  download_remote_images: false
  embed_images: false
  
  # Configuración de TOC
  include_toc: false
  toc_levels: 3
  number_headings: false
```

### **Templates Disponibles**
```bash
# Listar templates
python cli/md_to_pdf_converter.py --list-templates

# Usar template específico
python cli/md_to_pdf_converter.py --template light
python cli/md_to_pdf_converter.py --template dark
```

## 🎯 Casos de Uso Comunes

### **📝 Documentación de Proyecto**
```bash
# Convertir toda la documentación
python cli/md_to_pdf_converter.py \
  --input ./docs \
  --output ./pdfs \
  --toc \
  --validate
```

### **📊 Reportes Semanales**
```bash
# Reporte con validación automática
python cli/md_to_pdf_converter.py \
  --file reporte_semanal.md \
  --validate \
  --verbose
```

### **🎓 Documentos Académicos**
```bash
# Tesis con numeración y TOC
python cli/md_to_pdf_converter.py \
  --file tesis.md \
  --toc \
  --number-headings \
  --toc-levels 5
```

## 🔍 Solución de Problemas

### **Errores Comunes**

#### **❌ "No se encontró el archivo"**
```bash
# Verificar archivos disponibles
ls -la conversion/

# Usar patrón de archivos
python cli/md_to_pdf_converter.py --file "*.md"
```

#### **❌ "Error de validación"**
```bash
# Ver detalles completos
python cli/md_to_pdf_converter.py --validate --verbose

# Corregir problemas antes de convertir
```

#### **❌ "Error de permisos"**
```bash
# Verificar permisos de directorios
ls -la output/

# Crear directorios si no existen
mkdir -p output
```

### **Logs y Debugging**
```bash
# Ver información detallada
python cli/md_to_pdf_converter.py --verbose

# Revisar log de conversión
cat conversion.log
```

## 📚 Próximos Pasos

### **🎨 Personalización**
1. **[PERSONALIZACION_PALETAS.md](PERSONALIZACION_PALETAS.md)** - Personalizar colores y temas
2. **[CREAR_TEMPLATES.md](CREAR_TEMPLATES.md)** - Crear templates personalizados
3. **[CSS_PERSONALIZACION_AVANZADA.md](CSS_PERSONALIZACION_AVANZADA.md)** - CSS avanzado

### **🖼️ Manejo de Imágenes**
1. **[PROCESAMIENTO_IMAGENES.md](PROCESAMIENTO_IMAGENES.md)** - Procesamiento avanzado de imágenes

### **🔍 Validación y Calidad**
1. **[VALIDACION_GUIA.md](VALIDACION_GUIA.md)** - Validación completa de documentos

### **📋 Estructura y Navegación**
1. **[TABLA_CONTENIDO_GUIA.md](TABLA_CONTENIDO_GUIA.md)** - Tabla de contenidos automática

## 💡 Consejos Rápidos

### **✅ Mejores Prácticas**
- Siempre usa `--validate` antes de convertir documentos importantes
- Usa metadatos YAML para mejor documentación
- Personaliza estilos según el tipo de documento
- Usa `--verbose` para debugging

### **⚡ Optimización**
- Usa `--max-image-width` para optimizar imágenes grandes
- Configura `--image-quality` según necesidades
- Usa `--download-remote-images` para documentos con imágenes remotas

### **🎯 Productividad**
- Crea templates personalizados para proyectos repetitivos
- Usa `--html` para revisión rápida antes de generar PDF
- Automatiza conversiones con scripts

---

**¡Ya estás listo para crear documentos profesionales!** 🎉

Consulta las otras guías para funcionalidades avanzadas y personalización. 