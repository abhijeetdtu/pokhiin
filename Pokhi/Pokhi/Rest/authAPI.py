from flask import Blueprint
from flask import jsonify
from flask import request, url_for
from flask.ext.login import login_user

from sha256 import sha256

from Helpers import Helpers
from dbConnect import mongo , login_manager

class User:

    def __init__(self ,username, isAuthenticated , isActive , isAnonymous):
        self.is_authenticated = isAuthenticated
        self.is_active = isActive
        self.is_anonymous = isAnonymous
        self.username = username

    def get_id(self):
        return self.username

class AuthHelpers:

    @staticmethod
    def getEncryptedPassword(raw_password):
        print("Getting hashed password")
        try:
            password = raw_password.encode("utf-16")
            print(password , sha256(password).hexdigest())
            return sha256(password).hexdigest()
        except Exception as e:
            print(e)
            raise Exception("e")
    
    @staticmethod
    def checkPassword(raw_password, enc_password):
       print("Compare passwords")
       return sha256(raw_password.encode("utf-16")).hexdigest() == enc_password