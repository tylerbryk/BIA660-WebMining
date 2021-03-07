"""
Line Frequency Function
Returns the frequency of <word1> and <word2> appearing in a line in the file specified by <path>.
"""

def run(path,word1,word2):
    
    freq = {} # Hash Map
    freq[word1] = 0
    freq[word2] = 0

    file = open(path)
    for line in file:
        words = line.lower().strip().split(' ')
        
        f1 = False
        f2 = False

        for word in words:
            if word == word1 and not f1: 
                freq[word1] += 1
                f1 = True
            elif word == word2 and not f2: 
                freq[word2] += 1
                f2 = True
                
    file.close()
    return freq[word1],freq[word2]


print(run('textfile','blue','yellow'))
print(run('textfile','name','kate'))