from funciones import ejecutar_menu_principal, iniciar_sesion


def main() -> None:
    """Función principal que inicia la autenticación y el menú del sistema."""
    nombre_usuario_1 = "danilo"
    contrasena_1 = "DDC"

    acceso = iniciar_sesion(nombre_usuario_1, contrasena_1)

    if acceso:
        ejecutar_menu_principal("Danilo")


if __name__ == "__main__":
    main()