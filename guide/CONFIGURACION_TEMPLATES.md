# ⚙️ Configuración de Templates

Esta guía te enseñará a crear, configurar y gestionar templates personalizados para diferentes tipos de documentos.

## 🎯 ¿Qué son los Templates?

Los **templates** son configuraciones predefinidas que incluyen:
- Archivo CSS específico
- Configuración de página (tamaño, márgenes)
- Fuentes personalizadas
- Configuración de imágenes
- Configuración de TOC
- Metadatos por defecto

## 🚀 Templates Predefinidos

### **Listar Templates Disponibles**
```bash
python cli/md_to_pdf_converter.py --list-templates
```

### **Templates Incluidos**

#### **🌞 Template Light (Claro)**
```bash
python cli/md_to_pdf_converter.py --template light
```

**Características:**
- Fondo blanco
- Texto oscuro
- Colores azules para headings
- Ideal para documentos técnicos

#### **🌙 Template Dark (Oscuro)**
```bash
python cli/md_to_pdf_converter.py --template dark
```

**Características:**
- Fondo oscuro
- Texto claro
- Colores vibrantes
- Ideal para presentaciones

## 🛠️ Crear Template Personalizado

### **Paso 1: Crear Archivo CSS**
```css
/* templates/mi_template.css */
:root {
  /* Colores del template */
  --primary-color: #1e3a8a;
  --secondary-color: #3b82f6;
  --accent-color: #06b6d4;
  --text-primary: #1e293b;
  --text-secondary: #64748b;
  --bg-primary: #ffffff;
  --bg-secondary: #f1f5f9;
  --border-color: #e2e8f0;
}

/* Estilos del template */
body {
  font-family: 'Inter', 'Segoe UI', sans-serif;
  line-height: 1.7;
  color: var(--text-primary);
  background-color: var(--bg-primary);
}

h1, h2, h3, h4, h5, h6 {
  color: var(--primary-color);
  font-weight: 600;
  margin-top: 2em;
  margin-bottom: 1em;
}

h1 {
  font-size: 2.5em;
  border-bottom: 3px solid var(--primary-color);
  padding-bottom: 0.5em;
}

h2 {
  font-size: 2em;
  border-bottom: 2px solid var(--border-color);
  padding-bottom: 0.3em;
}

code {
  background-color: var(--bg-secondary);
  color: var(--accent-color);
  padding: 0.2em 0.4em;
  border-radius: 4px;
  font-family: 'Fira Code', 'Courier New', monospace;
}

pre {
  background-color: var(--bg-secondary);
  border-left: 4px solid var(--primary-color);
  padding: 1.5em;
  border-radius: 6px;
  overflow-x: auto;
}

blockquote {
  background-color: var(--bg-secondary);
  border-left: 4px solid var(--secondary-color);
  padding: 1em 1.5em;
  margin: 1.5em 0;
  font-style: italic;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 1.5em 0;
}

th, td {
  border: 1px solid var(--border-color);
  padding: 12px;
  text-align: left;
}

th {
  background-color: var(--primary-color);
  color: white;
  font-weight: 600;
}

tr:nth-child(even) {
  background-color: var(--bg-secondary);
}
```

### **Paso 2: Configurar Template en YAML**
```yaml
# config.yaml
templates:
  mi_template:
    style_file: "./templates/mi_template.css"
    page_size: "A4"
    margins: "2.5cm"
    font_family: "Inter, Segoe UI, sans-serif"
    language: "es"
    
    # Configuración de imágenes
    max_image_width: 1000
    max_image_height: 800
    image_quality: 90
    download_remote_images: true
    embed_images: false
    
    # Configuración de TOC
    include_toc: true
    toc_levels: 4
    number_headings: true
```

### **Paso 3: Usar el Template**
```bash
# Usar template personalizado
python cli/md_to_pdf_converter.py --template mi_template

# Con validación
python cli/md_to_pdf_converter.py --template mi_template --validate
```

## 📋 Templates por Tipo de Documento

### **📊 Template para Reportes Ejecutivos**
```yaml
templates:
  ejecutivo:
    style_file: "./templates/ejecutivo.css"
    page_size: "A4"
    margins: "3cm"
    font_family: "Times New Roman, serif"
    language: "es"
    include_toc: true
    toc_levels: 3
    number_headings: true
```

**CSS correspondiente:**
```css
/* templates/ejecutivo.css */
:root {
  --primary-color: #1e3a8a;      /* Azul corporativo */
  --secondary-color: #64748b;     /* Gris profesional */
  --accent-color: #dc2626;        /* Rojo para alertas */
  --text-primary: #1e293b;
  --bg-primary: #ffffff;
  --bg-secondary: #f8fafc;
}

body {
  font-family: 'Times New Roman', serif;
  line-height: 1.8;
  text-align: justify;
}

h1 {
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 2px;
}

/* Estilos para tablas ejecutivas */
table {
  border: 2px solid var(--primary-color);
}

th {
  background-color: var(--primary-color);
  color: white;
  text-transform: uppercase;
  font-size: 0.9em;
}
```

### **🎓 Template para Documentos Académicos**
```yaml
templates:
  academico:
    style_file: "./templates/academico.css"
    page_size: "A4"
    margins: "3.5cm"
    font_family: "Times New Roman, serif"
    language: "es"
    include_toc: true
    toc_levels: 5
    number_headings: true
```

**CSS correspondiente:**
```css
/* templates/academico.css */
:root {
  --primary-color: #374151;       /* Gris oscuro */
  --secondary-color: #6b7280;     /* Gris medio */
  --accent-color: #059669;        /* Verde para citas */
  --text-primary: #111827;
  --bg-primary: #ffffff;
  --bg-secondary: #f9fafb;
}

body {
  font-family: 'Times New Roman', serif;
  line-height: 2;
  text-align: justify;
}

h1, h2, h3 {
  font-weight: bold;
  text-align: left;
}

/* Estilos para citas académicas */
blockquote {
  font-style: italic;
  border-left: 4px solid var(--accent-color);
  background-color: var(--bg-secondary);
  padding: 1.5em;
  margin: 2em 0;
}

/* Numeración de páginas */
@page {
  @bottom-center {
    content: counter(page);
    font-size: 10pt;
  }
}
```

### **🎨 Template para Presentaciones**
```yaml
templates:
  presentacion:
    style_file: "./templates/presentacion.css"
    page_size: "A4 landscape"
    margins: "2cm"
    font_family: "Arial, sans-serif"
    language: "es"
    include_toc: false
    number_headings: false
```

**CSS correspondiente:**
```css
/* templates/presentacion.css */
:root {
  --primary-color: #7c3aed;       /* Púrpura */
  --secondary-color: #ec4899;     /* Rosa */
  --accent-color: #f59e0b;        /* Naranja */
  --text-primary: #1f2937;
  --bg-primary: #ffffff;
  --bg-secondary: #f3f4f6;
}

body {
  font-family: 'Arial', sans-serif;
  line-height: 1.6;
  text-align: center;
}

h1 {
  font-size: 3em;
  color: var(--primary-color);
  text-align: center;
  margin-bottom: 1em;
}

h2 {
  font-size: 2.2em;
  color: var(--secondary-color);
  text-align: center;
}

/* Estilos para slides */
.slide {
  page-break-after: always;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
```

### **📱 Template para Documentación Técnica**
```yaml
templates:
  tecnico:
    style_file: "./templates/tecnico.css"
    page_size: "A4"
    margins: "2cm"
    font_family: "Consolas, 'Courier New', monospace"
    language: "es"
    include_toc: true
    toc_levels: 4
    number_headings: true
```

**CSS correspondiente:**
```css
/* templates/tecnico.css */
:root {
  --primary-color: #059669;       /* Verde */
  --secondary-color: #3b82f6;     /* Azul */
  --accent-color: #dc2626;        /* Rojo para errores */
  --text-primary: #1f2937;
  --bg-primary: #ffffff;
  --bg-secondary: #f8fafc;
}

body {
  font-family: 'Consolas', 'Courier New', monospace;
  line-height: 1.6;
}

code {
  font-family: 'Fira Code', 'Consolas', monospace;
  background-color: var(--bg-secondary);
  color: var(--accent-color);
  padding: 0.3em 0.6em;
  border-radius: 4px;
  font-size: 0.9em;
}

pre {
  background-color: #1f2937;
  color: #f9fafb;
  border-left: 4px solid var(--primary-color);
  padding: 1.5em;
  border-radius: 6px;
  overflow-x: auto;
}

/* Estilos para diagramas */
.diagram {
  text-align: center;
  margin: 2em 0;
  padding: 1em;
  background-color: var(--bg-secondary);
  border-radius: 8px;
}
```

## 🔧 Gestión de Templates

### **Crear Template desde Línea de Comandos**
```bash
#!/bin/bash
# crear_template.sh

NOMBRE_TEMPLATE=$1
COLOR_PRIMARY=$2
COLOR_SECONDARY=$3
COLOR_ACCENT=$4

# Crear directorio de templates
mkdir -p templates

# Crear CSS del template
cat > "templates/${NOMBRE_TEMPLATE}.css" << EOF
/* Template: ${NOMBRE_TEMPLATE} */
:root {
  --primary-color: ${COLOR_PRIMARY};
  --secondary-color: ${COLOR_SECONDARY};
  --accent-color: ${COLOR_ACCENT};
  --text-primary: #1f2937;
  --text-secondary: #6b7280;
  --bg-primary: #ffffff;
  --bg-secondary: #f9fafb;
  --border-color: #e5e7eb;
}

body {
  font-family: 'Arial', sans-serif;
  line-height: 1.6;
  color: var(--text-primary);
  background-color: var(--bg-primary);
}

h1, h2, h3 {
  color: var(--primary-color);
  border-bottom-color: var(--border-color);
}

code {
  background-color: var(--bg-secondary);
  color: var(--accent-color);
}

pre {
  background-color: var(--bg-secondary);
  border-left-color: var(--primary-color);
}

blockquote {
  background-color: var(--bg-secondary);
  border-left-color: var(--secondary-color);
}
EOF

# Agregar a config.yaml
cat >> config.yaml << EOF

  ${NOMBRE_TEMPLATE}:
    style_file: "./templates/${NOMBRE_TEMPLATE}.css"
    page_size: "A4"
    margins: "2cm"
    font_family: "Arial, sans-serif"
    language: "es"
    include_toc: false
    toc_levels: 3
    number_headings: false
EOF

echo "✅ Template '${NOMBRE_TEMPLATE}' creado exitosamente"
echo "📝 Usa: python cli/md_to_pdf_converter.py --template ${NOMBRE_TEMPLATE}"
```

**Uso:**
```bash
# Crear template personalizado
./crear_template.sh "mi_proyecto" "#1e3a8a" "#3b82f6" "#06b6d4"

# Usar el template creado
python cli/md_to_pdf_converter.py --template mi_proyecto
```

### **Listar y Gestionar Templates**
```bash
#!/bin/bash
# gestionar_templates.sh

case $1 in
  "listar")
    echo "📋 Templates disponibles:"
    python cli/md_to_pdf_converter.py --list-templates
    ;;
  "crear")
    ./crear_template.sh $2 $3 $4 $5
    ;;
  "eliminar")
    rm -f "templates/${2}.css"
    echo "🗑️ Template '${2}' eliminado"
    ;;
  "copiar")
    cp "templates/${2}.css" "templates/${3}.css"
    echo "📋 Template '${2}' copiado como '${3}'"
    ;;
  *)
    echo "Uso: $0 {listar|crear|eliminar|copiar}"
    ;;
esac
```

## 🎯 Casos de Uso Avanzados

### **Template para Marca Corporativa**
```yaml
templates:
  corporativo:
    style_file: "./templates/corporativo.css"
    page_size: "A4"
    margins: "2.5cm"
    font_family: "Helvetica Neue, Arial, sans-serif"
    language: "es"
    include_toc: true
    toc_levels: 3
    number_headings: true
```

### **Template para Manuales de Usuario**
```yaml
templates:
  manual:
    style_file: "./templates/manual.css"
    page_size: "A4"
    margins: "2cm"
    font_family: "Segoe UI, Arial, sans-serif"
    language: "es"
    include_toc: true
    toc_levels: 4
    number_headings: true
```

### **Template para Tesis Doctorales**
```yaml
templates:
  tesis:
    style_file: "./templates/tesis.css"
    page_size: "A4"
    margins: "4cm"
    font_family: "Times New Roman, serif"
    language: "es"
    include_toc: true
    toc_levels: 6
    number_headings: true
```

## 💡 Consejos para Templates

### **✅ Mejores Prácticas**
- Usa nombres descriptivos para tus templates
- Mantén consistencia en la estructura CSS
- Documenta las características de cada template
- Prueba templates con diferentes tipos de contenido

### **⚡ Optimización**
- Reutiliza estilos comunes entre templates
- Usa variables CSS para fácil personalización
- Optimiza para impresión y pantalla
- Considera accesibilidad en tus templates

### **🎯 Productividad**
- Crea templates para proyectos repetitivos
- Comparte templates con tu equipo
- Mantén un archivo de referencia con todos los templates
- Automatiza la creación de templates

## 🔍 Solución de Problemas

### **❌ Template no encontrado**
```bash
# Verificar que el template existe en config.yaml
grep -A 10 "templates:" config.yaml

# Verificar que el archivo CSS existe
ls -la templates/mi_template.css
```

### **❌ Estilos no se aplican**
```bash
# Verificar sintaxis CSS
python cli/md_to_pdf_converter.py --template mi_template --verbose

# Verificar ruta del archivo CSS
python cli/md_to_pdf_converter.py --style ./templates/mi_template.css
```

### **❌ Configuración no se carga**
```bash
# Verificar sintaxis YAML
python -c "import yaml; yaml.safe_load(open('config.yaml'))"

# Verificar estructura del template
cat config.yaml | grep -A 15 "mi_template:"
```

## 📚 Próximos Pasos

### **🎨 Personalización Avanzada**
1. **[PERSONALIZACION_RAPIDA.md](PERSONALIZACION_RAPIDA.md)** - Personalización rápida de colores
2. **[PERSONALIZACION_PALETAS.md](PERSONALIZACION_PALETAS.md)** - Guía completa de personalización
3. **[CSS_PERSONALIZACION_AVANZADA.md](CSS_PERSONALIZACION_AVANZADA.md)** - CSS avanzado

### **🔧 Configuración**
1. **[INICIO_RAPIDO.md](INICIO_RAPIDO.md)** - Configuración básica
2. **[VALIDACION_GUIA.md](VALIDACION_GUIA.md)** - Validar documentos

---

**¡Ya puedes crear templates profesionales para cualquier tipo de documento!** ⚙️

Consulta las guías avanzadas para personalización completa y profesional. 