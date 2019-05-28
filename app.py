import requests
from flask import Flask, render_template, request, url_for
app = Flask(__name__)	
URL_BASE ="https://anapioficeandfire.com/api/"

#port = os.environ['PORT']
#language = 'es-ES'

@app.route('/')
def inicio():
	return render_template("index.html")

@app.route('/libros/', methods = ['GET'])
def libros():
	payload={"pagesize":20}
	r=requests.get(URL_BASE+'books/',params=payload)
	if r.status_code == 200:
		doc = r.json()
		return render_template("libros.html",datos=doc)

@app.route('/casas/', methods = ['GET'])
def casas():
	payload={"pagesize":5000}
	r=requests.get(URL_BASE+'houses/',params=payload)
	if r.status_code == 200:
		doc = r.json()
		return render_template("casas.html",datos=doc)

@app.route('/personajes/',methods = ['GET', 'POST'])
def personajes():
	if request.method == 'GET':
		return render_template("personajes.html")

app.run(debug=True)