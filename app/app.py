from flask import Flask, request, abort, render_template, redirect
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(port=33507)
