import os
import sys
import requests
import json

# Pievienojam saknes mapi ceļam, lai varētu ielādēt parallax_model.py no saknes
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

import parallax_model

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
AI_API_KEY = os.getenv("AI_API_KEY")

def fetch_live_updates():
    """
    Solis 1: Datu uztveres modulis, izmantojot Project Parallax modeli.
    """
    print("Skenēju un ielādēju Parallax zināšanu dzinēja moduļus...")
    engine = parallax_model.PARALLAX_KNOWLEDGE_ENGINE
    return engine

def adapt_to_user_ecosystem(engine_data):
    """
    Solis 2: AI adaptācijas dzinējs, kas strukturē datus priekš myparallax.org.
    """
    print("Pielāgoju arhitektūru Project Parallax mērķiem...")
    
    metadata = engine_data["project_metadata"]
    modules = engine_data["modules"]
    
    # Apkopojam moduļu mērķus un metodoloģiju
    modules_summary = "\n".join([f"• *{m['name']}*: {m['practical_goal']}" for m in modules])
    
    analysis = {
        "summary": metadata["core_objective"],
        "modules_text": modules_summary,
        "parallax_integration": "Dati un fenomenoloģiskie pētījumi tiek gatavoti myparallax.org matricas un mapped % celšanai.",
    }
    return analysis

def send_telegram_alert(message):
    """
    Solis 3: Piegāde uz Telegram.
    """
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram atslēgas nav iestatītas. Izlaižu sūtīšanu.")
        return
        
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    return response.json()

if __name__ == "__main__":
    raw_data = fetch_live_updates()
    adapted_result = adapt_to_user_ecosystem(raw_data)
    
    telegram_message = (
        "🚀 *Project Parallax — Autonomais Dzinējs*\n\n"
        f"📌 *Pamatuzdevums:*\n{adapted_result['summary']}\n\n"
        f"🌌 *Aktīvie Parallax moduļi un mērķi:*\n{adapted_result['modules_text']}\n\n"
        f"📈 *Platformas integrācija:* {adapted_result['parallax_integration']}\n\n"
        "_Sistēma veiksmīgi ielādējusi Parallax arhitektūru un gatava fonu analīzei._"
    )
    
    print(telegram_message)
    send_telegram_alert(telegram_message)