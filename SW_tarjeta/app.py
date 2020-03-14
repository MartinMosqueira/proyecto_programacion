from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

app = Flask(__name__)
db.init_app(app)
app.config.from_object('config.Config')

with app.app_context():
    from . import modelos
    db.create_all()
    
    

@app.route('/tarjeta')
def tarjeta():
    return render_template("index.html")

@app.route('/tarjeta', methods=['POST'])
def crear():
     if request.method == 'POST':
        tipo = request.form.get('tipo')
        numero = request.form.get('numero')
        cods = request.form.get('cods')
        return redirect(url_for('tarjeta'))



if __name__ == '__main__':
    app.run(debug=True)