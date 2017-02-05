from flask import Blueprint
from flask import jsonify
from flask import request, url_for
from flask.ext.login import login_user

from passlib.hash import pbkdf2_sha256

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
        return pbkdf2_sha256.hash(raw_password)
    
    @staticmethod
    def checkPassword(raw_password, enc_password):
       print("Compare passwords")
       return pbkdf2_sha256.verify(raw_password,enc_password)