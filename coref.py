from neuralcoref import Coref
import nltk
from nltk.tokenize import word_tokenize
import sys
import os


sys.stdout = open(os.devnull, "w")

resolved_sentence=[]

con=sys.argv[1].replace("_"," ")
utt=sys.argv[2].replace("_"," ")






coref = Coref()

clusters = coref.one_shot_coref(utterances=unicode(utt), context=unicode(con))

candidates = coref.get_mentions()


utterances = coref.get_utterances()

resolved_utterance_text = coref.get_resolved_utterances()

sys.stdout = sys.__stdout__
First=str(candidates[0]).split()

one=[]
for item in candidates:
	one.append(str(item))

two=[]
Three=[]
for item in one:

	tokens = nltk.word_tokenize(item)
	tagged = nltk.pos_tag(tokens)
	nouns = [word for word,pos in tagged \
		if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' )]
	downcased = [x.lower() for x in nouns]
	joined = " ".join(downcased).encode('utf-8')
	into_string = str(nouns)

	two=joined.split()
	for item in two:

		Three.append(item)



tokens = nltk.word_tokenize(utt)
tagged = nltk.pos_tag(tokens)
nouns = [word for word,pos in tagged \
	if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' )]
downcased = [x.lower() for x in nouns]
joined = " ".join(downcased).encode('utf-8')
nouns=joined.split()

for item in nouns:
	if item[-1]=="1":
		print item
		utt=utt.replace(item,"a "+item)







utt=utt.replace("it","a "+Three[0])




resolved_sentence.append(utt)


print resolved_sentence[0]


'''
COREFERENCE RESOLOUTION
'''


