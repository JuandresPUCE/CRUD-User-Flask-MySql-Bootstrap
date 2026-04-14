# Repository - Acceso a base de datos
# segundo en migrar despues del modelo aun utiliza CRUD de consultas SQL directas, luego se puede migrar a un ORM como SQLAlchemy
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import database as db
from models.user import User


class UserRepository:
    """Maneja todas las operaciones de base de datos para usuarios"""

    @staticmethod
    def get_all():
        """Obtiene todos los usuarios de la base de datos"""
        try:
            cursor = db.database.cursor()
            cursor.execute('SELECT * FROM users')
            myresult = cursor.fetchall()
            
            users = []
            column_names = [column[0] for column in cursor.description]
            
            for result in myresult:
                user_dict = dict(zip(column_names, result))
                user = User(
                    id=user_dict['id'],
                    username=user_dict['username'],
                    name=user_dict['name'],
                    password=user_dict['password']
                )
                users.append(user)
            
            cursor.close()
            return users
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return []

    @staticmethod
    def create(username, name, password):
        """Inserta un nuevo usuario en la base de datos"""
        try:
            cursor = db.database.cursor()
            sql = 'INSERT INTO users (username, name, password) VALUES (%s, %s, %s)'
            val = (username, name, password)
            cursor.execute(sql, val)
            db.database.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False

    @staticmethod
    def delete(user_id):
        """Elimina un usuario de la base de datos"""
        try:
            cursor = db.database.cursor()
            sql = 'DELETE FROM users WHERE id = %s'
            val = (user_id,)
            cursor.execute(sql, val)
            db.database.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return False

    @staticmethod
    def update(user_id, username, name, password):
        """Actualiza un usuario en la base de datos"""
        try:
            cursor = db.database.cursor()
            sql = 'UPDATE users SET username = %s, name = %s, password = %s WHERE id = %s'
            val = (username, name, password, user_id)
            cursor.execute(sql, val)
            db.database.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False
