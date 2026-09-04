import os
import datetime
import time
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No se encontró la variable de entorno GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

temas = [
    "Las mejores prácticas para programar en Python de forma eficiente",
    "Herramientas de IA indispensables para desarrolladores junior",
    "Cómo estructurar bases de datos relacionales sin morir en el intento"
]

dia_actual = datetime.datetime.now().day
tema_actual = temas[dia_actual % len(temas)]

prompt = f"""
Escribe un artículo de blog corto, útil y optimizado para SEO sobre: '{tema_actual}'.
Estructura el texto en formato Markdown con un título llamativo (H1), subtítulos (H2) y párrafos claros.
Al final del artículo, añade de forma natural una recomendación útil con un enlace de afiliado genérico.
"""

# Lista de modelos de respaldo por si uno presenta alta demanda
modelos_a_probar = ["gemini-1.5-flash", "gemini-2.0-flash"]
response = None

for modelo in modelos_a_probar:
    try:
        print(f"Intentando generar contenido con el modelo {modelo}...")
        response = client.models.generate_content(
            model=modelo,
            contents=prompt,
        )
        break
    except Exception as e:
        print(f"El modelo {modelo} no respondió ({e}), intentando con el siguiente...")
        time.sleep(3)

if not response:
    raise Exception("Todos los modelos reportaron alta demanda temporal. Intenta ejecutarlo nuevamente en unos minutos.")

fecha_str = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
nombre_archivo = f"posts/articulo-{fecha_str}.md"

os.makedirs("posts", exist_ok=True)

with open(nombre_archivo, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Artículo generado con éxito: {nombre_archivo}")
