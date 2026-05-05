class User:
    def __init__(self, cedula, nombre, email, password):
        self.cedula = cedula
        self.nombre = nombre
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "cedula": self.cedula,
            "nombre": self.nombre,
            "email": self.email,
            "password": self.password
        }
