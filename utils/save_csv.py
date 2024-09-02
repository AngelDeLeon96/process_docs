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
    with open(csv_filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Título", "Capítulo", "Sección", "Artículo", "Contenido"])
        writer.writerows(structured_content)
    print("La estructura se ha guardado en 'estructura_legal.csv'")
