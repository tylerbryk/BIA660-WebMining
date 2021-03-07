"""
Counter Function
Returns the frequency of <word1> and <word2> in the file specified by <path>.
"""

def run(path,word1,word2):
    
    freq = {} # Hash Map
    freq[word1] = 0
    freq[word2] = 0

    file = open(path)
    for line in file:
        # strip()  removes blank space from the start and end of the string
        # split(c) "A1B1C1D".split('1')" returns [A,B,C,D] 
        words = line.lower().strip().split(' ')

        for word in words:
            if word == word1: 
                freq[word1] += 1
            elif word == word2: 
                freq[word2] += 1
                
    file.close()
    return freq[word1],freq[word2]


print(run('textfile','blue','yellow'))
print(run('textfile','name','kate'))