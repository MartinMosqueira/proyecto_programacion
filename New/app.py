from flask import Flask, render_template, request, redirect, url_for
import stripe

app = Flask(__name__)

pub_key = 'pk_test_yvf1DYutOV6N54K8pH1xqWx500L6Ino96M'
secret_key = 'sk_test_sJPWHEqIx9tuM1oHQUO1O6GE00VZjvjqbu'

stripe.api_key = secret_key

@app.route('/')
def index():
    return render_template('index.html', pub_key=pub_key)

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/pay', methods=['POST'])
def pay():
    
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=9900,
        currency='usd',
        description='Stannis Baratheon T-Shirt'
    )

    return redirect(url_for('thanks'))

if __name__ == '__main__':
    app.run(debug=True)