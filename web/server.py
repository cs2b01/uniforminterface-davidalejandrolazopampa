from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/User')
def users():
    db_session = db.getSession(engine)
    user = db_session.query(entities.User)
    data = user[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype = 'application/json')

@app.route('/create_user', methods = ['GET'])
def create_test_books():
    db_session = db.getSession(engine)
    userdavid = entities.User(codigo=201810015, nombre="Nuevo Alumno" , apellido="Nuevo Apelldio", password="123")
    db_session.add(userdavid)
    db_session.commit()
    return "User Create DAVLP!"

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(debug=True,)

