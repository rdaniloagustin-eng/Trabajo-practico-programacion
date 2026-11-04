"""Módulo para la creación, carga, modificación y visualización de tablas (matrices)."""


# ==========================================
# Validaciones algorítmicas de consola (sin métodos de str)
# ==========================================

def es_cadena_entero(cadena: str) -> bool:
    """
    Verifica algorítmicamente con ASCII si una cadena representa un número entero.
    """
    es_valido = False
    largo = len(cadena)

    if largo > 0:
        es_valido = True
        inicio = 0

        if cadena[0] == "-":
            if largo > 1:
                inicio = 1
            else:
                es_valido = False

        for i in range(inicio, largo):
            if cadena[i] < "0" or cadena[i] > "9":
                es_valido = False

    return es_valido


def pedir_entero(mensaje: str) -> int:
    """
    Solicita un número entero por consola validando que no rompa ante letras.
    """
    entrada = input(mensaje)
    while not es_cadena_entero(entrada):
        print("Error: Debe ingresar un número entero válido (sin letras ni símbolos).")
        entrada = input(mensaje)

    numero = int(entrada)
    return numero


def validar_rango(numero: int, minimo: int, maximo: int) -> bool:
    """
    Verifica si un número se encuentra dentro de un rango inclusivo (Parte 2).
    """
    resultado = False
    if numero >= minimo and numero <= maximo:
        resultado = True
    return resultado


def pedir_entero_rango(mensaje: str, minimo: int, maximo: int) -> int:
    """
    Solicita un número entero reutilizando validar_rango (principio DRY).
    """
    numero = pedir_entero(mensaje)
    while not validar_rango(numero, minimo, maximo):
        print(f"Error: El número debe estar entre {minimo} y {maximo}.")
        numero = pedir_entero(mensaje)

    return numero


def pedir_texto_no_vacio(mensaje: str) -> str:
    """
    Solicita un texto por consola validando que no esté vacío.
    """
    texto = input(mensaje)
    while len(texto) == 0:
        print("Error: El campo no puede quedar vacío.")
        texto = input(mensaje)

    return texto


# ==========================================
# Funciones de Matrices (según diapositivas de clase)
# ==========================================

def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    """
    Crea e inicializa una matriz con un valor por defecto (según clase de Matrices).
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz


def obtener_tabla_ejemplo() -> list:
    """
    Devuelve la tabla de ejemplo del PDF del TP (Nombre, Apellido, Materia, Notas).
    """
    encabezados = ["Nombre", "Apellido", "Materia", "Nota PP", "Nota SP", "Nota final"]
    tipos = ["str", "str", "str", "int", "int", "int"]
    matriz = [
        ["Juan", "Pérez", "Matemática", 4, 6, 4],
        ["Celeste", "Rodríguez", "Inglés 1", 6, 7, 7],
        ["Pedro", "Suarez", "Programación", 4, 4, 4]
    ]
    paquete_tabla = [encabezados, tipos, matriz]
    return paquete_tabla


def pedir_dato_segun_tipo(nombre_col: str, tipo_col: str, fila_idx: int) -> any:
    """
    Pide un dato validando su tipo ('int' o 'str') según la configuración de la columna.
    """
    if tipo_col == "int":
        dato = pedir_entero(f"  Fila {fila_idx} - Ingrese '{nombre_col}' (entero): ")
    else:
        dato = pedir_texto_no_vacio(f"  Fila {fila_idx} - Ingrese '{nombre_col}' (texto): ")
    return dato


def cargar_matriz_secuencialmente(matriz: list, encabezados: list, tipos: list) -> None:
    """
    Carga todos los elementos de la matriz en orden desde la primera celda hasta la última.
    """
    print("\n--- Iniciando Carga Secuencial de la Tabla ---")
    for i in range(len(matriz)):
        print(f"\nCargando registro de la Fila {i}:")
        for j in range(len(matriz[i])):
            matriz[i][j] = pedir_dato_segun_tipo(encabezados[j], tipos[j], i)
    print("\nCarga secuencial finalizada con éxito.")


def cargar_matriz_aleatoriamente(matriz: list, encabezados: list, tipos: list) -> None:
    """
    Carga o modifica celdas específicas indicando índice de fila y columna (Carga Distribuida).
    """
    print("\n--- Iniciando Carga Distribuida / Aleatoria ---")
    total_filas = len(matriz)
    total_cols = len(encabezados)
    seguir = "S"

    while seguir == "S" or seguir == "s":
        fila = pedir_entero_rango(f"Índice de fila (0 a {total_filas - 1}): ", 0, total_filas - 1)
        columna = pedir_entero_rango(f"Índice de columna (0 a {total_cols - 1}): ", 0, total_cols - 1)
        matriz[fila][columna] = pedir_dato_segun_tipo(encabezados[columna], tipos[columna], fila)
        seguir = pedir_texto_no_vacio("¿Desea seguir cargando otra celda? (S/N): ")


# ==========================================
# Puntos B, C y D del Menú
# ==========================================

def menu_punto_b_crear_tabla() -> list:
    """
    Ejecuta el Punto B: Creación y carga secuencial o distribuida de una tabla.
    """
    print("\n==========================================")
    print("PUNTO B: Creación y Carga de Tablas")
    print("==========================================")
    print("1 - Crear una tabla nueva desde cero (definir filas, columnas y nombres)")
    print("2 - Cargar la tabla de ejemplo del TP (Alumnos y Notas)")
    modo = pedir_entero_rango("Seleccione una opción (1 o 2): ", 1, 2)

    if modo == 2:
        paquete_tabla = obtener_tabla_ejemplo()
        print("Se cargó correctamente la tabla de ejemplo de Alumnos.")
    else:
        cant_filas = pedir_entero_rango("Ingrese la cantidad de filas (1 a 50): ", 1, 50)
        cant_cols = pedir_entero_rango("Ingrese la cantidad de columnas (1 a 15): ", 1, 15)

        encabezados = [""] * cant_cols
        tipos = ["str"] * cant_cols

        print("\n--- Definición de nombres y tipos de cada columna ---")
        for j in range(cant_cols):
            encabezados[j] = pedir_texto_no_vacio(f"Nombre de la columna {j}: ")
            print(f"Tipo de dato para '{encabezados[j]}': 1 = Texto (str) | 2 = Número Entero (int)")
            tipo_num = pedir_entero_rango("Elija tipo (1 o 2): ", 1, 2)
            if tipo_num == 2:
                tipos[j] = "int"
            else:
                tipos[j] = "str"

        matriz = inicializar_matriz(cant_filas, cant_cols, "-")

        print("\n¿Cómo desea cargar los datos de la tabla?")
        print("1 - Carga Secuencial (todas las filas y columnas en orden)")
        print("2 - Carga Distribuida / Aleatoria (eligiendo fila y columna)")
        tipo_carga = pedir_entero_rango("Seleccione el método de carga (1 o 2): ", 1, 2)

        if tipo_carga == 1:
            cargar_matriz_secuencialmente(matriz, encabezados, tipos)
        else:
            cargar_matriz_aleatoriamente(matriz, encabezados, tipos)

        paquete_tabla = [encabezados, tipos, matriz]

    return paquete_tabla


def menu_punto_c_modificar(encabezados: list, tipos: list, matriz: list) -> None:
    """
    Ejecuta el Punto C: Modificar filas, columnas o tipos de variables de la tabla.
    """
    print("\n==========================================")
    print("PUNTO C: Modificación de Filas, Columnas y Variables")
    print("==========================================")
    print("1 - Modificar una fila completa (Carga Secuencial de fila)")
    print("2 - Modificar una columna completa (Carga Secuencial de columna)")
    print("3 - Modificar celdas puntuales por coordenada (Carga Distribuida)")
    print("4 - Modificar el nombre o el tipo de dato de una columna (Variable)")
    opcion = pedir_entero_rango("Seleccione qué desea modificar (1 a 4): ", 1, 4)

    total_filas = len(matriz)
    total_cols = len(encabezados)

    if opcion == 1:
        fila_idx = pedir_entero_rango(f"Ingrese el número de fila a modificar (0 a {total_filas - 1}): ", 0, total_filas - 1)
        for j in range(total_cols):
            matriz[fila_idx][j] = pedir_dato_segun_tipo(encabezados[j], tipos[j], fila_idx)
        print(f"Fila {fila_idx} actualizada correctamente.")
    elif opcion == 2:
        for j in range(total_cols):
            print(f"  {j} -> {encabezados[j]} ({tipos[j]})")
        col_idx = pedir_entero_rango(f"Ingrese el número de columna a modificar (0 a {total_cols - 1}): ", 0, total_cols - 1)
        for i in range(total_filas):
            matriz[i][col_idx] = pedir_dato_segun_tipo(encabezados[col_idx], tipos[col_idx], i)
        print(f"Columna '{encabezados[col_idx]}' actualizada correctamente.")
    elif opcion == 3:
        cargar_matriz_aleatoriamente(matriz, encabezados, tipos)
    else:
        for j in range(total_cols):
            print(f"  {j} -> {encabezados[j]} (Tipo actual: {tipos[j]})")
        col_idx = pedir_entero_rango(f"Ingrese la columna a reconfigurar (0 a {total_cols - 1}): ", 0, total_cols - 1)
        encabezados[col_idx] = pedir_texto_no_vacio("Nuevo nombre para la columna: ")
        print("Seleccione el nuevo tipo de variable: 1 = Texto (str) | 2 = Entero (int)")
        nuevo_tipo = pedir_entero_rango("Opción (1 o 2): ", 1, 2)
        if nuevo_tipo == 2:
            tipos[col_idx] = "int"
        else:
            tipos[col_idx] = "str"
        print("Reconfiguración completada. Cargue los nuevos valores de esa columna:")
        for i in range(total_filas):
            matriz[i][col_idx] = pedir_dato_segun_tipo(encabezados[col_idx], tipos[col_idx], i)


def rellenar_espacios(texto: str, ancho: int = 14) -> str:
    """
    Alinea un texto agregando espacios a la derecha hasta alcanzar el ancho fijo.
    """
    cadena = str(texto)
    largo = len(cadena)
    resultado = cadena

    if largo < ancho:
        espacios_faltantes = ancho - largo
        resultado = cadena + (" " * espacios_faltantes)
    elif largo > ancho:
        resultado = cadena[0:ancho]

    return resultado


def imprimir_tabla_formateada(encabezados: list, matriz: list, indices_cols: list) -> None:
    """
    Imprime por consola la tabla prolija con bordes al estilo del ejemplo del PDF.
    """
    ancho_col = 14
    separador = "-" * (len(indices_cols) * (ancho_col + 3) + 1)

    print(separador)
    linea_encabezado = "| "
    for k in range(len(indices_cols)):
        col_idx = indices_cols[k]
        linea_encabezado += rellenar_espacios(encabezados[col_idx], ancho_col) + " | "
    print(linea_encabezado)
    print(separador)

    for i in range(len(matriz)):
        linea_fila = "| "
        for k in range(len(indices_cols)):
            col_idx = indices_cols[k]
            linea_fila += rellenar_espacios(str(matriz[i][col_idx]), ancho_col) + " | "
        print(linea_fila)
    print(separador)


def menu_punto_d_mostrar(encabezados: list, matriz: list) -> None:
    """
    Ejecuta el Punto D: Mostrar tabla completa, una fila, una columna o filtrar datos.
    """
    print("\n==========================================")
    print("PUNTO D: Visualización y Filtrado de Tabla")
    print("==========================================")
    print("1 - Mostrar la tabla completa")
    print("2 - Mostrar una fila específica")
    print("3 - Mostrar una sola columna o selección de columnas")
    print("4 - Filtrar filas buscando un valor en una columna")
    opcion = pedir_entero_rango("Seleccione una opción (1 a 4): ", 1, 4)

    total_filas = len(matriz)
    total_cols = len(encabezados)

    todas_las_cols = [0] * total_cols
    for j in range(total_cols):
        todas_las_cols[j] = j

    if opcion == 1:
        imprimir_tabla_formateada(encabezados, matriz, todas_las_cols)
    elif opcion == 2:
        fila_idx = pedir_entero_rango(f"Ingrese el número de fila a mostrar (0 a {total_filas - 1}): ", 0, total_filas - 1)
        sub_matriz = [matriz[fila_idx]]
        imprimir_tabla_formateada(encabezados, sub_matriz, todas_las_cols)
    elif opcion == 3:
        print("Columnas disponibles:")
        for j in range(total_cols):
            print(f"  {j} -> {encabezados[j]}")
        cant_ver = pedir_entero_rango(f"¿Cuántas columnas desea visualizar? (1 a {total_cols}): ", 1, total_cols)
        cols_elegidas = [0] * cant_ver
        for k in range(cant_ver):
            cols_elegidas[k] = pedir_entero_rango(f"Ingrese el índice de la {k + 1}° columna a mostrar: ", 0, total_cols - 1)
        imprimir_tabla_formateada(encabezados, matriz, cols_elegidas)
    else:
        print("Columnas disponibles para filtrar:")
        for j in range(total_cols):
            print(f"  {j} -> {encabezados[j]}")
        col_filtro = pedir_entero_rango(f"Elija el índice de columna por la cual filtrar (0 a {total_cols - 1}): ", 0, total_cols - 1)
        valor_buscado = pedir_texto_no_vacio(f"Ingrese el valor exacto a buscar en '{encabezados[col_filtro]}': ")

        filas_filtradas = []
        for i in range(total_filas):
            if str(matriz[i][col_filtro]) == valor_buscado:
                filas_filtradas += [matriz[i]]

        if len(filas_filtradas) > 0:
            print(f"\nSe encontraron {len(filas_filtradas)} coincidencia(s):")
            imprimir_tabla_formateada(encabezados, filas_filtradas, todas_las_cols)
        else:
            print(f"\nNo se encontró ninguna fila donde '{encabezados[col_filtro]}' sea igual a '{valor_buscado}'.")