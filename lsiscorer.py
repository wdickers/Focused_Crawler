from gensim import corpora, models, similarities
from scorer import Scorer
from fcutils import tokenizeDocText

class LSIScorer(Scorer):
 
    def __init__(self, docTexts, numberTopics=20):
        super(LSIScorer, self).__init__(docTexts)
        self.numTopics = numberTopics

    def constructModel(self, docTexts):
        """ Given document texts, constructs the tf-idf and similarity models"""
        #construct list of document token lists
        docs = []
        for docText in docTexts :
            docs.append(tokenizeDocText(docText))

        #construct the corpus
        self.dictionary = corpora.Dictionary(docs)
        self.keywords = dictionary.values()
        corpus = [self.dictionary.doc2bow(doc) for doc in docs]

        # construct the tf-idf model
        tfidf_model = models.TfidfModel(corpus)
	corpus_tfidf = tfidf_model[corpus]
        
        # construct the lsi model
        self.model = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=self.numTopics)
        corpus_lsi = self.model[corpus_tfidf]

        # construct the similarity model
        self.similarityModel = similarities.MatrixSimilarity(self.model[corpus_lsi])


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
    scorer = LSIfScorer(documents)
    print scorer.calculateScore(doc)
    print scorer.dictionary.keys()
