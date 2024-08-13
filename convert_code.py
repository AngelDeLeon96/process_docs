# Importar la biblioteca re para expresiones regulares
import re
import pandas as pd
import PyPDF2

# Inicializar el diccionario donde se guardará la información
result = {}

# Variables para almacenar temporalmente el título, capítulo y artículo actuales
current_title = None
current_chapter = None


# Función para leer el contenido del PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text() + "\n"
        return text


# Ruta al archivo PDF
pdf_path = "docs/tu_documento.pdf"
pdf_text = extract_text_from_pdf(pdf_path).strip()

lines = pdf_text.split("\n")

# Recorrer cada línea del texto
print(lines)

for line in lines:
    # print(line)
    match_title = re.match(
        r"(Título\s{1}\w+)\s{1}(.*?)\s{2}(Capítulo\s{1}\w+)\s{1}(.*?)\s{2}", line
    )
    print(match_title)

    # Buscar títulos
    if match_title:
        current_title = match_title.group(1) + " " + match_title.group(2)
        result[current_title] = {}
        current_chapter = match_title.group(3)
        result[current_title][current_chapter] = []
        continue
    # Buscar capítulos
    match_chapter = re.match(r"(Capítulo\s+\w+)\s+(.+?)\s+(Artículo\s+\d+)", line)
    if match_chapter:
        current_chapter = match_chapter.group(1) + " " + match_chapter.group(2)
        if current_title not in result:
            result[current_title] = {}
        result[current_title][current_chapter] = []
        article = match_chapter.group(3)
        result[current_title][current_chapter].append(article)
        continue

    # Buscar artículos
    match_article = re.match(r"(Artículo\s+\d+)\.", line)
    if match_article:
        article = match_article.group(1)
        if current_chapter not in result[current_title]:
            result[current_title][current_chapter] = []
        result[current_title][current_chapter].append(article)


# Mostrar el diccionario resultante
print(result)
