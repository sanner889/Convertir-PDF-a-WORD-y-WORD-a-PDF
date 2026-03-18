import os
import copy
from pdf2docx import Converter
from docx2pdf import convert
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from tkinter import Tk,filedialog

# ─────────────────────────────────────────────────────────────────────────────
# CORRECCIÓN DE IMÁGENES FLOTANTES
# ─────────────────────────────────────────────────────────────────────────────


# // FUNCION HECHA POR IA //

def fix_floating_images(docx_path):
    """
    Convierte imágenes flotantes/ancladas (wp:anchor) a imágenes en línea
    (wp:inline) en un .docx, evitando que se superpongan con el texto.

    pdf2docx por defecto coloca las imágenes con posición absoluta (anchor),
    lo que provoca el bug de superposición. Al convertirlas a inline, las
    imágenes quedan integradas en el flujo del texto respetando su posición.
    """
    doc = Document(docx_path)
    modified = False

    # Atributos exclusivos de wp:anchor que NO existen en wp:inline
    # (son los que controlan posición absoluta y tipo de ajuste de texto)
    anchor_only_local_names = {
        'simplePos',        # posición simplificada
        'positionH',        # posición horizontal absoluta
        'positionV',        # posición vertical absoluta
        'wrapNone',         # sin ajuste de texto
        'wrapSquare',       # ajuste cuadrado
        'wrapThrough',      # ajuste a través
        'wrapTight',        # ajuste ajustado
        'wrapTopAndBottom', # ajuste arriba y abajo
    }

    for para in doc.paragraphs:
        for run in para.runs:
            # Buscar todos los elementos <w:drawing> dentro del run
            for drawing in run._element.findall('.//' + qn('w:drawing')):
                # Buscar imágenes flotantes (anchor) dentro del drawing
                for anchor in list(drawing.findall(qn('wp:anchor'))):

                    # Crear el elemento inline equivalente
                    inline = OxmlElement('wp:inline')

                    # Copiar atributos de distancia (margen alrededor de la imagen)
                    inline.set('distT', anchor.get('distT', '0'))
                    inline.set('distB', anchor.get('distB', '0'))
                    inline.set('distL', anchor.get('distL', '0'))
                    inline.set('distR', anchor.get('distR', '0'))

                    # Copiar todos los hijos del anchor al inline,
                    # EXCEPTO los que son exclusivos del modo flotante
                    for child in anchor:
                        local_name = (
                            child.tag.split('}')[-1]
                            if '}' in child.tag
                            else child.tag
                        )
                        if local_name not in anchor_only_local_names:
                            inline.append(copy.deepcopy(child))

                    # Reemplazar anchor por inline dentro del drawing
                    drawing.remove(anchor)
                    drawing.append(inline)
                    modified = True

    if modified:
        doc.save(docx_path)
        print(f"  → Posición de imágenes corregida en: {os.path.basename(docx_path)}")

    return modified

# // FUNCIONES HECHAS POR MI //
# ─────────────────────────────────────────────────────────────────────────────
# CONVERTIR PDF → WORD
# ─────────────────────────────────────────────────────────────────────────────

def one_file_pdf(file):
    if not file.endswith(".pdf"):
        print("Error: no es un archivo PDF")
        return

    output_file = os.path.basename(file).replace(".pdf", ".docx")

    try:
        cv = Converter(pdf_file=file)
        cv.convert(output_file)
        cv.close()

        # ← CORRECCIÓN: post-procesar el docx para arreglar imágenes flotantes
        fix_floating_images(output_file)

        print(f"Convertido exitosamente: {output_file}")
    except Exception as e:
        print(f"Error al convertir {file}: {e}")


def folder_to_pdf(folder):
    for file in os.listdir(folder):
        ruta_unida = os.path.join(folder, file)

        if os.path.isdir(ruta_unida):
            for i in os.listdir(ruta_unida):
                archivo_completo = os.path.join(ruta_unida, i)
                one_file_pdf(archivo_completo)
            continue

        one_file_pdf(ruta_unida)


# ─────────────────────────────────────────────────────────────────────────────
# CONVERTIR WORD → PDF
# ─────────────────────────────────────────────────────────────────────────────

def one_file_word(file):
    if not file.endswith(".docx"):
        print("Error: no es un archivo .docx")
        return

    output_file = os.path.basename(file).replace(".docx", ".pdf")

    try:
        convert(file, output_file)
        print(f"Convertido exitosamente: {output_file}")
    except Exception as e:
        print(f"Error al convertir {file}: {e}")


def folder_to_word(folder):
    for file in os.listdir(folder):
        ruta_unida = os.path.join(folder, file)

        if os.path.isdir(ruta_unida):
            for i in os.listdir(ruta_unida):
                archivo_completo = os.path.join(ruta_unida, i)
                one_file_word(archivo_completo)
            continue

        one_file_word(ruta_unida)


# ─────────────────────────────────────────────────────────────────────────────
# FUNCIONES CONVERTIDORAS
# ─────────────────────────────────────────────────────────────────────────────

def pdf_to_word(file="", number=1, folder=""):
    if number == 1:
        one_file_pdf(file)
    elif number == 2:
        folder_to_pdf(folder)


def word_to_pdf(file="", number=1, folder=""):
    if number == 1:
        one_file_word(file)
    elif number == 2:
        folder_to_word(folder)


# ─────────────────────────────────────────────────────────────────────────────
# FUNCIONES DE SELECCION DE ARCHIVOS
# ─────────────────────────────────────────────────────────────────────────────

def seleccionar_archivo(verificador):
    try:
        verificador = int(verificador)
    except:
        print("ERROR")
        return
    root = Tk()
    root.withdraw()
    root.attributes("-topmost",True)

    # // ARCHIVOS PDF //

    if verificador == 1:
        ruta = filedialog.askopenfilename(
            title="Seleccione un archivo PDF",
            filetypes=[("Archivos PDF", "*.pdf")]
        )
    
    # // ARCHIVOS WORD //

    elif verificador == 2:
        ruta = filedialog.askopenfilename(
            title="Seleccione un archivo WORD",
            filetypes=[("Archivos WORD", "*.docx")]
        )
    else:
        print("ERROR")
        return
    
    root.destroy()
    return ruta

def seleccionar_carpeta():
    root = Tk()
    root.withdraw()
    root.attributes("-topmost",True)

    ruta = filedialog.askdirectory(title="Seleccione la carpeta")
    root.destroy()

    return ruta


# ─────────────────────────────────────────────────────────────────────────────
# CONFIRMAR QUE LOS INPUTS ESTEN EN 1 - 2
# ─────────────────────────────────────────────────────────────────────────────

def confirmar(mensaje):
    respuesta = input(mensaje)
    while respuesta not in ["1","2"]:
        respuesta = input(mensaje)
    return respuesta
