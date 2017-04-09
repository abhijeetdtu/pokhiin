from flask import Blueprint
from flask import jsonify
from flask import request, url_for
from flask.ext.login import current_user
from Helpers import Helpers
from config import Config
from logger import Logger

import dbAccess
import os

researchAPI = Blueprint('researchAPI', __name__)

@researchAPI.route("/api/research/getGraphItems" ,methods=['GET'])
def GetGraphItems():
    try:
        return jsonify({"success" : True , "data" : dbAccess.PlotLy.GetAllPlotLyGraphs()})
    except Exception as e:
        print(e)
        Logger.Log(e)
        return jsonify({"success" : False , "data" : []})
