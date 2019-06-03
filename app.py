import requests
from flask import Flask, render_template, request
app = Flask(__name__)	
URL_BASE ="https://anapioficeandfire.com/api/"

#port = os.environ['PORT']

@app.route('/')
def inicio():
	return render_template("index.html")

@app.route('/books/', methods = ['GET'])
def libros():
	payload={"pagesize":20}
	r=requests.get(URL_BASE+'books/',params=payload)
	if r.status_code == 200:
		doc = r.json()
		return render_template("books.html",datos=doc)

@app.route('/houses/', methods = ['GET'])
@app.route('/houses/page=<id>')
def houses(id=1):
	payload={"page":id,"pagesize":20}
	id=int(id)
	nexe=id+1
	previous=id-1
	r=requests.get(URL_BASE+'houses/',params=payload)
	if r.status_code == 200:
		doc = r.json()
		return render_template("houses.html",datos=doc,id=id,nexe=nexe,previous=previous)

@app.route("/house/<name>")
def house(name):
	payload={"name":name}
	r=requests.get(URL_BASE+'houses/',params=payload)
	if r.status_code == 200:
		doc = r.json()
		return render_template("house.html",datos=doc)
	

@app.route('/characters/',methods = ['GET', 'POST'])
def characters():
	if request.method == 'GET':
		return render_template("characters.html")
	else:
		personaje=request.form['busqueda']
		if personaje != '':
			payload={"name":personaje}
			r=requests.get(URL_BASE+'characters/',params=payload)
			if r.status_code == 200:
				doc=r.json()
				return render_template("characters.html",datos=doc)
		else:
			error="You must enter some data."
			return render_template("characters.html",error=error)

@app.route("/books/<name>")
def books(name):
	payload={"name":name}
	r=requests.get(URL_BASE+'books/',params=payload)
	if r.status_code == 200:
		doc = r.json()
		return render_template("books_info.html",datos=doc)

app.run(debug=True)
#app.run('0.0.0.0',int(port), debug=True)