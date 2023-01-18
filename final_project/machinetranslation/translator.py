import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(version='{version}', authenticator=authenticator)

language_translator.set_service_url(f'{url}')

def englishToFrench(englishText):
    """Usimg IBM Watson's Language Translation API to convert English Text to French"""

    translation = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    
    frenchText = translation['translations'][0]['translation']

    return frenchText

def frenchToEnglish(frenchText):
    """Usimg IBM Watson's Language Translation API to convert English Text to French"""

    translation = language_translator.translate(text=frenchText,model_id='fr-en').get_result()
    
    englishText = translation['translations'][0]['translation']

    return englishText