from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisthesecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database1.db'
db = SQLAlchemy(app)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message' : 'Falta el token'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'Token invalido'}), 403
        
        return f(*args, **kwargs)
    
    return decorated

    
class Tarjeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(15))
    numero = db.Column(db.Integer)
    cods = db.Column(db.Integer)
    ven = db.Column(db.Integer)


@app.route('/tarjeta')
#@token_required
def tarjeta():
    tarjetas = Tarjeta.query.all()
    return render_template("index.html", tarjetas=tarjetas)

@app.route('/tarjeta', methods=['POST'])
def crear():
    tarjeta = Tarjeta(tipo = request.form['tipo'], numero = request.form['numero'], cods = request.form['cods'], ven = request.form['ven'])
    db.session.add(tarjeta)
    db.session.commit()
    return redirect(url_for('tarjeta'))

@app.route('/eliminar/<id>')
def eliminar(id):
    tarjeta = Tarjeta.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('tarjeta'))

#terminar
@app.route('/actualizar/<id>')
def actualizar(id):
    tarjeta = Tarjeta.query.filter_by(id=int(id)).first()
    db.session.commit()
    return redirect(url_for('tarjeta'))

@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=50)}, app.config['SECRET_KEY'])

        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('could not verify',401, {'www-Authenticate' : 'Basic realm="Login Required"'})

if __name__ == '__main__':
    app.run(debug=True)