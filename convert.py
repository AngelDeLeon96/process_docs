import re
import pdfplumber  # o PyPDF2, dependiendo de su preferencia
import csv
from datetime import datetime, date


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text


def process_document(text):
    titles = {}
    current_title = None
    current_chapter = None

    # Patrones regex
    title_pattern = r"Título (\w+)\n(.*?)\n"
    chapter_pattern = r"Capítulo (\w+)\n(.*?)\n"
    article_pattern = (
        r"Artículo (\d+)\.(.*?)(?=Artículo \d+\.|Capítulo \w+|Título \w+|$)"
    )

    # Dividir el texto en secciones (títulos)
    title_sections = re.split(title_pattern, text)[
        1:
    ]  # Ignoramos el texto antes del primer título

    for i in range(
        0, len(title_sections), 3
    ):  # Procesamos de 3 en 3 porque cada título tiene 3 partes (número, nombre, contenido)
        title_num, title_name, title_content = title_sections[i : i + 3]
        current_title = f"Título {title_num}: {title_name.strip()}"
        titles[current_title] = {}

        # Buscar capítulos dentro del título
        chapter_sections = re.split(chapter_pattern, title_content)[
            1:
        ]  # Ignoramos el texto antes del primer capítulo

        for j in range(
            0, len(chapter_sections), 3
        ):  # Procesamos de 3 en 3 por la misma razón
            chapter_num, chapter_name, chapter_content = chapter_sections[j : j + 3]
            current_chapter = f"Capítulo {chapter_num}: {chapter_name.strip()}"
            titles[current_title][current_chapter] = {}

            # Buscar artículos dentro del capítulo
            article_matches = re.finditer(article_pattern, chapter_content, re.DOTALL)
            for article_match in article_matches:
                article_num, article_content = article_match.groups()
                titles[current_title][current_chapter][
                    f"Artículo {article_num}"
                ] = article_content.strip()

    return titles


# Uso
pdf_path = "docs/code5.pdf"
text = extract_text_from_pdf(pdf_path)
structured_content = process_document(text)

# Imprimir la estructura
for title, chapters in structured_content.items():
    print(title)
    for chapter, articles in chapters.items():
        print(f"  {chapter}")
        for article, content in articles.items():
            print(
                f"    {article}: {content[:50]}..."
            )  # Imprime los primeros 50 caracteres del contenido


def save_to_csv(structured_content, csv_filename):
    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile)

        # Escribir los encabezados
        csvwriter.writerow(["Título", "Capítulo", "Artículo", "Contenido"])

        # Escribir los datos
        for title, chapters in structured_content.items():
            for chapter, articles in chapters.items():
                for article, content in articles.items():
                    csvwriter.writerow([title, chapter, article, content])


# Uso
csv_filename = f"output/documento_estructurado{datetime.now().microsecond}.csv"
save_to_csv(structured_content, csv_filename)
