import csv


def save_to_csv(structured_content, csv_filename):
    with open(csv_filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["Título", "Capítulo", "Sección", "Artículo", "Contenido"])
        writer.writerows(structured_content)
    print("La estructura se ha guardado en 'estructura_legal.csv'")
