import spacy
import unicodedata

nlp = spacy.load("es_core_news_sm")

def normalize_text(text):
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    return text.lower().replace('?', '').replace('¿', '').strip()

def get_intent(message):
    normalized_message = normalize_text(message)
    doc = nlp(normalized_message)

    if any(token.lemma in ["clima", "tiempo"] for token in doc):
        return "weather"
    elif "unidad de fomento" in normalized_message or "uf" in normalized_message:
        return "uf"
    elif any(token.lemma in ["dolar", "usd"] for token in doc):
        return "dollar"
    elif any(token.lemma_ in ["noticia", "noticias", "novedad"] for token in doc):
        return "news"
    else:
        return "unknown"