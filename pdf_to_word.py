import os
import module

#SABER SI QUIERE WORD A PDF O PDF A WORD
print("Bienvenido al convertidor de Word a PDF y PDF  a WORD")
verificador = input("Ingrese el numero de lo que desea hacer \n" \
"1. PDF a WORD\n" \
"2. WORD a PDF\n" \
">> ")

while not verificador in ("12"):
    verificador = input("Ingrese el numero de lo que desea hacer \n" \
"1. PDF a WORD\n" \
"2. WORD a PDF\n" \
">> ")
    
new_path = input("Ingrese la ruta donde iran los/el archivo nuevo: ")
os.chdir(new_path)
os.makedirs("WORD Y PDFs CONVERTIDOS",exist_ok=True)
new_path = os.path.join(new_path,"WORD Y PDFs CONVERTIDOS")

os.chdir(new_path)

#UN ARCHIVO O VARIOS ARCHIVOS

if int(verificador) == 1:
    print("Decidio convertir PDF a WORD")
    number = input("Ingrese el numero que se ajuste a los archivos que subira\n" \
    "1. Subir un archivo\n" \
    "2. Usar una carpeta de archivos\n" \
    ">> ")
    while not number in ("12"):
        number = input("Ingrese el numero que se ajuste a los archivos que subira\n" \
        "1. Subir un archivo\n" \
        "2. Usar una carpeta de archivos\n" \
        ">> ")

    if int(number) == 1:
        file = input("Ingrese la ruta del archivo a convertir a WORD: ")
        while not file.endswith(".pdf"):
            file = input("Ingrese una ruta con un archivo pdf: ")
        module.pdf_to_word(file = file,number=int(number),folder="")
    elif int(number) == 2:
        folder = input("Ingrese la ruta de la carpeta con los archivos: ")
        while not os.path.exists(folder):
            folder = input("Ingrese una ruta valida con una carpeta con los archivos: ")
        module.pdf_to_word(file="",number=int(number),folder=folder)




elif int(verificador) == 2:
    print("Decidio convertir WORD a PDF")
    number = input("Ingrese el numero que se ajuste a los archivos que subira\n" \
    "1. Subir un archivo\n" \
    "2. Usar una carpeta de archivos\n" \
    ">> ")
    while not number in ("12"):
        number = input("Ingrese el numero que se ajuste a los archivos que subira\n" \
        "1. Subir un archivo\n" \
        "2. Usar una carpeta de archivos\n" \
        ">> ")

    if int(number) == 1:
        file = input("Ingrese la ruta del archivo a convertir a PDF: ")
        while not file.endswith(".docx"):
            file = input("Ingrese una ruta con un archivo docx: ")
        module.word_to_pdf(file=file,number=int(number),folder="")
    elif int(number) == 2:
        folder = input("Ingrese la ruta de la carpeta con los archivos: ")
        while not os.path.exists(folder):
            folder = input("Ingrese una ruta valida con una carpeta con los archivos: ")
        module.word_to_pdf(file="",number=int(number),folder=folder)

