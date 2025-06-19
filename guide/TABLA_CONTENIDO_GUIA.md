# 📋 Guía de Tabla de Contenidos Automática

La tabla de contenidos (TOC) se genera automáticamente basándose en los headings de tu documento Markdown, sin necesidad de configuración manual.

## ✨ Características de la TOC Automática

- ✅ **Generación automática**: Se crea basándose en los headings del documento
- ✅ **Posicionamiento inteligente**: Se inserta después del primer heading
- ✅ **Estilos profesionales**: Diseño integrado con el template técnico
- ✅ **Jerarquía visual**: Sangrías progresivas para diferentes niveles
- ✅ **Enlaces funcionales**: Navegación directa a cada sección
- ✅ **Sin configuración**: No requiere marcadores especiales

## 🚀 Uso Automático

### Conversión Normal
```bash
# La TOC se genera automáticamente
python md_to_pdf_converter.py --file documento.md
```

### Con Template Específico
```bash
# TOC con estilos del template técnico (por defecto)
python md_to_pdf_converter.py --file documento.md --template technical

# TOC con estilos de reporte
python md_to_pdf_converter.py --file documento.md --template report
```

## 📝 Estructura de Headings

### Jerarquía Soportada
La TOC reconoce hasta 6 niveles de headings:

```markdown
# Título Principal (H1) - Nivel 1
## Sección (H2) - Nivel 2
### Subsección (H3) - Nivel 3
#### Sub-subsección (H4) - Nivel 4
##### Detalle (H5) - Nivel 5
###### Específico (H6) - Nivel 6
```

### Ejemplo de Documento
```markdown
---
title: "Manual de Usuario"
author: "Equipo de Desarrollo"
date: 2024-06-18
---

# Introducción

Bienvenido al manual de usuario.

## Instalación

### Requisitos Previos

#### Sistema Operativo
- Windows 10 o superior
- macOS 10.14 o superior
- Linux Ubuntu 18.04 o superior

#### Dependencias
- Python 3.7+
- 4GB RAM mínimo

### Pasos de Instalación

#### Paso 1: Descargar
Descarga el instalador desde nuestro sitio web.

#### Paso 2: Ejecutar
Ejecuta el instalador con permisos de administrador.

## Configuración

### Configuración Básica

#### Usuario
Configura tu perfil de usuario.

#### Preferencias
Ajusta las preferencias del sistema.

### Configuración Avanzada

#### Red
Configuración de red y conectividad.

#### Seguridad
Opciones de seguridad y privacidad.

## Uso

### Funciones Principales

#### Crear Documento
Cómo crear un nuevo documento.

#### Editar Contenido
Técnicas de edición avanzada.

### Funciones Avanzadas

#### Automatización
Configurar tareas automáticas.

#### Integración
Integrar con otros sistemas.

## Solución de Problemas

### Problemas Comunes

#### Error de Conexión
Cómo resolver problemas de red.

#### Error de Permisos
Solución a problemas de permisos.

### Contacto

#### Soporte Técnico
Información de contacto para soporte.

#### FAQ
Preguntas frecuentes.
```

## 🎨 Estilos de la TOC

### Apariencia Visual
La TOC generada incluye:

- **Título**: "Tabla de Contenidos" con estilo destacado
- **Jerarquía visual**: Sangrías progresivas por nivel
- **Enlaces**: Números de página y enlaces directos
- **Separadores**: Líneas visuales entre secciones
- **Tipografía**: Consistente con el resto del documento

### Ejemplo de TOC Generada
```
Tabla de Contenidos

1. Introducción ......................... 1
2. Instalación .......................... 2
   2.1. Requisitos Previos ............. 2
       2.1.1. Sistema Operativo ........ 3
       2.1.2. Dependencias ............. 3
   2.2. Pasos de Instalación ........... 4
       2.2.1. Paso 1: Descargar ........ 4
       2.2.2. Paso 2: Ejecutar .......... 5
3. Configuración ........................ 6
   3.1. Configuración Básica ........... 6
       3.1.1. Usuario .................. 7
       3.1.2. Preferencias ............. 7
   3.2. Configuración Avanzada ......... 8
       3.2.1. Red ...................... 8
       3.2.2. Seguridad ................ 9
4. Uso .................................. 10
   4.1. Funciones Principales .......... 10
       4.1.1. Crear Documento .......... 11
       4.1.2. Editar Contenido .......... 12
   4.2. Funciones Avanzadas ............ 13
       4.2.1. Automatización ............ 13
       4.2.2. Integración ............... 14
5. Solución de Problemas ............... 15
   5.1. Problemas Comunes .............. 15
       5.1.1. Error de Conexión ........ 16
       5.1.2. Error de Permisos ........ 17
6. Contacto ............................. 18
   6.1. Soporte Técnico ................ 18
   6.2. FAQ ............................ 19
```

## 🔧 Personalización

### CSS Personalizado
Puedes personalizar la apariencia de la TOC con CSS:

```css
/* Estilos para la tabla de contenidos */
.toc {
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 5px;
    padding: 20px;
    margin: 20px 0;
}

.toc h2 {
    color: #2c3e50;
    border-bottom: 2px solid #3498db;
    padding-bottom: 10px;
    margin-bottom: 15px;
}

.toc ul {
    list-style: none;
    padding-left: 0;
}

.toc li {
    margin-bottom: 5px;
    line-height: 1.4;
}

.toc a {
    color: #2c3e50;
    text-decoration: none;
    transition: color 0.3s;
}

.toc a:hover {
    color: #3498db;
}

/* Sangrías por nivel */
.toc ul ul {
    padding-left: 20px;
}

.toc ul ul ul {
    padding-left: 40px;
}
```

### Usar CSS Personalizado
```bash
python md_to_pdf_converter.py --file documento.md --style ./style/toc_personalizada.css
```

## 📊 Mejores Prácticas

### Estructura de Headings
1. **Usa un solo H1** por documento
2. **Mantén jerarquía consistente**: H1 → H2 → H3
3. **Evita saltar niveles**: No uses H1 → H3 sin H2
4. **Usa títulos descriptivos** para mejor navegación
5. **Mantén profundidad razonable** (máximo 4-5 niveles)

### Ejemplo de Buena Estructura
```markdown
# Título Principal
## Sección 1
### Subsección 1.1
### Subsección 1.2
## Sección 2
### Subsección 2.1
#### Detalle 2.1.1
#### Detalle 2.1.2
### Subsección 2.2
```

### Ejemplo de Estructura Evitar
```markdown
# Título Principal
### Subsección (❌ Salta H2)
#### Detalle (❌ Demasiado profundo)
# Otro Título (❌ Múltiples H1)
```

## 🐛 Solución de Problemas

### TOC No Aparece
- **Causa**: No hay headings en el documento
- **Solución**: Agrega al menos un heading `# Título`

### TOC Vacía
- **Causa**: Headings mal formateados
- **Solución**: Verifica que los headings usen `#` correctamente

### Estructura Incorrecta
- **Causa**: Saltos en jerarquía de headings
- **Solución**: Usa H1 → H2 → H3 sin saltar niveles

### Validación de Estructura
```bash
# Validar estructura de headings
python md_to_pdf_converter.py --validate --file documento.md --verbose
```

## 📈 Beneficios de la TOC Automática

### Para el Usuario
- **Navegación fácil**: Encuentra secciones rápidamente
- **Vista general**: Entiende la estructura del documento
- **Acceso directo**: Enlaces a cada sección
- **Sin trabajo manual**: Se genera automáticamente

### Para el Autor
- **Ahorro de tiempo**: No necesita crear TOC manualmente
- **Consistencia**: Mismo formato en todos los documentos
- **Mantenimiento**: Se actualiza automáticamente al cambiar headings
- **Profesionalismo**: TOC con estilo profesional

## 🔮 Próximas Mejoras

### Funcionalidades Planificadas
- **TOC personalizable**: Opciones de formato y estilo
- **Niveles configurables**: Elegir qué niveles incluir
- **Estilos múltiples**: Diferentes estilos de TOC
- **Números de página**: Enlaces directos a páginas específicas

---

**¿Necesitas más ayuda?** Consulta las otras guías o ejecuta `python md_to_pdf_converter.py --help`

> **Nota:** La tabla de contenido generada automáticamente es compatible con títulos que incluyen emojis y con secciones que contienen imágenes SVG. Los emojis en títulos aparecerán en la TOC y los SVG se mostrarán correctamente en las secciones referenciadas. 