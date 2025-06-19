# 🖼️ Procesamiento Avanzado de Imágenes

Esta guía explica todas las funcionalidades de procesamiento de imágenes del conversor, incluyendo redimensionamiento automático, descarga de imágenes remotas, soporte SVG y optimización.

## 📋 Contenido
- [Características Principales](#características-principales)
- [Tipos de Imágenes Soportadas](#tipos-de-imágenes-soportadas)
- [Procesamiento Local](#procesamiento-local)
- [Procesamiento Remoto](#procesamiento-remoto)
- [Opciones de Configuración](#opciones-de-configuración)
- [Ejemplos Prácticos](#ejemplos-prácticos)
- [Solución de Problemas](#solución-de-problemas)

## ✨ Características Principales

### 🔧 Funcionalidades Disponibles
- **🔄 Redimensionamiento automático** - Ajusta imágenes grandes automáticamente
- **📥 Descarga remota** - Descarga imágenes de URLs automáticamente
- **💾 Embedding base64** - Embeber imágenes en el HTML
- **🎨 Optimización SVG** - Procesamiento especial para gráficos vectoriales
- **📊 Control de calidad** - Ajusta la compresión de imágenes
- **🖼️ Múltiples formatos** - PNG, JPG, GIF, SVG, WebP, BMP, TIFF

### 🚀 Beneficios
- **Archivos portables** - Las imágenes se incluyen en el PDF
- **Mejor rendimiento** - Imágenes optimizadas cargan más rápido
- **Calidad consistente** - Todas las imágenes tienen el mismo tamaño
- **Compatibilidad** - Funciona con cualquier fuente de imagen

## 📁 Tipos de Imágenes Soportadas

### Formatos Raster
- **PNG** - Imágenes con transparencia
- **JPG/JPEG** - Fotos y gráficos
- **GIF** - Animaciones simples
- **WebP** - Formato moderno de Google
- **BMP** - Formato básico de Windows
- **TIFF** - Formato de alta calidad

### Formatos Vectoriales
- **SVG** - Gráficos escalables (procesamiento especial)

## 🏠 Procesamiento Local

### Imágenes en el Sistema de Archivos

```markdown
# Imagen en el mismo directorio
![Logo](logo.png)

# Imagen en subdirectorio
![Diagrama](images/diagrama.png)

# Imagen con ruta absoluta
![Screenshot](/home/user/screenshots/app.png)
```

### Comando de Procesamiento

```bash
# Procesamiento básico
python cli/md_to_pdf_converter.py --file documento.md

# Con redimensionamiento específico
python cli/md_to_pdf_converter.py \
  --file documento.md \
  --max-image-width 800 \
  --max-image-height 600 \
  --image-quality 85
```

### Procesamiento Automático

El conversor automáticamente:
1. **Detecta** imágenes en el documento
2. **Redimensiona** si exceden los límites
3. **Optimiza** la calidad según la configuración
4. **Guarda** en `processed_images/` para reutilización

## 🌐 Procesamiento Remoto

### Descarga Automática de URLs

```markdown
# Imagen desde HTTP
![Logo Python](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

# Imagen desde HTTPS
![GitHub Logo](https://github.githubassets.com/images/modules/logos_page/GitHub-Logo.png)

# Imagen con protocolo relativo
![Logo](//example.com/logo.png)
```

### Comando para Descarga Remota

```bash
# Habilitar descarga remota
python cli/md_to_pdf_converter.py \
  --file documento.md \
  --download-remote-images

# Con configuración completa
python cli/md_to_pdf_converter.py \
  --file documento.md \
  --download-remote-images \
  --max-image-width 800 \
  --max-image-height 600 \
  --image-quality 85
```

### Proceso de Descarga

1. **Detecta** URLs de imágenes
2. **Descarga** a `downloaded_images/`
3. **Procesa** como imagen local
4. **Optimiza** según configuración
5. **Incluye** en el PDF final

## ⚙️ Opciones de Configuración

### Dimensiones de Imagen

```bash
# Ancho máximo (por defecto: 800px)
--max-image-width 600

# Alto máximo (por defecto: 600px)
--max-image-height 400

# Ambos valores
--max-image-width 800 --max-image-height 600
```

### Calidad de Imagen

```bash
# Calidad JPEG (1-100, por defecto: 85)
--image-quality 90

# Calidad alta para fotos
--image-quality 95

# Calidad baja para diagramas
--image-quality 70
```

### Embedding Base64

```bash
# Embeber imágenes en HTML
--embed-images

# Útil para archivos portables
python cli/md_to_pdf_converter.py \
  --file documento.md \
  --embed-images \
  --download-remote-images
```

## 🎨 Procesamiento SVG

### Características Especiales

Los archivos SVG reciben tratamiento especial:
- **Optimización** - Remoción de comentarios y espacios
- **Escalabilidad** - Mantiene calidad en cualquier tamaño
- **Tamaño reducido** - Archivos más pequeños
- **Compatibilidad** - Funciona en todos los navegadores

### Ejemplo SVG

```markdown
# SVG como imagen
![Diagrama de flujo](diagrama.svg)

# SVG con descripción
![Arquitectura del sistema](architecture.svg "Diagrama de arquitectura")
```

### Comando para SVG

```bash
# Procesamiento con SVG
python cli/md_to_pdf_converter.py \
  --file documento.md \
  --max-image-width 1200 \
  --max-image-height 800
```

## 💡 Ejemplos Prácticos

### Documento Técnico con Diagramas

```markdown
---
title: "Arquitectura del Sistema"
author: "Equipo de Desarrollo"
---

# 🏗️ Arquitectura del Sistema

## Diagrama General

![Arquitectura completa](https://example.com/architecture.png)

## Componentes Principales

### Frontend
![Frontend](frontend-diagram.svg)

### Backend
![Backend](backend-diagram.svg)

## Flujo de Datos

![Flujo de datos](https://example.com/data-flow.png)
```

### Comando de Conversión

```bash
python cli/md_to_pdf_converter.py \
  --file arquitectura.md \
  --toc \
  --download-remote-images \
  --max-image-width 1000 \
  --max-image-height 800 \
  --image-quality 90 \
  --theme light
```

### Documento de Presentación

```markdown
---
title: "Presentación del Proyecto"
---

# 📊 Métricas del Proyecto

## Gráfico de Progreso

![Progreso](https://charts.example.com/progress.png)

## Distribución de Tareas

![Tareas](task-distribution.svg)
```

### Comando para Presentación

```bash
python cli/md_to_pdf_converter.py \
  --file presentacion.md \
  --theme dark \
  --download-remote-images \
  --max-image-width 1200 \
  --max-image-height 900 \
  --image-quality 95
```

## 🔧 Configuración Avanzada

### Archivo de Configuración

```yaml
# config.yaml
default:
  # Configuración de imágenes
  max_image_width: 800
  max_image_height: 600
  image_quality: 85
  download_remote_images: false
  embed_images: false

templates:
  presentacion:
    max_image_width: 1200
    max_image_height: 900
    image_quality: 95
    download_remote_images: true
    
  tecnico:
    max_image_width: 800
    max_image_height: 600
    image_quality: 85
    download_remote_images: true
```

### Uso con Configuración

```bash
# Usar configuración por defecto
python cli/md_to_pdf_converter.py --file documento.md

# Usar template específico
python cli/md_to_pdf_converter.py --file documento.md --template presentacion

# Sobrescribir configuración
python cli/md_to_pdf_converter.py \
  --file documento.md \
  --template presentacion \
  --max-image-width 1500 \
  --image-quality 100
```

## 🚨 Solución de Problemas

### Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| "Imagen no encontrada" | Ruta incorrecta | Verifica la ruta relativa al archivo MD |
| "Error de red" | Problema de conexión | Verifica la conexión a internet |
| "Formato no soportado" | Formato de imagen | Convierte a PNG, JPG o SVG |
| "Archivo muy grande" | Imagen demasiado grande | Usa `--max-image-width/height` |
| "Error de descarga" | URL inválida o inaccesible | Verifica la URL y permisos |

### Comandos de Diagnóstico

```bash
# Validar documento con imágenes
python cli/md_to_pdf_converter.py --validate --verbose --file documento.md

# Verificar imágenes descargadas
ls -la downloaded_images/

# Verificar imágenes procesadas
ls -la processed_images/

# Revisar log de conversión
tail -f conversion.log
```

### Optimización de Rendimiento

```bash
# Para documentos con muchas imágenes
python cli/md_to_pdf_converter.py \
  --file documento.md \
  --max-image-width 600 \
  --max-image-height 400 \
  --image-quality 80

# Para documentos con imágenes remotas
python cli/md_to_pdf_converter.py \
  --file documento.md \
  --download-remote-images \
  --embed-images
```

## 📚 Recursos Adicionales

- [Guía de Inicio Rápido](INICIO_RAPIDO.md) - Comenzar con imágenes
- [CLI Completo](CLI_COMPLETO.md) - Todas las opciones de imagen
- [CSS Personalización](CSS_PERSONALIZACION_AVANZADA.md) - Estilos para imágenes
- [Configuración Avanzada](CONFIGURACION_AVANZADA.md) - Configuración de imágenes

---

**¿Necesitas ayuda?** Ejecuta `python cli/md_to_pdf_converter.py --help` para ver todas las opciones de imagen disponibles. 