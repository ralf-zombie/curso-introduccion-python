#!/usr/bin/env python
"""
pip install validate_email
pip install flask
export FLASK_APP=app#linux
set FLASK_APP=app#windows
flask run
"""
import time
from flask import Flask, request, render_template
from validate_email import validate_email
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/equipo')
def equipo():
    return render_template('equipo.html')
@app.route('/dinamico')
@app.route('/dinamico/<parametro>')
def dinamico(parametro=None):
    fecha = time.strftime("%d/%m/%y")
    return render_template('dinamico.html',parametro=parametro,fecha=fecha)
@app.route('/contacto',methods=['POST'])#@app.route('/contacto',methods=['POST', 'GET'])
def contacto():
    error_txt = None
    if request.method == 'POST':
        if request.form['nombre'] is None or request.form['correo'] is None:
            error_txt = "Error: Debe completar los campos necesarios."
        else:
            if validate_email(request.form['correo']):
                 error_txt = "En hora buena, su correo ha sido enviado"
            else:           
                error_txt = 'Error: '+request.form['correo']+' no es e-mail válido'
    else:
        error_txt = "Método no permitido :("
            
    return render_template('contacto.html',error_txt=error_txt)
