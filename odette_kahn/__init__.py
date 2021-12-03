from flask import Flask

app = Flask(__name__)

from odette_kahn.api import routes
