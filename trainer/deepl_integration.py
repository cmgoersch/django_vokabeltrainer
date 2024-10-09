import requests

def translate_to_finnish(text, api_key):
    url = "https://api-free.deepl.com/v2/translate"
    data = {
        'auth_key': api_key,
        'text': text,
        'target_lang': 'FI'  # Finnische Sprache
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:
        result = response.json()
        return result['translations'][0]['text']  # Rückgabe des übersetzten Textes
    else:
        return None  # Rückgabe von None, falls die Übersetzung fehlschlägt