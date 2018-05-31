import speech_recognition as ss
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import spacy
from nltk import Tree

##nlp = spacy.load('en')




#stop_words = set(stopwords.words('english'))
r=ss.Recognizer()




with ss.Microphone() as source:
	print ('Say somethin dude!!!')
	audio = r.listen(source)





try:
	result = r.recognize_google(audio)
	
	text = word_tokenize(result)
	print ('\nTokenized result : \n')
	print (text)

	
	'''def find_ngrams(input_list, n):
  		return zip(*[input_list[i:] for i in range(n)])

	filtered_sentence = [w for w in text if not w in stop_words]
	filtered_sentence = []

	

	for w in text:
		if w not in stop_words :
			filtered_sentence.append(w)

	print ('\nstop words removal :\n')
	print(filtered_sentence)

	
	tagged = nltk.pos_tag(filtered_sentence)

	print ('\nPOS tagged result:\n')
	print (tagged)

	sent = nlp(result)

	def to_nltk_tree(node):
	    if node.n_lefts + node.n_rights > 0:
	        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
	    else:
	        return node.orth_

	print ('\nDependency Tree from sentence :\n')

	[to_nltk_tree(sent.root).pretty_print() for sent in sent.sents]

	
	ngrams = find_ngrams(text , 3)
	print(ngrams)'''
	
except:
	print ('say once more')
