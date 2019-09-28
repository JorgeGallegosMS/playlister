from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists

app = Flask(__name__)

# @app.route('/')
# def index():
#     """Return homepage."""
#     return render_template('home.html.j2', msg='Flask is cool!')

# playlists = [
#     { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
#     { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
# ]

@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html.j2', playlists=playlists.find())

@app.route('/playlists/new')
def new_playlists():
    """ Create a new playlist"""
    return render_template('new_playlists.html.j2')

if __name__ == '__main__':
    app.run(debug=True)
