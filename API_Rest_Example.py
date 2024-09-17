from flask import Flask, jsonify, request

app = Flask(__name__)


# Base de datos simulada
peliculas = [
    {"id": 1, "title": "El kaiz", "director": "Nolan", "year": 2010},
    {"id": 2, "title": "Modern Family", "director": "Ford Cpola", "year": 1972},
]


# Ruta para obtener todas las peliculas
@app.route('/peliculas', methods=['GET'])
def get_peliculas():
    return jsonify(peliculas)


# Ruta para obtener una pelicula específica
@app.route('/peliculas/<int:pelicula_id>', methods=['GET'])
def get_pelicula(pelicula_id):
    pelicula = next((pelicula for pelicula in peliculas if pelicula['id'] == pelicula_id), None)
    if pelicula:
        return jsonify(pelicula)
    return jsonify({"error": "pelicula no encontrada"}), 404


# Ruta para crear una nueva pelicula
@app.route('/peliculas', methods=['POST'])
def create_pelicula():
    new_pelicula = request.json
    new_pelicula['id'] = max(pelicula['id'] for pelicula in peliculas) + 1
    peliculas.append(new_pelicula)
    return jsonify(new_pelicula), 201



# Ruta para actualizar una pelicula existente
@app.route('/peliculas/<int:pelicula_id>', methods=['PUT'])
def update_pelicula(pelicula_id):
    pelicula = next((pelicula for pelicula in peliculas if pelicula['id'] == pelicula_id), None)
    if pelicula:
        pelicula.update(request.json)
        return jsonify(pelicula)
    return jsonify({"error": "pelicula no encontrada"}), 404



# Ruta para eliminar una pelicula
@app.route('/peliculas/<int:pelicula_id>', methods=['DELETE'])
def delete_pelicula(pelicula_id):
    global peliculas
    peliculas = [pelicula for pelicula in peliculas if pelicula['id'] != pelicula_id]
    return '', 204



if __name__ == '__main__':
    app.run(debug=True)