from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/favorites")
def favorites():
    favorites = [
        {'name':'Prince', 'background': 'bg-info'},
        {'name':'James Brown', 'background': 'bg-info'},
        {'name':'George Clinton', 'background': 'bg-info'},
        {'name':'Stevie Wonder', 'background': 'bg-info'},
        {'name':'The Beatles', 'background': 'bg-info'},
    ]
    return render_template('favorites.html', musicians=favorites)