import os
import glob

archivos_posts = sorted(glob.glob("posts/*.md"), reverse=True)

lista_html = ""
for archivo in archivos_posts:
    nombre_limpio = os.path.basename(archivo).replace(".md", "").replace("-", " ")
    lista_html += f'<li><a href="{archivo}">{nombre_limpio.capitalize()}</a></li>\n'

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agente Blog - Tecnología e IA</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width: 700px; margin: 40px auto; padding: 0 20px; line-height: 1.6; color: #333; }}
        h1 {{ border-bottom: 2px solid #eaeaea; padding-bottom: 10px; }}
        ul {{ padding-left: 20px; }}
        li {{ margin: 10px 0; }}
        a {{ color: #0066cc; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>Artículos y Reseñas</h1>
    <p>Bienvenido a nuestro blog automatizado de tecnología y software.</p>
    <ul>
        {lista_html}
    </ul>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html generado correctamente.")
