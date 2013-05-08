from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from fcutils import textsFromFilenames

class Classifier(object):
        
    def __init__(self):
        self.vectorizer = CountVectorizer(charset_error="ignore")
        self.transformer = TfidfTransformer() # idf by default
        self.classifierModel = None # set by child class

        self.pipeline = None

        
    def trainClassifierFromNames(self, docNames, labels):
        """ Takes a list of document filenames and a list of labels,
        with each label an integer
        Returns a list of predicted labels"""
        self.trainClassifierFromTexts(textsFromFilenames(docNames), labels)


    def trainClassifierFromTexts(self, docTexts, labels):
        """ Takes a list of document texts and a list of labels,
        with each label an integer
        Returns a list of predicted labels"""
        self.pipeline = Pipeline([('vect', self.vectorizer),
                                  ('trans', self.transformer),
                                  ('clf', self.classifierModel)])
        self.pipeline.fit(docTexts, labels)
                
    def predictFromNames(self, docNames):
        """ After being trained, takes a list of document filenames
        and returns the list of predicted labels """
        return self.predictFromTexts(textsFromFilenames(docNames))

    def predictFromTexts(self, docTexts):
        """ After being trained, takes a list of document texts
        and returns the list of predicted labels """
        return self.pipeline.predict(docTexts)
            
    def calculate_score(self, docText):
        """ Takes a single document text and returns its predicted label """
        predicted = self.pipeline.predict([docText])
        return predicted[0]
