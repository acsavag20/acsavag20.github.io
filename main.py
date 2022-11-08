from flask import Flask,render_template

app = Flask(__name__)

@app.route("/home.html")
def home():
    return render_template("home.html")


import requests,re,pandas as pd
#World Golf Ranking List Sub-site
#url = "https://www.owgr.com/current-world-ranking"
url = "https://www.pgatour.com/stats/stat.186.html"
r=requests.get(url)
df_list=pd.read_html(r.text)
df=df_list[1]
wgrank=df.rename(columns={"RANK\xa0THIS WEEK":"Rank","PLAYER NAME":"Name"})

@app.route('/')
def WGRankings():
    animal='dog'
    return render_template('WGRankings.html',data=wgrank,value=animal,animals=['dog','cat'])

if __name__ == "__main__":
    app.run(debug=True)

