from flask import Flask
from flask import render_template
from flask import request
import json
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def search():
    return render_template('index.html')

def fetch():
    data = request.json
    url = 'https://www.omdbapi.com/?apikey=9e9808e5&t=oppenheimer&plot=full' 

if __name__ == "__main__":
    app.run(debug=True)
