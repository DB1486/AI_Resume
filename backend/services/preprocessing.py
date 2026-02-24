import re
import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)

    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop]

    return " ".join(tokens)