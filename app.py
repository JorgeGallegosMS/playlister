from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
# db.playlists.drop()
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
def playlists_new():
    """Create a new playlist"""
    return render_template('playlists_new.html.j2')

@app.route('/playlists', methods=['POST'])
def playlists_submit():
    """Submit a new playlist"""
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    playlists.insert_one(playlist)
    return redirect(url_for('playlists_index'))

if __name__ == '__main__':
    app.run(debug=True)
