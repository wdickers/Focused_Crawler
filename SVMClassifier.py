from sklearn import svm
from classifier import Classifier

class SVMClassifier(Classifier):

    def __init__(self):
        super(SVMClassifier, self).__init__()
        self.classifierModel = svm.SVC(probability=True)
