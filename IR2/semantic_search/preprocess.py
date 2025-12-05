from hazm import Normalizer, Lemmatizer

normalizer = Normalizer()
lemmatizer = Lemmatizer()

def preprocess_text(text: str) -> str:
    if not text:
        return ""
    text = normalizer.normalize(text)
    text = " ".join([lemmatizer.lemmatize(w) for w in text.split()])
    return text
