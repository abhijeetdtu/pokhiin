from flask import Flask , render_template
from Pokhi.Pokhi.Rest.dbConnect import mongo , login_manager
from Pokhi.Pokhi.Rest.starAPI import starAPI
from Pokhi.Pokhi.Rest.loginAPI import loginAPI
from Pokhi.Pokhi.Rest.fileAPI import fileAPI
from Pokhi.Pokhi.Rest.authAPI import AuthHelpers

import os

app = Flask(__name__ , template_folder="Pokhi/Pokhi/templates" , static_folder="Pokhi/Pokhi/static")
app.config['MONGO_DBNAME'] = 'python'
app.config['MONGO_URI'] =  'mongodb://admin:DJ7FltP4ZWLY@localhost:27017/python'

     
if('OPENSHIFT_MONGODB_DB_URL' in  os.environ):
    app.config['MONGO_URI'] = os.environ['OPENSHIFT_MONGODB_DB_URL'] + app.config['MONGO_DBNAME']

login_manager.init_app(app)
mongo.init_app(app)
app.register_blueprint(starAPI)
app.register_blueprint(loginAPI)
app.register_blueprint(fileAPI)
app.secret_key = AuthHelpers.getEncryptedPassword('super secret key')


@app.route('/')
def Index():
    return render_template("/Views/Index.html")


@app.route('/Views/<path:path>', methods=['GET', 'POST'])
def Views(path):
    print(path ,"/Views/{}".format(path) ) 
    return render_template("/Views/{}".format(path))

@app.route('/Apps/<path:path>', methods=['GET', 'POST'])
def Apps(path):
    return render_template("/Apps/{}".format(path))

if __name__ == '__main__':
    app.run()