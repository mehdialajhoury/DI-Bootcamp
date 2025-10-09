"""Instructions :

Consider this list

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
Look at this result :
{"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}"""


from googletrans import Translator
import asyncio


async def TranslateText(text):
  async with Translator() as translator:
    result = await translator.translate(text, src="fr", dest="en")
    return result.text

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

text ="Bonjour"
dict_trad = {}

for word in french_words:
  dict_trad[word] = asyncio.run(TranslateText(word))