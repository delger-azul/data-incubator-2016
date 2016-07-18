from flask import Flask, request, abort, render_template, redirect
app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return "Hello world!"
#     return render_template('index.html', name=name)
#
# @app.route('/aboutme')
# def hello(name=None):
#     return render_template('aboutme.html', name=name)

if __name__ == '__main__':
    app.run(port=33507)
