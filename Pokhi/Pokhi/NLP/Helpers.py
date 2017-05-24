from __future__ import absolute_import
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import AgglomerativeClustering

import RAKE
import re 

class Helpers:

    @staticmethod
    def ExtractKeywords(data,k=10):
        data = re.sub(r"[\r\n=]" , " ", data)
        Rake = RAKE.Rake("Pokhi\Pokhi\NLP\StopWordList.txt");
        extract = Rake.run(data)
        keypoints = [x for x in extract if len(x[0].split(" ")) > 4][:k]
        keywords = [x for x in extract if len(x[0].split(" ")) <= 3][:k]
        return [keywords , keypoints];
        
        #data = [x.strip("\r\n") for x in data.split(".")]
        #vectorizer = TfidfVectorizer(stop_words='english' , decode_error="replace")
        #X = vectorizer.fit_transform(data)
        #C = 1 - cosine_similarity(X.T)
        #ward = AgglomerativeClustering(n_clusters=k, linkage='ward').fit(C)
        #return vectorizer.inverse_transform(ward.labels_)