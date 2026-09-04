import os
import datetime
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No se encontró la GEMINI_API_KEY en las variables de entorno.")

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-2.0-flash"
print(f"Intentando generar contenido con el modelo {MODEL_NAME}...")

try:
    prompt = """
    Escribe un artículo de blog persuasivo, moderno y con enfoque de conversión sobre una herramienta de Inteligencia Artificial o software de productividad.
    
    Sigue estrictamente esta estructura:
    1. Un título llamativo y directo (en formato Markdown #).
    2. Una introducción que enganche al lector.
    3. Subtítulos claros (##) que desarrollen las características principales.
    4. Viñetas (-) resaltando los beneficios clave.
    5. Un párrafo final de conclusión con un Llamado a la Acción (CTA) invitando a probar la herramienta mediante un enlace de afiliado (ejemplo: [Accede aquí con descuento especial](TUS_HOTLINKS_AQUÍ)).
    
    Escribe todo en formato Markdown limpio y en idioma español. No agregues texto introductorio fuera del artículo.
    """
    
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )
    contenido_markdown = response.text

except Exception as e:
    print(f"Error al conectar con el modelo: {e}")
    raise e

os.makedirs("posts", exist_ok=True)

fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
nombre_archivo = f"posts/articulo-{fecha_actual}.md"

with open(nombre_archivo, "w", encoding="utf-8") as f:
    f.write(contenido_markdown)

print(f"Artículo generado y guardado con éxito en {nombre_archivo}")
