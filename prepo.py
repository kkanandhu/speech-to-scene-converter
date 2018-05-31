import nltk
from nltk.tokenize import word_tokenize
import sys
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


context=sys.argv[1].replace('.',' ')
color=['red','blue','green','yellow']
size=['very small','tiny','small','big','very big']
stopwords=['of','side','to','the','colour']
stems=[]
number = {'one':1,
     	'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9,
        'ten':10,

        }

context=context.replace(" a "," one ");
tokens = nltk.word_tokenize(context)
tagged = nltk.pos_tag(tokens)
nouns = [word for word,pos in tagged \
	if (pos == 'JJ' or pos == 'NNP' or pos == 'NNS' or pos == 'IN' or pos == 'NN' or pos == 'CD' or pos == 'CC' )]
downcased = [x.lower() for x in nouns]
joined = " ".join(downcased).encode('utf-8')
into_string = str(nouns)
for item in stopwords:
	joined=joined.replace(item,"")

clearedList=joined.split()
ps = PorterStemmer()
lmtzr = WordNetLemmatizer()

for word in clearedList:
    stems.append( lmtzr.lemmatize(word))

conjunction=[]
tagged = nltk.pos_tag(stems)
nouns = [word for word,pos in tagged \
	if (pos == 'CC' or pos == 'IN')]
downcased = [x.lower() for x in nouns]
conjunction = " ".join(downcased).encode('utf-8')

tagged = nltk.pos_tag(stems)
nouns = [word for word,pos in tagged \
	if (pos == 'NNP' or pos == 'NNS' or pos == 'NN' or pos == 'CD' or pos == 'IN')]
downcased = [x.lower() for x in nouns]
joined = " ".join(downcased).encode('utf-8')



tokens = nltk.word_tokenize(joined)
tagged = nltk.pos_tag(tokens)
n_n= [word for word, tag in tagged if tag in ('CD')]

for item in n_n:
	joined=joined.replace(item+" ",str(number[item])+".")

joined+=" ."

second=""
first=""
if conjunction=="":
	second="."
	first=joined
else:
	first=joined.replace(conjunction,"");
	second=joined



print first
print second



