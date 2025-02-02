import json

class TranslationManager:
    def __init__(self, file_path="assets/translation.json", default_lang="fr"):
        self.file_path = file_path
        self.default_lang = default_lang
        self.translations = self.load_translations()

    def load_translations(self):
        try:
            with open(self.file_path, "r", encoding="utf8") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Erreur : Le fichier translation.json est introuvable !")
            return {}

    def set_language(self, lang):
        if lang in self.translations:
            self.default_lang = lang
        else:
            print(f"Langue '{lang}' non disponible, utilisation de {self.default_lang}")

    def translate(self, need_translation):

        data = self.translations.get(self.default_lang, {})
        # for word in need_translation:
            # if word in data:
            #     translation = data[word]
            # else:
            #     return word
        if need_translation in data:
            translation = data[need_translation]
        else:
            return need_translation
        return translation
