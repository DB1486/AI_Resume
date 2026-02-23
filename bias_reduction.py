import spacy
import re
nlp = spacy.load("en_core_web_sm")
GENDER_WORDS = ["he", "she", "him", "her", "male", "female"]
def remove_bias(text):
    doc = nlp(text)
    cleaned_tokens = []
    for token in doc:
        if token.ent_type_ in ["PERSON", "GPE"]:
            continue
        if token.text.lower() in GENDER_WORDS:
            continue
        cleaned_tokens.append(token.text)
    return " ".join(cleaned_tokens)