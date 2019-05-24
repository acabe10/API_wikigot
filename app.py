from flask import Flask, render_template,abort,request
import os,requests
app = Flask(__name__)

URL_BASE = 'https://anapioficeandfire.com/api/'

port = os.environ['PORT']
app.run('0.0.0.0',int(port), debug=True)

language = 'es-ES'

@app.route('/',methods = ['GET'])
def inicio():
   def inicio():
        return render_template("inicio.html")

@app.route('/busqueda', methods = ['GET', 'POST'])
def busqueda():
        if request.method == 'GET':
            return render_template("busqueda.html")

@app.route('/contacto')
def contacto():
    return render_template("contact.html")

@app.route('/listas')
def listas():
    return render_template("listas.html")
