import requests
from flask import Flask, render_template, request
app = Flask(__name__)	
URL_BASE ="https://anapioficeandfire.com/api/"

#port = os.environ['PORT']

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
@app.route('/casas/page=<id>')
def casas(id=1):
	payload={"page":id,"pagesize":20}
	id=int(id)
	nexe=id+1
	previous=id-1
	r=requests.get(URL_BASE+'houses/',params=payload)
	if r.status_code == 200:
		doc = r.json()
		return render_template("casas.html",datos=doc,id=id,nexe=nexe,previous=previous)

@app.route('/casas/<id>/<id2>')
def casas_2(id=1,id2=1):
	payload={"name":id2}
	r=requests.get(URL_BASE+'houses/',params=payload)
	if r.status_code == 200:
		doc = r.json()
		okis = "okis"
		return render_template("casas.html",datos=doc,id=id,id2=id2,okis=okis)

@app.route('/personajes/',methods = ['GET', 'POST'])
def personajes():
	if request.method == 'GET':
		return render_template("personajes.html")
	else:
		personaje=request.form['busqueda']
		if personaje != '':
			payload={"name":personaje}
			r=requests.get(URL_BASE+'characters/',params=payload)
			if r.status_code == 200:
				doc=r.json()
				return render_template("personajes.html",datos=doc)
		else:
			error="Hay que introducir algún dato."
			return render_template("personajes.html",error=error)

app.run(debug=True)
#app.run('0.0.0.0',int(port), debug=True)