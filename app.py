import requests
from flask import Flask, render_template, request, url_for
app = Flask(__name__)	
URL_BASE ="https://anapioficeandfire.com/api/"

#port = os.environ['PORT']
#language = 'es-ES'

@app.route('/')
def inicio():
	return render_template("index.html")

@app.route('/libros/')
def libros():
	r=requests.get(URL_BASE+'books/')
	if r.status_code == 200:
		doc = r.json()
		return render_template("libros.html",datos=doc)

@app.route('/casas/')
def casas():
	return render_template("casas.html")

@app.route('/personajes/')
def personajes():
	return render_template("personajes.html")

app.run(debug=True)