import re
from nltk.corpus import stopwords
import networkx as nx
from nltk.tokenize import sent_tokenize
from networkx.algorithms import community

sw = set(stopwords.words('english'))
G = nx.Graph()
c = 0
file = open('article.txt')
text = file.read()
file.close()

sentences = sent_tokenize(text)
for sentence in sentences:
    sentence = re.sub('[^a-z]', ' ', sentence.lower()).strip()
    terms = sentence.split()
    for i in range(len(terms)):
        if terms[i] in sw or len(terms[i]) < 3: continue
        for j in range(i+1, len(terms)):
            if terms[j] in sw or len(terms[j]) < 3: continue
            if not G.has_edge(terms[i],terms[j]):
                G.add_edge(terms[i],terms[j]) 
                G[terms[i]][terms[j]]['freq'] = 1
            else:
                G[terms[i]][terms[j]]['freq'] += 1
            
remove = []
for N1, N2 in G.edges():
    if G[N1][N2]['freq'] < 3: remove.append((N1,N2))
G.remove_edges_from(remove)
  
cliques = list(nx.find_cliques(G))
sorted_cliques = sorted(cliques, key=len,reverse=True)
print (sorted_cliques[0])

kcliques = list(community.k_clique_communities(G,3))
sorted_cliques = sorted(kcliques, key=len,reverse=True)
print (sorted_cliques[0])