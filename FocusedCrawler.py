#!/usr/local/bin/python
import numpy as np

from fcconfig import FCConfig
from fcutils import linesFromFile, getUrlTexts, intLinesFromFile
from tfidfscorer import TfidfScorer
from lsiscorer import LSIScorer
from SVMClassifier import SVMClassifier
from NBClassifier import NaiveBayesClassifier
from priorityQueue import PriorityQueue


def main():
    conf = FCConfig("config.ini")

    seedUrls = linesFromFile(conf["seedFile"])
    repositoryDocNames = linesFromFile(conf["docsFile"])

    if conf["labelFile"]:
        print "Using labels"
        labels = intLinesFromFile(conf["labelFile"])
        relevantDocs = [doc for doc,lab in zip(repositoryDocNames, labels) if lab==1]
        irrelevantDocs = [doc for doc,lab in zip(repositoryDocNames, labels) if lab==0]     
    else:
        # use VSM model to label training docs
        vsmModel = None
        if conf["VSMFilterModel"].lower() == "tf-idf":
            vsmModel = TfidfScorer(getUrlTexts(seedUrls))
        elif conf["VSMFilterModel"].lower() == "lsi":
            vsmModel = LSIScorer(getUrlTexts(seedUrls))
        print "constructed vsm model"
    
        relevantDocs , irrelevantDocs = vsmModel.labelDocs(
            repositoryDocNames, conf["minRepositoryDocNum"],
            conf["filterIrrelevantThreshold"],
            conf["filterRelevantThreshold"])
        
    print len(relevantDocs), len(irrelevantDocs)
    
    
    
    # Train classifier
    classifier = None
    testSize = min(len(relevantDocs), len(irrelevantDocs))
    trainSize = conf["trainDocNum"]
    if (trainSize > testSize):
        raise Exception("Training size is larger than test size")
    trainDocs = relevantDocs[:trainSize] + irrelevantDocs[:trainSize]
    trainLabels = [1]*trainSize + [0]*trainSize
    if conf["classifier"].upper() == "NB":
        classifier = NaiveBayesClassifier()
    elif conf["classifier"].upper() == "SVM":
        classifier = SVMClassifier()
    classifier.trainClassifierFromNames(trainDocs, trainLabels)

    print "Training complete"
    
    # Test classifier
    testSize = min(len(relevantDocs), len(irrelevantDocs))
    testDocs = relevantDocs[:testSize] + irrelevantDocs[:testSize]
    testLabels = [1]*testSize + [0]*testSize
    predictedLabels = list(classifier.predictFromNames(testDocs))

    # Statistical analysis (recall and precision)
    allRelevant = testSize
    allIrrelevant = testSize
    predictedRelevant = predictedLabels.count(1)
    predictedIrrelevant = predictedLabels.count(0)
    correctlyRelevant = 0
    for i in range(0, testSize):
        if predictedLabels[i] == 1:
            correctlyRelevant += 1
    correctlyIrrelevant = 0
    for i in range(testSize, 2*testSize):
        if predictedLabels[i] == 0:
            correctlyIrrelevant += 1
    relevantRecall = float(correctlyRelevant) / allRelevant
    relevantPrecision = float(correctlyRelevant) / (predictedRelevant)
    irrelevantRecall = float(correctlyIrrelevant) / allIrrelevant
    irrelevantPrecision = float(correctlyIrrelevant) / (predictedIrrelevant)
    print relevantRecall, relevantPrecision


    [(-1,p) for p in seedUrls]
    priorityQueue = PriorityQueue(t)
    crawler = Crawler(priorityQueue,classifier,10)
    crawler.crawl()
    print crawler.relevantPagesCount

    print crawler.pagesCount


if __name__ == "__main__":
    x = main()
