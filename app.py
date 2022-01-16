from flask import Flask
from main import *

app = Flask(__name__)

import auth
import index

app.register_blueprint(auth.bp)
app.register_blueprint(index.bp)
