from flask import request, render_template, redirect, url_for, make_response
from datetime import datetime as dt
from flask import current_app as app
from .modelos import db, Persona, Tarjeta, Venta

@app.route('/prueba/<token>/<llamado>', methods=["GET","POST"])
def probando(token, llamado):
    print('token: {}'.format(token))
    print('llamado: {}'.format(llamado))
    print('request.args')
    print(request.args)
    print('request.base_url')
    print(request.base_url)
    print('request.data')
    print(request.data)
    print('request.form')
    print(request.form)
    print('request.get_json()')
    print(request.get_json())
    print('request.get_data()')
    print(request.get_data())
    print('request.full_path')
    print(request.full_path)
    print('request.headers')
    print(request.headers)
    print('request.method')
    print(request.method)
    print('request.query_string')
    print(request.query_string)
    print('request.referrer')
    print(request.referrer)
    print('request.user_agent')
    print(request.user_agent)
    response = app.response_class(
        response={},
        status=200,
#        mimetype='application/json'
    )
    return response
