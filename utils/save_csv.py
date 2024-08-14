import csv

"""
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
"""


"""
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
"""


def save_to_csv(structured_content, csv_filename):
    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile)

        # Escribir los encabezados
        csvwriter.writerow(["Título", "Capítulo", "Sección", "Artículo", "Contenido"])

        # Escribir los datos
        for title, chapters in structured_content.items():
            if isinstance(chapters, dict):
                for chapter, sections_or_articles in chapters.items():
                    if isinstance(sections_or_articles, dict):
                        for section, articles in sections_or_articles.items():
                            if isinstance(articles, dict):
                                for article, content in articles.items():
                                    csvwriter.writerow(
                                        [title, chapter, section, article, content]
                                    )
                            else:
                                csvwriter.writerow(
                                    [title, chapter, section, "", articles]
                                )
                    else:
                        csvwriter.writerow(
                            [title, chapter, "", "", sections_or_articles]
                        )
            else:
                csvwriter.writerow([title, "", "", "", chapters])
