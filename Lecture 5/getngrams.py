# Tyler Bryk

import nltk,re
from nltk.tokenize import sent_tokenize
from nltk import load

def process(text1 , text2):

    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)

    txt1 = text1.lower().strip()
    txt2 = text2.lower().strip()
    
    sentences1 = sent_tokenize(txt1)
    sentences2 = sent_tokenize(txt2)

    nnAfterAdj1 = []
    nnAfterAdj2 = []
    
    for sentence in sentences1:
        terms = nltk.word_tokenize(sentence)    # Tokenize the sentence
        tagged_terms = tagger.tag(terms)        # Do POS tagging on the tokenized sentence
        for i in range(len(tagged_terms)-1):    # For every tagged term
            term1a = tagged_terms[i]
            term2a = tagged_terms[i+1]
            if re.match('JJ',term1a[1]) and re.match('NN',term2a[1]):
                nnAfterAdj1.append((term1a[0],term2a[0]))
                
    for sentence in sentences2:
        terms = nltk.word_tokenize(sentence)    # Tokenize the sentence
        tagged_terms = tagger.tag(terms)        # Do POS tagging on the tokenized sentence
        for i in range(len(tagged_terms)-1):    # For every tagged term
            term1b = tagged_terms[i]
            term2b = tagged_terms[i+1]
            if re.match('JJ',term1b[1]) and re.match('NN',term2b[1]):
                nnAfterAdj2.append((term1b[0],term2b[0]))
                
    finalList = 0    
    if len(nnAfterAdj1) < len(nnAfterAdj2): 
        small = nnAfterAdj1
        lrg = nnAfterAdj2
    else: 
        small = nnAfterAdj2
        lrg = nnAfterAdj1
    
    for i in range(len(small)):
        if small[i] in lrg:
            finalList = finalList + 1
    
    return finalList


if __name__ == '__main__':
    print(process('String 1 (INSERT HERE)' , 'String 2 (INSERT HERE)'))