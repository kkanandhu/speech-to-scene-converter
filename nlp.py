import speech_recognition as sr
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import Tree
import os
import sys




#nlp =  spacy.load('en')
stop_words = set(stopwords.words('english'))
r = sr.Recognizer()
with sr.Microphone() as source:
	print ('Say somethin dude!!!')
	audio = r.listen(source)
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    result =r.recognize_google(audio)
    #result = "box1 is on a table1 "
    
    print("You said: " + result)
    print ('Tokenized result :')
    text = word_tokenize(result)
    text=[str(item) for item in text]
    res = [w for w in text if not w in stop_words]
 
    res = []
    for w in text:
    	if w not in stop_words:
    		res.append(w)
        
   

    tagged = nltk.pos_tag(res)
   # print( [str(item) for item in text])
    print( [str(item) for item in tagged])
    nouns = [] #empty to array to hold all nouns
    relatn= []
    attr = []
    pnouns = []
    
    '''
    out = open('Test.txt','r')
    i=0
    for line in out:
	    val = line
	    break
    out.close()  
    '''

    for word,pos in nltk.pos_tag(text):
        if (pos== 'NN' or pos=='IN' or  pos=='VBG'):
            relatn.append(word) 
        elif(pos == 'PRP' or pos == 'PRP$'):
        	pnouns.append(val)
    for word,pos in nltk.pos_tag(res):
        if (pos == 'NN'):
            nouns.append(word)
        elif (pos=='JJ'):
        	attr.append(word)

    '''print(nouns)
    print (relatn)
    print(attr)
    print(pnouns)
    print ("*************************OBJECTS & RELATIONS******************************")''' 
    #print([str(item) for item in nouns])
    #print ("*************************RELATIONS******************************")
    #print([str(item) for item in relatn])

    if sys.argv[1]=="clicked":
    	os.remove("C:\Users\Joyal\Desktop\project\init.txt")
    	os.remove("C:\Users\Joyal\Desktop\project\Test.txt")
    	os.remove("C:\Users\Joyal\Desktop\project\\attr.txt")
    	os.remove("C:\Users\Joyal\Desktop\project\\rel.txt")
    	print ("files deleted")
    else:
    	init_file = open('init.txt', 'a')
        init_file.write("%s\n" % result)


    	thefile = open('Test.txt', 'a')
        for item in nouns:
        	thefile.write("%s " % item)
        thefile.write("\n" )
        thefile.close()


        att = open('attr.txt', 'a') 
        for items in attr:
        	att.write("%s " % items)
        att.write("\n")
        att.close()


        rel =open('rel.txt', 'a')
        for items in relatn:
        	rel.write("%s " % items)
        rel.write("\n")
        rel.close()


        '''
        i=0
        b= {}
    
        b= {i : nouns[i] for i in range(0 , len(nouns))}
        
        print (b)
        '''

    	
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
