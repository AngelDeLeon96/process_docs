import re

texto = """
Título I Sufragio y Padrón Electoral  Capítulo I Principios Generales  Artículo 1.
Título II Organización Electoral  Capítulo I Organismos Electorales  Artículo 10.
Título III Procedimientos Electorales  Capítulo I Convocatoria  Artículo 20.
"""

patron = r"(Título\s{1}\w+)\s{1}(.*?)\s{2}"

resultados = {}

for match in re.finditer(patron, texto):
    numero_titulo = match.group(1)
    nombre_titulo = match.group(2)
    resultados[numero_titulo] = nombre_titulo

# Imprimir el diccionario resultante
for numero, nombre in resultados.items():
    print(f"{numero}: {nombre}")
