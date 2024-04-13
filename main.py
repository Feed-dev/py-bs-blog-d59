from flask import Flask, render_template, request, redirect, url_for, abort

# Assuming fetching posts from an API
import requests

posts = requests.get("https://api.npoint.io/05e3044c5e7900f3b069").json()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = next((post for post in posts if post["id"] == post_id), None)
    if post is None:
        abort(404)
    return render_template('post.html', post=post)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        # Here, implement your logic for what should happen with the data
        print(f"Received message from {name}, Email: {email}, Phone: {phone}, Message: {message}")

        # Redirect or display a success message
        return '<h1>Successfully sent your message</h1>'
    else:
        return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
