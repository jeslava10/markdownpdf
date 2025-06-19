# 🎨 Personalización de Paletas de Colores

Esta guía te enseñará cómo crear y personalizar paletas de colores para tus documentos PDF, incluyendo temas claros, oscuros y personalizados.

## 📋 Contenido
- [Conceptos Básicos](#conceptos-básicos)
- [Paletas Predefinidas](#paletas-predefinidas)
- [Crear Paletas Personalizadas](#crear-paletas-personalizadas)
- [Temas Claros y Oscuros](#temas-claros-y-oscuros)
- [Variables CSS](#variables-css)
- [Ejemplos Prácticos](#ejemplos-prácticos)
- [Mejores Prácticas](#mejores-prácticas)

## 🎯 Conceptos Básicos

### ¿Qué es una Paleta de Colores?

Una paleta de colores es un conjunto de colores que definen la apariencia visual de tu documento:

- **Colores primarios** - Para elementos principales (títulos, enlaces)
- **Colores secundarios** - Para elementos de apoyo (bordes, fondos)
- **Colores de texto** - Para legibilidad y contraste
- **Colores de acento** - Para destacar información importante

### Estructura de una Paleta

```css
:root {
  /* Colores primarios */
  --primary-color: #3498db;
  --primary-dark: #2980b9;
  --primary-light: #5dade2;
  
  /* Colores secundarios */
  --secondary-color: #2c3e50;
  --secondary-light: #34495e;
  
  /* Colores de texto */
  --text-primary: #2c3e50;
  --text-secondary: #7f8c8d;
  --text-light: #ecf0f1;
  
  /* Colores de fondo */
  --bg-primary: #ffffff;
  --bg-secondary: #f8f9fa;
  --bg-accent: #e3f2fd;
  
  /* Colores de estado */
  --success: #27ae60;
  --warning: #f39c12;
  --error: #e74c3c;
  --info: #3498db;
}
```

## 🌈 Paletas Predefinidas

### Tema Claro (light.css)

```css
:root {
  /* Paleta principal */
  --primary-color: #3498db;
  --secondary-color: #2c3e50;
  
  /* Texto */
  --text-primary: #2c3e50;
  --text-secondary: #7f8c8d;
  
  /* Fondos */
  --bg-primary: #ffffff;
  --bg-secondary: #f8f9fa;
  --bg-accent: #e3f2fd;
  
  /* Estados */
  --success: #27ae60;
  --warning: #f39c12;
  --error: #e74c3c;
}
```

### Tema Oscuro (dark.css)

```css
:root {
  /* Paleta principal */
  --primary-color: #5dade2;
  --secondary-color: #ecf0f1;
  
  /* Texto */
  --text-primary: #ecf0f1;
  --text-secondary: #bdc3c7;
  
  /* Fondos */
  --bg-primary: #2c3e50;
  --bg-secondary: #34495e;
  --bg-accent: #1a252f;
  
  /* Estados */
  --success: #2ecc71;
  --warning: #f1c40f;
  --error: #e74c3c;
}
```

## 🎨 Crear Paletas Personalizadas

### Paso 1: Definir la Paleta Base

Crea un archivo CSS con tu paleta personalizada:

```css
/* mi_paleta.css */
:root {
  /* Paleta corporativa azul */
  --primary-color: #1a5f7a;
  --primary-dark: #0f4c63;
  --primary-light: #2d7a9a;
  
  /* Colores de apoyo */
  --secondary-color: #34495e;
  --accent-color: #e67e22;
  
  /* Texto */
  --text-primary: #2c3e50;
  --text-secondary: #7f8c8d;
  --text-light: #ecf0f1;
  
  /* Fondos */
  --bg-primary: #ffffff;
  --bg-secondary: #f8f9fa;
  --bg-accent: #e8f4f8;
  
  /* Estados */
  --success: #27ae60;
  --warning: #f39c12;
  --error: #e74c3c;
  --info: #3498db;
}
```

### Paso 2: Aplicar la Paleta

```css
/* Aplicar colores a elementos */
body {
  background-color: var(--bg-primary);
  color: var(--text-primary);
  font-family: 'Arial', sans-serif;
}

h1, h2, h3, h4, h5, h6 {
  color: var(--primary-color);
  border-bottom: 2px solid var(--primary-light);
}

a {
  color: var(--primary-color);
  text-decoration: none;
}

a:hover {
  color: var(--primary-dark);
  border-bottom: 1px solid var(--primary-color);
}

code {
  background-color: var(--bg-secondary);
  color: var(--accent-color);
  border: 1px solid var(--primary-light);
}

pre {
  background-color: var(--bg-accent);
  border-left: 4px solid var(--primary-color);
}

blockquote {
  background-color: var(--bg-accent);
  border-left: 4px solid var(--primary-color);
}
```

### Paso 3: Usar la Paleta

```bash
# Usar paleta personalizada
python cli/md_to_pdf_converter.py --file documento.md --style ./style/mi_paleta.css
```

## 🌓 Temas Claros y Oscuros

### Crear Tema Oscuro Personalizado

```css
/* tema_oscuro_personalizado.css */
:root {
  /* Paleta oscura personalizada */
  --primary-color: #5dade2;
  --primary-dark: #3498db;
  --primary-light: #85c1e9;
  
  /* Colores de texto */
  --text-primary: #ecf0f1;
  --text-secondary: #bdc3c7;
  --text-muted: #95a5a6;
  
  /* Fondos */
  --bg-primary: #2c3e50;
  --bg-secondary: #34495e;
  --bg-tertiary: #1a252f;
  --bg-accent: #1e3a5f;
  
  /* Estados */
  --success: #2ecc71;
  --warning: #f1c40f;
  --error: #e74c3c;
  --info: #3498db;
}

/* Aplicar colores */
body {
  background-color: var(--bg-primary);
  color: var(--text-primary);
}

h1, h2, h3, h4, h5, h6 {
  color: var(--primary-color);
  border-bottom: 2px solid var(--primary-light);
}

code {
  background-color: var(--bg-tertiary);
  color: var(--primary-light);
  border: 1px solid var(--primary-color);
}

pre {
  background-color: var(--bg-tertiary);
  border-left: 4px solid var(--primary-color);
}

table {
  background-color: var(--bg-secondary);
}

th {
  background-color: var(--bg-accent);
  color: var(--text-primary);
}

td {
  border: 1px solid var(--primary-color);
}
```

### Usar Tema Oscuro

```bash
# Usar tema oscuro predefinido
python cli/md_to_pdf_converter.py --file documento.md --theme dark

# Usar tema oscuro personalizado
python cli/md_to_pdf_converter.py --file documento.md --style ./style/tema_oscuro_personalizado.css
```

## 🔧 Variables CSS

### Sistema de Variables

```css
/* Definir variables base */
:root {
  /* Espaciado */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;
  
  /* Tipografía */
  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  
  /* Bordes */
  --border-radius-sm: 0.25rem;
  --border-radius-md: 0.5rem;
  --border-radius-lg: 1rem;
  
  /* Sombras */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
}
```

### Aplicar Variables

```css
/* Usar variables en elementos */
h1 {
  font-size: var(--font-size-2xl);
  margin-bottom: var(--spacing-lg);
  padding-bottom: var(--spacing-sm);
}

p {
  font-size: var(--font-size-base);
  margin-bottom: var(--spacing-md);
  line-height: 1.6;
}

code {
  padding: var(--spacing-xs) var(--spacing-sm);
  border-radius: var(--border-radius-sm);
  font-size: var(--font-size-sm);
}

pre {
  padding: var(--spacing-lg);
  border-radius: var(--border-radius-md);
  box-shadow: var(--shadow-md);
}

blockquote {
  padding: var(--spacing-md);
  margin: var(--spacing-lg) 0;
  border-radius: var(--border-radius-sm);
}
```

## 💡 Ejemplos Prácticos

### Paleta Corporativa

```css
/* paleta_corporativa.css */
:root {
  /* Colores de marca */
  --brand-primary: #1a5f7a;
  --brand-secondary: #e67e22;
  --brand-accent: #f39c12;
  
  /* Paleta completa */
  --primary-color: var(--brand-primary);
  --secondary-color: #34495e;
  --accent-color: var(--brand-secondary);
  
  /* Texto */
  --text-primary: #2c3e50;
  --text-secondary: #7f8c8d;
  
  /* Fondos */
  --bg-primary: #ffffff;
  --bg-secondary: #f8f9fa;
  --bg-accent: #e8f4f8;
  
  /* Estados */
  --success: #27ae60;
  --warning: var(--brand-accent);
  --error: #e74c3c;
  --info: var(--brand-primary);
}

/* Aplicación */
body {
  background-color: var(--bg-primary);
  color: var(--text-primary);
  font-family: 'Arial', sans-serif;
}

h1 {
  color: var(--brand-primary);
  border-bottom: 3px solid var(--brand-secondary);
}

h2 {
  color: var(--brand-primary);
  border-bottom: 2px solid var(--brand-accent);
}

a {
  color: var(--brand-primary);
}

a:hover {
  color: var(--brand-secondary);
}

.note {
  background-color: var(--bg-accent);
  border-left: 4px solid var(--brand-primary);
}

.warning {
  background-color: #fff3e0;
  border-left: 4px solid var(--brand-accent);
}
```

### Paleta Académica

```css
/* paleta_academica.css */
:root {
  /* Colores académicos */
  --primary-color: #2c3e50;
  --secondary-color: #34495e;
  --accent-color: #3498db;
  
  /* Texto */
  --text-primary: #2c3e50;
  --text-secondary: #7f8c8d;
  
  /* Fondos */
  --bg-primary: #ffffff;
  --bg-secondary: #f8f9fa;
  --bg-accent: #e3f2fd;
  
  /* Estados */
  --success: #27ae60;
  --warning: #f39c12;
  --error: #e74c3c;
  --info: #3498db;
}

/* Aplicación académica */
body {
  background-color: var(--bg-primary);
  color: var(--text-primary);
  font-family: 'Times New Roman', serif;
  font-size: 12pt;
  line-height: 1.6;
}

h1 {
  color: var(--primary-color);
  font-size: 18pt;
  font-weight: bold;
  text-align: center;
  margin-top: 2em;
  margin-bottom: 1em;
}

h2 {
  color: var(--primary-color);
  font-size: 14pt;
  font-weight: bold;
  margin-top: 1.5em;
}

h3 {
  color: var(--secondary-color);
  font-size: 12pt;
  font-weight: bold;
  margin-top: 1em;
}

blockquote {
  background-color: var(--bg-accent);
  border-left: 4px solid var(--accent-color);
  padding: 1em;
  margin: 1.5em 0;
  font-style: italic;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 1.5em 0;
}

th {
  background-color: var(--primary-color);
  color: white;
  font-weight: bold;
  padding: 8px 12px;
}

td {
  border: 1px solid #ddd;
  padding: 8px 12px;
}
```

### Paleta para Presentaciones

```css
/* paleta_presentacion.css */
:root {
  /* Colores vibrantes para presentaciones */
  --primary-color: #e74c3c;
  --secondary-color: #2c3e50;
  --accent-color: #f39c12;
  
  /* Texto */
  --text-primary: #2c3e50;
  --text-secondary: #7f8c8d;
  --text-light: #ecf0f1;
  
  /* Fondos */
  --bg-primary: #ffffff;
  --bg-secondary: #f8f9fa;
  --bg-accent: #fff3e0;
  
  /* Estados */
  --success: #27ae60;
  --warning: #f39c12;
  --error: #e74c3c;
  --info: #3498db;
}

/* Aplicación para presentaciones */
body {
  background-color: var(--bg-primary);
  color: var(--text-primary);
  font-family: 'Arial', sans-serif;
  line-height: 1.4;
}

h1 {
  color: var(--primary-color);
  font-size: 2.5em;
  text-align: center;
  margin-bottom: 1em;
  text-transform: uppercase;
  letter-spacing: 2px;
}

h2 {
  color: var(--secondary-color);
  font-size: 1.8em;
  margin-top: 1em;
  border-bottom: 2px solid var(--accent-color);
  padding-bottom: 0.3em;
}

h3 {
  color: var(--primary-color);
  font-size: 1.4em;
  margin-top: 0.8em;
}

p {
  font-size: 1.1em;
  margin-bottom: 0.8em;
}

ul, ol {
  font-size: 1.1em;
  margin-bottom: 1em;
}

li {
  margin-bottom: 0.3em;
}

blockquote {
  background-color: var(--bg-accent);
  border-left: 4px solid var(--accent-color);
  padding: 1em;
  margin: 1.5em 0;
  font-style: italic;
  font-size: 1.1em;
}

.note {
  background-color: #e3f2fd;
  border-left: 4px solid var(--info);
  padding: 1em;
  margin: 1em 0;
  border-radius: 4px;
}
```

## 🚀 Uso de Paletas

### Comandos Básicos

```bash
# Usar paleta predefinida
python cli/md_to_pdf_converter.py --file documento.md --theme light
python cli/md_to_pdf_converter.py --file documento.md --theme dark

# Usar paleta personalizada
python cli/md_to_pdf_converter.py --file documento.md --style ./style/mi_paleta.css

# Combinar con otras opciones
python cli/md_to_pdf_converter.py \
  --file documento.md \
  --style ./style/paleta_corporativa.css \
  --toc \
  --theme light
```

### Configuración en YAML

```yaml
# config.yaml
templates:
  corporativo:
    style_file: "./style/paleta_corporativa.css"
    page_size: "A4"
    margins: "2.5cm"
    
  academico:
    style_file: "./style/paleta_academica.css"
    page_size: "A4"
    margins: "3cm"
    
  presentacion:
    style_file: "./style/paleta_presentacion.css"
    page_size: "A4"
    margins: "1.5cm"
```

## 📋 Mejores Prácticas

### 1. Contraste y Legibilidad

```css
/* ✅ Buen contraste */
:root {
  --text-primary: #2c3e50;  /* Oscuro sobre claro */
  --bg-primary: #ffffff;
}

/* ❌ Mal contraste */
:root {
  --text-primary: #cccccc;  /* Gris claro sobre blanco */
  --bg-primary: #ffffff;
}
```

### 2. Consistencia de Colores

```css
/* ✅ Usar variables consistentemente */
h1, h2, h3 {
  color: var(--primary-color);
}

a {
  color: var(--primary-color);
}

/* ❌ Colores hardcodeados */
h1 { color: #3498db; }
h2 { color: #2980b9; }
a { color: #5dade2; }
```

### 3. Accesibilidad

```css
/* ✅ Colores accesibles */
:root {
  --text-primary: #2c3e50;  /* Alto contraste */
  --bg-primary: #ffffff;
  --link-color: #3498db;    /* Azul estándar */
}

/* ✅ Estados claros */
a:hover {
  color: var(--primary-dark);
  text-decoration: underline;
}

a:visited {
  color: var(--primary-light);
}
```

### 4. Organización del CSS

```css
/* ✅ Estructura organizada */
:root {
  /* 1. Variables de color */
  --primary-color: #3498db;
  --secondary-color: #2c3e50;
  
  /* 2. Variables de tipografía */
  --font-size-base: 1rem;
  --line-height: 1.6;
  
  /* 3. Variables de espaciado */
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  
  /* 4. Variables de estado */
  --success: #27ae60;
  --warning: #f39c12;
  --error: #e74c3c;
}
```

## 📚 Recursos Adicionales

- [Guía de Inicio Rápido](INICIO_RAPIDO.md) - Comenzar con temas
- [CSS Personalización Avanzada](CSS_PERSONALIZACION_AVANZADA.md) - Estilos avanzados
- [Configuración Avanzada](CONFIGURACION_AVANZADA.md) - Configuración de temas
- [Procesamiento de Imágenes](PROCESAMIENTO_IMAGENES.md) - Imágenes con temas

---

**¿Necesitas ayuda?** Ejecuta `python cli/md_to_pdf_converter.py --help` para ver todas las opciones de temas disponibles. 