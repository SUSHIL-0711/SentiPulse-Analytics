# --- src/preprocess.py ---
import re
from sklearn.base import TransformerMixin

class TextCleaner(TransformerMixin):
    def transform(self, X, **transform_params):
        return [self.clean_text(text) for text in X]

    def fit(self, X, y=None, **fit_params):
        return self

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r'http\S+|www\S+', '', text)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        return text.strip()