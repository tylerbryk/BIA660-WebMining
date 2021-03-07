"""
Return all 2-grams of the form: <ADVERB> <ADJECTIVE>
POS tags list: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
"""

import nltk,re
from nltk.tokenize import sent_tokenize
from nltk import load

def run(fpath):

    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)

    file = open(fpath)
    text = file.read().strip()
    file.close()
    
    sentences = sent_tokenize(text)
    print('NUMBER OF SENTENCES: ' , len(sentences))

    adjAfterAdv = []
    for sentence in sentences:
        terms = nltk.word_tokenize(sentence)    # Tokenize the sentence
        tagged_terms = tagger.tag(terms)        # Do POS tagging on the tokenized sentence
        
        for i in range(len(tagged_terms)-1):    # For every tagged term
            term1 = tagged_terms[i]
            term2 = tagged_terms[i+1]
            if re.match('RB',term1[1]) and re.match('JJ',term2[1]):
                adjAfterAdv.append((term1[0],term2[0]))
    
    return adjAfterAdv


if __name__ == '__main__':
    print(run('input.txt'))