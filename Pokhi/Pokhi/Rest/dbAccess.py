from dbConnect import mongo


#files
class Files:

    @staticmethod
    def SaveFileMetaData(userGivenFileName ,systemGeneratedFileName, creator , tags , absPath):
        try:
            success = mongo.db.uploadedFiles.insert({"userGivenFileName" : userGivenFileName , "systemGeneratedFileName":systemGeneratedFileName , "creator" : creator , "tags":tags , "absPath":absPath})
            return success
        except Exception as e:
            print(e)
            return False
