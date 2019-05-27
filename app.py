from flask import Flask, render_template
app = Flask(__name__)	

#URL_BASE = 'https://anapioficeandfire.com/api/'
#port = os.environ['PORT']
#language = 'es-ES'

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/libros/')
def libros():
    return render_template("libros.html")

@app.route('/casas/')
def casas():
	return render_template("casas.html")

@app.route('/personajes/')
def personajes():
	return render_template("personajes.html")

app.run(debug=True)