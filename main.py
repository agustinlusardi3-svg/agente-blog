import os
import datetime
import time
from google import genai
from google.genai.errors import ServerError

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No se encontró la GEMINI_API_KEY en las variables de entorno.")

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-3.6-flash"
print(f"Intentando generar contenido con el modelo {MODEL_NAME}...")

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

intentos = 5
exito = False
contenido_markdown = ""

for intento in range(1, intentos + 1):
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )
        contenido_markdown = response.text
        exito = True
        break
    except ServerError as e:
        tiempo_espera = intento * 8  # Espera progresiva: 8s, 16s, 24s, 32s...
        print(f"Intento {intento} fallido por alta demanda (503). Reintentando en {tiempo_espera} segundos...")
        if intento == intentos:
            raise e
        time.sleep(tiempo_espera)
    except Exception as e:
        print(f"Error inesperado al conectar con el modelo: {e}")
        raise e

if not exito:
    raise Exception("No se pudo generar contenido tras varios intentos debido a la alta demanda.")

os.makedirs("posts", exist_ok=True)

fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
nombre_archivo = f"posts/articulo-{fecha_actual}.md"

with open(nombre_archivo, "w", encoding="utf-8") as f:
    f.write(contenido_markdown)

print(f"Artículo generado y guardado con éxito en {nombre_archivo}")
