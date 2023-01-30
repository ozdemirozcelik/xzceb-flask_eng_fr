import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

apikey='1Hm8VgotC85OAchxsi4P5iuUrgz9owNEHEhEl54W9OYy'
url='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/d73e4c52-aa64-47b5-8c33-fef2e586592e'


#translator_instance

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# e2f_translator_function

def englishToFrench(englishText):
    if englishText is not None:
        translation = language_translator.translate(text=englishText, model_id='en-fr').get_result()
        return translation['translations'][0]["translation"]
    else:
        return "null input"

# f2e_translator_function

def frenchToEnglish(frenchText):
    if frenchText is not None:
        translation = language_translator.translate(text=frenchText, model_id='fr-en').get_result()
        return translation['translations'][0]['translation']
    else:
        return "null input"