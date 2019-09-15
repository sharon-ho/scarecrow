# -*- encoding: utf-8 -*-

import os

from flask            import Flask

from flask_restful     import Api

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

api = Api(app) # flask_restful

from app import views

