import os
import datetime
import google.generativeai as genai

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No se encontró la GEMINI_API_KEY en las variables de entorno.")

genai.configure(api_key=api_key)

MODEL_NAME = "gemini-1.5-flash"
print(f"Intentando generar contenido con el modelo {MODEL_NAME}...")

try:
    model = genai.GenerativeModel(MODEL_NAME)
    
    prompt = """
    Escribe un artículo de blog persuasivo, moderno y con enfoque de conversión (tipo reseña o recomendación de valor) sobre una herramienta de Inteligencia Artificial o software de productividad muy útil actualmente.
    
    Sigue estrictamente esta estructura:
    1. Un título llamativo y directo (en formato Markdown #).
    2. Una introducción que enganche al lector conectando con un problema real.
    3. Subtítulos claros (##) que desarrollen las características principales y beneficios clave.
    4. Viñetas (-) resaltando por qué vale la pena usarla.
    5. Un párrafo final de conclusión con un Llamado a la Acción (CTA) muy persuasivo que invite a hacer clic y adquirir la herramienta recomendada a través de un enlace de afiliado (deja el enlace preparado con este formato de ejemplo: [Accede aquí con descuento especial](TUS_HOTLINKS_AQUÍ)).
    
    Escribe todo el contenido en formato Markdown limpio y en idioma español. No agregues texto introductorio fuera del artículo.
    """
    
    response = model.generate_content(prompt)
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
