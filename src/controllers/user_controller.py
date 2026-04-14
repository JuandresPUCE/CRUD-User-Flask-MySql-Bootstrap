# Controller - Maneja las rutas y la orquestación
# cuarto en migrar, es el encargado de recibir las solicitudes HTTP, llamar al servicio correspondiente y devolver la respuesta adecuada (renderizar templates o redirigir)
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import render_template, request, redirect, url_for
from services.user_service import UserService


class UserController:
    """Maneja las rutas relacionadas con usuarios"""

    @staticmethod
    def home():
        """Muestra la página principal con todos los usuarios"""
        try:
            users = UserService.get_all_users()
            return render_template('index.html', data=users)
        except Exception as e:
            print(f"Error en home: {e}")
            return render_template('index.html', data=[])

    @staticmethod
    def add_user():
        """Añade un nuevo usuario"""
        try:
            user_name = request.form['username']
            name = request.form['name']
            password = request.form['password']

            UserService.create_user(user_name, name, password)
            return redirect(url_for('home'))
        except ValueError as e:
            print(f"Validación error: {e}")
            return redirect(url_for('home'))
        except Exception as e:
            print(f"Error al agregar usuario: {e}")
            return redirect(url_for('home'))

    @staticmethod
    def delete_user(user_id):
        """Elimina un usuario"""
        try:
            UserService.delete_user(user_id)
            return redirect(url_for('home'))
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return redirect(url_for('home'))

    @staticmethod
    def update_user(user_id):
        """Actualiza un usuario"""
        try:
            user_name = request.form['username']
            name = request.form['name']
            password = request.form['password']

            UserService.update_user(user_id, user_name, name, password)
            return redirect(url_for('home'))
        except ValueError as e:
            print(f"Validación error: {e}")
            return redirect(url_for('home'))
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return redirect(url_for('home'))
