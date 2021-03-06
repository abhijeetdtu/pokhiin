import os

class Config:

    ENV = {}
    ENV["DATA_DIR"] = os.path.abspath(os.path.join(os.path.realpath(__file__), "../../static/Data/"))
    print(ENV["DATA_DIR"])
    if('OPENSHIFT_DATA_DIR' in os.environ):
        ENV["DATA_DIR"] =  os.environ['OPENSHIFT_DATA_DIR']

    ENV["UPLOAD_FOLDER"] = os.path.abspath(os.path.join( ENV["DATA_DIR"], "UploadedFiles/"))
    print(ENV["DATA_DIR"])
    print(ENV["UPLOAD_FOLDER"])

    ENV["OPEN_CV_HOME"] = "C:\\Users\\Abhijeet\\Downloads\\OpenCv\\opencv\\sources\\data"

    if(os.path.exists(ENV["UPLOAD_FOLDER"]) == False):
        os.mkdir(ENV["UPLOAD_FOLDER"])