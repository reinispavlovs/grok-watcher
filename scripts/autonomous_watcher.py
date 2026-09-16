import os
import sys
import requests
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

import parallax_model

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
AI_API_KEY = os.getenv("AI_API_KEY")

def watch_and_extract_sources():
    return {"status": "scanning"}

def analyze_and_filter_noise(targets):
    engine = parallax_model.PARALLAX_KNOWLEDGE_ENGINE
    metadata = engine["project_metadata"]
    
    if not AI_API_KEY:
        return "Kļūda: Nav atrasta AI_API_KEY GitHub Secrets."

    # Pareizais un stabils xAI API galapunkts
    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {AI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    prompt = (
        f"Tu esi Project Parallax autonomais izlūkošanas aģents. Tavs mērķis ir analizēt jaunāko informāciju par xAI un autonomajām sistēmām. "
        "Atmet visu mārketinga troksni un izvelc vienu konkrētu tehnisko kodolu, "
        f"kas uzlabotu mūsu platformu ('{metadata['name']}', mērķis: {metadata['core_objective']})."
    )
    
    payload = {
        "model": "grok-2",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=45)
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
    targets = watch_and_extract_sources()
    ai_result = analyze_and_filter_noise(targets)
    
    telegram_message = (
        "🚀 *Project Parallax — Live Watcher Rezultāts*\n\n"
        f"{ai_result}"
    )
    
    print(telegram_message)
    send_telegram_alert(telegram_message)