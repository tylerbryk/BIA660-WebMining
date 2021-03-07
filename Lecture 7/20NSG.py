from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.datasets import fetch_20newsgroups

def labelData(data, label):
    reviews = []
    labels = []
    for file in data:
        reviews.append(file.strip().lower())    
        labels.append(label)
    return reviews, labels

# Prepare TRAINING Data
trainComp = fetch_20newsgroups(remove=('headers', 'footers'), categories=['comp.os.ms-windows.misc'])
trainSpor = fetch_20newsgroups(remove=('headers', 'footers'), categories=['rec.sport.hockey'])
trainRec  = fetch_20newsgroups(remove=('headers', 'footers'), categories=['rec.motorcycles'])
trainPoli = fetch_20newsgroups(remove=('headers', 'footers'), categories=['talk.politics.mideast', 'talk.politics.guns'])
trainData1, trainLabel1 = labelData(trainComp, 'comp')
trainData2, trainLabel2 = labelData(trainSpor, 'sports')
trainData3, trainLabel3 = labelData(trainRec , 'rec')
trainData4, trainLabel4 = labelData(trainPoli, 'politics')
trainData = trainData1 + trainData2 + trainData3 + trainData4
trainLabels = trainLabel1 + trainLabel2 + trainLabel3 + trainLabel4

# Prepare TEST Data
testComp = fetch_20newsgroups(remove=('headers', 'footers'), categories=['comp.windows.x'])
testSpor = fetch_20newsgroups(remove=('headers', 'footers'), categories=['rec.sport.baseball'])
testRec  = fetch_20newsgroups(remove=('headers', 'footers'), categories=['rec.autos'])
testPoli = fetch_20newsgroups(remove=('headers', 'footers'), categories=['talk.politics.misc'])
testData1, testLabel1 = labelData(testComp, 'comp')
testData2, testLabel2 = labelData(testSpor, 'sports')
testData3, testLabel3 = labelData(testRec , 'rec')
testData4, testLabel4 = labelData(testPoli, 'politics')
testData = testData1 + testData2 + testData3 + testData4
testLabels = testLabel1 + testLabel2 + testLabel3 + testLabel4


counter = CountVectorizer()
counter.fit(trainData)
counts_train = counter.transform(trainData)
counts_test  = counter.transform(testData)

clf = MultinomialNB()

clf.fit(counts_train, trainLabels)
pred = clf.predict(counts_test)
print (accuracy_score(pred, testLabels))