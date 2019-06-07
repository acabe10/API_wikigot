import requests
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)	
URL_BASE ="https://anapioficeandfire.com/api/"

#port = os.environ["PORT"]

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

@app.route('/houses/', methods = ['GET', 'POST'])
@app.route('/houses/page=<id>')
def houses(id=1):
	if request.method == 'GET':
		payload={"page":id,"pagesize":20}
		id=int(id)
		nexe=id+1
		previous=id-1
		r=requests.get(URL_BASE+'houses/',params=payload)
		if r.status_code == 200:
			doc = r.json()
			return render_template("houses.html",datos=doc,id=id,nexe=nexe,previous=previous)
	else:
		name=request.form['busqueda']
		if name != '':
			return redirect(url_for('house',name=name))
		else:
			error="You must enter some data."
			return render_template("houses.html",error=error)

@app.route("/house/<name>")
def house(name):
	payload={"name":name}
	r=requests.get(URL_BASE+'houses/',params=payload)
	lista=[]
	if r.status_code == 200:
		doc = r.json()
		try:
			current_lord=doc[0]['currentLord']
			r_2=requests.get(current_lord)
			if r_2.status_code == 200:
				doc_2 = r_2.json()
		except:
			doc_2=""
		try:
			for i in doc[0]['swornMembers']:
				r_3=requests.get(i)
				if r_3.status_code == 200:
					doc_3 = r_3.json()
					lista.append(doc_3['name'])
		except:
			lista=""
		return render_template("house.html",datos=doc,datos_2=doc_2,datos_3=lista)
	

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
		fecha=doc[0]['released'].strip('T00:00:00')
		return render_template("books_id.html",datos=doc,fecha=fecha)

@app.route("/character/<name>")
def character(name):
	payload={"name":name}
	r=requests.get(URL_BASE+'characters/',params=payload)
	lista=[]
	if r.status_code == 200:
		doc=r.json()
		try:
			for i in doc[0]['allegiances']:
				r_3=requests.get(i)
				if r_3.status_code == 200:
					doc_3 = r_3.json()
					lista.append(doc_3['name'])
		except:
			lista=""
		return render_template("character.html",datos=doc,lista=lista)


app.run(debug=True)
#app.run('0.0.0.0',int(port), debug=True)