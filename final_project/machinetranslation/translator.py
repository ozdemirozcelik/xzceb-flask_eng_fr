import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

#translator_instance

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

# e2f_translator_function

def english_to_french(english_text):
    if english_text is not None:
        translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
        return translation['translations'][0]["translation"]
    else:
        return "null input"

# f2e_translator_function

def french_to_english(french_text):
    if french_text is not None:
        translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
        return translation['translations'][0]['translation']
    else:
        return "null input"
