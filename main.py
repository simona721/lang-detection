from deep_translator import GoogleTranslator


lang_text = input("Enter a text to be translated: ")
trans_to = input("Enter a language you want to translate the text to: ")

#The entered text is translated in the language you want
translated = GoogleTranslator(source="en", target=trans_to).translate(text=lang_text)
#print(translated)

#This auto detects the input text and translates it in the language you want
auto_detection = GoogleTranslator(source="auto", target=trans_to).translate(text=lang_text)
print(auto_detection)