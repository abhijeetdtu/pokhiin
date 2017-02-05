from flask import Blueprint
from flask import jsonify

from Helpers import Helpers
from dbConnect import mongo

starAPI = Blueprint('starAPI', __name__)

@starAPI.route('/api/star', methods=['POST'])
def add_star():
  star = mongo.db.stars
  name = request.json['name']
  distance = request.json['distance']
  print(request.json['name'] , request.json['distance'] , star)
  try:
      star_id = star.insert({'name': name, 'distance': distance})
  except Exception as e:
      print(e)
  print("inserted")
  new_star = star.find_one({'_id': star_id })
  print("finding")
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  print("returning")
  return jsonify({'result' : output})


@starAPI.route('/api/star', methods=['GET'])
def GetStar():
    print("Getting star")
    star = mongo.db.stars
    print(star)
    try:
        results =  star.find()
        results = [Helpers.GetProperties(x) for x in results]
        print(results)
    except Exception as e:
        print(e)
    return jsonify({'result' :results})


