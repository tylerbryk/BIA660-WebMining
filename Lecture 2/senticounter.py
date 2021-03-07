# Tyler Bryk

def loadDict(fname):
    newLex = set()
    lex_conn = open(fname)
    for line in lex_conn:
        newLex.add(line.strip())
    lex_conn.close()
    return newLex

def run(path):
    freq = {}
    negLex = loadDict('negative-words.txt')
    
    file = open(path)
    for line in file:        
        line = line.lower().strip()   
        words = line.split(' ')
   
        for word in words:
            if word in negLex:
                if word in freq.keys():
                    if word == words[-1]:
                        freq[word] += 1
                else:
                    freq[word] = 0;
                    if word == words[-1]:
                        freq[word] += 1
                    
            
    file.close()
    return freq

if __name__ == "__main__": 
    freq = run('textfile')
    for i in range(len(freq)):
        print(freq)