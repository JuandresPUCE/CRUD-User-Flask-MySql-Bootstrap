# Modelo de usuario - Define la estructura de datos
# primero en migrar
class User:
    def __init__(self, id=None, username=None, name=None, password=None):
        self.id = id
        self.username = username
        self.name = name
        self.password = password

    def to_dict(self):
        """Convierte el usuario a diccionario"""
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'password': self.password
        }

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, name={self.name})"
