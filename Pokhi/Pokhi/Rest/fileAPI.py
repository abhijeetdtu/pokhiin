from flask import Blueprint
from flask import jsonify
from flask import request, url_for
from Helpers import Helpers

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

        location = os.path.abspath(os.path.join(os.path.realpath(__file__), "../../static/Data/UploadedFiles/"))
        #location = "e:\\Books\\"
        print(location)
        fileID = Helpers.GetRandomString(10)
        print(fileID)
        print(request.files)
        if request.method == 'POST':
            # check if the post request has the file part
            file = request.files['files']
            name = file.filename
            # if user does not select file, browser also
            # submit a empty part without filename
            if name == '':
                return  jsonify({'success' : str(False) , 'msg':"no file selected"})
            if file and allowed_file(name):
                filename = secure_filename(name)
                file.save(os.path.join(location ,name))
                return jsonify({'success' : str(True) , 'msg':"Successfully uploaded"})
    except Exception as e:
        print("exception" , e)
        return jsonify({'success' : str(False) , 'msg':e})
        
    