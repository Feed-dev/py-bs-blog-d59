from flask import Flask, render_template
import requests

# Fetch posts from the API
posts = requests.get("https://api.npoint.io/05e3044c5e7900f3b069").json()

app = Flask(__name__)


@app.route('/')
def index():
    # Pass the posts to the template
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
