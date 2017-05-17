from __future__ import absolute_import
from flask import Blueprint
from flask import jsonify
from flask import request, url_for
from flask.ext.login import login_user, login_required ,logout_user , current_user
from Pokhi.Pokhi.WebScrap.WikiScrap import WikiScrapper
from Pokhi.Pokhi.Rest.logger import Logger

wikipediaAPI = Blueprint('wikipediaAPI', __name__)

@wikipediaAPI.route('/api/wikipedia/page' , methods=['POST'])
def GetPage():
     try:
        topic = request.json['topic']
        data = WikiScrapper.GetPage(topic)
        success = True
        return jsonify({'success' : success , 'data' : data})
     except Exception as e:
         success = False
         print(e)
         Logger.Log("Error" , e.message)
         return jsonify({'success' : success , 'data' :  {"topic" : topic , "title":"LoremIpsem" , "images": [""] ,"content" : "No content" , "summary": "No page retrieved" }})
     
@wikipediaAPI.route('/api/wikipedia/feed' , methods=['POST'])
def GetFeed():
     try:
        lastId = request.json['lastId']
        if(request.json != None and 'count' in request.json):
            count = request.json['count']
        else:
            count = 10
        data = WikiScrapper.GetFeed(lastId)
        success = True
        return jsonify({'success' : success , 'data' : data})
     except Exception as e:
         success = False
         print(e , "GetFeed")
         Logger.Log("Error" , e.message)
         return jsonify({'success' : success , 'data' :  [{"topic" : topic , "title":"LoremIpsem" , "images": [""] ,"content" : "No content" , "summary": "No page retrieved" }]})

     