from gensim import corpora, models, similarities
from scorer import Scorer
from fcutils import tokenizeDocText

class TfidfScorer(Scorer):
 
    def __init__(self, docTexts):
        super(TfidfScorer, self).__init__(docTexts)

    def constructModel(self, docTexts):
        """ Given document texts, constructs the tf-idf and similarity models"""
        #construct list of document token lists
        print "constructing model"
        docs = []
        for docText in docTexts :
            docs.append(tokenizeDocText(docText))
        print "constructing corpus"
        #construct the corpus
        self.dictionary = corpora.Dictionary(docs)
        self.keywords = self.dictionary.values()
        corpus = [self.dictionary.doc2bow(doc) for doc in docs]

        # construct the tf-idf model
        self.model = models.TfidfModel(corpus)

        # construct the similarity model
        self.similarityModel = similarities.MatrixSimilarity(self.model[corpus])


if __name__ == "__main__":
    documents = ["Human machine interface for lab abc computer applications",
        "A survey of user opinion of computer system response time",
        "The EPS user interface management system",
        "System and human system engineering testing of EPS",
        "Relation of user perceived response time to error measurement",
        "The generation of random binary unordered trees",
        "The intersection graph of paths in trees",
        "Graph minors IV Widths of trees and well quasi ordering",
        "Graph minors A survey"]
    doc = "A human is not a machine, he is an organic"
    #doc = "Human machine interface for lab abc computer applications"
    scorer = TfidfScorer(documents)
    print scorer.calculateScore(doc)
    print scorer.dictionary.values()
