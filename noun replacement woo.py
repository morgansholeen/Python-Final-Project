import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from googletrans import Translator
import pyttsx3
engine = pyttsx3.init()
translator = Translator()
from nltk.tokenize import word_tokenize

dict1 = []
result = ''
destlang= 'es'

while(1):
   mode = input("Welcome to SpInPy! Enter 1 for speech mode, 2 for dictionary mode or 3 for language settings: ") 
   imode = int(mode)
   if (imode== 1):
        sentence = input("Please type a sentence in English: ")
        words = word_tokenize(sentence)
        del words[-1]
        tagged_words = nltk.pos_tag(words)
        #print(tagged_words)
        for word in tagged_words:
            if word[1] == 'NN' or word[1] == 'NNS':
                es_word = (translator.translate(word[0], dest=destlang).text)
                words[tagged_words.index(word)] = es_word
                dict1.extend((es_word, word[0]))
        s = ' '
        cs_sentence = s.join(words) 
        result = cs_sentence + '.'

   if (imode== 2):
        result=dict1

   if (imode== 3):
       alang = ''
       lang = input("Enter f for French, g for German or s for Spanish (default): ")
       ilang = str(lang)
       if(ilang == 'f'):
           alang = 'fr'
       if(ilang == 'g'):
           alang = 'de'
       if(ilang == 's'):
           alang = 'es'
       destlang=alang
           
          

   if imode== 1 or imode==2:        
       print(result)
       engine.say(result)
       engine.runAndWait()

   if imode==2:       
       dict1.clear()
