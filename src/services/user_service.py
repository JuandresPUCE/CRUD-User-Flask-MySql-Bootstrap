# Service - Lógica de negocio
# tercero en migrar, lee el repositorio y el modelo para aplicar validaciones y reglas de negocio antes de enviar datos al controlador
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from repositories.user_repository import UserRepository


class UserService:
    """Maneja la lógica de negocio para usuarios"""

    @staticmethod
    def get_all_users():
        """Obtiene todos los usuarios"""
        users = UserRepository.get_all()
        # Convertir a lista de diccionarios para enviar al template
        return [user.to_dict() for user in users]

    @staticmethod
    def create_user(username, name, password):
        """Crea un nuevo usuario con validaciones"""
        # Validación de campos vacíos
        if not username or not name or not password:
            raise ValueError("El nombre de usuario, nombre y contraseña son requeridos")
        
        # Validación de longitud mínima
        if len(username) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres")
        if len(name) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres")
        if len(password) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")
        
        # Crear usuario en BD
        success = UserRepository.create(username, name, password)
        if not success:
            raise Exception("Error al crear el usuario en la base de datos")
        
        return success

    @staticmethod
    def delete_user(user_id):
        """Elimina un usuario"""
        if not user_id:
            raise ValueError("ID de usuario es requerido")
        
        success = UserRepository.delete(user_id)
        if not success:
            raise Exception("Error al eliminar el usuario")
        
        return success

    @staticmethod
    def update_user(user_id, username, name, password):
        """Actualiza un usuario con validaciones"""
        if not user_id:
            raise ValueError("ID de usuario es requerido")
        
        # Validación de campos vacíos
        if not username or not name or not password:
            raise ValueError("El nombre de usuario, nombre y contraseña son requeridos")
        
        # Validación de longitud mínima
        if len(username) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres")
        if len(name) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres")
        if len(password) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")
        
        success = UserRepository.update(user_id, username, name, password)
        if not success:
            raise Exception("Error al actualizar el usuario")
        
        return success
