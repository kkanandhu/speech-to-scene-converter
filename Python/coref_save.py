from neuralcoref import Coref
import nltk
'''

paragraph="There is a table.There is a lamp on it.It has red colour"
sentences=paragraph.split('.')

for item in sentences[:1]:
	print item
'''







'''
COREFERENCE RESOLUTION

'''
con="lamp on table"
utt="chair near to table"


paragraph="there is a table.there is a lamp on it.it has white colour"
sentences=paragraph.split('.')

coref = Coref()
clusters = coref.one_shot_coref(utterances=unicode(utt), context=unicode(con))
a = coref.get_mentions()
first=str(a[0])
one=[]
for item in a:
	one.append(str(item))
two=first.split()

utterances = coref.get_utterances()

resolved_utterance_text = coref.get_resolved_utterances()
print(resolved_utterance_text)

diff=list(set(two) - set(one))

tagged = nltk.pos_tag(diff)
nouns = [word for word,pos in tagged \
	if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
downcased = [x.lower() for x in nouns]
joined = " ".join(downcased).encode('utf-8')
into_string = str(nouns)

utt=utt.replace("it",joined)
utt=utt.replace("It",joined)
utt=utt.replace("she",joined)
utt=utt.replace("he",joined)
print utt


'''
COREFERENCE RESOLUTION
'''