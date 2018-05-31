import speech_recognition as sr
import nltk
#nltk.download('punkt')
#nltk.download('brown')
#nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from nltk import Tree
from textblob import TextBlob
import spacy




#nlp =  spacy.load('en')

r = sr.Recognizer()
with sr.Microphone() as source:
	print ('Say somethin dude!!!')
	audio = r.listen(source)
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    result =r.recognize_google(audio)
    print("You said: " + result)
    print ('Tokenized result :')
    text = word_tokenize(result)
    text=[str(item) for item in text]
    tagged = nltk.pos_tag(text)
   # print( [str(item) for item in text])
    print( [str(item) for item in tagged])
    nouns = [] #empty to array to hold all nouns
    relatn= []
    #blob = TextBlob(result)
    #print(blob.noun_phrases)
    #for sentence in tagged:
    for word,pos in nltk.pos_tag(text):
        if (pos == 'NN'or pos=='IN'or pos=='VBG' ):
            nouns.append(word)
        #elif (pos=='IN'or pos=='VBG'):
           # relatn.append(word)
    print(nouns)
    print ("*************************OBJECTS & RELATIONS******************************") 
    print([str(item) for item in nouns])
    #print ("*************************RELATIONS******************************")
    #print([str(item) for item in relatn])
    thefile = open('test.txt', 'w')
    for item in nouns:
        thefile.write("%s\n" % item)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
