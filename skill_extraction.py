import spacy
from spacy.matcher import PhraseMatcher
nlp = spacy.load("en_core_web_sm")
SKILLS = [
    "python", "machine learning", "deep learning",
    "nlp", "tensorflow", "pytorch",
    "sql", "data analysis", "scikit-learn"
]
def extract_skills(text):
    doc = nlp(text.lower())
    matcher = PhraseMatcher(nlp.vocab)
    patterns = [nlp(skill) for skill in SKILLS]
    matcher.add("SKILLS", patterns)
    matches = matcher(doc)
    extracted = set()
    for match_id, start, end in matches:
        extracted.add(doc[start:end].text)
    return list(extracted)