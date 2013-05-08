from sklearn.naive_bayes import MultinomialNB
from classifier import Classifier

class NaiveBayesClassifier(Classifier):
        
    def __init__(self):
        super(NaiveBayesClassifier, self).__init__()
        self.classifierModel = MultinomialNB()
