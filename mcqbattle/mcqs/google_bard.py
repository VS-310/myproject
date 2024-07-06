# mcqs/google_bard.py
from django.conf import settings
import google.generativeai as gemini # type: ignore

# Configure the API key
gemini.configure(token=settings.BARD_API_KEY)

def get_response(prompt):
    response = gemini.chat(messages=prompt)
    return response