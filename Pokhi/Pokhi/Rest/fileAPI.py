from flask import Blueprint
from flask import jsonify
from flask import request, url_for
from flask.ext.login import current_user
from Helpers import Helpers
from config import Config
import dbAccess
import os

fileAPI = Blueprint('fileAPI', __name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

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
            file = request.files['files']
            name = request.form["filename"]+"_"+fileID
            tags = request.form["tags"].split(",")
            #print(file,name,tags)
            # if user does not select file, browser also
            # submit a empty part without filename
            if name == '':
                return  jsonify({'success' : str(False) , 'msg':"No file selected"})
            if file and allowed_file(file.filename):
                filename = secure_filename(name)
                file.save(os.path.join(location ,name))
                dbAccess.Files.SaveFileMetaData(request.form["filename"] , name , current_user.username , tags , location)
                return jsonify({'success' : str(True) , 'msg':"Successfully uploaded"})
    except Exception as e:
        print("exception" , e)
        return jsonify({'success' : str(False) , 'msg':e})
        
    