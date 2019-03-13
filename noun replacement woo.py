import nltk
nltk.download('punkt')
from googletrans import Translator
translator = Translator()

while(1):
    from nltk.tokenize import word_tokenize
    sentence = input("Welcome to SpInPy! Enter '*' to exit.\nPlease type a sentence in English: ")
    if sentence == '*':
        break
    words = word_tokenize(sentence)
    if words[-1] == '.':
        del words[-1]
    tagged_words = nltk.pos_tag(words)
    print(tagged_words)

    for word in tagged_words:
        if word[1] == 'NN' or word[1] == 'NNS':
            es_word = (translator.translate(word[0], dest='es').text)
            i = tagged_words.index(word)
            words[i] = es_word

    s = ' '
    cs_sentence = s.join(words) 
    cs_sentence = cs_sentence + '.'
    print(cs_sentence)
