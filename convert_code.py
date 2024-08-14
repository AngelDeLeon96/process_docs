import re
import PyPDF2
import pprint


# Función para extraer el texto del PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text


# Ruta al archivo PDF
pdf_path = "docs/tu_documento.pdf"
# Extraer el texto del PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Inicializar el diccionario donde se guardará la información
result = {}

# Variables para almacenar temporalmente el título, capítulo y artículo actuales
current_title = None
current_chapter = None

# Recorrer cada línea del texto
for line in pdf_text.splitlines():
    # Limpiar espacios adicionales
    line = line.strip()

    # Buscar títulos
    match_title = re.match(r"(Título\s+\w+)\s+(.+)", line)
    if match_title:
        current_title = match_title.group(1) + " " + match_title.group(2)
        result[current_title] = {}
        current_chapter = None
        continue

    # Buscar capítulos
    match_chapter = re.match(r"(Capítulo\s+\w+)\s+(.+)", line)
    if match_chapter:
        current_chapter = match_chapter.group(1) + " " + match_chapter.group(2)
        result[current_title][current_chapter] = []
        continue

    # Buscar artículos
    match_article = re.match(r"(Artículo\s+\d+)\.", line)
    if match_article:
        article = (
            match_article.group(1)
            + " "
            + line.split(match_article.group(1) + ".")[1].strip()
        )
        if current_chapter:
            result[current_title][current_chapter].append(article)
        else:
            # Si no hay capítulo actual, crear una lista de artículos en el título directamente
            if "Artículos" not in result[current_title]:
                result[current_title]["Artículos"] = []
            result[current_title]["Artículos"].append(article)

# Mostrar el diccionario resultante
pprint.pprint(result)
