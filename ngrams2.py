# this is a program which can generate sentences based on ngrams

# sample input is n = 2 and m= 10 

# algorithm

# step 1: inpu the the ngram model type the sentences to be genearted
# step 2 create the ngra,
# step 3 create the conditinal probabilities 
# step 4 generate the senetences


from sys import argv
import nltk
import random
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.util import ngrams
from collections import Counter # to coun the frequency
from nltk.corpus import gutenberg # importing the gutenburg corpus 

ngram_value = int(argv[1]) # to intend the ngram model
sent_count = int(argv[2]) # to intend the sentencce count 
CORPORA = argv[3:]   # to intend the number of text files

text = ' '.join(gutenberg.raw(corpus) for corpus in CORPORA) #accepting the gutenberg text
token = word_tokenize(text.lower())  # tokenizing the text

print (" this is a program which will genearte the sentences based on ngrams.Created by Shravan and Adithya")
print (" the ngram value and sentence count value are:")
print (ngram_value, sent_count)

print(len(token))



ngrams1 = ngrams(token,ngram_value) # creating the ngram 

cfd = nltk.ConditionalFreqDist(ngrams1) # genearting the probalities of the markov chain
print(cfd)

for i in range(sent_count):
    def generate_model(cfdist, word, num= sent_count):  # the sentence geneation function
        for i in range(num):
            print (word, end=" "),
            word = cfdist[word].max()
        print('\n')
    generate_model(cfd,random.choice(token))