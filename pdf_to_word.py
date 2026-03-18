import os
import module

#SABER SI QUIERE WORD A PDF O PDF A WORD
print("Bienvenido al convertidor de Word a PDF y PDF  a WORD")
verificador = module.confirmar("Ingrese el numero de lo que desea hacer \n" \
"1. PDF a WORD\n" \
"2. WORD a PDF\n" \
">> ")


print("Ingrese la ruta donde iran los/el archivo nuevo: ")
new_path = module.seleccionar_carpeta()
os.chdir(new_path)
os.makedirs("WORD Y PDFs CONVERTIDOS",exist_ok=True)
new_path = os.path.join(new_path,"WORD Y PDFs CONVERTIDOS")

os.chdir(new_path)

#UN ARCHIVO O VARIOS ARCHIVOS

# ─────────────────────────────────────────────────────────────────────────────
# PDF A WORD
# ─────────────────────────────────────────────────────────────────────────────

if int(verificador) == 1:
    print("\nDecidio convertir PDF a WORD")
    number = module.confirmar("\nIngrese el numero que se ajuste a los archivos que subira\n" \
    "1. Subir un archivo\n" \
    "2. Usar una carpeta de archivos\n" \
    ">> ")

    if int(number) == 1:
        print("Ingrese la ruta del archivo a convertir de PDF a WORD: ")
        file = module.seleccionar_archivo(verificador)
        module.pdf_to_word(file = file,number=int(number),folder="")

    elif int(number) == 2:
        print("Ingrese la ruta de la carpeta: ")
        folder = module.seleccionar_carpeta()
        module.pdf_to_word(file="",number=int(number),folder=folder)

# ─────────────────────────────────────────────────────────────────────────────
# WORD A PDF
# ─────────────────────────────────────────────────────────────────────────────

elif int(verificador) == 2:
    print("\nDecidio convertir WORD a PDF")
    number = module.confirmar("\nIngrese el numero que se ajuste a los archivos que subira\n" \
    "1. Subir un archivo\n" \
    "2. Usar una carpeta de archivos\n" \
    ">> ")

    if int(number) == 1:
        print("Ingrese la ruta del archivo a convertir de WORD a PDF: ")
        file = module.seleccionar_archivo(verificador)
        module.word_to_pdf(file = file,number=int(number),folder="")

    elif int(number) == 2:
        print("Ingrese la ruta de la carpeta: ")
        folder = module.seleccionar_carpeta()
        module.word_to_pdf(file="",number=int(number),folder=folder)

