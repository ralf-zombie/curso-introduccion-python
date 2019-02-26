#!/usr/bin/env python
"""
pip install flask
export FLASK_APP=app#linux
set FLASK_APP=app#windows
flask run
"""
import time
import pandas
import os
from flask import Flask, request, render_template, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    #datos = {'pais':'Chile','cantidad':1280,'ebola':'si'}
    url = r"C:\Users\ralf\Dropbox\cursos-charlas\bigdata-data-science\data-ejemplo\ebola_data.csv"
    names = ['desc', 'pais', 'fecha', 'cantidad']
    dataset = pandas.read_csv(url, names=names)
    variable = dataset.to_json()  
    return jsonify(variable)