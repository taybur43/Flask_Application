#!/usr/bin/env python
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('home.html')
@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/hello')
def hello():
  return render_template('hello.html')


@app.route('/login')
def login():
  return render_template('login.html')


if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0',port='5001') 

