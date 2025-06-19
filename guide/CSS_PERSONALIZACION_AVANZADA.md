# 🎨 Personalización Avanzada de CSS

Esta guía te enseñará cómo crear estilos CSS personalizados para control total del diseño de tus documentos PDF.

## 📋 Contenido
- [Estructura de CSS Personalizado](#estructura-de-css-personalizado)
- [Estilos de Página](#estilos-de-página)
- [Tipografía y Texto](#tipografía-y-texto)
- [Elementos de Markdown](#elementos-de-markdown)
- [Tabla de Contenidos Personalizada](#tabla-de-contenidos-personalizada)
- [Control de Saltos de Página](#control-de-saltos-de-página)
- [Estilos para Impresión](#estilos-para-impresión)
- [Ejemplos Prácticos](#ejemplos-prácticos)

## 🏗️ Estructura de CSS Personalizado

Crea un archivo CSS completo para control total del diseño:

```css
/* Configuración general del documento */
@page {
    size: A4;
    margin: 2cm;
    @top-center {
        content: "Mi Documento";
        font-size: 10pt;
        color: #666;
    }
    @bottom-center {
        content: counter(page);
        font-size: 10pt;
    }
}

/* Estilos del cuerpo del documento */
body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: #2c3e50;
    max-width: 100%;
    margin: 0;
    padding: 0;
}
```

## 📄 Estilos de Página

### Configuración de Página
```css
@page {
    size: A4;                    /* Tamaño: A4, Letter, Legal, etc. */
    margin: 2cm;                 /* Márgenes uniformes */
    margin-top: 2.5cm;           /* Márgenes específicos */
    margin-bottom: 2.5cm;
    margin-left: 2cm;
    margin-right: 2cm;
    
    /* Encabezado de página */
    @top-center {
        content: "Mi Documento";
        font-size: 10pt;
        color: #666;
    }
    
    /* Pie de página */
    @bottom-center {
        content: counter(page);
        font-size: 10pt;
    }
    
    /* Encabezado izquierdo */
    @top-left {
        content: "Capítulo " counter(chapter);
        font-size: 9pt;
    }
    
    /* Pie de página derecho */
    @bottom-right {
        content: "Página " counter(page) " de " counter(pages);
        font-size: 9pt;
    }
}
```

## 🔤 Tipografía y Texto

### Headings Personalizados
```css
h1 {
    color: #e74c3c;
    font-size: 2.5em;
    border-bottom: 4px solid #3498db;
    padding-bottom: 0.5em;
    margin-top: 2em;
    margin-bottom: 1em;
    page-break-after: avoid;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 2px;
}

h2 {
    color: #2c3e50;
    font-size: 1.8em;
    border-bottom: 2px solid #ecf0f1;
    padding-bottom: 0.3em;
    margin-top: 1.5em;
    margin-bottom: 0.8em;
    page-break-after: avoid;
}

h3 {
    color: #34495e;
    font-size: 1.4em;
    margin-top: 1.2em;
    margin-bottom: 0.6em;
    page-break-after: avoid;
    font-weight: 600;
}

h4, h5, h6 {
    color: #7f8c8d;
    margin-top: 1em;
    margin-bottom: 0.5em;
    page-break-after: avoid;
}
```

### Párrafos y Texto
```css
p {
    margin-bottom: 1em;
    text-align: justify;
    orphans: 3;              /* Mínimo líneas al inicio de página */
    widows: 3;               /* Mínimo líneas al final de página */
    line-height: 1.6;
    text-indent: 0;          /* Sin sangría */
}

/* Párrafos con sangría */
p.indented {
    text-indent: 2em;
}

/* Párrafos centrados */
p.centered {
    text-align: center;
    margin: 1em 0;
}
```

## 📝 Elementos de Markdown

### Listas Personalizadas
```css
ul, ol {
    margin-bottom: 1em;
    padding-left: 2em;
}

li {
    margin-bottom: 0.3em;
    line-height: 1.5;
}

/* Listas con bullets personalizados */
ul li::marker {
    color: #3498db;
    font-weight: bold;
}

/* Listas numeradas personalizadas */
ol {
    counter-reset: item;
}

ol li {
    counter-increment: item;
}

ol li::marker {
    content: counter(item) ". ";
    color: #e74c3c;
    font-weight: bold;
}
```

### Código con Resaltado
```css
code {
    background-color: #f8f9fa;
    color: #e74c3c;
    padding: 0.2em 0.4em;
    border-radius: 3px;
    font-family: 'Fira Code', 'Courier New', monospace;
    font-size: 0.9em;
    border: 1px solid #e9ecef;
}

pre {
    background-color: #2c3e50;
    color: #ecf0f1;
    padding: 1.5em;
    border-radius: 8px;
    border-left: 5px solid #3498db;
    margin: 1.5em 0;
    overflow-x: auto;
    page-break-inside: avoid;
    font-family: 'Fira Code', 'Courier New', monospace;
    font-size: 0.9em;
    line-height: 1.4;
}

pre code {
    background-color: transparent;
    color: inherit;
    padding: 0;
    border: none;
    font-size: inherit;
}
```

### Tablas Profesionales
```css
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1.5em 0;
    page-break-inside: avoid;
    font-size: 0.9em;
}

th, td {
    border: 1px solid #ddd;
    padding: 12px 15px;
    text-align: left;
    vertical-align: top;
}

th {
    background-color: #34495e;
    color: white;
    font-weight: bold;
    text-transform: uppercase;
    font-size: 0.9em;
    letter-spacing: 0.5px;
}

tr:nth-child(even) {
    background-color: #f8f9fa;
}

tr:hover {
    background-color: #e3f2fd;
}

/* Tablas responsivas */
@media print {
    table {
        font-size: 8pt;
    }
    
    th, td {
        padding: 6px 8px;
    }
}
```

### Imágenes
```css
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 1.5em auto;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    page-break-inside: avoid;
}

/* Imágenes con caption */
figure {
    margin: 2em 0;
    text-align: center;
    page-break-inside: avoid;
}

figcaption {
    font-style: italic;
    color: #666;
    margin-top: 0.5em;
    font-size: 0.9em;
}
```

### Enlaces
```css
a {
    color: #3498db;
    text-decoration: none;
    border-bottom: 1px solid transparent;
    transition: border-bottom-color 0.3s;
}

a:hover {
    border-bottom-color: #3498db;
}

/* Enlaces externos */
a[href^="http"]::after {
    content: " ↗";
    font-size: 0.8em;
    color: #666;
}
```

### Citas y Blockquotes
```css
blockquote {
    border-left: 4px solid #3498db;
    background-color: #f8f9fa;
    padding: 1em 1.5em;
    margin: 1.5em 0;
    font-style: italic;
    color: #555;
    border-radius: 0 8px 8px 0;
}

blockquote::before {
    content: '"';
    font-size: 3em;
    color: #3498db;
    float: left;
    margin-right: 0.2em;
    line-height: 0.8;
}
```

### Notas y Advertencias
```css
.note {
    background-color: #e3f2fd;
    border-left: 4px solid #2196f3;
    padding: 1em;
    margin: 1em 0;
    border-radius: 4px;
}

.warning {
    background-color: #fff3e0;
    border-left: 4px solid #ff9800;
    padding: 1em;
    margin: 1em 0;
    border-radius: 4px;
}

.error {
    background-color: #ffebee;
    border-left: 4px solid #f44336;
    padding: 1em;
    margin: 1em 0;
    border-radius: 4px;
}

.success {
    background-color: #e8f5e8;
    border-left: 4px solid #4caf50;
    padding: 1em;
    margin: 1em 0;
    border-radius: 4px;
}
```

## 📑 Tabla de Contenidos Personalizada

```css
.toc {
    background-color: #f8f9fa;
    border: 2px solid #dee2e6;
    border-radius: 8px;
    padding: 2em;
    margin: 2em 0;
    page-break-inside: avoid;
}

.toc h2 {
    color: #2c3e50;
    border-bottom: 3px solid #3498db;
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
    color: #2c3e50;
    text-decoration: none;
    transition: color 0.3s;
    display: block;
    padding: 0.2em 0;
}

.toc a:hover {
    color: #3498db;
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

/* Numeración en TOC */
.toc li::before {
    content: counter(toc-counter) ". ";
    counter-increment: toc-counter;
    color: #3498db;
    font-weight: bold;
}
```

## 📄 Control de Saltos de Página

```css
/* Forzar salto de página */
.page-break {
    page-break-before: always;
}

/* Evitar salto de página */
.no-break {
    page-break-inside: avoid;
}

/* Evitar salto después de elementos */
h1, h2, h3, h4, h5, h6 {
    page-break-after: avoid;
}

/* Evitar salto antes de elementos */
table, pre, blockquote, figure {
    page-break-inside: avoid;
}

/* Salto de página después de secciones importantes */
.chapter {
    page-break-before: always;
}

.section {
    page-break-before: auto;
}
```

## 🖨️ Estilos para Impresión

```css
@media print {
    /* Configuración general para impresión */
    body {
        font-size: 12pt;
        line-height: 1.4;
    }
    
    /* Headings para impresión */
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
    
    /* Ocultar elementos en impresión */
    .no-print {
        display: none !important;
    }
    
    /* Ajustar colores para impresión */
    * {
        -webkit-print-color-adjust: exact;
        color-adjust: exact;
    }
    
    /* Optimizar tablas para impresión */
    table {
        font-size: 10pt;
    }
    
    th, td {
        padding: 4px 6px;
    }
}
```

## 💡 Ejemplos Prácticos

### CSS Corporativo
```css
/* Estilo corporativo profesional */
@page {
    size: A4;
    margin: 2.5cm;
    @top-center {
        content: "Mi Empresa - Documento Interno";
        font-size: 9pt;
        color: #666;
    }
    @bottom-center {
        content: "Página " counter(page);
        font-size: 9pt;
    }
}

body {
    font-family: 'Arial', sans-serif;
    line-height: 1.5;
    color: #333;
}

h1 {
    color: #1a5f7a;
    font-size: 2.2em;
    border-bottom: 3px solid #1a5f7a;
    text-align: center;
    margin-top: 2em;
}
```

### CSS Académico
```css
/* Estilo académico formal */
@page {
    size: A4;
    margin: 3cm;
    @bottom-center {
        content: counter(page);
        font-size: 10pt;
    }
}

body {
    font-family: 'Times New Roman', serif;
    line-height: 1.6;
    color: #000;
    font-size: 12pt;
}

h1 {
    font-size: 16pt;
    font-weight: bold;
    text-align: center;
    margin-top: 2em;
    margin-bottom: 1em;
}

h2 {
    font-size: 14pt;
    font-weight: bold;
    margin-top: 1.5em;
}
```

### CSS para Presentaciones
```css
/* Estilo para presentaciones */
@page {
    size: A4 landscape;
    margin: 1.5cm;
}

body {
    font-family: 'Arial', sans-serif;
    line-height: 1.4;
    color: #333;
}

h1 {
    font-size: 2.5em;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 1em;
}

h2 {
    font-size: 1.8em;
    color: #34495e;
    margin-top: 1em;
}

p {
    font-size: 1.1em;
    margin-bottom: 0.8em;
}
```

## 🚀 Uso del CSS Personalizado

```bash
# Usar CSS personalizado
python md_to_pdf_converter.py --file documento.md --style ./style/mi_estilo.css

# Usar template con CSS específico
python md_to_pdf_converter.py --file documento.md --template corporativo

# Convertir múltiples archivos con el mismo estilo
python md_to_pdf_converter.py --input ./documentos --style ./style/corporativo.css
```

## 📚 Recursos Adicionales

- [Guía de Inicio Rápido](INICIO_RAPIDO.md) - Para comenzar rápidamente
- [Guía de Configuración](CONFIGURACION_AVANZADA.md) - Configuración avanzada
- [Guía de Validación](VALIDACION_GUIA.md) - Validación de documentos

---

**¿Necesitas ayuda?** Ejecuta `python md_to_pdf_converter.py --help` para ver todas las opciones disponibles. 