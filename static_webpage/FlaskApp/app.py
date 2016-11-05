'''
setting up flask
'''

from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

# now defining the basic route and its corresponding request handler

@app.route("/")
def main():
    return render_template('index.html')

# check if executed file is the main program and run the app

if __name__ == "__main__":
    app.run()
