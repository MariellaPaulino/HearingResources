# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/parent_central')
def parent_central():
	return render_template('parent_central.html')


