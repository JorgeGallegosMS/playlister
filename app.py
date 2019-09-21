from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html.j2', msg='Flask is cool!')

if __name__ == '__main__':
    app.run(debug=True)
