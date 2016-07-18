from flask import Flask, request, abort, render_template, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/index')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/aboutme')
def about(name=None):
    return render_template('aboutme.html', name=name)

if __name__ == '__main__':
    app.run(port=33507)
