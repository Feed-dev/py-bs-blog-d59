from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/05e3044c5e7900f3b069").json()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
