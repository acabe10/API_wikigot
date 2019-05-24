from flask import Flask, render_template,abort,request
import os,requests
app = Flask(__name__)

URL_BASE = 'https://anapioficeandfire.com/api/'

port = os.environ['PORT']
app.run('0.0.0.0',int(port), debug=True)
language = 'es-ES'

@app.route('/',methods = ['GET'])
def inicio():
	return render_template("templates/index.html")