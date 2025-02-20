from flask import Flask, jsonify
from flask import render_template
from flask import request
import requests
import json
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        value = request.form.get('name')
        fetching = fetch(value)
        return fetching
        
    return render_template('index.html')
def fetch(movie_name):
    url = f'https://www.omdbapi.com/?apikey=9e9808e5&s={movie_name}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Convert response to JSON
        
        # Extract the list under "Search"
        movies = data.get("Search", [])
        return render_template('index.html', movies=movies)
                
         

if __name__ == "__main__":
    app.run(debug=True)
