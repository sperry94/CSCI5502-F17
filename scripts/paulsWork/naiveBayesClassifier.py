#!/opt/local/bin/python2.7 
import sys
import pdb
import nltk
import re
import random

import YelpDB

class NaiveBayes ():

    ### This class exists purely to override Process from the base
    def __init__ (self, fileName):
        self.ydb       = YelpDB.YelpDB()
        self.file      = open (fileName)
        self.reviewIDs     = []
        self.processedText = []

    ### Override the process() to accumulate a training set of the unigrams
    ### bigrams
    #
    def process (self, stars, text, business_id, user_id):
       
        ### Stake out what is positive and negative
        if stars > 3:
           score = "positive"
        else:
           score = "negative"

        ### Filter out stopwords
        stopwords = nltk.corpus.stopwords.words("english")
        np = r"(\w)"
        
        filteredStopWords = []
        try:
            words = nltk.word_tokenize(text)
            words = [word.lower() for word in words]
            for t in  words:
                if t not in stopwords:
                    filteredStopWords.append(t)

            filteredComplete = []
            for t in filteredStopWords:
                result = re.search(np, t)
                if result != None:
                    filteredComplete.append(t)
 
            thisVector = (text, filteredComplete, score)
            self.processedText.append(thisVector)

        except:
            pass
            #print "Review failed to tokenize"

    ### Loop through the reviews in reviewList pulling out the relevant data
    ### from the SQL database
    #
    def loop (self, reviewList ):
        for nextID in reviewList:
            (stars, date, text, business_id, user_id) = self.ydb.getReview (nextID)
            self.process (stars, text, business_id, user_id)

    ### Build the list of review IDs from the passed file
    def readReviewIDs (self):
        i = 0
        for nextID in self.file:
            nextID = nextID.rstrip()
            self.reviewIDs.append(nextID)
            i = i + 1

    ### I used much of the techniques for building the featureset from:
    ###    https://github.com/Katy-katy 
    ### Ekaterina Tcareva did review processing using Python and the nltk 
    ### and I used her scheme largely for building unigram and bigram featuresets.
    # 
    def buildFeatures (self, reviewText, reviewWords):

        featureVector = {}

        unigramDistribution   = nltk.FreqDist(reviewWords)
        for word, frequency in unigramDistribution.items():
            featureVector[word] = frequency

        bigrams               = list(nltk.bigrams(reviewWords))
        bigramDistribution    = nltk.FreqDist(bigrams)
        for word, frequency in bigramDistribution.items():
            featureVector[word] = frequency

        return featureVector
 
### Get the filename with the review IDs
if len(sys.argv) < 2:
    print "\nProvide training and test files as arguments\n"
    sys.exit (-1)

### Get and instance and process the file
processor = NaiveBayes (sys.argv[1])
processor.readReviewIDs()

### Randomize the reviews
random.shuffle(processor.reviewIDs)

trainingListEnd = int(len(processor.reviewIDs) * 0.67)
processor.loop(processor.reviewIDs[:trainingListEnd])

trainingFeatureSet = []
for (text, filteredWords, score) in processor.processedText:
    featureVector = processor.buildFeatures(text, filteredWords)
    trainingFeatureSet.append ((featureVector, score))

### Better clear the list of processed reviews from training
processor.processedText = []
processor.loop(processor.reviewIDs[trainingListEnd:])
testFeatureSet = []
for (text, filteredWords, score) in processor.processedText:
    featureVector = processor.buildFeatures(text, filteredWords)
    testFeatureSet.append ((featureVector, score))

classifier = nltk.NaiveBayesClassifier.train (trainingFeatureSet)

accuracy = nltk.classify.accuracy(classifier, testFeatureSet)
print "\nNaive Bayesian Classifier Accuracy of %5.3f\n" % accuracy

classifier.show_most_informative_features(100)
