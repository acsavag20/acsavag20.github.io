from flask import Flask,render_template
import requests,re,pandas as pd
app = Flask(__name__)

@app.route("/About Me")
def about():
    # Obtain the data and extract the table.
    resp = requests.get('https://www.pgatour.com/stats/stat.186.html')
    df = pd.read_html(resp.content)[1]
    # Rename the specified columns and extract them into a new DataFrame.
    data = df.rename(columns={"RANK\xa0THIS WEEK":"Rank","PLAYER NAME":"Name"})[['Rank', 'Name']]
    # Pass all local variables to the template by name.
    return render_template('ranking.html', **locals())




#World Golf Ranking List Sub-site
#url = "https://www.owgr.com/current-world-ranking"


@app.route('/Golf')
def ranking():
    # Obtain the data and extract the table.
    resp = requests.get('https://www.pgatour.com/stats/stat.186.html')
    df = pd.read_html(resp.content)[1]
    # Rename the specified columns and extract them into a new DataFrame.
    data = df.rename(columns={"RANK\xa0THIS WEEK":"Rank","PLAYER NAME":"Name"})[['Rank', 'Name']]
    # Pass all local variables to the template by name.
    return render_template('/Golf/rankings.html', **locals())

if __name__ == "__main__":
    app.run(debug=True)

