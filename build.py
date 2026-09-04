import os
import glob

archivos_posts = sorted(glob.glob("posts/*.md"), reverse=True)

lista_html = ""
for archivo in archivos_posts:
    nombre_limpio = os.path.basename(archivo).replace(".md", "").replace("-", " ")
    lista_html += f'''
    <article class="post-card">
        <h2><a href="{archivo}">{nombre_limpio.capitalize()}</a></h2>
        <p>Análisis detallado, ventajas y recursos recomendados sobre tecnología e innovación digital.</p>
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
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --text: #1e293b;
            --text-light: #64748b;
        }}
        body {{
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            max-width: 800px;
            margin: 0 auto;
            padding: 50px 20px;
            line-height: 1.6;
        }}
        header {{
            text-align: center;
            margin-bottom: 50px;
        }}
        header h1 {{
            font-size: 2.8rem;
            color: var(--text);
            margin-bottom: 10px;
            letter-spacing: -0.03em;
        }}
        header p {{
            color: var(--text-light);
            font-size: 1.2rem;
        }}
        .posts-grid {{
            display: flex;
            flex-direction: column;
            gap: 24px;
        }}
        .post-card {{
            background: var(--card-bg);
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            border: 1px solid #e2e8f0;
        }}
        .post-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 20px -3px rgba(0, 0, 0, 0.08);
        }}
        .post-card h2 {{
            margin: 0 0 12px 0;
            font-size: 1.6rem;
        }}
        .post-card h2 a {{
            color: var(--text);
            text-decoration: none;
            transition: color 0.2s;
        }}
        .post-card h2 a:hover {{
            color: var(--primary);
        }}
        .post-card p {{
            color: var(--text-light);
            margin: 0 0 20px 0;
            font-size: 1.05rem;
        }}
        .read-more {{
            display: inline-block;
            font-weight: 600;
            color: var(--primary);
            text-decoration: none;
            font-size: 0.95rem;
        }}
        .read-more:hover {{
            color: var(--primary-dark);
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <header>
        <h1>Tech & IA Insights</h1>
        <p>Las mejores herramientas, reseñas y guías seleccionadas para potenciar tus proyectos.</p>
    </header>
    <main class="posts-grid">
        {lista_html}
    </main>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html rediseñado correctamente.")
