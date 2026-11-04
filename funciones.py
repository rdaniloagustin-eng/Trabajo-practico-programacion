# PARTE 1: Autenticación y Menú de Opciones

def verificar_usuario(nombre_ingresado: str, usuario_valido: str) -> bool:
    """
    Verifica si el nombre de usuario ingresado coincide con el registrado.
    """
    es_valido = False
    if nombre_ingresado == usuario_valido:
        es_valido = True
    return es_valido


def verificar_contrasena(contrasena_valida: str, max_intentos: int = 5) -> bool:
    """
    Solicita y valida la contraseña permitiendo un máximo de intentos.
    """
    acceso = True
    contador = 1
    contrasena = input("Por favor, ingresa tu contraseña: ")

    while contrasena != contrasena_valida and contador < max_intentos:
        print("Contraseña incorrecta. Intenta nuevamente.")
        contrasena = input("Por favor, ingresa correctamente tu contraseña: ")
        contador += 1

    if contrasena != contrasena_valida:
        print("Has excedido el número máximo de intentos. Acceso denegado.")
        acceso = False

    return acceso


def iniciar_sesion(usuario_valido: str = "danilo", contrasena_valida: str = "DDC") -> bool:
    """
    Gestiona el proceso completo de inicio de sesión del usuario.
    """
    acceso = False
    nombre_usuario = input("Por favor, ingresa tu nombre: ")

    if verificar_usuario(nombre_usuario, usuario_valido):
        acceso = verificar_contrasena(contrasena_valida, 5)
    else:
        print("Nombre de usuario incorrecto. Acceso denegado.")

    return acceso


def mostrar_menu() -> None:
    """Muestra por pantalla las opciones disponibles del menú principal."""
    print("Menu de opciones ")
    print("a - proyectos")
    print("b - tablas")
    print("c - variables")
    print("d - mostrar")
    print("e - estadisticas")
    print("f - salir")


def procesar_opcion(opcion: str) -> bool:
    """
    Ejecuta la acción correspondiente a la opción seleccionada.
    """
    continuar = True

    match opcion:
        case "a":
            print("generacion y gestion de proyectos")
            input("Presiona Enter para continuar...")
        case "b":
            print("creacion y modificacion de tablas")
            input("Presiona Enter para continuar...")
        case "c":
            print("creacion, carga y modificacion de variables")
            input("Presiona Enter para continuar...")
        case "d":
            print("mostrar por pantalla informacion disponible en una tabla")
            input("Presiona Enter para continuar...")
        case "e":
            print("conteos o frecuencias")
            input("Presiona Enter para continuar...")
        case "f":
            print("Saliendo del programa...")
            continuar = False
        case _:
            print("Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar...")

    return continuar


def ejecutar_menu_principal(nombre_mostrar: str = "Danilo") -> None:
    """
    Ejecuta el ciclo principal del menú luego de un inicio de sesión exitoso.
    """
    print(f"Bienvenido, {nombre_mostrar}. Has ingresado correctamente.")
    continuar = True

    while continuar:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        continuar = procesar_opcion(opcion)


# ==========================================
# PARTE 2: Validaciones y Recursividad
# ==========================================

def validar_rango(numero: int, minimo: int, maximo: int) -> bool:
    """
    Verifica si un número se encuentra dentro de un rango inclusivo.
    """
    resultado = False
    if numero >= minimo and numero <= maximo:
        resultado = True
    return resultado


def es_par(numero: int) -> bool:
    """
    Verifica si un número entero es par.
    """
    resultado = False
    if numero % 2 == 0:
        resultado = True
    return resultado


def es_multiplo(numero: int, divisor: int) -> bool:
    """
    Verifica si un número es múltiplo de otro divisor distinto de cero.
    """
    resultado = False
    if divisor != 0 and numero % divisor == 0:
        resultado = True
    return resultado


def comprobar_primo(numero: int, divisor: int = 2) -> bool:
    """
    Busca divisores de un número de manera recursiva sin usar early return.
    """
    if divisor * divisor > numero:
        resultado = True
    elif numero % divisor == 0:
        resultado = False
    else:
        resultado = comprobar_primo(numero, divisor + 1)

    return resultado


def es_primo(numero: int) -> bool:
    """
    Verifica si un número entero es primo utilizando recursividad.
    """
    if numero < 2:
        resultado = False
    else:
        resultado = comprobar_primo(numero, 2)

    return resultado