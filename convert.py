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
    current_section = None

    # Patrones regex ajustados
    title_pattern = r"Título (\w+)\s*(.*?)(?=Título \w+|\Z)"
    chapter_pattern = r"Capítulo (\w+)\s*(.*?)(?=Capítulo \w+|Título \w+|\Z)"
    section_pattern = (
        r"Sección (\d+\.?\w*)\s+(.*?)(?=Sección \d+\.?\w*|Capítulo \w+|Título \w+|\Z)"
    )
    article_pattern = r"Artículo (\d+)\.(.*?)(?=Artículo \d+\.|Sección \d+\.?\w*|Capítulo \w+|Título \w+|\Z)"

    # Encontrar todos los títulos
    title_matches = re.finditer(title_pattern, text, re.DOTALL)

    for title_match in title_matches:
        title_num, title_content = title_match.groups()
        current_title = f"Título {title_num}"
        titles[current_title] = {}

        print(f"Procesando Título: {current_title}")
        # Encontrar capítulos dentro del título
        chapter_matches = re.finditer(chapter_pattern, title_content, re.DOTALL)

        for chapter_match in chapter_matches:
            chapter_num, chapter_content = chapter_match.groups()
            current_chapter = f"Capítulo {chapter_num}"
            titles[current_title][current_chapter] = {}

            print(f"Procesando Capítulo: {current_chapter}")
            # Buscar secciones dentro del capítulo
            section_matches = re.finditer(section_pattern, chapter_content, re.DOTALL)
            section_found = False

            for section_match in section_matches:
                section_found = True
                section_num, section_content = section_match.groups()
                current_section = f"Sección {section_num}"
                titles[current_title][current_chapter][current_section] = {}

                # Buscar artículos dentro de la sección
                article_matches = re.finditer(
                    article_pattern, section_content, re.DOTALL
                )
                for article_match in article_matches:
                    article_num, article_content = article_match.groups()
                    titles[current_title][current_chapter][current_section][
                        f"Artículo {article_num}"
                    ] = article_content.strip()

            if not section_found:
                # Si no hay secciones, buscar artículos directamente en el capítulo
                article_matches = re.finditer(
                    article_pattern, chapter_content, re.DOTALL
                )
                for article_match in article_matches:
                    article_num, article_content = article_match.groups()
                    titles[current_title][current_chapter][
                        f"Artículo {article_num}"
                    ] = article_content.strip()

            print(
                f"Artículos encontrados: {len(titles[current_title][current_chapter])}"
            )
    return titles


# Uso
pdf_path = "docs/complete_code.pdf"
text = extract_text_from_pdf(pdf_path)
structured_content = process_document(text)

# Imprimir la estructura


def save_to_csv(structured_content, csv_filename):
    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile)

        # Escribir los encabezados
        csvwriter.writerow(["Título", "Capítulo", "Sección", "Artículo", "Contenido"])

        # Escribir los datos
        for title, chapters in structured_content.items():
            for chapter, sections_or_articles in chapters.items():
                if isinstance(next(iter(sections_or_articles.values())), dict):
                    # Si hay secciones
                    for section, articles in sections_or_articles.items():
                        for article, content in articles.items():
                            csvwriter.writerow(
                                [title, chapter, section, article, content]
                            )
                else:
                    # Si no hay secciones
                    for article, content in sections_or_articles.items():
                        csvwriter.writerow([title, chapter, "", article, content])


# Uso
csv_filename = f"output/code_estructurado{datetime.now().microsecond}.csv"
save_to_csv(structured_content, csv_filename)
