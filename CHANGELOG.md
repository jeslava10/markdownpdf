# 📋 Changelog

Todas las notables mejoras y cambios en el Conversor Markdown a PDF Avanzado.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [1.1.0] - 2025-06-19

### ✨ Nuevas funcionalidades
- Configuración inicial del flujo de trabajo GitFlow:
  - `main`: rama principal para producción
  - `develop`: rama de integración de cambios
  - `feature/*`: ramas para funcionalidades nuevas (merge squash hacia `develop`)
  - `release/x.y.z`: ramas para preparar releases desde `develop`, con ajustes de versión y changelog
  - `hotfix/x.y.z`: correcciones urgentes desde `main` directamente
- Estructura de release documentada y soportada mediante GitHub Actions.
- Flujo automático de publicación al hacer `merge` de `release/*` a `main`:
  - Generación de tag (`vX.Y.Z`)
  - Publicación de release en GitHub con base en `CHANGELOG.md`

### 🛠 Mejoras técnicas
- Se agregó workflow `release-on-main.yml` para automatizar la creación de releases.
- Validación de formato semántico del número de versión desde `CHANGELOG.md`.


## [1.0.0] - 2025-06-18

### 🎉 Lanzamiento Oficial - Versión Estable

Esta es la primera versión estable del Conversor Markdown a PDF Avanzado, con todas las funcionalidades principales implementadas y documentadas.

### ✨ Nuevas Funcionalidades

#### 🚀 **Conversión Avanzada**
- **Soporte completo de Markdown** con todas las extensiones estándar
- **Metadatos YAML** con parsing automático y validación
- **Tabla de contenidos automática** (TOC) con niveles configurables (H1-H6)
- **Numeración automática** de headings opcional
- **Generación de HTML** para previsualización rápida
- **Procesamiento por lotes** de múltiples archivos
- **Patrones de archivos** soportados (ej: `*.md`, `manual_*.md`)

#### 🖼️ **Procesamiento Automático de Imágenes**
- **Redimensionamiento inteligente** manteniendo proporciones
- **Descarga automática** de imágenes remotas con configuración
- **Optimización de calidad** configurable (1-100)
- **Soporte SVG** con optimización automática
- **Embedding base64** para archivos portables
- **Múltiples formatos soportados**: PNG, JPG, GIF, SVG, WebP, BMP, TIFF
- **Configuración de dimensiones máximas** (ancho/alto)
- **Procesamiento de imágenes locales y remotas**

#### 🎨 **Sistema de Templates y Personalización**
- **Templates predefinidos**: Light (claro) y Dark (oscuro)
- **CSS personalizado** con control total del diseño
- **Sistema de paletas de colores** configurables
- **Templates personalizados** para diferentes tipos de documento
- **Configuración YAML** avanzada y flexible
- **Variables CSS** para fácil personalización
- **Scripts de automatización** para crear templates

#### 🔍 **Sistema de Validación Inteligente**
- **20+ tipos** de problemas detectados automáticamente
- **3 niveles de severidad**: Error, Warning, Info
- **Códigos específicos** para cada problema (E001-E020)
- **Sugerencias automáticas** de solución para cada problema
- **Reportes detallados** con estadísticas completas
- **Validación interactiva** con confirmación del usuario
- **Validación de enlaces rotos** y recursos faltantes
- **Análisis de estructura** de headings y jerarquía
- **Validación de metadatos YAML** con sintaxis correcta

#### 📋 **CLI Completo y Profesional**
- **Interfaz de línea de comandos** completa con 20+ opciones
- **Validación interactiva** con confirmación del usuario
- **Logging detallado** para debugging y monitoreo
- **Ayuda contextual** con ejemplos prácticos
- **Manejo de errores** robusto con mensajes claros
- **Sugerencias inteligentes** para archivos no encontrados
- **Modo no interactivo** para automatización

#### 📊 **Funcionalidades de Salida**
- **Generación de PDF** con calidad profesional
- **Generación de HTML** para previsualización
- **Configuración de página** (tamaño, márgenes)
- **Fuentes personalizables** con fallbacks
- **Idioma configurable** (español por defecto)
- **Metadatos PDF** automáticos
- **Optimización de archivos** de salida

### 🔧 Mejoras Técnicas

#### **Arquitectura Modular**
- **Separación clara** de responsabilidades
- **Módulos independientes**: config_manager, exporter, image_processor, parser, renderer, validator
- **Interfaces bien definidas** entre componentes
- **Código mantenible** y extensible

#### **Gestión de Configuración**
- **Sistema de configuración YAML** flexible
- **Templates configurables** por tipo de documento
- **Configuración por defecto** sensible
- **Sobrescritura** de configuración por argumentos CLI
- **Validación de configuración** automática

#### **Procesamiento de Imágenes**
- **Clase ImageProcessor** dedicada
- **Optimización automática** de SVGs
- **Redimensionamiento inteligente** con proporciones
- **Descarga segura** de imágenes remotas
- **Manejo de errores** robusto
- **Soporte para múltiples formatos**

#### **Validación Avanzada**
- **Clase MarkdownValidator** completa
- **Detección automática** de problemas comunes
- **Análisis de estructura** de documentos
- **Validación de recursos** (imágenes, enlaces)
- **Reportes detallados** con contexto
- **Sugerencias de mejora** automáticas

### 📚 Documentación Completa

#### **Guías Organizadas (9 archivos)**
- **[INICIO_RAPIDO.md](guide/INICIO_RAPIDO.md)** - Comenzar en 5 minutos
- **[PERSONALIZACION_RAPIDA.md](guide/PERSONALIZACION_RAPIDA.md)** - Personalizar colores en 10 minutos
- **[CONFIGURACION_TEMPLATES.md](guide/CONFIGURACION_TEMPLATES.md)** - Crear y configurar templates
- **[PERSONALIZACION_PALETAS.md](guide/PERSONALIZACION_PALETAS.md)** - Personalización completa de estilos
- **[CREAR_TEMPLATES.md](guide/CREAR_TEMPLATES.md)** - Crear templates personalizados
- **[CSS_PERSONALIZACION_AVANZADA.md](guide/CSS_PERSONALIZACION_AVANZADA.md)** - CSS avanzado
- **[PROCESAMIENTO_IMAGENES.md](guide/PROCESAMIENTO_IMAGENES.md)** - Manejo de imágenes
- **[TABLA_CONTENIDO_GUIA.md](guide/TABLA_CONTENIDO_GUIA.md)** - Tabla de contenidos
- **[VALIDACION_GUIA.md](guide/VALIDACION_GUIA.md)** - Validación de documentos

#### **Índice y Navegación**
- **[INDICE_GUIAS.md](guide/INDICE_GUIAS.md)** - Índice completo con rutas de aprendizaje
- **Rutas de aprendizaje** organizadas por nivel de experiencia
- **Casos de uso específicos** documentados
- **Ejemplos prácticos** en cada guía

### 🎯 Casos de Uso Soportados

#### **📝 Documentación Técnica**
- Manuales técnicos con TOC automática
- Documentación de API con ejemplos de código
- Guías de usuario con imágenes optimizadas
- Diagramas técnicos con soporte SVG

#### **📊 Reportes Ejecutivos**
- Reportes mensuales con validación automática
- Presentaciones ejecutivas con tema corporativo
- Análisis de datos con gráficos y tablas
- Documentos con imágenes remotas integradas

#### **🎓 Documentos Académicos**
- Tesis con numeración automática
- Papers académicos con formato estándar
- Presentaciones de investigación
- Documentos con citas y referencias

#### **📱 Documentación Técnica**
- Manuales de usuario con capturas de pantalla
- Documentación de código con resaltado de sintaxis
- Diagramas técnicos con soporte SVG
- Guías de instalación con imágenes locales

### 🔧 Configuración y Personalización

#### **Archivo de Configuración (`config.yaml`)**
- Configuración por defecto completa
- Templates predefinidos (light/dark)
- Configuración de validación avanzada
- Configuración de metadatos
- Configuración de rendimiento
- Configuración de salida

#### **Templates Personalizables**
- Templates por tipo de documento
- CSS personalizado con variables
- Configuración específica por template
- Scripts de automatización incluidos

### 🚀 Comandos CLI Principales

#### **Conversión Básica**
```bash
# Convertir todos los archivos .md
python cli/md_to_pdf_converter.py

# Convertir archivo específico
python cli/md_to_pdf_converter.py --file documento.md

# Usar tema oscuro
python cli/md_to_pdf_converter.py --dark-theme
```

#### **Validación**
```bash
# Validar antes de convertir
python cli/md_to_pdf_converter.py --validate

# Validar con detalles completos
python cli/md_to_pdf_converter.py --validate --verbose
```

#### **Personalización**
```bash
# Usar CSS personalizado
python cli/md_to_pdf_converter.py --style mi_estilo.css

# Usar template específico
python cli/md_to_pdf_converter.py --template dark

# Listar templates disponibles
python cli/md_to_pdf_converter.py --list-templates
```

#### **Funcionalidades Avanzadas**
```bash
# Tabla de contenidos automática
python cli/md_to_pdf_converter.py --toc --toc-levels 4

# Procesamiento de imágenes
python cli/md_to_pdf_converter.py --download-remote-images --max-image-width 1200

# Generación de HTML
python cli/md_to_pdf_converter.py --html
```

### 📈 Estadísticas del Proyecto

#### **Código**
- **Líneas de código**: ~2,500+
- **Módulos principales**: 6 (config_manager, exporter, image_processor, parser, renderer, validator)
- **Clases principales**: 4 (MarkdownToPDFConverter, ConfigManager, ImageProcessor, MarkdownValidator)
- **Funciones principales**: 50+

#### **Documentación**
- **Total de guías**: 9 archivos
- **Total de líneas**: 3,685 líneas
- **Tamaño total**: 80KB
- **Ejemplos prácticos**: 50+
- **Tiempo total de lectura**: ~4 horas

#### **Funcionalidades**
- **Opciones CLI**: 20+
- **Tipos de validación**: 20+
- **Formatos de imagen**: 8
- **Templates incluidos**: 2 (light/dark)
- **Extensiones Markdown**: 15+

### 🔍 Validación y Calidad

#### **Tipos de Validación Implementados**
- **Errores críticos**: Archivos no encontrados, enlaces rotos, YAML inválido
- **Advertencias**: Líneas muy largas, headings duplicados, imágenes grandes
- **Sugerencias**: Metadatos faltantes, mejoras de estructura

#### **Códigos de Error**
- **E001-E010**: Errores de archivo y sintaxis
- **E011-E020**: Errores de estructura y contenido
- **W001-W999**: Advertencias de calidad
- **I001-I999**: Sugerencias de mejora

### 🎨 Personalización Avanzada

#### **Sistema de Paletas**
- Paletas predefinidas (Azul Profesional, Verde Naturaleza, Rojo Energético, Púrpura Creativa)
- Generador de paletas automático
- Variables CSS para fácil personalización
- Scripts de automatización incluidos

#### **Templates por Tipo de Documento**
- **Ejecutivo**: Para reportes corporativos
- **Académico**: Para tesis y papers
- **Presentación**: Para slides y presentaciones
- **Técnico**: Para documentación técnica

### 🔧 Instalación y Configuración

#### **Requisitos**
- Python 3.7 o superior
- Dependencias: `weasyprint`, `markdown`, `pyyaml`, `pillow`, `requests`, `colorama`

#### **Instalación**
```bash
# Instalación automática
git clone <repositorio>
cd renderizador_mardown
chmod +x install.sh && ./install.sh

# Instalación manual
pip install -r requirements.txt
mkdir -p conversion output style
```

### 🚀 Funcionalidades Únicas

#### **Procesamiento Automático de Imágenes**
- Redimensionamiento inteligente manteniendo proporciones
- Optimización de calidad configurable
- Descarga automática de imágenes remotas
- Soporte SVG con optimización
- Embedding base64 para archivos portables

#### **Tabla de Contenidos Inteligente**
- Generación automática basada en headings
- Niveles configurables (H1-H6)
- Numeración automática opcional
- Enlaces funcionales en PDF
- Estilos personalizables

#### **Validación Avanzada**
- 20+ tipos de problemas detectados
- Códigos específicos para cada problema
- Sugerencias automáticas de solución
- Reportes detallados con estadísticas
- Validación interactiva con confirmación

#### **Personalización Total**
- Templates configurables por tipo de documento
- CSS personalizado con control total
- Paletas de colores predefinidas y personalizables
- Configuración YAML avanzada
- Scripts de automatización incluidos

### 🎯 Próximas Versiones

#### **v1.1.0 (Planeado)**
- Soporte para más formatos de salida (DOCX, EPUB)
- Integración con sistemas de control de versiones
- API REST para integración web
- Plugin para editores populares

#### **v1.2.0 (Planeado)**
- Soporte para diagramas Mermaid
- Integración con LaTeX para fórmulas matemáticas
- Sistema de plugins extensible
- Interfaz gráfica web

### 🙏 Agradecimientos

- **WeasyPrint** por el motor de renderizado PDF
- **Python-Markdown** por el procesamiento de Markdown
- **Pillow** por el procesamiento de imágenes
- **PyYAML** por el manejo de configuración
- **Requests** por el manejo de descargas HTTP
- **Colorama** por el output colorido en terminal

### 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

**¡Versión 1.0.0 lista para producción!** 🎉

Esta versión representa un conversor Markdown a PDF completo, profesional y listo para uso en producción con todas las funcionalidades principales implementadas y documentadas. 