def loadDict(fname):
    newLex = set()
    lex_conn = open(fname)
    for line in lex_conn:
        newLex.add(line.strip())
    lex_conn.close()
    return newLex

def run(path):
    decisions = [] 
    reviews = []
    posLex = loadDict('positive-words.txt')
    negLex = loadDict('negative-words.txt')
    
    file = open(path)
    for line in file:
        posList = []
        negList = []
        
        line = line.lower().strip()   
        reviews.append(line)
        words = line.split(' ')
   
        for word in words:
            if word in posLex:
                posList.append(word)
            if word in negLex:
                negList.append(word)

        decision = 0 
        if len(posList) > len(negList):
            decision = 1
        elif len(negList) > len(posList):
            decision = -1
        decisions.append(decision)
            
    file.close()
    return reviews, decisions 

if __name__ == "__main__": 
    reviews,decisions = run('textfile')
    for i in range(len(reviews)):
        print(reviews[i], decisions[i])