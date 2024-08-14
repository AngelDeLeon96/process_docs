import re

"""
def process_document(text):
    titles = {}
    current_title = None
    current_chapter = None
    current_section = None

    # Patrones regex ajustados
    title_pattern = r"Título (\w+)\s*(.*?)(?=\nTítulo|\Z)"
    chapter_pattern = r"Capítulo (\w+)\s*(.*?)(?=\nCapítulo|\nTítulo|\Z)"
    section_pattern = r"Sección (\d+\.?\w*)\s*(.*?)(?=\nSección|\nCapítulo|\nTítulo|\Z)"
    article_pattern = (
        r"Artículo (\d+)\.(.*?)(?=\nArtículo|\nSección|\nCapítulo|\nTítulo|\Z)"
    )

    # Encontrar todos los títulos
    title_matches = list(re.finditer(title_pattern, text, re.DOTALL))

    for i, title_match in enumerate(title_matches):
        title_num, title_content = title_match.groups()
        title_name = title_content.strip().split("\n")[0]
        current_title = f"Título {title_num}: {title_name}"
        titles[current_title] = {}

        # Determinar el final del contenido del título
        title_end = (
            text.index(title_matches[i + 1].group())
            if i < len(title_matches) - 1
            else len(text)
        )
        title_full_content = text[title_match.start() : title_end]

        # Encontrar capítulos dentro del título
        chapter_matches = list(
            re.finditer(chapter_pattern, title_full_content, re.DOTALL)
        )

        for j, chapter_match in enumerate(chapter_matches):
            chapter_num, chapter_content = chapter_match.groups()
            chapter_name = chapter_content.strip().split("\n")[0]
            current_chapter = f"Capítulo {chapter_num}: {chapter_name}"
            titles[current_title][current_chapter] = {}

            # Determinar el final del contenido del capítulo
            chapter_end = (
                title_full_content.index(chapter_matches[j + 1].group())
                if j < len(chapter_matches) - 1
                else len(title_full_content)
            )
            chapter_full_content = title_full_content[
                chapter_match.start() : chapter_end
            ]

            # Buscar secciones dentro del capítulo
            section_matches = list(
                re.finditer(section_pattern, chapter_full_content, re.DOTALL)
            )

            if section_matches:
                for k, section_match in enumerate(section_matches):
                    section_num, section_content = section_match.groups()
                    section_name = section_content.strip().split("\n")[0]
                    current_section = f"Sección {section_num}: {section_name}"
                    titles[current_title][current_chapter][current_section] = {}

                    # Determinar el final del contenido de la sección
                    section_end = (
                        chapter_full_content.index(section_matches[k + 1].group())
                        if k < len(section_matches) - 1
                        else len(chapter_full_content)
                    )
                    section_full_content = chapter_full_content[
                        section_match.start() : section_end
                    ]

                    # Buscar artículos dentro de la sección
                    article_matches = re.finditer(
                        article_pattern, section_full_content, re.DOTALL
                    )
                    for article_match in article_matches:
                        article_num, article_content = article_match.groups()
                        titles[current_title][current_chapter][current_section][
                            f"Artículo {article_num}"
                        ] = article_content.strip()
            else:
                # Si no hay secciones, buscar artículos directamente en el capítulo
                article_matches = re.finditer(
                    article_pattern, chapter_full_content, re.DOTALL
                )
                for article_match in article_matches:
                    article_num, article_content = article_match.groups()
                    titles[current_title][current_chapter][
                        f"Artículo {article_num}"
                    ] = article_content.strip()

    return titles
"""

import re


def process_document(text):
    titles = {}
    current_title = None
    current_chapter = None
    current_section = None

    # Patrones regex ajustados
    title_pattern = r"Título (\w+)\s*(.*?)(?=\nTítulo|\Z)"
    chapter_pattern = r"Capítulo (\w+)\s*(.*?)(?=\nCapítulo|\nTítulo|\Z)"
    section_pattern = r"Sección (\d+\.?\w*)\s*(.*?)(?=\nSección|\nCapítulo|\nTítulo|\Z)"
    article_pattern = (
        r"Artículo (\d+)\.(.*?)(?=\nArtículo|\nSección|\nCapítulo|\nTítulo|\Z)"
    )

    # Encontrar todos los títulos
    title_matches = list(re.finditer(title_pattern, text, re.DOTALL))

    for i, title_match in enumerate(title_matches):
        title_num, title_content = title_match.groups()
        title_name = title_content.strip().split("\n")[0]
        current_title = f"Título {title_num}: {title_name}"
        titles[current_title] = {}

        # Determinar el final del contenido del título
        title_end = (
            text.index(title_matches[i + 1].group())
            if i < len(title_matches) - 1
            else len(text)
        )
        title_full_content = text[title_match.start() : title_end]

        # Encontrar capítulos dentro del título
        chapter_matches = list(
            re.finditer(chapter_pattern, title_full_content, re.DOTALL)
        )
        if chapter_matches:
            for j, chapter_match in enumerate(chapter_matches):
                chapter_num, chapter_content = chapter_match.groups()
                chapter_name = chapter_content.strip().split("\n")[0]
                current_chapter = f"Capítulo {chapter_num}: {chapter_name}"
                titles[current_title][current_chapter] = {}

                # Determinar el final del contenido del capítulo
                chapter_end = (
                    title_full_content.index(chapter_matches[j + 1].group())
                    if j < len(chapter_matches) - 1
                    else len(title_full_content)
                )
                chapter_full_content = title_full_content[
                    chapter_match.start() : chapter_end
                ]

                # Buscar secciones dentro del capítulo
                section_matches = list(
                    re.finditer(section_pattern, chapter_full_content, re.DOTALL)
                )

                if section_matches:
                    for k, section_match in enumerate(section_matches):
                        section_num, section_content = section_match.groups()
                        section_name = section_content.strip().split("\n")[0]
                        current_section = f"Sección {section_num}: {section_name}"
                        titles[current_title][current_chapter][current_section] = {}

                        # Determinar el final del contenido de la sección
                        section_end = (
                            chapter_full_content.index(section_matches[k + 1].group())
                            if k < len(section_matches) - 1
                            else len(chapter_full_content)
                        )
                        section_full_content = chapter_full_content[
                            section_match.start() : section_end
                        ]

                        # Buscar artículos dentro de la sección
                        process_articles(
                            section_full_content,
                            titles[current_title][current_chapter][current_section],
                        )
                else:
                    # Si no hay secciones, buscar artículos directamente en el capítulo
                    process_articles(
                        chapter_full_content, titles[current_title][current_chapter]
                    )
        else:
            # Si no hay capítulos, procesar los artículos directamente en el título
            process_articles(title_full_content, titles[current_title])
    return titles


def process_articles(content, container):
    article_pattern = r"Artículo (\d+)\.(.*?)(?=Artículo \d+\.|\Z)"
    article_matches = list(re.finditer(article_pattern, content, re.DOTALL))

    for i, article_match in enumerate(article_matches):
        article_num, article_content = article_match.groups()
        article_end = (
            content.index(article_matches[i + 1].group())
            if i < len(article_matches) - 1
            else len(content)
        )
        full_article_content = content[article_match.start() : article_end].strip()

        # Eliminar cualquier título de capítulo o sección que pueda estar al final del contenido del artículo
        full_article_content = re.sub(
            r"\n(Capítulo|Sección).*$", "", full_article_content, flags=re.MULTILINE
        )

        container[f"Artículo {article_num}"] = full_article_content

    # Verificar si hay saltos en la numeración de los artículos
    article_numbers = [int(re.search(r"\d+", key).group()) for key in container.keys()]
    for i in range(len(article_numbers) - 1):
        if article_numbers[i + 1] - article_numbers[i] > 1:
            print(
                f"Advertencia: Posible salto detectado entre Artículo {article_numbers[i]} y Artículo {article_numbers[i+1]}"
            )


"""
def process_articles(content, container):
    article_pattern = r"Artículo (\d+)\.(.*?)(?=\nArtículo|\Z)"
    article_matches = list(re.finditer(article_pattern, content, re.DOTALL))

    for i, article_match in enumerate(article_matches):
        article_num, article_content = article_match.groups()
        article_end = (
            content.index(article_matches[i + 1].group())
            if i < len(article_matches) - 1
            else len(content)
        )
        full_article_content = content[article_match.start() : article_end].strip()
        container[f"Artículo {article_num}"] = full_article_content

    # Verificar si hay saltos en la numeración de los artículos
    article_numbers = [int(re.search(r"\d+", key).group()) for key in container.keys()]
    for i in range(len(article_numbers) - 1):
        if article_numbers[i + 1] - article_numbers[i] > 1:
            print(
                f"Advertencia: Salto detectado entre Artículo {article_numbers[i]} y Artículo {article_numbers[i+1]}"
            )
"""
