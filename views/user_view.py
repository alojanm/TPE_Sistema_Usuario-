print("hola")

from models.user_model import User


def validar_campos(cedula, nombre, email, password):
    if not cedula.strip():
        return "La cédula es obligatoria"

    if not nombre.strip():
        return "El nombre es obligatorio"

    if not email.strip():
        return "El email es obligatorio"

    if "@" not in email:
        return "Email inválido"

    if not password.strip():
        return "La contraseña es obligatoria"

    return None


def registrar_usuario():
    print("\n=== REGISTRO DE USUARIO ===")

    cedula = input("Cédula: ")
    nombre = input("Nombre: ")
    email = input("Email: ")
    password = input("Contraseña: ")

    error = validar_campos(
        cedula,
        nombre,
        email,
        password
    )

    if error:
        print(error)
        return

    usuarios = cargar_usuarios()

    for usuario in usuarios:

        if usuario["email"] == email:
            print("El email ya está registrado")
            return

    nuevo_usuario = User(
        cedula,
        nombre,
        email,
        password
    )

    usuarios.append(
        nuevo_usuario.to_dict()
    )

    guardar_usuarios(
        usuarios
    )

    print("Usuario registrado correctamente")