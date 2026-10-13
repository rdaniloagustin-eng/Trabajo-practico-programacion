#parte 1
 
nombre_usuario_1 = "danilo"
contraseña_1 = "DDC"

acceso = True

nombre_usuario = input("Por favor, ingresa tu nombre: ")

if nombre_usuario != nombre_usuario_1:
    print("Nombre de usuario incorrecto. Acceso denegado.")
    acceso = False

if acceso:
    contador = 1
    contraseña = input("Por favor, ingresa tu contraseña: ")

    while contraseña != contraseña_1 and contador < 5:
        print("Contraseña incorrecta. Intenta nuevamente.")
        contraseña = input("Por favor, ingresa tu contraseña: ")
        contador += 1

    if contraseña != contraseña_1:
        print("Has excedido el número máximo de intentos. Acceso denegado.")
        acceso = False

if acceso:
    print("Bienvenido, Danilo. Has ingresado correctamente.")

    continuar = True

    while continuar:
        print("menu de opciones")
        print("a - proyectos")
        print("b - tablas")
        print("c - variables")
        print("d - mostrar")
        print("e - estadisticas")
        print("f - salir")

        opcion = input("Selecciona una opción: ")
        
        match opcion:
            case "a":
                print("generacion y gestion de proyectos")
                input ("Presiona Enter para continuar...")
            case "b":
                print("creacion y modificacion de tablas")
                input ("Presiona Enter para continuar...")
            case "c":
                print("creacion, carga y modificacion de variables")
                input ("Presiona Enter para continuar...")
            case "d":
                print("mostrar por pantalla informacion disponible en una tabla")
                input ("Presiona Enter para continuar...")
            case "e":
                print("conteos o frecuencias")
                input ("Presiona Enter para continuar...")
            case "f":
                print("Saliendo del programa...")
                continuar = False


#parte 2

def validar_rango(numero, minimo, maximo) -> bool:
    """Verifica si un número está dentro de un rango."""
    if numero >= minimo and numero <= maximo:
        return True
    else:
        return False


def es_par(numero) -> bool:
    """Verifica si un número es par."""
    if numero % 2 == 0:
        return True
    else:
        return False


def es_multiplo(numero, divisor) -> bool:
    """Verifica si un número es múltiplo de otro."""
    if divisor == 0:
        return False

    if numero % divisor == 0:
        return True
    else:
        return False


def es_primo(numero) -> bool:
    """Verifica si un número es primo."""
    if numero < 2:
        return False

    return comprobar_primo(numero, 2)


def comprobar_primo(numero, divisor) -> bool:
    """Busca divisores mediante recursividad."""
    if divisor * divisor > numero:
        return True

    if numero % divisor == 0:
        return False

    return comprobar_primo(numero, divisor + 1)