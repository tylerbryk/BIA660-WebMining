# Tyler Bryk
# Web Counter Assignment

import re
from nltk.corpus import stopwords
import requests

def run(url,w1,w2):
    freq = {}
    stopLex = set(stopwords.words('english'))
    success = False

    for i in range(5):
        try:
            response = requests.get(url, headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',})    
            success = True
            break
        except:
            print('Failed Attempt',i+1)
     
    if not success: return None
    
    text = response.text
    sentences = text.split('.')
	
    for sentence in sentences:
        sentence = sentence.lower().strip()
        sentence = re.sub('[^a-z]', ' ', sentence)
        words = sentence.split(' ')
        for word in words:
            if word == '' or word in stopLex: continue
            else: freq[word] = freq.get(word,0) + 1
            
    finalList = set()        
            
    for sentence in sentences:
        sentence = sentence.lower().strip()
        sentence = re.sub('[^a-z]', ' ', sentence)
        words = sentence.split(' ')
        f1 = freq.get(w1,0)
        f2 = freq.get(w2,0)
        for word in words:
            if word == '' or word in stopLex: continue
            elif f1 < freq[word] and freq[word] < f2:
                finalList.add(word)
                
    return finalList


if __name__ == '__main__':
    w1 = 'null'
    w2 = 'life'
    url = 'https://gist.githubusercontent.com/corydolphin/d2d76dae81df22a18d036244979c3c7b/raw/f3237ee708b4f685a5e5ded3514afcf0863768aa/Speech.txt'
    print(run(url, w1, w2))