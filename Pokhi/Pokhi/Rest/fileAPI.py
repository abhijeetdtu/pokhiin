from flask import Blueprint
from flask import jsonify
from flask import request, url_for
from flask.ext.login import current_user
from Helpers import Helpers
from config import Config
from logger import Logger
from Pokhi.Pokhi.DocToHtml.docToHtml import DocToHtml
import dbAccess
import os

fileAPI = Blueprint('fileAPI', __name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'docx'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def secure_filename(filename):
    return filename


@fileAPI.route('/api/files/uploadFile' , methods=['POST'])
def UploadFile():
    try:
        location = Config.ENV["UPLOAD_FOLDER"]
        print(location)
        #location = "e:\\Books\\"
        fileID = Helpers.GetRandomString(10)
        if request.method == 'POST':
            # check if the post request has the file part
            file = request.files['file']
            fileType= "." + file.filename.rsplit('.', 1)[1].lower()
            convertToHtml = request.form["convertToHtml"] == "on"
            name = request.form["filename"] + "_" + fileID
            fullName = name + fileType
            tags = request.form["tags"].split(",")
            path = os.path.join(location ,fullName)
            #print(file,name,tags)
            # if user does not select file, browser also
            # submit a empty part without filename
            if name == '':
                return  jsonify({'success' : str(False) , 'msg':"No file selected"})
            if file and allowed_file(file.filename):
                filename = secure_filename(name)
                file.save(path)
                if(convertToHtml):
                    DocToHtml.Convert(path , name)
                dbAccess.Files.SaveFileMetaData(request.form["filename"] , name , current_user.username , tags , path , fileType , convertToHtml)
                return jsonify({'success' : str(True) , 'msg':"Successfully uploaded"})
            else:
                return jsonify({'success' : False , 'msg':"File not valid"})
    except Exception as e:
        print("exception" , e)
        return jsonify({'success' : str(False) , 'msg':e})

@fileAPI.route('/api/files/uploadedFiles' , methods=['GET'])
def UploadedFiles():
        try:
            files = dbAccess.Files.GetAllUploadedFilesForUser(current_user.username)
            return jsonify({'success' : True , 'data':files})
        except Exception as e:
            print(e)
            Logger.Log("Exception" , e)         
            return jsonify({'success' : False , 'data':[]})

@fileAPI.route("/api/files/getHTMLFileFeed" , methods=['GET'])
def GetHTMLFileFeed():
    fileName = 


@fileAPI.route('/api/files/deleteFile' , methods=['POST'])
def DeleteFile():
        try:
            id = request.json['id']
            metadata = dbAccess.Files.GetFileMetaData(id)   
            pathToFile = metadata["absPath"]
            success = dbAccess.Files.DeleteFile(pathToFile)
            if(metadata["convertToHtml"]):
                sucess = success and dbAccess.Files.DeleteFile(pathToFile.split(".")[0]+".html")
            success = success and dbAccess.Files.DeleteFileMetaData(id)
            if(success):
                return jsonify({'success' : success  , 'msg' : "File Successfully deleted"})
            else:
                return jsonify({'success' : False  , 'msg' : "Failed to delete File"})
        except Exception as e:
            print(e)
            Logger.Log("Exception" , e)
            return jsonify({'success' : False  , 'msg' : "Failed to delete File"})



    