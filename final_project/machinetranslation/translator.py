from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate English text to French.
    
    Parameters:
        english_text (str): The English text to be translated.
    
    Returns:
        str: The translated French text.
    """
    french_text = MyMemoryTranslator(source='en-US', target='fr-FR').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translate French text to English.
    
    Parameters:
        french_text (str): The French text to be translated.
    
    Returns:
        str: The translated English text.
    """
    english_text = MyMemoryTranslator(source='fr-FR', target='en-US').translate(french_text)
    return english_text
