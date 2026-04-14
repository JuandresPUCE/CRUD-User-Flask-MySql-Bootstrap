from flask import Flask, render_template, request, redirect, url_for
# Framework de Flask para crear aplicaciones web en Python
# pip install flask
import os
import sys

# Agregar el directorio actual al path para imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importar los controladores
from controllers.user_controller import UserController

# Directorio de plantillas vistas
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# Unir directorios
template_dir = os.path.join(template_dir, 'src', 'templates')

# Crear la aplicación de Flask
app = Flask(__name__, template_folder=template_dir)

# ========== RUTAS DE LA APLICACIÓN ==========

@app.route('/')
def home():
    """Ruta principal que muestra todos los usuarios"""
    return UserController.home()

@app.route('/user_add', methods=['POST'])
def add_user():
    """Ruta para agregar un nuevo usuario"""
    return UserController.add_user()

@app.route('/user_delete/<int:id>', methods=['POST'])
def delete_user(id):
    """Ruta para eliminar un usuario"""
    return UserController.delete_user(id)

@app.route('/user_update/<int:id>', methods=['POST'])
def update_user(id):
    """Ruta para actualizar un usuario"""
    return UserController.update_user(id)




# ========== EJECUCIÓN DE LA APLICACIÓN ==========
if __name__ == '__main__':
    # Escuchar solo en localhost para evitar problemas de permisos
    app.run(debug=True, host='127.0.0.1', port=5002)


