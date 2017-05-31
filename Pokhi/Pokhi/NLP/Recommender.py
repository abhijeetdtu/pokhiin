from sklearn.feature_extraction.text import TfidfVectorizer , CountVectorizer
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering , DBSCAN , AffinityPropagation
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import fetch_20newsgroups

from Pokhi.Pokhi.RawDBAccess.RawDBAccess import RawDBAccess

import pickle


class Recommender:
    
    def __init__(self , load=False):
        self.Vectorizer = TfidfVectorizer()#CountVectorizer(analyzer='char_wb', ngram_range=(5, 5), min_df=1)
        self.collection = RawDBAccess.GetMongoDB()["wikipediaFeed"]
        self.model = None

        if load == True:
            self.model = pickle.load(open("model", "r"))
            self.Vectorizer = pickle.load(open("vectorizer" , "r"))

    def GetFeatureVectors(text):
        textList = text.split()
        return  Recommender.Vectorizer.fit_transform(text)

    def TrainModel(self , content = True , newsGroup= False):
        if newsGroup :
            self._TrainNewsGroups()
        elif content:
            self._TrainContent()
        else:
            self._TrainKeywords()

    def _TrainContent(self):
        print("Starting training...")
        allContent =  [ x["content"] for x in self.collection.find() if 'content' in x]
        self._Train(allContent)

    def _TrainKeywords(self):
        print("Starting training...")
        allKeywords =  [ map(lambda y : y[0] , x["keywords"]) for x in self.collection.find() if 'keywords' in x]
        allContent = [" ".join(keywords) for keywords in allKeywords]
        self._Train(allContent)
        

    def _Train(self, allContent):
        print("Starting Vectorization...")
        features = self.Vectorizer.fit_transform(allContent).toarray()

        print("Starting Clustering...")
        #model = KMeans(n_clusters=10, random_state=0).fit(features)
        model = AgglomerativeClustering(n_clusters = 10 , linkage ='ward', affinity='euclidean')
        #model = AffinityPropagation()
        model.fit(features)

        print("Dumping model...")
        #pickle.dump(model , open("model" , "w"))
        #pickle.dump(self.Vectorizer , open("vectorizer" , "w"))

        print("Labels...")
        outfile = open("results.txt" , "w")
        sort = sorted([(allContent[i] , label) for i,label in enumerate(model.labels_)] , key=lambda x:x[1])
        for content , label in sort:
            outfile.write(content[:200].encode("utf-8") + " ::: " + str(label) + "\n\n")
        
    def _TrainNewsGroups(self):
        categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med' , 'talk.politics.misc' , 'rec.sport.baseball']

        print("Fetch Data...")
        twenty_train = fetch_20newsgroups(subset='train',categories=categories, shuffle=True, random_state=42)
        vectorizer =TfidfVectorizer()

        print("Starting Vectorization...")
        features = vectorizer.fit_transform(twenty_train.data)
        print(features)

        print("Starting Classifying...")
        clf = MultinomialNB().fit(features, twenty_train.target)


        print("Predicting...")
        allDocs = [x["content"] for x in self.collection.find().limit(100) if 'content' in x]
        features = vectorizer.transform(allDocs)
        
        predicted = clf.predict(features)

        print("Out file...")
        outfile = open("results.txt" , "w")
        sort = sorted([(allDocs[i] , twenty_train.target_names[label]) for i,label in enumerate(predicted)] , key=lambda x:x[1])

        for content , label in sort:
            outfile.write(content[:200].encode("utf-8") + " ::: " + str(label) + "\n\n")
        

    def PredictCluster(self,doc):
        feature =  self.Vectorizer.transform(doc["content"])
        label = self.model.Predict(feature)
        print(label)
        return label


    def TestModel(self):
        print("Loading content from DB....")
        dicMap = {}
        allDocs = [(x["content"] , x["keywords"]) for x in self.collection.find().limit(50) if 'content' in x and 'keywords' in x]
        for x in allDocs:
            dicMap[ " ".join(map(lambda y: y[0] , x[1])) ] = x[0]

        allKeywords =  [  " ".join(map(lambda y : y[0] , x["keywords"])) for x in self.collection.find().limit(50) if 'keywords' in x]

        print("Extracting features....")
        features = self.Vectorizer.transform(allKeywords).toarray()
        
        

        print("Predicting....")
        labels = self.model.predict(features)

        print("Finalizing....")
        sortedList = sorted([(dicMap[ allKeywords[i] ] , labels[i]) for (i,x) in enumerate(labels)] , key = lambda x : x[1])

        #print(labels , sortedList)
        print("Writing to file....")
        outfile = open("results.txt" , "w")
        for sorteddata in sortedList:
            print(sorteddata)
            outfile.write(sorteddata[0][:200].encode("utf-8") + " ::: " + str(sorteddata[1]) + "\n\n")



        

