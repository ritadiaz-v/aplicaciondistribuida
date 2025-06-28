from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir solicitudes desde el navegador

@app.route('/crear_carpeta', methods=['POST'])
def crear_carpeta():
    datos = request.json
    ruta_base = datos.get('ruta_base')
    subcarpetas = datos.get('subcarpetas')

    if not ruta_base or not subcarpetas:
        return jsonify({"error": "Faltan datos"}), 400

    ruta_completa = os.path.join(ruta_base, *subcarpetas)

    try:
        os.makedirs(ruta_completa, exist_ok=True)
        return jsonify({"mensaje": f"Carpeta creada: {ruta_completa}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
