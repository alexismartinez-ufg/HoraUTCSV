from flask import Flask, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def hello():
    return obtener_horas()


@app.route('/horas', methods=['GET'])
def obtener_horas():
    hora_utc = datetime.utcnow()
    hora_el_salvador = hora_utc - timedelta(hours=6)

    resultado = {
        'hora_UTC': hora_utc.strftime('%Y-%m-%d %H:%M:%S'),
        'hora_El_Salvador': hora_el_salvador.strftime('%Y-%m-%d %H:%M:%S')
    }

    return jsonify(resultado)

@app.route('/hora-utc', methods=['GET'])
def obtener_hora_utc():
    hora_utc = datetime.utcnow()

    resultado = {
        'hora_UTC': hora_utc.strftime('%Y-%m-%d %H:%M:%S')
    }

    return jsonify(resultado)

@app.route('/hora-el-salvador', methods=['GET'])
def obtener_hora_el_salvador():
    hora_utc = datetime.utcnow()
    hora_el_salvador = hora_utc - timedelta(hours=6)

    resultado = {
        'hora_El_Salvador': hora_el_salvador.strftime('%Y-%m-%d %H:%M:%S')
    }

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
