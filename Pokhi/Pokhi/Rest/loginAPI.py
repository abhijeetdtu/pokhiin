from flask import Blueprint
from flask import jsonify
from flask import request, url_for
from flask.ext.login import login_user, login_required ,logout_user , current_user

from Helpers import Helpers
from dbConnect import mongo , login_manager
from authAPI import AuthHelpers , User
import sys, traceback

loginAPI = Blueprint('loginAPI', __name__)


def JsonifyUser(user):
    print("jsonify user" , user , type(user) ==  type(User) , type(user))
    return {'username': user.username , 'isAuthenticated':user.is_authenticated}

def GetUserForFlaskLoadManager(username , isAuthenticated =False, isActive = True , isAnonymous = False ):
    try:
        user = mongo.db.pokhiusers.find_one( { "username": username })      
        if("isLoggedIn" in user and user["isLoggedIn"] == True):
            isAuthenticated = True
        print("GetUserForFlask" , user , isAuthenticated)
        user = User(username , isAuthenticated, isActive , isAnonymous)      
        return user
    except Exception as e:
        print("Exception" , e)
        traceback.print_exc(file=sys.stdout)
        return User(username , False, isActive , isAnonymous)
    

def GetUserFromCredentials(username , password):
    user = {}
    try:
        user["username"] = username
        user["password"] = AuthHelpers.getEncryptedPassword(password)
    except Exception as e:
        print(e)
        raise Exception("error")
    return user


def _UserExists(username):
    print("Checking existing")
    try:
        print(mongo.db.pokhiusers.find({'username' : username}).count() > 0)
        return mongo.db.pokhiusers.find({'username' : username}).count() > 0
    except Exception as e:
        print(e)
    return True

def Authenticate(username ,password):
    try:
        user = mongo.db.pokhiusers.find_one({'username' : username})
        print("Authenticate", user)
        if(user != None):
            return AuthHelpers.checkPassword(password , user['password'])
    except Exception as e:
        print("Authenticate" , e)
    return False

@login_manager.user_loader
def load_user(user_id):
    print("load_user" , user_id)
    try:
        return GetUserForFlaskLoadManager(user_id)
    except Exception as e:
        print("Exception" ,e)
        traceback.print_exc(file=sys.stdout)


@loginAPI.route('/api/users/getcurrentuser' , methods=['GET'])
def GetCurrentUser():
    try:
        print(JsonifyUser(current_user))
        return jsonify({'success' : 'true' , 'data' : JsonifyUser(current_user)})
    except Exception as e:
        print(e)
        return jsonify({'success' : 'false'})

@loginAPI.route('/api/users/login' , methods=['POST'])
def Login():
    print("try login" , request.json)
    try:
        username = request.json['username']
        password =  request.json['password']
        print(username , password)
        authenticated = Authenticate(username,password)
        print("authenticated" , authenticated)
        if(authenticated == True):
            success = login_user(GetUserForFlaskLoadManager(username , authenticated))
            mongo.db.pokhiusers.update( { "username": username }  , { '$set' : { "isLoggedIn" : True } })
        else:
            success = False
    except Exception as e:
        print(e)
    return jsonify({'success' : success})

@loginAPI.route("/api/users/logout" , methods=['GET'])
def logout():
    try:
        username = current_user.username
        logout_user()
        mongo.db.pokhiusers.update( { "username": username }  , { '$set' : { "isLoggedIn" : False } })
    except Exception as e:
        print(e)
        return jsonify({"success" : False})

    return jsonify({"success" : True})


@loginAPI.route('/api/users/register' , methods=['POST'])
def Register():
    print("try login" , request.json)
    msg = "registerd"
    try:
        username = request.json['username']
        password =  request.json['password']
        print(username , password ,mongo.db.pokhiusers)
        success = False
        if(_UserExists(username) == False):
            success = mongo.db.pokhiusers.insert(GetUserFromCredentials(username, password))
        else:
            msg = "User already exists . Try a different username"

        print("Registered" , str(success))
    except Exception as e:
        print(e)
    return jsonify({'success' : str(success) , 'msg':msg})

@loginAPI.route('/api/users/getall' , methods=['GET'])
def Users():
    return jsonify({"results" : Helpers.CollectionToArray(mongo.db.pokhiusers.find()) })

@loginAPI.route('/api/users/userexists/<path:path>' , methods=['GET'])
def UserExists(path):
    return jsonify({"result" : _UserExists(path)})   
