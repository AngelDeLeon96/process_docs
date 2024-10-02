import re


title_pattern = r"(?:^|\n)Título (\w+)\s*(.*?)(?=\nTítulo|\nCapítulo|\nArtículo|\Z)"
chapter_pattern = (
    r"(?:^|\n)Capítulo (\w+)(?:\s*|\n)(.*?)(?=\nCapítulo|\nTítulo|\nArtículo|\Z)"
)
section_pattern = r"(?:^|\n)Sección (\d+\.?\w*)\s*(.*?)(?=\nSección|\nCapítulo|\nTítulo|\nArtículo|\Z)"
article_pattern = (
    r"(?:^|\n)Artículo (\d+)\.(.*?)(?=\nArtículo|\nCapítulo|\nTítulo|\nSección|\Z)"
)


def find_and_print_matches(pattern, text, name):
    matches = list(re.finditer(pattern, text, re.DOTALL | re.MULTILINE))
    for match in matches:
        number = match.group(1)
        content = match.group(2).strip() if len(match.groups()) > 1 else ""
        print(f"{name} {number}:")
        print(content)
        print()


def process_document(content):
    # Encontramos todas las coincidencias
    title_matches = list(re.finditer(title_pattern, content, re.DOTALL | re.MULTILINE))
    chapter_matches = list(
        re.finditer(chapter_pattern, content, re.DOTALL | re.MULTILINE)
    )
    section_matches = list(
        re.finditer(section_pattern, content, re.DOTALL | re.MULTILINE)
    )
    article_matches = list(
        re.finditer(article_pattern, content, re.DOTALL | re.MULTILINE)
    )

    # Combinamos y ordenamos todas las coincidencias
    all_matches = (
        [(m.start(), "title", m) for m in title_matches]
        + [(m.start(), "chapter", m) for m in chapter_matches]
        + [(m.start(), "section", m) for m in section_matches]
        + [(m.start(), "article", m) for m in article_matches]
    )
    all_matches.sort(key=lambda x: x[0])

    # Inicializamos variables para seguir la estructura
    current_title = current_chapter = current_section = ""
    structure = []

    # Procesamos las coincidencias en orden
    for _, match_type, match in all_matches:
        if match_type == "title":
            current_title = f"Título {match.group(1).strip()}: {match.group(2).strip()}"
            current_chapter = current_section = ""
        elif match_type == "chapter":
            current_subtitle = match.group(2).strip()
            if "\n" in current_subtitle:
                current_subtitle = current_subtitle.split("\n", 1)[0]
            else:
                current_subtitle = current_subtitle
            current_chapter = f"Capítulo {match.group(1).strip()}: {current_subtitle}"
            current_section = ""
        elif match_type == "section":
            current_section = f"Sección {match.group(1)}"
        elif match_type == "article":
            article_number = match.group(1)
            article_content = match.group(2).strip()
            structure.append(
                [
                    current_title,
                    current_chapter,
                    current_section,
                    f"Artículo {article_number}",
                    article_content,
                ]
            )

    return structure
