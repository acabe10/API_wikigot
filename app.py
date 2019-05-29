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
	else:
		personaje=request.form['busqueda']
		if personaje != '':
			pagina=1
			r=request.get(URL_BASE+'characters/'+pagina)
			if r.status_code == 200:
				doc = r.json()
				while personaje != doc["name"]:
					pagina=pagina+1
					r=request.get(URL_BASE+'characters/'+pagina)
				return render_template("personajes.html",datos=doc)
		else:
			error="Hay que introducir algún dato."
			return render_template("personajes.html",error=error)

app.run(debug=True)
#app.run('0.0.0.0',int(port), debug=True)