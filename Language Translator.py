pip install translate

from translate import Translator

def translate_text(text, target_languages, api_key):
    translations = {}
    for lang in target_languages:
        translator = Translator(provider='microsoft', to_lang=lang, secret_access_key=api_key)
        translation = translator.translate(text)
        translations[lang] = translation
    return translations

if __name__ == "__main__":
    text_to_translate = "Hello, how are you?"
    languages = ['es', 'fr', 'de', 'zh', 'ar']  # Spanish, French, German, Chinese, Arabic
    api_key = 'YOUR_MICROSOFT_TRANSLATOR_API_KEY'
    
    translated_texts = translate_text(text_to_translate, languages, api_key)

    for lang, translation in translated_texts.items():
        print(f"Translation in {lang}: {translation}")
