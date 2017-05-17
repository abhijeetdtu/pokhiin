from __future__ import absolute_import
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import AgglomerativeClustering

class Helpers:

    @staticmethod
    def ExtractKeywords(data,k):
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(data)
        C = 1 - cosine_similarity(X.T)
        ward = AgglomerativeClustering(n_clusters=k, linkage='ward').fit(C)
        return ward.labels_