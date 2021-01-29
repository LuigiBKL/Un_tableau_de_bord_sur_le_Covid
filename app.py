from flask import Flask, render_template,url_for,redirect,request
from flask.helpers import flash
import pandas as pd
from data import traitement_dataset

app = Flask(__name__)

@app.route('/')
def site():

    donnees = traitement_dataset()
   
    return render_template("covid2019.html",donnees=donnees)


if __name__ == "__main__":
    app.run(port=5000,debug=True)

