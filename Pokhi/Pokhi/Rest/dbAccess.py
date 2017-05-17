from __future__ import absolute_import

from Pokhi.Pokhi.Rest.dbConnect import mongo
from Pokhi.Pokhi.Rest.logger import Logger

from bson.json_util import dumps
from bson.objectid import ObjectId

import os

def GetDataItemWithId(mongoItem):
    mongoItem["_id"] = str(mongoItem["_id"])
    return mongoItem

#files
class Files:

    @staticmethod
    def DeleteFile(absPath):
        try:
            os.remove(absPath)
            return True
        except Exception as e:
            Logger.Log("Exception" , e)
            return False

    @staticmethod
    def GetFileMetaData(id):
        try:
            data = mongo.db.uploadedFiles.find_one({"_id" : ObjectId(id)})
            return data
        except Exception as e:
            print(e)
            Logger.Log("Exception" , e)
            return None

    @staticmethod
    def SaveFileMetaData(userGivenFileName ,systemGeneratedFileName, creator , tags , absPath , fileType , convertToHtml):
        try:
            success = mongo.db.uploadedFiles.insert({"userGivenFileName" : userGivenFileName 
                                                     , "systemGeneratedFileName":systemGeneratedFileName 
                                                     , "creator" : creator 
                                                     , "tags":tags 
                                                     , "absPath":absPath
                                                     , "fileType":fileType
                                                     , "convertToHtml" : convertToHtml
                                                     })
            return success
        except Exception as e:
            Logger.Log("Exception" , e)
            return False

    @staticmethod
    def DeleteFileMetaData(id):
        try:
            success = mongo.db.uploadedFiles.delete_one({"_id" : ObjectId(id)})
            return success.deleted_count > 0
        except Exception as e:
            print(e)
            Logger.Log("Exception DeleteFileMetaData" , e)
            return False

    @staticmethod
    def GetAllUploadedFilesForUser(username):
        try:
            files = mongo.db.uploadedFiles.find({"creator" : username})
            results = [{"name" : f["userGivenFileName"] , "tags" : f["tags"] , "id": str(f["_id"])} for f in files]
            return results
        except Exception as e:
            Logger.Log("Exception" , e)
            print(e)
            return []


class PlotLy:

    @staticmethod
    def GetAllPlotLyGraphs():
        try:
            return [ {"name" : x["name"] , "url" : x["url"] , "_id" : str(x["_id"])} for x in mongo.db.plotly.find({}) ]
        except Exception as e:
            Logger.Log("DBAccess:Error" , "Failed to Get PlotLy")
            return []

class WikipediaFeed:

    @staticmethod
    def AddPageToDB(page):
        try:
            mongo.db.wikipediaFeed.insert(page)
        except Exception as e:
            print(e)
            Logger.Log("DBAccess:Error - WikipediaFeed.AddPageToDB" , "Failed to insert page")
            
    @staticmethod
    def GetPages(lastId):
        try:
            if(lastId == 0):
                pages = mongo.db.wikipediaFeed.find().limit(WikipediaFeed.PageSize)
                return [GetDataItemWithId(p) for p in pages]
            else:
                pages = mongo.db.wikipediaFeed.find({"_id" : {"$gt" :   ObjectId(lastId) }}).limit(WikipediaFeed.PageSize)
                return [GetDataItemWithId(p) for p in pages]
        except Exception as e:
            print(e)
            Logger.Log("DBAccess:Error - WikipediaFeed.GetPages" , "Failed to insert page")

WikipediaFeed.PageSize = 10
