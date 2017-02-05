from flask import Flask, request, send_from_directory ,render_template
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__ , template_folder="Pokhi/Pokhi/templates" , static_folder="Pokhi/Pokhi/static")



mongo = PyMongo(app)


@app.route('/')
def Index():
    return render_template("/Views/Index.html")

@app.route('/Views/<path:path>', methods=['GET', 'POST'])
def Views(path):
    print(path ,"/Views/%s".format(path) ) 
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

if __name__ == '__main__':
    app.run()