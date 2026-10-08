import os
import requests

# Obtener credenciales desde las variables de entorno de GitHub
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def enviar_mensaje_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mensaje,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

def buscar_plazas():
    # Simulación/Ejemplo de búsqueda
    # Aquí irá la lógica de extracción de convocatorias (MINSA, EsSalud, etc.)
    
    mensaje = (
        "🚨 *ALERTA DE PLAZAS MÉDICAS* 🚨\n\n"
        "🔎 *Regiones:* La Libertad, Ancash, Lambayeque (Costa)\n"
        "👨‍⚕️ *Especialidad:* Médico General\n\n"
        "✅ El sistema automatizado está activo y funcionando correctamente."
    )
    
    enviar_mensaje_telegram(mensaje)

if __name__ == "__main__":
    buscar_plazas()
