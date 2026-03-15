import os
from pdf2docx import Converter
from docx2pdf import convert



#CONVERTIR A PDF
def one_file_pdf(file):
    if not file.endswith(".pdf"):
        print("Error no es archivo PDF")
        return
    output_file = os.path.basename(file)
    output_file = output_file.replace(".pdf",".docx")
    
    try:
        cv = Converter(pdf_file=file)
        cv.convert(output_file)
        cv.close()
    except:
        print(f"Error al convertir {file}")

#CARPETA A PDFs
def folder_to_pdf(folder):
    for file in os.listdir(folder):
        ruta_unida = os.path.join(folder,file)

        if os.path.isdir(ruta_unida):
            for i in os.listdir(ruta_unida):
                archivo_completo = os.path.join(ruta_unida,i)
                one_file_pdf(archivo_completo)
            continue

        one_file_pdf(ruta_unida)

#ARCHIVO WORD
def one_file_word(file):
    if not file.endswith(".docx"):
        print("Error no es archivo .docx")
        return
    
    output_file = os.path.basename(file)
    output_file = output_file.replace(".docx",".pdf")
    try:
        convert(file,output_file)
    except:
        print(f"Error al convertir {file}")

#CARPETA WORD
def folder_to_word(folder):
    for file in os.listdir(folder):
        ruta_unida = os.path.join(folder,file)

        if os.path.isdir(ruta_unida):
            for i in os.listdir(ruta_unida):
                archivo_completo = os.path.join(ruta_unida,i)
                one_file_word(archivo_completo)
            continue

        one_file_word(ruta_unida)


#PDF TO WORD
def pdf_to_word(file="",number=1,folder=""):
    if number == 1:
        one_file_pdf(file)
    if number == 2:
        folder_to_pdf(folder)

#WORD TO PDF
def word_to_pdf(file="",number=1,folder=""):
    if number == 1:
        one_file_word(file)
    if number == 2:
        folder_to_word(folder)
