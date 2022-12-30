from flask import Flask,render_template
import openpyxl
import requests,re,pandas as pd
import time
import git
import openpyxl
app = Flask(__name__)


@app.route("/About Me")
def about():
    return render_template('About Me/about.html', **locals())




#World Golf Ranking List Sub-site
#url = "https://www.owgr.com/current-world-ranking"


if __name__ == "__main__":
    app.run(debug=True)


resp = requests.get('https://www.pgatour.com/stats/stat.186.html')
df = pd.read_html(resp.content)[1]
# Rename the specified columns and extract them into a new DataFrame.
df = df.rename(columns={"RANK\xa0THIS WEEK":"Rank","PLAYER NAME":"Name"})[['Rank', 'Name']]
df['Update Time']=pd.Timestamp.now()

repo = git.Repo("")
workbook= openpyxl.Workbook()
sheet= workbook.active
sheet = df
workbook.save("wgr_rankings.xlsx")
repo.index.add(["wgr_rankings.xlsx"])
repo.index.commit("Added golfers excel")
origin=repo.remote("origin")
origin.push()