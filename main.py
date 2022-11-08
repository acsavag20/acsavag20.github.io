from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/Pictures")
def pictureex():
    return render_template("pictureex.html")

@app.route("/fun")
def FunPage():
    return render_template("FunPage.html")


if __name__ == "__main__":
    app.run(debug=True)

import requests
import re
import pandas as pd
import sqlite3
from pandas.io.html import read_html

@app.route('/WGRankings')
def wgrank():
    #World Golf Ranking List Sub-site
    #url = "https://www.owgr.com/current-world-ranking"
    url = "https://www.pgatour.com/stats/stat.186.html"

    r=requests.get(url)
    df_list=pd.read_html(r.text)
    df=df_list[1]
    df=df.rename(columns={"RANK\xa0THIS WEEK":"Rank","PLAYER NAME":"Name"})
    wgranking=df
    return render_template('WGRankings.html',title="World Golf Rankings",names=df['Name'],rankings=df['Rank'],data=df['Rank','Name'])