# 📝 Conversor Markdown a PDF Avanzado

Un conversor profesional de Markdown a PDF con funcionalidades avanzadas, validación inteligente, procesamiento automático de imágenes y personalización completa.

## ✨ Características Principales

### 🚀 **Conversión Avanzada**
- ✅ **Markdown completo** con todas las extensiones estándar
- ✅ **Metadatos YAML** con soporte completo
- ✅ **Tabla de contenidos automática** (TOC) con niveles configurables
- ✅ **Numeración automática** de headings
- ✅ **Generación de HTML** para previsualización rápida

### 🖼️ **Procesamiento de Imágenes**
- ✅ **Redimensionamiento automático** de imágenes
- ✅ **Descarga de imágenes remotas** con configuración
- ✅ **Optimización de calidad** (1-100)
- ✅ **Soporte SVG** con optimización
- ✅ **Embedding base64** para archivos portables
- ✅ **Múltiples formatos**: PNG, JPG, GIF, SVG, WebP, BMP, TIFF

### 🎨 **Personalización Completa**
- ✅ **Templates predefinidos** (light/dark)
- ✅ **CSS personalizado** con control total
- ✅ **Paletas de colores** configurables
- ✅ **Templates personalizados** para diferentes tipos de documento
- ✅ **Configuración YAML** avanzada

### 🔍 **Validación Inteligente**
- ✅ **20+ tipos** de problemas detectados
- ✅ **3 niveles** de severidad (error, warning, info)
- ✅ **Códigos específicos** para cada problema
- ✅ **Sugerencias automáticas** de solución
- ✅ **Reportes detallados** con estadísticas

### 📋 **CLI Completo**
- ✅ **Múltiples opciones** de línea de comandos
- ✅ **Validación interactiva** con confirmación
- ✅ **Procesamiento por lotes** de archivos
- ✅ **Logging detallado** para debugging
- ✅ **Ayuda contextual** con ejemplos

## 🚀 Instalación Rápida

### **Requisitos**
- Python 3.7 o superior
- Dependencias: `weasyprint`, `markdown`, `pyyaml`, `pillow`, `requests`, `colorama`

### **Instalación Automática**
```bash
git clone <tu-repositorio>
cd renderizador_mardown
chmod +x install.sh && ./install.sh
```

### **Instalación Manual**
```bash
pip install -r requirements.txt
mkdir -p conversion output style
```

## ⚡ Uso Básico

### **Conversión Simple**
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
python cli/md_to_pdf_converter.py \
  --file reporte.md \
  --dark-theme \
  --max-image-width 1000 \
  --image-quality 90 \
  --download-remote-images
```

### **Presentación**
```bash
python cli/md_to_pdf_converter.py \
  --file presentacion.md \
  --html \
  --style style/presentation.css
```

## 🎯 Casos de Uso

### **📝 Documentación de Proyecto**
- Manuales técnicos con TOC automática
- Documentación de API con ejemplos de código
- Guías de usuario con imágenes optimizadas

### **📊 Reportes Ejecutivos**
- Reportes mensuales con validación automática
- Presentaciones ejecutivas con tema corporativo
- Análisis de datos con gráficos y tablas

### **🎓 Documentos Académicos**
- Tesis con numeración automática
- Papers académicos con formato estándar
- Presentaciones de investigación

### **📱 Documentación Técnica**
- Manuales de usuario con capturas de pantalla
- Documentación de código con resaltado de sintaxis
- Diagramas técnicos con soporte SVG

## 🔧 Configuración

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

## 📚 Documentación Completa

### **🚀 Guías de Inicio**
- **[INICIO_RAPIDO.md](guide/INICIO_RAPIDO.md)** - Comenzar en 5 minutos
- **[PERSONALIZACION_RAPIDA.md](guide/PERSONALIZACION_RAPIDA.md)** - Personalizar colores en 10 minutos

### **🎨 Personalización**
- **[CONFIGURACION_TEMPLATES.md](guide/CONFIGURACION_TEMPLATES.md)** - Crear y configurar templates
- **[PERSONALIZACION_PALETAS.md](guide/PERSONALIZACION_PALETAS.md)** - Personalización completa de estilos
- **[CREAR_TEMPLATES.md](guide/CREAR_TEMPLATES.md)** - Crear templates personalizados
- **[CSS_PERSONALIZACION_AVANZADA.md](guide/CSS_PERSONALIZACION_AVANZADA.md)** - CSS avanzado

### **🖼️ Manejo de Imágenes**
- **[PROCESAMIENTO_IMAGENES.md](guide/PROCESAMIENTO_IMAGENES.md)** - Procesamiento automático de imágenes

### **📋 Estructura y Navegación**
- **[TABLA_CONTENIDO_GUIA.md](guide/TABLA_CONTENIDO_GUIA.md)** - Tabla de contenidos automática

### **🔍 Validación y Calidad**
- **[VALIDACION_GUIA.md](guide/VALIDACION_GUIA.md)** - Validación completa de documentos

### **📖 Índice Completo**
- **[INDICE_GUIAS.md](guide/INDICE_GUIAS.md)** - Índice de todas las guías disponibles

## 🛠️ Estructura del Proyecto

```
renderizador_mardown/
├── cli/                    # Interfaz de línea de comandos
│   └── md_to_pdf_converter.py
├── core/                   # Funcionalidades principales
│   ├── config_manager.py   # Gestión de configuración
│   ├── exporter.py         # Exportación a PDF
│   ├── image_processor.py  # Procesamiento de imágenes
│   ├── parser.py           # Parsing de Markdown
│   ├── renderer.py         # Renderizado HTML
│   └── validator.py        # Validación de documentos
├── conversion/             # Archivos de ejemplo
├── guide/                  # Documentación completa
├── output/                 # Archivos generados
├── style/                  # Estilos CSS
│   ├── light.css          # Tema claro
│   └── dark.css           # Tema oscuro
├── tests/                  # Pruebas automatizadas
├── README.md              # Documentación principal
├── CHANGELOG.md           # Historial de versiones
├── config.yaml            # Configuración
├── requirements.txt       # Dependencias
└── install.sh             # Script de instalación
```

## 🔍 Validación y Calidad

### **Tipos de Validación**
- **Errores críticos**: Archivos no encontrados, enlaces rotos, YAML inválido
- **Advertencias**: Líneas muy largas, headings duplicados, imágenes grandes
- **Sugerencias**: Metadatos faltantes, mejoras de estructura

### **Ejemplo de Validación**
```bash
python cli/md_to_pdf_converter.py --validate --verbose
```

**Salida:**
```
🔍 Iniciando validación avanzada de archivos Markdown...
✅ documento1.md: Válido (0 problemas)
❌ documento2.md: 2 problemas encontrados
   - E004: Enlace roto en línea 15: [Manual](manual.pdf)
   - W009: Línea muy larga en línea 8 (150 caracteres)
```

## 🎨 Personalización Avanzada

### **Crear Template Personalizado**
```yaml
# config.yaml
templates:
  mi_template:
    style_file: "./templates/mi_template.css"
    page_size: "A4"
    margins: "2.5cm"
    font_family: "Inter, Segoe UI, sans-serif"
    language: "es"
    include_toc: true
    toc_levels: 4
    number_headings: true
```

### **CSS Personalizado**
```css
/* mi_template.css */
:root {
  --primary-color: #1e3a8a;
  --secondary-color: #3b82f6;
  --accent-color: #06b6d4;
  --text-primary: #1e293b;
  --bg-primary: #ffffff;
}

body {
  font-family: 'Inter', sans-serif;
  line-height: 1.7;
  color: var(--text-primary);
}

h1, h2, h3 {
  color: var(--primary-color);
  border-bottom-color: var(--accent-color);
}
```

## 🔧 Comandos Avanzados

### **Procesamiento por Lotes**
```bash
# Convertir todos los archivos de un directorio
python cli/md_to_pdf_converter.py --input ./docs --output ./pdfs

# Convertir archivos específicos con patrones
python cli/md_to_pdf_converter.py --file "*.md" "manual_*.md"
```

### **Configuración Avanzada**
```bash
# Usar configuración personalizada
python cli/md_to_pdf_converter.py --config mi_config.yaml

# Configuración con tema específico
python cli/md_to_pdf_converter.py --theme dark --style ./style/corporativo.css
```

### **Debugging y Logging**
```bash
# Información detallada
python cli/md_to_pdf_converter.py --verbose

# Revisar log de conversión
cat conversion.log
```

## 🚀 Funcionalidades Únicas

### **🔄 Procesamiento Automático de Imágenes**
- **Redimensionamiento inteligente** manteniendo proporciones
- **Optimización de calidad** configurable
- **Descarga automática** de imágenes remotas
- **Soporte SVG** con optimización
- **Embedding base64** para archivos portables

### **📋 Tabla de Contenidos Inteligente**
- **Generación automática** basada en headings
- **Niveles configurables** (H1-H6)
- **Numeración automática** opcional
- **Enlaces funcionales** en PDF
- **Estilos personalizables**

### **🔍 Validación Avanzada**
- **20+ tipos** de problemas detectados
- **Códigos específicos** para cada problema
- **Sugerencias automáticas** de solución
- **Reportes detallados** con estadísticas
- **Validación interactiva** con confirmación

### **🎨 Personalización Total**
- **Templates configurables** por tipo de documento
- **CSS personalizado** con control total
- **Paletas de colores** predefinidas y personalizables
- **Configuración YAML** avanzada
- **Scripts de automatización** incluidos

## 📈 Estadísticas del Proyecto

- **Total de guías**: 9
- **Total de líneas de documentación**: 3,685
- **Tamaño total de documentación**: 80KB
- **Funcionalidades principales**: 15+
- **Opciones de CLI**: 20+
- **Tipos de validación**: 20+
- **Formatos de imagen soportados**: 8
- **Templates incluidos**: 2 (light/dark)

## 🤝 Contribuir

### **Reportar Problemas**
- Usa el sistema de issues del repositorio
- Incluye información detallada del problema
- Adjunta archivos de ejemplo si es posible

### **Mejorar Documentación**
- Actualiza guías existentes
- Agrega nuevos ejemplos
- Mejora la claridad de las instrucciones

### **Desarrollar Funcionalidades**
- Sigue las convenciones del código
- Agrega pruebas para nuevas funcionalidades
- Actualiza la documentación correspondiente

## 📋 Versiones

### **Versión Actual: 1.0.0** 🎉
- **Fecha de lanzamiento**: 17 de junio de 2025
- **Estado**: Estable - Lista para producción
- **Funcionalidades**: Completas con todas las características principales

### **Historial de Versiones**
- **[CHANGELOG.md](CHANGELOG.md)** - Historial completo de cambios y mejoras

### **Próximas Versiones**
- **v1.1.0**: Soporte para más formatos de salida (DOCX, EPUB)
- **v1.2.0**: Soporte para diagramas Mermaid y fórmulas LaTeX

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🙏 Agradecimientos

- **WeasyPrint** por el motor de renderizado PDF
- **Python-Markdown** por el procesamiento de Markdown
- **Pillow** por el procesamiento de imágenes
- **PyYAML** por el manejo de configuración

---

**¡Convierte tus documentos Markdown a PDF profesionales con facilidad!** 🎉

Consulta las [guías de documentación](guide/INDICE_GUIAS.md) para comenzar.