import os
import glob
import markdown

os.makedirs("posts", exist_ok=True)
archivos_posts = sorted(glob.glob("posts/*.md"), reverse=True)

lista_html = ""
for i, archivo in enumerate(archivos_posts):
    nombre_base = os.path.basename(archivo).replace(".md", "")
    html_nombre_archivo = f"posts/{nombre_base}.html"
    
    # Leer contenido del markdown
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            contenido_md = f.read()
    except Exception:
        contenido_md = "# Artículo sin título\n\nContenido en proceso de actualización."

    # Extraer el título real (primera línea que empieza con #)
    titulo = "Artículo de Tecnología e IA"
    lineas = contenido_md.split("\n")
    cuerpo_md_filtrado = []
    titulo_encontrado = False
    
    for linea in lineas:
        if not titulo_encontrado and linea.strip().startswith("# "):
            titulo = linea.strip().replace("# ", "")
            titulo_encontrado = True
        else:
            cuerpo_md_filtrado.append(linea)
            
    cuerpo_md = "\n".join(cuerpo_md_filtrado)
    contenido_html_post = markdown.markdown(cuerpo_md)
    
    # Generar un resumen limpio
    resumen = "Descubre las claves, herramientas y el análisis detallado para potenciar tus resultados."
    for linea in lineas:
        l = linea.strip()
        if l and not l.startswith("#") and not l.startswith("-"):
            resumen = l[:140] + "..."
            break

    # Imágenes atractivas de alta tecnología vía Unsplash con semilla única por artículo
    imagen_url = f"https://picsum.photos/seed/{nombre_base}/700/400"

    # HTML individual para cada artículo con diseño inmersivo
    pagina_post_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo} | Tech & IA Insights</title>
    <style>
        :root {{
            --primary: #6366f1;
            --primary-glow: rgba(99, 102, 241, 0.4);
            --bg: #090d16;
            --card-bg: #111827;
            --text: #f3f4f6;
            --text-light: #9ca3af;
            --border: #1f2937;
            --accent: #38bdf8;
        }}
        body {{
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
            line-height: 1.8;
        }}
        .back-link {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--accent);
            text-decoration: none;
            font-weight: 600;
            margin-bottom: 30px;
            transition: opacity 0.2s;
        }}
        .back-link:hover {{
            opacity: 0.8;
        }}
        .post-header {{
            margin-bottom: 40px;
        }}
        .post-header h1 {{
            font-size: 2.5rem;
            font-weight: 800;
            letter-spacing: -0.025em;
            color: #ffffff;
            margin-bottom: 20px;
            line-height: 1.2;
        }}
        .post-banner {{
            width: 100%;
            height: 380px;
            object-fit: cover;
            border-radius: 16px;
            margin-bottom: 30px;
            border: 1px solid var(--border);
            box-shadow: 0 20px 40px rgba(0,0,0,0.5);
        }}
        .post-content {{
            background: var(--card-bg);
            padding: 40px;
            border-radius: 20px;
            border: 1px solid var(--border);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }}
        .post-content h2 {{
            color: #ffffff;
            font-size: 1.5rem;
            margin-top: 35px;
            margin-bottom: 15px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 8px;
        }}
        .post-content p {{
            margin-bottom: 20px;
            color: var(--text-light);
        }}
        .post-content ul {{
            margin-bottom: 20px;
            padding-left: 20px;
            color: var(--text-light);
        }}
        .post-content li {{
            margin-bottom: 8px;
        }}
        .post-content a {{
            color: var(--accent);
            text-decoration: underline;
        }}
        footer {{
            text-align: center;
            margin-top: 60px;
            color: var(--text-light);
            font-size: 0.85rem;
            border-top: 1px solid var(--border);
            padding-top: 25px;
        }}
    </style>
</head>
<body>
    <a href="../index.html" class="back-link">&larr; Volver al inicio</a>
    <article>
        <header class="post-header">
            <h1>{titulo}</h1>
            <img src="{imagen_url}" alt="{titulo}" class="post-banner">
        </header>
        <div class="post-content">
            {contenido_html_post}
        </div>
    </article>
    <footer>
        <p>&copy; 2026 Tech & IA Insights. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
"""

    # Guardar la página HTML individual del post
    with open(html_nombre_archivo, "w", encoding="utf-8") as f_post:
        f_post.write(pagina_post_content)

    # Agregar tarjeta estilizada al índice principal
    lista_html += f"""
    <div class="post-card">
        <div class="card-image-wrapper">
            <img src="{imagen_url}" alt="{titulo}" loading="lazy">
            <span class="badge">Inteligencia Artificial</span>
        </div>
        <div class="card-body">
            <h2><a href="{html_nombre_archivo}">{titulo}</a></h2>
            <p>{resumen}</p>
            <a href="{html_nombre_archivo}" class="read-more">Leer artículo completo &rarr;</a>
        </div>
    </div>
    """

# HTML del Index principal con diseño moderno tipo revista digital
html_index = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tech & IA Insights | Reseñas y Recomendaciones</title>
    <style>
        :root {{
            --primary: #6366f1;
            --primary-glow: rgba(99, 102, 241, 0.4);
            --bg: #090d16;
            --card-bg: #111827;
            --text: #f3f4f6;
            --text-light: #9ca3af;
            --border: #1f2937;
            --accent: #38bdf8;
        }}
        body {{
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            max-width: 1100px;
            margin: 0 auto;
            padding: 50px 20px;
            line-height: 1.6;
        }}
        header {{
            text-align: center;
            margin-bottom: 60px;
            padding: 40px 20px;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(56, 189, 248, 0.1) 100%);
            border-radius: 24px;
            border: 1px solid var(--border);
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        }}
        header h1 {{
            font-size: 3rem;
            color: #ffffff;
            margin-bottom: 12px;
            letter-spacing: -0.03em;
            font-weight: 800;
            background: linear-gradient(to right, #ffffff, #93c5fd);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        header p {{
            color: var(--text-light);
            font-size: 1.2rem;
            max-width: 650px;
            margin: 0 auto;
        }}
        .posts-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 30px;
        }}
        .post-card {{
            background: var(--card-bg);
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
            transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
            border: 1px solid var(--border);
            display: flex;
            flex-direction: column;
        }}
        .post-card:hover {{
            transform: translateY(-6px);
            box-shadow: 0 20px 40px var(--primary-glow);
            border-color: var(--primary);
        }}
        .card-image-wrapper {{
            position: relative;
            width: 100%;
            height: 200px;
            overflow: hidden;
        }}
        .card-image-wrapper img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }}
        .post-card:hover .card-image-wrapper img {{
            transform: scale(1.05);
        }}
        .badge {{
            position: absolute;
            top: 15px;
            left: 15px;
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(8px);
            color: var(--accent);
            padding: 6px 12px;
            font-size: 0.75rem;
            font-weight: 700;
            border-radius: 20px;
            border: 1px solid rgba(56, 189, 248, 0.3);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        .card-body {{
            padding: 25px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }}
        .post-card h2 {{
            margin: 0 0 12px 0;
            font-size: 1.35rem;
            line-height: 1.4;
        }}
        .post-card h2 a {{
            color: #ffffff;
            text-decoration: none;
            transition: color 0.2s;
        }}
        .post-card h2 a:hover {{
            color: var(--accent);
        }}
        .post-card p {{
            color: var(--text-light);
            margin: 0 0 20px 0;
            font-size: 0.95rem;
            flex-grow: 1;
        }}
        .read-more {{
            display: inline-flex;
            align-items: center;
            font-weight: 600;
            color: var(--accent);
            text-decoration: none;
            font-size: 0.95rem;
            transition: opacity 0.2s;
        }}
        .read-more:hover {{
            opacity: 0.8;
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
        <p>Reseñas de software, análisis avanzados y las mejores herramientas seleccionadas para potenciar tu productividad.</p>
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
    f.write(html_index)

print("index.html y páginas individuales generadas con diseño moderno tipo revista.")
