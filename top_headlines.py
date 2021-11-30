
from flask import Flask, render_template
import requests
import json
from secret import api_key

#Get top 5 articles from technology section at NYT
url='https://api.nytimes.com/svc/topstories/v2/technology.json'
params={'api-key':api_key}
nyt_response = requests.get(url, params)
print(nyt_response)
nyt = nyt_response.json()

headlines_list = [nyt['results'][x]['title'] for x in range(5)]
links_list = [nyt['results'][x]['url'] for x in range(5)]
links_and_headlines_list = tuple(zip(headlines_list, links_list))

app = Flask(__name__)

@app.route('/')
def index():     
    return '<h1>Hello World!</h1>'

@app.route('/name/<nm>')
def name(nm):
    return render_template('name.html', name=nm)

@app.route('/headlines/<nm>')
def headlines(nm):
    return render_template('headlines.html', name=nm, headlines=headlines_list)

@app.route('/links/<nm>')
def links(nm):
    return render_template('links.html', name=nm, links_and_headlines=links_and_headlines_list)

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)
