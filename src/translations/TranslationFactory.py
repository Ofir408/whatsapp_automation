from src.translations.English import EnglishTranslation


class TranslationFactory(object):
    TRANSLATIONS = {
        'Default': EnglishTranslation,
        'English': EnglishTranslation
    }

    @classmethod
    def get_translation(cls, lang='Default'):
        if lang not in cls.TRANSLATIONS:
            lang = 'Default'
        return cls.TRANSLATIONS[lang]()
