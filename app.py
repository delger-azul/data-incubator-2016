from flask import Flask, request, abort, render_template, redirect
app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/aboutme')
def about(name=None):
    return render_template('aboutme.html', name=name)

@app.route('/plot_aid_coverage')
def plot1(name=None):
    return render_template('plot_aid_coverage.html', name=name)

@app.route('/tableau')
def tableau(name=None):
    return render_template('tableau.html', name=name)

if __name__ == '__main__':
    app.run(port=33507)
