from flask import Flask, render_template
app = Flask(__name__)	

#URL_BASE = 'https://anapioficeandfire.com/api/'
#port = os.environ['PORT']
#language = 'es-ES'

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/libros/')
def articulos():
    return render_template("libros.html")

@app.route('/libros/')
def articulos():
    return render_template("libros.html")

app.run(debug=True)