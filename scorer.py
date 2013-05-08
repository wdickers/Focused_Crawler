import nltk
import codecs
from fcutils import tokenizeDocText

class Scorer(object):
    """ Base class for VSM scorers """
 
    def __init__(self, docTexts):
        self.keywords = []
        self.dictionary = None;
        self.model = None;
        self.similarityModel = None
        self.constructModel(docTexts)

    def constructModel(self, docTexts):
        """ Given document texts, constructs the VSM and similarity models"""
        return

    
    def calculate_score(self,docText):
        """ Given document text, returns relevancy score.
        Document text is tokenized, transformed into vector space,
        and then the maximum dot-product is returned"""

        docTokens = tokenizeDocText(docText)
        
        # transform document into model's vector space
        doc_bow = self.dictionary.doc2bow(docTokens)
        vec = self.model[doc_bow]

        # return maximum similarity (dot products)
        simList = self.similarityModel[vec]
        return max(simList)


    def labelDocs(self, docNames, minSize, irrelThresh, relThresh):
        """ Labels a list of documents as relevant (score >= relThresh) or non-relevant (score <= irrelThresh). """
        
        relevantDocNames = []
        irrelevantDocNames = []
        for docName in docNames:
            f = codecs.open(docName, "r")
            text = f.read()
            f.close()
            score = self.calculateScore(text)
            if score <= irrelThresh:
                irrelevantDocNames.append(docName)
            elif score >= relThresh:
                relevantDocNames.append(docName)
        if len(relevantDocNames) < minSize:
            raise Exception("Not enough relevant documents")
        if len(irrelevantDocNames) < minSize:
            raise Exception("Not enough irrelevant documents")
        return relevantDocNames, irrelevantDocNames
