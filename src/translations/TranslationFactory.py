from src.translations.English import EnglishTranslation
from src.translations.Hebrew import HebrewTranslation


class TranslationFactory(object):
    TRANSLATIONS = {
        'Default': EnglishTranslation,
        'English': EnglishTranslation,
        'Hebrew': HebrewTranslation
    }

    @classmethod
    def get_translation(cls, lang='Default'):
        if lang not in cls.TRANSLATIONS:
            lang = 'Default'
        return cls.TRANSLATIONS[lang]()
