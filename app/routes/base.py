from flask import Flask,render_template
from app import app

@app.route("/base")
def base():
    return render_template('base.html')