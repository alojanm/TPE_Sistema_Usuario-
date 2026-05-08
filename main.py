from views.user_view import (
    registrar_usuario,
    autenticar_usuario,
    cargar_usuarios
)


# =====================================
# MOSTRAR MENÚ
# =====================================

def mostrar_menu():

    print("\n" + "=" * 40)
    print("      SISTEMA DE USUARIOS")
    print("=" * 40)

    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Listar usuarios")
    print("4. Salir")


# =====================================
# LISTAR USUARIOS
# =====================================

def listar_usuarios():

    usuarios = cargar_usuarios()

    if not usuarios:

        print(
            "\nNo existen usuarios registrados."
        )

        return

    print("\n=== USUARIOS REGISTRADOS ===")

    for indice, usuario in enumerate(
            usuarios,
            start=1
    ):

        print(
            f"{indice}. "
            f"{usuario.get('nombre')} | "
            f"{usuario.get('email')} | "
            f"{usuario.get('cedula')}"
        )


# =====================================
# FUNCIÓN PRINCIPAL
# =====================================

def main():

    while True:

        mostrar_menu()

        opcion = input(
            "\nSeleccione una opción: "
        ).strip()

        # REGISTRAR
        if opcion == "1":

            registrar_usuario()

        # LOGIN
        elif opcion == "2":

            autenticar_usuario()

        # LISTAR
        elif opcion == "3":

            listar_usuarios()

        # SALIR
        elif opcion == "4":

            print(
                "\nSistema finalizado correctamente."
            )

            break

        # ERROR
        else:

            print(
                "\nError: opción inválida."
                "\nSeleccione una opción del 1 al 4."
            )


# =====================
# INICIAR PROGRAMA
# =====================

if __name__ == "__main__":
    main()