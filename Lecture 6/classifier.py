import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from sklearn.neural_network import MLPClassifier
#from sklearn.model_selection import GridSearchCV

def loadData(fname):
    reviews = []
    labels = []
    stop_words = set(stopwords.words('english')) 
    f = open(fname)
    for line in f:
        review,rating = line.strip().split('\t')
        word_tokens = word_tokenize(review)   
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence2 = []
        for w in word_tokens: 
            if w not in stop_words: 
                filtered_sentence.append(w)
        for w in filtered_sentence: 
            if w not in string.punctuation: 
                filtered_sentence2.append(w)
        stopremoved = ' '.join([str(elem) for elem in filtered_sentence2])
        reviews.append(stopremoved)    
        labels.append(int(rating))
    f.close()
    return reviews,labels

rev_train,labels_train = loadData('reviews_train.txt')
rev_test,labels_test = loadData('reviews_test.txt')

counter = CountVectorizer()
counter.fit(rev_train)
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data
clf = MLPClassifier(hidden_layer_sizes=(1000, ), activation='logistic', solver='adam', alpha=0.0001, batch_size='auto', learning_rate='constant', learning_rate_init=0.005, power_t=0.5, max_iter=200, shuffle=False, random_state=8, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True, early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08, n_iter_no_change=10 )

# Code used to Tune Model Hyperparameters
#print("[INFO] Tuning Hyperparameters via GridSearchCV")
#params = {"alpha": [0.00006, 0.0001, 0.0006], "learning_rate_init": [0.003, 0.004, 0.005, 0.006, 0.007], 'beta_1': [0.85, 0.9, 0.95], 'beta_2':[0.995, 0.997, 0.999] }
#grid = GridSearchCV(clf, params)
#grid.fit(counts_train, labels_train)
#acc = grid.score(counts_test, labels_test)
#print("[INFO] grid search accuracy: {:.2f}%".format(acc * 100))
#print("[INFO] grid search best parameters: {}".format(grid.best_params_))

clf.fit(counts_train,labels_train)
pred = clf.predict(counts_test)
print(accuracy_score(pred,labels_test))