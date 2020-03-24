from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import jwt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
db = SQLAlchemy(app)
    
class Tarjeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(15))
    numero = db.Column(db.Integer)
    cods = db.Column(db.Integer)


@app.route('/tarjeta')
def tarjeta():
    tarjetas = Tarjeta.query.all()
    return render_template("index.html", tarjetas=tarjetas)

@app.route('/tarjeta', methods=['POST'])
def crear():
    tarjeta = Tarjeta(tipo = request.form['tipo'], numero = request.form['numero'], cods = request.form['cods'] )
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


if __name__ == '__main__':
    app.run(debug=True)