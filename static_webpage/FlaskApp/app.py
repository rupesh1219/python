'''
setting up flask
'''

from flask import Flask
from flask import render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/agentoptouts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#creating a database

db = SQLAlchemy(app)


class agentoptouts(db.Model):
    __tablename__ = 'optouts'
    agent_number = db.Column(db.String(50),  primary_key=True)
    agent_firstname = db.Column(db.String(50))
    agent_lastname = db.Column(db.String(50))


def __init__(self, agent_number, agent_firstname, agent_lastname):
    self.agent_number = agent_number
    self.agent_firstname = agent_firstname
    self.agent_lastname = agent_lastname

db.create_all()

# now defining the basic route and its corresponding request handler

@app.route("/")
def enter():
    return render_template('signup.html',agentoptouts=agentoptouts.query.all())


@app.route("/submit",methods=['POST','GET'])
def store():

    if request.method == 'POST':
        if not request.form['agntnum'] or \
           not request.form['fname'] or \
           not request.form['lname']:
            flash('Plese enter all the fields')
        else:
            agentoptout = agentoptouts(agent_number=request.form['agntnum'],
                                       agent_firstname=request.form['fname'],
                                       agent_lastname=request.form['lname'])
            db.session.add(agentoptout)
            db.session.commit()
            flash('records successfully added')
            return redirect(url_for('enter'))


# check if executed file is the main program and run the app

if __name__ == "__main__":
    app.run()
