
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html', title="About")


@app.route('/contact/')
def contact():
    return render_template('contact.html', title="Contact")


@app.route('/portfolio/')
def portfolio():
    return render_template('portfolio.html', title="Portfolio")


@app.route('/test/')
def test():
    return render_template('test.html', title="test")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
