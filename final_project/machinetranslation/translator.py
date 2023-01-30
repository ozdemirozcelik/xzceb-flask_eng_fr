import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


# translator_instance

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# e2f_translator_function

def englishToFrench(englishText):
    translation = language_translator.translate(
    frenchText=englishText,
    model_id='en-fr').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return frenchText

# f2e_translator_function

def frenchToEnglish(frenchText):
    translation = language_translator.translate(
    englishText=frenchText,
    model_id='fr-en').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return englishText