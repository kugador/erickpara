from flask import Flask, render_template, request
from funciones import escribir_usuario as crear_usu
from funciones import leer_usuario as leer_usu
import os

app= Flask(__name__)

@app.route('/')
def index():
	return render_template("index2.html")
@app.route('/base')
def about():
	return render_template("base.html")
@app.route('/index2')
def indice():
	return render_template("index2.html")

@app.route('/registrar')
def registrar():
	return render_template("registrar.html")
@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/', methods=['POST'])
def obtener_datos():
	names=request.form['name']
	year=int(request.form['year'])
	an=2019-year-1
	es=float(request.form['estatura'])
	met=int(es)
	centi=int((es-met)*100)
	sexo=request.form['sex']
	origen=request.form['pais']
	amig=request.form['amigos'].split(",")
	estado='activo'
	muro=[]
	crear_usu(names,an,met,centi,sexo,origen,amig,estado,muro)
	return render_template("perfil.html",
	 n=names, 
	 ed=an, 
	 tam=""+str(met)+"m y "+ str(centi)+"cm", 
	 sex=sexo, 
	 pa=origen, 
	 num_amigos=amig,
	 esta=estado,
	 mur=muro)

def logearse():
	names=request.form['name']
	lista=[leer_usu(names)]
	return render_template("logon.html", n=names)

if __name__ == "__main__":
	app.run(debug=True, port=7000)