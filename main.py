import os
import datetime
from google import genai

# Configura tu clave de API desde las variables secretas de la nube
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No se encontró la variable de entorno GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# Lista de temas que el bot irá alternando
temas = [
    "Las mejores prácticas para programar en Python de forma eficiente",
    "Herramientas de IA indispensables para desarrolladores junior",
    "Cómo estructurar bases de datos relacionales sin morir en el intento"
]

# Seleccionar un tema de forma segura usando el día del mes
dia_actual = datetime.datetime.now().day
tema_actual = temas[dia_actual % len(temas)]

prompt = f"""
Escribe un artículo de blog corto, útil y optimizado para SEO sobre: '{tema_actual}'.
Estructura el texto en formato Markdown con un título llamativo (H1), subtítulos (H2) y párrafos claros.
Al final del artículo, añade de forma natural una recomendación útil con un enlace de afiliado genérico.
"""

# Llamada a la IA usando el modelo actual disponible
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
)

# Generar nombre de archivo único basado en la fecha actual
fecha_str = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
nombre_archivo = f"posts/articulo-{fecha_str}.md"

# Asegurar que la carpeta posts exista
os.makedirs("posts", exist_ok=True)

# Guardar el contenido generado
with open(nombre_archivo, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Artículo generado con éxito: {nombre_archivo}")
