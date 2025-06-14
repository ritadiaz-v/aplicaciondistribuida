from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/crear_y_subir', methods=['POST'])
def crear_y_subir():
    ruta_base = request.form.get('ruta_base')
    subcarpetas = request.form.getlist('subcarpetas[]')
    archivos = request.files.getlist('archivos[]')

    if not ruta_base or not subcarpetas:
        return jsonify({"error": "Faltan datos"}), 400

    ruta_final = os.path.join(ruta_base, *subcarpetas)

    try:
        os.makedirs(ruta_final, exist_ok=True)

        for archivo in archivos:
            archivo.save(os.path.join(ruta_final, archivo.filename))

        return jsonify({"mensaje": f"Carpeta creada y archivos subidos en: {ruta_final}"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

