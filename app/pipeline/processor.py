from typing import List, Dict
import re

class DocumentProcessor:
    def __init__(self):
        pass

    def clean_text(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        return text.strip()

    def extract_entities(self, text: str) -> List[Dict[str, str]]:
        # Placeholder for entity extraction logic
        entities = []
        # Example: Extracting simple entities based on keywords
        if "NLP" in text:
            entities.append({"entity": "NLP", "type": "Technology"})
        return entities

    def process_document(self, document: str) -> Dict[str, List[Dict[str, str]]]:
        cleaned_text = self.clean_text(document)
        entities = self.extract_entities(cleaned_text)
        return {
            "cleaned_text": cleaned_text,
            "entities": entities
        }