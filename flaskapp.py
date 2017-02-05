from flask import Flask, request, send_from_directory ,render_template
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import os


app = Flask(__name__ , template_folder="Pokhi/Pokhi/templates" , static_folder="Pokhi/Pokhi/static")

app.config['MONGO_DBNAME'] = 'python'


app.config['MONGO_URI'] =  'mongodb://admin:DJ7FltP4ZWLY@localhost:27017/python'

if('OPENSHIFT_MONGODB_DB_URL' in  os.environ):
    app.config['MONGO_URI'] = os.environ['OPENSHIFT_MONGODB_DB_URL'] + app.config['MONGO_DBNAME']

app.config['MONGO_USERNAME'] = 'admin'
app.config['MONGO_PASSWORD'] = 'DJ7FltP4ZWLY'

mongo = PyMongo(app)

print(app.config["MONGO_URI"])

@app.route('/')
def Index():
    return render_template("/Views/Index.html")

@app.route('/Views/<path:path>', methods=['GET', 'POST'])
def Views(path):
    print(path ,"/Views/{}".format(path) ) 
    return render_template("/Views/{}".format(path))

@app.route('/api/star', methods=['POST'])
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


@app.route('/api/star', methods=['GET'])
def GetStar():
    star = mongo.db.stars
    print(star)
    try:
        results =  star.find()
        results = [GetProperties(x) for x in results]
        print(results)
    except Exception as e:
        print(e)
    return jsonify({'result' :results})


def  GetProperties(obj , propArray = None):
    retobj = {}
    
    retobj["_id"] = str(obj["_id"])
    print(retobj)
    if(propArray == None):
        for x in obj:
            if(x != '_id'):
                retobj[x] = obj[x]
    else:
        for x in propArray:
            if(x != '_id'):
                retobj[x] = obj[x]
    return retobj

if __name__ == '__main__':
    app.run()