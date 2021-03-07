# ===================================================
#
#    BIA660 Web Mining Final Porject
#    By: Tyler Bryk & Kristina Cheng
#
# ===================================================

import re
import pandas as pd
from pandas import DataFrame
from nltk.corpus import stopwords
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import CountVectorizer

def loadData(fname):
    reviews = []
    file = open(fname)
    for line in file:
        review = line.strip()  
        reviews.append(review.lower())    
    file.close()
    return reviews

def exportData(data, fname):
    file = open(fname, "w")
    for line in data:
        file.write(str(line) + '\n')
    file.close()


# Timer Stuff =================================
from datetime import datetime
startTime = datetime.now()
# =============================================

# Load Training Data
df = pd.read_csv("TrainingData.csv", header = None, encoding='latin-1')
df.columns = ['review' , 'rating']


# Load Testing Data ===========================================================
teDf = loadData("TestData.txt")     # <--------- PUT TEST DATA FILE NAME HERE
# =============================================================================


# Clean and Pre-Process Data
stop = stopwords.words('english')
teDf = DataFrame(teDf, columns = ['review'])
df['review'] = df['review'].apply(lambda x: re.sub('[^a-zA-z0-9\s]' , '' , x))
df['review'] = df['review'].apply(lambda x: ' '.join([item for item in x.split() if item not in stop]))
teDf['review'] = teDf['review'].apply(lambda x: re.sub('[^a-zA-z0-9\s]' , '' , x))
teDf['review'] = teDf['review'].apply(lambda x: ' '.join([item for item in x.split() if item not in stop]))
trData  = df['review']
trLabel = df['rating']
teData = teDf['review']


# Transform Data and Fit Neural Network
counter = CountVectorizer()
counter.fit(trData)
trCount = counter.transform(trData)
teCount = counter.transform(teData)
clf = MLPClassifier(hidden_layer_sizes=(10, ), activation='logistic', solver='adam', alpha=0.0001, batch_size='auto', learning_rate='constant', learning_rate_init=0.005, power_t=0.5, max_iter=200, shuffle=False, random_state=8, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True, early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08, n_iter_no_change=10)





# Code used to Tune Model Hyperparameters
def loadDataCust(fname):
    labels = []
    file = open(fname)
    for line in file:
        rating = line.strip()   
        labels.append(int(rating))
    file.close()
    return labels
from sklearn.model_selection import GridSearchCV
teLabel = loadDataCust('TestData-TrueLabels.txt')
print("[INFO] Tuning Hyperparameters via GridSearchCV")
params = {"alpha": [0.00006, 0.0001, 0.0006], "learning_rate_init": [0.003, 0.005, 0.007], 'beta_1': [0.85, 0.9, 0.95], 'beta_2':[0.995, 0.997, 0.999] }
grid = GridSearchCV(clf, params)
grid.fit(trCount, trLabel)
acc = grid.score(teCount, teLabel)
print("[INFO] grid search accuracy: {:.2f}%".format(acc * 100))
print("[INFO] grid search best parameters: {}".format(grid.best_params_))







# Fit Model and Make Predictions
#clf.fit(trCount, trLabel)
#pred = clf.predict(teCount)
# =============================================================================
#exportData(pred, "OUTPUT-LabeledTestData.txt") # <--------- PUT TEST DATA OUTPUT FILE NAME HERE
# =============================================================================

# ================================
print(datetime.now() - startTime)