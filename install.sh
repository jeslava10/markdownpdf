#!/bin/bash

# Script de instalación mejorado para el conversor Markdown a PDF
# Autor: Generado automáticamente
# Fecha: 2024

set -e  # Salir si hay algún error

echo "🚀 Instalando conversor Markdown a PDF con mejoras..."

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para imprimir mensajes con colores
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Detectar sistema operativo
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]]; then
        OS="windows"
    else
        OS="unknown"
    fi
    print_status "Sistema operativo detectado: $OS"
}

# Verificar si Python está instalado
check_python() {
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
        print_success "Python $PYTHON_VERSION encontrado"
        return 0
    elif command -v python &> /dev/null; then
        PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
        print_success "Python $PYTHON_VERSION encontrado"
        return 0
    else
        print_error "Python no está instalado. Por favor, instala Python 3.7 o superior."
        return 1
    fi
}

# Instalar dependencias del sistema (macOS)
install_system_dependencies_macos() {
    if command -v brew &> /dev/null; then
        print_status "Instalando dependencias del sistema con Homebrew..."
        brew install pango gdk-pixbuf libffi
        print_success "Dependencias del sistema instaladas"
    else
        print_warning "Homebrew no está instalado. Instalando dependencias manualmente..."
        # Instalar dependencias manualmente si es necesario
        if ! pkg-config --exists pango; then
            print_error "Pango no está instalado. Por favor, instala las dependencias manualmente."
            return 1
        fi
    fi
}

# Instalar dependencias del sistema (Linux)
install_system_dependencies_linux() {
    if command -v apt-get &> /dev/null; then
        print_status "Instalando dependencias del sistema con apt-get..."
        sudo apt-get update
        sudo apt-get install -y python3-pip python3-dev build-essential \
            libpango1.0-dev libcairo2-dev libgdk-pixbuf2.0-dev libffi-dev
    elif command -v yum &> /dev/null; then
        print_status "Instalando dependencias del sistema con yum..."
        sudo yum install -y python3-pip python3-devel gcc \
            pango-devel cairo-devel gdk-pixbuf2-devel libffi-devel
    elif command -v dnf &> /dev/null; then
        print_status "Instalando dependencias del sistema con dnf..."
        sudo dnf install -y python3-pip python3-devel gcc \
            pango-devel cairo-devel gdk-pixbuf2-devel libffi-devel
    else
        print_warning "No se pudo detectar el gestor de paquetes. Instala las dependencias manualmente."
    fi
}

# Crear entorno virtual
create_virtual_environment() {
    if [ ! -d "venv" ]; then
        print_status "Creando entorno virtual..."
        python3 -m venv venv
        print_success "Entorno virtual creado"
    else
        print_status "Entorno virtual ya existe"
    fi
    
    print_status "Activando entorno virtual..."
    source venv/bin/activate
    print_success "Entorno virtual activado"
}

# Instalar dependencias de Python
install_python_dependencies() {
    print_status "Actualizando pip..."
    pip install --upgrade pip
    
    print_status "Instalando dependencias de Python..."
    pip install -r requirements.txt
    
    print_success "Dependencias de Python instaladas"
}

# Crear directorios necesarios
create_directories() {
    print_status "Creando directorios necesarios..."
    
    mkdir -p conversion
    mkdir -p output
    mkdir -p estilos
    
    print_success "Directorios creados"
}

# Verificar instalación
verify_installation() {
    print_status "Verificando instalación..."
    
    # Verificar que las dependencias están instaladas
    python3 -c "import markdown, weasyprint, yaml, click, watchdog" 2>/dev/null
    if [ $? -eq 0 ]; then
        print_success "Todas las dependencias están instaladas correctamente"
    else
        print_error "Algunas dependencias no están instaladas correctamente"
        return 1
    fi
    
    # Verificar que el script principal funciona
    python3 md_to_pdf_converter.py --help >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        print_success "Script principal funciona correctamente"
    else
        print_error "El script principal no funciona correctamente"
        return 1
    fi
    
    return 0
}

# Mostrar información post-instalación
show_post_installation_info() {
    echo ""
    echo "🎉 ¡Instalación completada exitosamente!"
    echo ""
    echo "📋 Información importante:"
    echo "   • Entorno virtual: ./venv"
    echo "   • Archivos Markdown: ./conversion"
    echo "   • PDFs generados: ./output"
    echo "   • Estilos CSS: ./estilos"
    echo "   • Configuración: ./config.yaml"
    echo ""
    echo "🚀 Para usar el conversor:"
    echo "   1. Activa el entorno virtual: source venv/bin/activate"
    echo "   2. Coloca tus archivos .md en ./conversion"
    echo "   3. Ejecuta: python md_to_pdf_converter.py"
    echo ""
    echo "📚 Comandos útiles:"
    echo "   • python md_to_pdf_converter.py --help"
    echo "   • python md_to_pdf_converter.py --list-templates"
    echo "   • python md_to_pdf_converter.py --validate"
    echo "   • python md_to_pdf_converter.py --template report"
    echo ""
    echo "📖 Para más información, consulta el README.md"
}

# Función principal
main() {
    echo "=========================================="
    echo "  CONVERSOR MARKDOWN A PDF - INSTALADOR"
    echo "=========================================="
    echo ""
    
    # Detectar sistema operativo
    detect_os
    
    # Verificar Python
    if ! check_python; then
        exit 1
    fi
    
    # Instalar dependencias del sistema según el OS
    case $OS in
        "macos")
            install_system_dependencies_macos
            ;;
        "linux")
            install_system_dependencies_linux
            ;;
        "windows")
            print_warning "En Windows, las dependencias se instalarán automáticamente con pip"
            ;;
        *)
            print_warning "Sistema operativo no reconocido. Las dependencias se instalarán con pip"
            ;;
    esac
    
    # Crear entorno virtual
    create_virtual_environment
    
    # Instalar dependencias de Python
    install_python_dependencies
    
    # Crear directorios
    create_directories
    
    # Verificar instalación
    if verify_installation; then
        show_post_installation_info
    else
        print_error "La instalación no se completó correctamente"
        exit 1
    fi
}

# Ejecutar función principal
main "$@" 