import json


class TranslationManager:
    def __init__(self, file_path="translation.json", default_lang="fr"):
        self.file_path = file_path
        self.default_lang = default_lang
        self.translations = self.load_translations()

    def load_translations(self):
        try:
            with open(self.file_path, "r", encoding="utf8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("Erreur : Le fichier translation.json est introuvable !")
            return {}

    def set_language(self, lang):
        if lang in self.translations:
            self.default_lang = lang
        else:
            print(f"Langue '{lang}' non disponible, utilisation de {self.default_lang}")

    def translate(self, *keys):
       
        data = self.translations.get(self.default_lang, {})
        for key in keys:
            if isinstance(data, dict) and key in data:
                data = data[key]
            else:
                return key
        return data
