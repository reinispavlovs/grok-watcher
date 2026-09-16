import os
import sys
import requests
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

import parallax_model
import parallax_graph_engine

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
AI_API_KEY = os.getenv("AI_API_KEY")

def analyze_and_extract_triples():
    """
    Izmanto Grok 4.6, lai analizētu avotus un izvilktu strukturētus trijniekus,
    novēršot mārketinga troksni.
    """
    if not AI_API_KEY:
        return "Kļūda: Nav atrasta AI_API_KEY GitHub Secrets."

    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {AI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    prompt = (
        "Tu esi Project Parallax autonomais zināšanu grafa ekstrakcijas aģents. "
        "Analizē jaunākos datus par xAI un autonomajām sistēmām. "
        "Atmet visu mārketinga troksni. Atgriez datus formātā: "
        "Subjekts | Relācija | Objekts | Slānis (module_1_lost_engineering / module_2_precession_and_cycles / module_3_clinical_consciousness / cosmic_isomorphism)"
    )
    
    payload = {
        "model": "grok-4.6",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=120)
        if response.status_code == 200:
            result_json = response.json()
            return result_json["choices"][0]["message"]["content"]
        else:
            return f"API Kļūda (Status {response.status_code}): {response.text}"
    except Exception as e:
        return f"Izņēmuma kļūda savienojumā: {str(e)}"

def send_telegram_alert(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    # Inicializējam zināšanu grafa dzinēju
    engine = parallax_graph_engine.ParallaxGraphEngine()
    
    # Pievienojam bāzes dzinēja testa trijnieku vai dinamiski iegūtos datus
    engine.add_triple("Project_Watcher", "EXTRACTS_VIA", "Grok_4.6", "cosmic_isomorphism", "GitHub_Action", 0.95)
    
    # Iegūstam datus caur AI
    ai_extraction = analyze_and_extract_triples()
    
    # Aprēķinām pašreizējo matricas mapped %
    current_mapped = engine.calculate_mapped_percentage()
    graph_state = engine.export_graph_state()
    
    telegram_message = (
        "🧠 *Project Parallax — Knowledge Graph Watcher*\n\n"
        f"📊 *Pašreizējais Mapped Coverage:* `{current_mapped}%`\n"
        f"🔗 *Kopējie trijnieki grafa matricā:* {graph_state['total_triples']}\n"
        f"⚠️ *Saglabātās pretrunas (konflikti):* {graph_state['total_contradictions']}\n\n"
        f"⚙️ *Grok 4.6 Ekstrakcijas kodols:*\n{ai_extraction}"
    )
    
    print(telegram_message)
    send_telegram_alert(telegram_message)