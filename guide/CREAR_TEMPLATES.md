# 🎨 Crear Templates Personalizados

Esta guía te enseñará cómo crear templates personalizados para diferentes tipos de documentos.

## Conceptos Básicos

### ¿Qué es un Template?

Un template es una configuración completa que incluye:
- **Archivo CSS** - Estilos visuales del documento
- **Configuración YAML** - Parámetros de conversión
- **Metadatos por defecto** - Información del documento

## Estructura de un Template

```
templates/
├── mi_template/
│   ├── style.css          # Estilos del template
│   ├── config.yaml        # Configuración específica
│   └── README.md          # Documentación del template
```

## Crear CSS Personalizado

```css
/* templates/mi_template/style.css */

/* Variables CSS */
:root {
  --primary-color: #3498db;
  --secondary-color: #2c3e50;
  --accent-color: #e74c3c;
  
  --font-family: 'Arial', sans-serif;
  --font-size-base: 1rem;
  --line-height: 1.6;
  
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
}

/* Configuración de página */
@page {
  size: A4;
  margin: 2cm;
  
  @top-center {
    content: "Mi Template";
    font-size: 10pt;
    color: #666;
  }
  
  @bottom-center {
    content: counter(page);
    font-size: 10pt;
  }
}

/* Estilos base */
body {
  font-family: var(--font-family);
  font-size: var(--font-size-base);
  line-height: var(--line-height);
  color: #333;
  margin: 0;
  padding: 0;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
  color: var(--primary-color);
  margin-top: var(--spacing-lg);
  margin-bottom: var(--spacing-md);
  page-break-after: avoid;
}

h1 {
  font-size: 2.2em;
  border-bottom: 3px solid var(--primary-color);
  padding-bottom: var(--spacing-sm);
  text-align: center;
}

h2 {
  font-size: 1.8em;
  border-bottom: 2px solid var(--secondary-color);
  padding-bottom: var(--spacing-sm);
}

/* Párrafos y texto */
p {
  margin-bottom: var(--spacing-md);
  text-align: justify;
}

/* Listas */
ul, ol {
  margin-bottom: var(--spacing-md);
  padding-left: 2em;
}

li {
  margin-bottom: var(--spacing-sm);
}

/* Código */
code {
  background-color: #f8f9fa;
  color: var(--accent-color);
  padding: 0.2em 0.4em;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
  font-size: 0.9em;
  border: 1px solid #e9ecef;
}

pre {
  background-color: #2c3e50;
  color: #ecf0f1;
  padding: var(--spacing-lg);
  border-radius: 8px;
  border-left: 5px solid var(--primary-color);
  margin: var(--spacing-lg) 0;
  overflow-x: auto;
  page-break-inside: avoid;
}

pre code {
  background-color: transparent;
  color: inherit;
  padding: 0;
  border: none;
}

/* Tablas */
table {
  border-collapse: collapse;
  width: 100%;
  margin: var(--spacing-lg) 0;
  page-break-inside: avoid;
}

th, td {
  border: 1px solid #ddd;
  padding: 12px 15px;
  text-align: left;
  vertical-align: top;
}

th {
  background-color: var(--primary-color);
  color: white;
  font-weight: bold;
  text-transform: uppercase;
  font-size: 0.9em;
  letter-spacing: 0.5px;
}

tr:nth-child(even) {
  background-color: #f8f9fa;
}

/* Imágenes */
img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: var(--spacing-lg) auto;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  page-break-inside: avoid;
}

/* Enlaces */
a {
  color: var(--primary-color);
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: border-bottom-color 0.3s;
}

a:hover {
  border-bottom-color: var(--primary-color);
}

/* Blockquotes */
blockquote {
  border-left: 4px solid var(--primary-color);
  background-color: #f8f9fa;
  padding: var(--spacing-md) var(--spacing-lg);
  margin: var(--spacing-lg) 0;
  font-style: italic;
  color: #555;
  border-radius: 0 8px 8px 0;
}

/* Notas y advertencias */
.note {
  background-color: #e3f2fd;
  border-left: 4px solid var(--info);
  padding: var(--spacing-md);
  margin: var(--spacing-md) 0;
  border-radius: 4px;
}

.warning {
  background-color: #fff3e0;
  border-left: 4px solid var(--warning);
  padding: var(--spacing-md);
  margin: var(--spacing-md) 0;
  border-radius: 4px;
}

.error {
  background-color: #ffebee;
  border-left: 4px solid var(--error);
  padding: var(--spacing-md);
  margin: var(--spacing-md) 0;
  border-radius: 4px;
}

.success {
  background-color: #e8f5e8;
  border-left: 4px solid var(--success);
  padding: var(--spacing-md);
  margin: var(--spacing-md) 0;
  border-radius: 4px;
}

/* Tabla de contenidos */
.toc {
  background-color: #f8f9fa;
  border: 2px solid #dee2e6;
  border-radius: 8px;
  padding: 2em;
  margin: 2em 0;
  page-break-inside: avoid;
}

.toc h2 {
  color: var(--primary-color);
  border-bottom: 3px solid var(--primary-color);
  padding-bottom: 0.5em;
  margin-bottom: 1.5em;
  font-size: 1.5em;
  text-align: center;
}

.toc ul {
  list-style: none;
  padding-left: 0;
}

.toc li {
  margin-bottom: 0.5em;
  line-height: 1.4;
}

.toc a {
  color: var(--text-primary);
  text-decoration: none;
  transition: color 0.3s;
  display: block;
  padding: 0.2em 0;
}

.toc a:hover {
  color: var(--primary-color);
  background-color: #e3f2fd;
  border-radius: 4px;
  padding-left: 0.5em;
}

/* Sangrías por nivel en TOC */
.toc ul ul {
  padding-left: 1.5em;
}

.toc ul ul ul {
  padding-left: 3em;
}

/* Control de saltos de página */
.page-break {
  page-break-before: always;
}

.no-break {
  page-break-inside: avoid;
}

/* Estilos para impresión */
@media print {
  body {
    font-size: 12pt;
    line-height: 1.4;
  }
  
  h1 {
    font-size: 18pt;
    margin-top: 1em;
  }
  
  h2 {
    font-size: 14pt;
    margin-top: 0.8em;
  }
  
  h3 {
    font-size: 12pt;
    margin-top: 0.6em;
  }
  
  .no-print {
    display: none !important;
  }
  
  * {
    -webkit-print-color-adjust: exact;
    color-adjust: exact;
  }
}
```

## Configurar Template en YAML

```yaml
# config.yaml
templates:
  mi_template:
    # Archivo CSS
    style_file: "./templates/mi_template/style.css"
    
    # Configuración de página
    page_size: "A4"
    margins: "2cm"
    font_family: "Arial, sans-serif"
    language: "es"
    
    # Configuración de imágenes
    max_image_width: 800
    max_image_height: 600
    image_quality: 85
    download_remote_images: true
    
    # Configuración de TOC
    include_toc: true
    toc_levels: 3
    number_headings: false
    
    # Metadatos por defecto
    metadata:
      default_author: "Mi Empresa"
      default_title: "Documento"
      default_date_format: "%Y-%m-%d"
      include_creation_date: true
      include_modification_date: true
    
    # Validación específica
    validation:
      check_broken_links: true
      check_missing_images: true
      max_line_length: 100
```

## Uso de Templates

```bash
# Usar template personalizado
python cli/md_to_pdf_converter.py --file documento.md --template mi_template

# Ver templates disponibles
python cli/md_to_pdf_converter.py --list-templates

# Combinar con otras opciones
python cli/md_to_pdf_converter.py \
  --file documento.md \
  --template mi_template \
  --toc \
  --validate \
  --verbose
```

## Mejores Prácticas

### 1. Organización de Archivos
```
templates/
├── mi_template/
│   ├── style.css          # Estilos principales
│   ├── config.yaml        # Configuración
│   └── README.md          # Documentación
```

### 2. Nomenclatura Consistente
```css
/* ✅ Nomenclatura consistente */
:root {
  --primary-color: #3498db;
  --primary-dark: #2980b9;
  --primary-light: #5dade2;
  
  --text-primary: #2c3e50;
  --text-secondary: #7f8c8d;
  
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
}
```

### 3. Documentación
```markdown
# Template Mi Template

## Descripción
Template personalizado para documentación técnica.

## Uso
```bash
python cli/md_to_pdf_converter.py --template mi_template --file documento.md
```

## Configuración
- Tamaño de página: A4
- Márgenes: 2cm
- Fuente: Arial
```

## Recursos Adicionales

- [Guía de Inicio Rápido](INICIO_RAPIDO.md) - Comenzar con templates
- [Personalización de Paletas](PERSONALIZACION_PALETAS.md) - Colores y temas
- [CSS Personalización Avanzada](CSS_PERSONALIZACION_AVANZADA.md) - Estilos avanzados
- [Configuración Avanzada](CONFIGURACION_AVANZADA.md) - Configuración completa

---

**¿Necesitas ayuda?** Ejecuta `python cli/md_to_pdf_converter.py --help` 