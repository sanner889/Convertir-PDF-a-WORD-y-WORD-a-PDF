📄🔄 Convertidor de PDF ↔ WORD

Un programa en Python que permite convertir archivos entre PDF y Word (.docx) de forma sencilla, ya sea un solo archivo o carpetas completas.

🚀 Características

✅ Convertir PDF → Word

✅ Convertir Word → PDF

✅ Soporte para:

Un solo archivo

Carpetas completas (procesamiento en lote)

✅ Interfaz amigable con selección de archivos y carpetas (sin escribir rutas)

✅ Corrección automática de imágenes en documentos Word

🧠 Funcionalidad destacada
🔧 Corrección de imágenes en Word

El programa incluye una función especial:

fix_floating_images()

📌 ¿Qué hace?

Convierte imágenes flotantes a imágenes en línea

Evita que se superpongan con el texto después de convertir desde PDF

📦 Requisitos

Instala las siguientes librerías antes de usar el programa:

pip install pdf2docx docx2pdf python-docx
▶️ Uso

Ejecuta el archivo principal:

python "Convertir PDF y WORD.py"
🖥️ Flujo del programa

Seleccionas el tipo de conversión:

1 → PDF a Word

2 → Word a PDF

Seleccionas:

Un archivo

O una carpeta completa

Seleccionas la carpeta donde se guardarán los resultados

El programa crea automáticamente:

WORD Y PDFs CONVERTIDOS/

Y guarda ahí los archivos convertidos.

📁 Estructura del proyecto
📦 Proyecto
 ┣ 📜 Convertir PDF y WORD.py   # Archivo principal
 ┣ 📜 module.py                 # Lógica del programa
⚠️ Notas importantes

Solo se aceptan:

.pdf para convertir a Word

.docx para convertir a PDF

Si no seleccionas archivo, el programa no continuará

Funciona mejor en Windows (por docx2pdf)
