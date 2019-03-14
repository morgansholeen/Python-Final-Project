#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:50:53 2019

@author: lindiatjuatja
"""

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
   mode = input("Welcome to SpInPy!\n Main menu-- (1) code switch    (2) dictionary   (3) change language   (*) exit\n Mode select: ") 
   imode = mode
   
   if (imode == '*'):
       print('¡Adios¡ Goodbye!')
       break
   
   if (imode == '1'):
     print('\nCode switch mode. Enter (*) to go back to the main menu.')
     while(1): 
        sentence = input("Type a sentence in English: ")
        if sentence == '*':
            break
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
        print(result)

   if (imode== '2'):
        result=dict1

   if (imode== '3'):
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
        
        
        