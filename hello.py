from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/favorites")
def favorites():
    favorites = [
        {'name':'Blue', 'background': 'bg-primary'},
        {'name':'Red', 'background': 'bg-danger'},
        {'name':'Green', 'background': 'bg-success'},
        {'name':'Orange', 'background': 'bg-warning'},
        {'name':'Light Blue', 'background': 'bg-info'},
    ]
    return render_template('favorites.html', colors=favorites)