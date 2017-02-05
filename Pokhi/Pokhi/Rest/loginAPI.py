from flask import Blueprint
from flask import jsonify
from flask import request, url_for
from flask.ext.login import login_user, login_required ,logout_user

from Helpers import Helpers
from dbConnect import mongo , login_manager
from authAPI import AuthHelpers , User


loginAPI = Blueprint('loginAPI', __name__)


def GetUserForFlaskLoadManager(username , isAuthenticated = False , isActive = True , isAnonymous = False ):
    user = User(username , isAuthenticated, isActive , isAnonymous)
    print("GetUserForFlask" , user)
    return user
    

def GetUserFromCredentials(username , password):
    user = {}
    user["username"] = username
    user["password"] = AuthHelpers.getEncryptedPassword(password)
    return user


@login_manager.user_loader
def load_user(user_id):
    print("load_user" , user_id)
    return GetUserForFlaskLoadManager(user_id , True)

@loginAPI.route('/api/users/login' , methods=['POST'])
def Login():
    print("try login" , request.json)
    try:
        username = request.json['username']
        password =  request.json['password']
        print(username , password)
        authenticated = Authenticate(username,password)
        if(authenticated == True):
            success = login_user(GetUserForFlaskLoadManager(username , authenticated))
        else:
            success = False
    except Exception as e:
        print(e)
    return jsonify({'success' : success})

@loginAPI.route("/api/users/logout")
@login_required
def logout():
    try:
        logout_user()
    except Exception as e:
        print(e)
        return jsonify({"result" , False})

    return jsonify({"result" , True})


@loginAPI.route('/api/users/register' , methods=['POST'])
def Register():
    print("try login" , request.json)
    msg = ""
    try:
        username = request.json['username']
        password =  request.json['password']
        print(username , password ,mongo.db.pokhiusers)
        success = False
        if(_UserExists(username) == False):
            success = mongo.db.pokhiusers.insert(GetUserFromCredentials(username, password))
        else:
            msg = "User already exists . Try a different username"
    except Exception as e:
        print(e)
    return jsonify({'success' : success})

@loginAPI.route('/api/users/getall' , methods=['GET'])
def Users():
    return jsonify({"results" : Helpers.CollectionToArray(mongo.db.pokhiusers.find()) })

@loginAPI.route('/api/users/userexists/<path:path>' , methods=['GET'])
def UserExists(path):
    return jsonify({"result" : _UserExists(path)})   

def _UserExists(username):
    print("Checking existing")
    try:
        print(mongo.db.pokhiusers.find({'username' : username}).count() > 0)
        return mongo.db.pokhiusers.find({'username' : username}).count() > 0
    except Exception as e:
        print(e)
    return True

def Authenticate(username ,password):
    user = mongo.db.pokhiusers.find_one({'username' : username})
    print("Authenticate", user)
    if(user != None):
        return AuthHelpers.checkPassword(password , user['password'])
    return False
