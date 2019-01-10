from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ciezki do zgadniecia string'

from app import routes