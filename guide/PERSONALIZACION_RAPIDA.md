# 🎨 Personalización Rápida de Paletas

Esta guía te enseñará a personalizar rápidamente los colores y temas de tus documentos PDF en menos de 10 minutos.

## 🚀 Personalización en 3 Pasos

### **Paso 1: Elegir un Template Base**

```bash
# Listar templates disponibles
python cli/md_to_pdf_converter.py --list-templates

# Usar template claro (por defecto)
python cli/md_to_pdf_converter.py --template light

# Usar template oscuro
python cli/md_to_pdf_converter.py --template dark
```

### **Paso 2: Personalizar Colores Rápidamente**

Crea un archivo CSS personalizado `mi_paleta.css`:

```css
/* Paleta de colores personalizada */
:root {
  /* Colores principales */
  --primary-color: #3498db;      /* Azul principal */
  --secondary-color: #2ecc71;    /* Verde secundario */
  --accent-color: #e74c3c;       /* Rojo acento */
  
  /* Colores de texto */
  --text-primary: #2c3e50;       /* Texto principal */
  --text-secondary: #7f8c8d;     /* Texto secundario */
  --text-light: #ecf0f1;         /* Texto claro */
  
  /* Colores de fondo */
  --bg-primary: #ffffff;         /* Fondo principal */
  --bg-secondary: #f8f9fa;       /* Fondo secundario */
  --bg-accent: #e3f2fd;          /* Fondo acento */
  
  /* Colores de bordes */
  --border-color: #bdc3c7;       /* Bordes */
  --border-accent: #3498db;      /* Bordes acento */
}

/* Aplicar colores personalizados */
body {
  color: var(--text-primary);
  background-color: var(--bg-primary);
}

h1, h2, h3 {
  color: var(--primary-color);
  border-bottom-color: var(--border-accent);
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
  background-color: var(--bg-accent);
  border-left-color: var(--secondary-color);
}
```

### **Paso 3: Aplicar tu Paleta**

```bash
# Usar tu paleta personalizada
python cli/md_to_pdf_converter.py --style mi_paleta.css
```

## 🎯 Paletas Predefinidas Rápidas

### **🌊 Paleta Azul Profesional**
```css
:root {
  --primary-color: #1e3a8a;
  --secondary-color: #3b82f6;
  --accent-color: #06b6d4;
  --text-primary: #1e293b;
  --bg-primary: #ffffff;
  --bg-secondary: #f1f5f9;
}
```

### **🌿 Paleta Verde Naturaleza**
```css
:root {
  --primary-color: #059669;
  --secondary-color: #10b981;
  --accent-color: #34d399;
  --text-primary: #064e3b;
  --bg-primary: #ffffff;
  --bg-secondary: #f0fdf4;
}
```

### **🔥 Paleta Roja Energética**
```css
:root {
  --primary-color: #dc2626;
  --secondary-color: #ef4444;
  --accent-color: #f87171;
  --text-primary: #450a0a;
  --bg-primary: #ffffff;
  --bg-secondary: #fef2f2;
}
```

### **🟣 Paleta Púrpura Creativa**
```css
:root {
  --primary-color: #7c3aed;
  --secondary-color: #8b5cf6;
  --accent-color: #a78bfa;
  --text-primary: #2e1065;
  --bg-primary: #ffffff;
  --bg-secondary: #faf5ff;
}
```

## ⚡ Personalización Ultra Rápida

### **Cambiar Solo el Color Principal**
```css
/* Solo cambiar el color principal */
h1, h2, h3 {
  color: #your-color-here;
  border-bottom-color: #your-color-here;
}

code {
  color: #your-color-here;
}
```

### **Cambiar Solo el Fondo**
```css
/* Solo cambiar el fondo */
body {
  background-color: #your-bg-color;
}

pre, code {
  background-color: #your-secondary-bg;
}
```

### **Cambiar Solo los Enlaces**
```css
/* Solo cambiar enlaces */
a {
  color: #your-link-color;
}

a:hover {
  color: #your-hover-color;
}
```

## 🎨 Generador de Paletas Rápido

### **Script para Generar Paletas**
```bash
#!/bin/bash
# generar_paleta.sh

COLOR_PRIMARY=$1
COLOR_SECONDARY=$2
COLOR_ACCENT=$3
NOMBRE_PALETA=$4

cat > "${NOMBRE_PALETA}.css" << EOF
/* Paleta: ${NOMBRE_PALETA} */
:root {
  --primary-color: ${COLOR_PRIMARY};
  --secondary-color: ${COLOR_SECONDARY};
  --accent-color: ${COLOR_ACCENT};
  --text-primary: #2c3e50;
  --text-secondary: #7f8c8d;
  --bg-primary: #ffffff;
  --bg-secondary: #f8f9fa;
}

h1, h2, h3 { color: var(--primary-color); }
code { color: var(--accent-color); }
blockquote { border-left-color: var(--secondary-color); }
EOF

echo "✅ Paleta ${NOMBRE_PALETA}.css generada"
```

**Uso:**
```bash
# Generar paleta personalizada
./generar_paleta.sh "#3498db" "#2ecc71" "#e74c3c" "mi_paleta"

# Usar la paleta generada
python cli/md_to_pdf_converter.py --style mi_paleta.css
```

## 🔧 Configuración Rápida en YAML

### **Agregar Template Personalizado**
```yaml
# config.yaml
templates:
  mi_paleta:
    style_file: "./mi_paleta.css"
    page_size: "A4"
    margins: "2cm"
    font_family: "Arial, sans-serif"
    language: "es"
```

**Usar:**
```bash
python cli/md_to_pdf_converter.py --template mi_paleta
```

## 🎯 Casos de Uso Rápidos

### **📊 Reporte Ejecutivo**
```css
/* Paleta ejecutiva */
:root {
  --primary-color: #1e3a8a;    /* Azul corporativo */
  --secondary-color: #64748b;   /* Gris profesional */
  --accent-color: #dc2626;      /* Rojo para alertas */
}
```

### **🎓 Documento Académico**
```css
/* Paleta académica */
:root {
  --primary-color: #374151;     /* Gris oscuro */
  --secondary-color: #6b7280;   /* Gris medio */
  --accent-color: #059669;      /* Verde para citas */
}
```

### **🎨 Presentación Creativa**
```css
/* Paleta creativa */
:root {
  --primary-color: #7c3aed;     /* Púrpura */
  --secondary-color: #ec4899;   /* Rosa */
  --accent-color: #f59e0b;      /* Naranja */
}
```

### **📱 Documento Técnico**
```css
/* Paleta técnica */
:root {
  --primary-color: #059669;     /* Verde */
  --secondary-color: #3b82f6;   /* Azul */
  --accent-color: #dc2626;      /* Rojo para errores */
}
```

## 💡 Consejos Rápidos

### **✅ Mejores Prácticas**
- Usa máximo 3-4 colores principales
- Mantén contraste suficiente para legibilidad
- Usa colores semánticos (rojo para errores, verde para éxito)
- Prueba tu paleta con `--html` antes de generar PDF

### **⚡ Optimización**
- Reutiliza paletas exitosas
- Crea variaciones con diferentes saturaciones
- Usa herramientas online para generar paletas armónicas
- Guarda tus paletas favoritas como templates

### **🎯 Productividad**
- Crea paletas por tipo de documento
- Usa nombres descriptivos para tus paletas
- Mantén un archivo de referencia con todas tus paletas
- Comparte paletas con tu equipo

## 🔍 Solución de Problemas

### **❌ Colores no se aplican**
```bash
# Verificar que el archivo CSS existe
ls -la mi_paleta.css

# Verificar sintaxis CSS
python cli/md_to_pdf_converter.py --style mi_paleta.css --verbose
```

### **❌ Contraste insuficiente**
```css
/* Aumentar contraste */
:root {
  --text-primary: #000000;      /* Negro puro */
  --bg-primary: #ffffff;        /* Blanco puro */
}
```

### **❌ Colores no coinciden**
```bash
# Verificar que estás usando el archivo correcto
python cli/md_to_pdf_converter.py --style ./ruta/completa/mi_paleta.css
```

## 📚 Próximos Pasos

### **🎨 Personalización Avanzada**
1. **[PERSONALIZACION_PALETAS.md](PERSONALIZACION_PALETAS.md)** - Guía completa de personalización
2. **[CSS_PERSONALIZACION_AVANZADA.md](CSS_PERSONALIZACION_AVANZADA.md)** - CSS avanzado
3. **[CREAR_TEMPLATES.md](CREAR_TEMPLATES.md)** - Crear templates completos

### **🔧 Configuración**
1. **[INICIO_RAPIDO.md](INICIO_RAPIDO.md)** - Configuración básica
2. **[VALIDACION_GUIA.md](VALIDACION_GUIA.md)** - Validar documentos

---

**¡Ya puedes personalizar tus documentos en minutos!** 🎨

Consulta las guías avanzadas para personalización completa y profesional. 