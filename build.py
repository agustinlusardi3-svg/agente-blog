import os
import glob

archivos_posts = sorted(glob.glob("posts/*.md"), reverse=True)

lista_html = ""
for archivo in archivos_posts:
    nombre_limpio = os.path.basename(archivo).replace(".md", "").replace("-", " ")
    
    # Intentamos leer un poco del contenido del post para ponerlo como resumen
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()
            resumen = "Descubre las claves y el análisis detallado en este artículo."
            for linea in lineas:
                linea_limpia = linea.strip()
                if linea_limpia and not linea_limpia.startswith("#"):
                    resumen = linea_limpia[:150] + "..."
                    break
    except Exception:
        resumen = "Análisis detallado y recursos recomendados sobre tecnología e innovación."

    lista_html += f'''
    <article class="post-card">
        <h2><a href="{archivo}">{nombre_limpio.capitalize()}</a></h2>
        <p>{resumen}</p>
        <a href="{archivo}" class="read-more">Leer artículo completo &rarr;</a>
    </article>
    '''

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tech & IA Insights | Reseñas y Recomendaciones</title>
    <style>
        :root {{
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --bg: #0f172a;
            --card-bg: #1e293b;
            --text: #f8fafc;
            --text-light: #94a3b8;
            --border: #334155;
        }}
        body {{
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            max-width: 850px;
            margin: 0 auto;
            padding: 60px 20px;
            line-height: 1.7;
        }}
        header {{
            text-align: center;
            margin-bottom: 60px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 40px;
        }}
        header h1 {{
            font-size: 3rem;
            color: var(--text);
            margin-bottom: 15px;
            letter-spacing: -0.03em;
            font-weight: 800;
        }}
        header p {{
            color: var(--text-light);
            font-size: 1.25rem;
            max-width: 600px;
            margin: 0 auto;
        }}
        .posts-grid {{
            display: flex;
            flex-direction: column;
            gap: 24px;
        }}
        .post-card {{
            background: var(--card-bg);
            padding: 35px;
            border-radius: 20px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
            transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
            border: 1px solid var(--border);
        }}
        .post-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 20px 35px -10px rgba(0, 0, 0, 0.4);
            border-color: var(--primary);
        }}
        .post-card h2 {{
            margin: 0 0 14px 0;
            font-size: 1.75rem;
        }}
        .post-card h2 a {{
            color: var(--text);
            text-decoration: none;
            transition: color 0.2s;
        }}
        .post-card h2 a:hover {{
            color: #60a5fa;
        }}
        .post-card p {{
            color: var(--text-light);
            margin: 0 0 25px 0;
            font-size: 1.05rem;
        }}
        .read-more {{
            display: inline-flex;
            align-items: center;
            font-weight: 600;
            color: #60a5fa;
            text-decoration: none;
            font-size: 1rem;
            transition: color 0.2s;
        }}
        .read-more:hover {{
            color: #93c5fd;
            text-decoration: underline;
        }}
        footer {{
            text-align: center;
            margin-top: 80px;
            color: var(--text-light);
            font-size: 0.9rem;
            border-top: 1px solid var(--border);
            padding-top: 30px;
        }}
    </style>
</head>
<body>
    <header>
        <h1>Tech & IA Insights</h1>
        <p>Las mejores herramientas, reseñas y guías seleccionadas para potenciar tu productividad.</p>
    </header>
    <main class="posts-grid">
        {lista_html}
    </main>
    <footer>
        <p>&copy; 2026 Tech & IA Insights. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html actualizado con diseño moderno oscuro.")
