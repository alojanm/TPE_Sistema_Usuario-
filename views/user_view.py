#Maribel
import json
import os
import re

from models.user_model import User

RUTA_USUARIOS = "usuarios.json"


def cargar_usuarios():
    """
    Lee la información almacenada en usuarios.json
    y devuelve la lista de usuarios.
    """

    if not os.path.exists(RUTA_USUARIOS):
        return []

    try:
        with open(RUTA_USUARIOS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()

            if not contenido:
                return []

            return json.loads(contenido)

    except (json.JSONDecodeError,FileNotFoundError):

        return []


def guardar_usuarios(lista_usuarios):
    """
    Guarda la lista actualizada de usuarios
    dentro del archivo JSON.
    """

    with open(RUTA_USUARIOS, "w", encoding="utf-8") as archivo:
        json.dump(lista_usuarios, archivo, indent=4, ensure_ascii=False)

#Ana
# ================
# VALIDACIONES
# ================

def validar_campos(cedula,nombre,email,password):

    # CEDULA
    if not cedula.strip():
        return "Error: la cédula es obligatoria."

    if not cedula.isdigit():
        return "Error: la cédula solo debe contener números."

    if len(cedula) != 10:
        return "Error: la cédula debe tener exactamente 10 dígitos."

    # NOMBRE
    if not nombre.strip():
        return "Error: el nombre es obligatorio."

    if len(nombre.strip()) < 2:
        return "Error: el nombre es demasiado corto."

    if not nombre.replace(" ", "").isalpha():
        return "Error: el nombre solo debe contener letras."

    # EMAIL
    if not email.strip():
        return "Error: el email es obligatorio."

    patron_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(patron_email,email):

        return (
            "Error: el correo debe tener "
            "formato ejemplo@dominio.com"
        )

    # PASSWORD
    if not password.strip():
        return "Error: la contraseña es obligatoria."

    if len(password) < 6:
        return (
            "Error: la contraseña debe "
            "tener mínimo 6 caracteres."
        )

    if not any(
            caracter.isdigit()
            for caracter in password
    ):

        return (
            "Error: la contraseña debe "
            "contener al menos un número."
        )

    if not any(
            caracter.isalpha()
            for caracter in password
    ):

        return (
            "Error: la contraseña debe "
            "contener al menos una letra."
        )

    return None


# =====================================
# REGISTRO
# =====================================

def registrar_usuario():

    print("\n=== REGISTRO DE USUARIO ===")

    cedula = input("Cédula: ").strip()
    nombre = input("Nombre: ").strip()
    email = input("Email: ").strip().lower()
    password = input("Contraseña: ").strip()

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

        if usuario.get("cedula") == cedula:

            print(
                "Error: la cédula ya se encuentra registrada."
            )

            return

        if usuario.get("email") == email:

            print(
                "Error: el email ya se encuentra registrado."
            )

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

    print(
        "Usuario registrado correctamente."
    )


# =====================================
# LOGIN
# =====================================

def autenticar_usuario():

    print("\n=== INICIO DE SESIÓN ===")

    email = input(
        "Email: "
    ).strip().lower()

    password = input(
        "Contraseña: "
    ).strip()

    usuarios = cargar_usuarios()

    if not usuarios:

        print(
            "No existen usuarios registrados."
        )

        return

    for usuario in usuarios:

        if (
                usuario.get("email") == email
                and
                usuario.get("password") == password
        ):

            print(
                "Login exitoso."
            )

            return

    print(
        "Credenciales incorrectas."
    )