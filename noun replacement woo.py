"""
Created on Tue Mar 12 21:50:53 2019

@author: lindiatjuatja
"""
#modules to be used
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from googletrans import Translator
import pyttsx3
engine = pyttsx3.init()
translator = Translator()
from nltk.tokenize import word_tokenize

#global variables
dict1 = []
result = ''
destlang= 'es'

#codeswitch function for mode (1)
def codeswitch():
    flag = 1
    while(flag): 
        sentence = input("Type a sentence in English: ")
        if sentence == '*':
            break
        words = word_tokenize(sentence)
        if words[-1] == '.':
            del words[-1]
        tagged_words = nltk.pos_tag(words)
        for word in tagged_words:
            if word[1] == 'NN' or word[1] == 'NNS':
                es_word = (translator.translate(word[0], dest=destlang).text)
                words[tagged_words.index(word)] = es_word
                dict1.extend((es_word, word[0]))
        s = ' '
        cs_sentence = s.join(words) 
        result = cs_sentence + '.'
        while(1):
            listen = input(f'{result}\nEnter (@) to listen, (n) to enter a new sentence, (*) to go back to main menu: ')
            if (listen == '@'):
                engine.say(result)
                engine.runAndWait()
                break
            elif (listen == 'n'):
                break
            elif (listen == '*'):
                flag = 0
                break
            else: 
                print("\nNot a valid input. ")
    return;

#outer loop - main menu and exit
while(1):
   mode = input("Welcome to SpInPy!\n Main menu-- (1) code switch    (2) dictionary   (3) change language   (*) exit\n Mode select: ") 
   imode = mode
   
   if imode == '*':
       print('¡Adios¡ Goodbye!')
       break
   
   elif imode == '1':
     print('\nCode switch mode. Enter (*) to go back to the main menu.')
     codeswitch()
     
#   if (imode== '2'):
#        result=dict1

   elif imode == '3':
       langPrompt = 1
       alang = ''
       while(langPrompt):
           lang = input("To return to the main menu, enter (*)\nEnter (f) for French, (g) for German or (s) for Spanish (default): ")
           if (lang == '*'):
               langPrompt = 0;
           elif (lang == 'f'):
               alang = 'fr'
               langPrompt = 0
           elif (lang == 'g'):
               alang = 'de'
               langPrompt = 0
           elif(lang == 's'):
               alang = 'es'   
               langPrompt = 0
           else: 
               print("\nNot a valid input. ")
       destlang = alang
       
   else:
       print("\nNot a valid input. ")
           
#   if imode==2:       
#       dict1.clear()
       
   else:
       print("\nNot a valid input. ")
           
#   if imode==2:       
#       dict1.clear()
        
