from flask import Flask,render_template
from app import app,db


@app.route('/')
def home():
    return render_template('home.html')