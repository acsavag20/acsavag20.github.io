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

import requests,re,pandas as pd
#World Golf Ranking List Sub-site
#url = "https://www.owgr.com/current-world-ranking"
url = "https://www.pgatour.com/stats/stat.186.html"
r=requests.get(url)
df_list=pd.read_html(r.text)
df=df_list[1]
wgrank=df.rename(columns={"RANK\xa0THIS WEEK":"Rank","PLAYER NAME":"Name"})

@app.route('/WGRankings')
def WGRankings():
    return render_template('WGRankings.html',data=wgrank,animal='dog',animals=['dog','cat'])

if __name__ == "__main__":
    app.run(debug=True)

