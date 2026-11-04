"""Módulo de cálculos estadísticos para el Punto E del Trabajo Práctico."""

from tablas import pedir_entero, pedir_entero_rango


def extraer_columna_numerica(matriz: list, col_idx: int) -> list:
    """
    Extrae los valores numéricos de una columna de la matriz en un vector.
    """
    valores = [0] * len(matriz)
    for i in range(len(matriz)):
        valores[i] = int(matriz[i][col_idx])
    return valores


def ordenar_burbuja(lista_original: list) -> list:
    """
    Ordena una copia de la lista de menor a mayor usando Bubble Sort (visto en clase).
    """
    n = len(lista_original)
    lista = [0] * n
    for i in range(n):
        lista[i] = lista_original[i]

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

    return lista


def calcular_maximo(valores: list) -> int:
    """
    Obtiene el valor máximo de una lista de forma algorítmica sin usar max().
    """
    maximo = valores[0]
    for i in range(1, len(valores)):
        if valores[i] > maximo:
            maximo = valores[i]
    return maximo


def calcular_minimo(valores: list) -> int:
    """
    Obtiene el valor mínimo de una lista de forma algorítmica sin usar min().
    """
    minimo = valores[0]
    for i in range(1, len(valores)):
        if valores[i] < minimo:
            minimo = valores[i]
    return minimo


def calcular_suma(valores: list) -> float:
    """
    Suma todos los elementos de una lista mediante un acumulador sin usar sum().
    """
    acumulador = 0
    for i in range(len(valores)):
        acumulador += valores[i]
    return acumulador


def calcular_promedio_aritmetico(valores: list) -> float:
    """
    Calcula la media aritmética (suma total dividida por cantidad de elementos).
    """
    promedio = 0.0
    if len(valores) > 0:
        promedio = calcular_suma(valores) / len(valores)
    return promedio


def calcular_promedio_geometrico(valores: list) -> float:
    """
    Calcula la media geométrica (raíz n-ésima del producto de todos los valores).
    """
    promedio_geo = 0.0
    n = len(valores)

    if n > 0:
        producto = 1.0
        todos_positivos = True
        for i in range(n):
            if valores[i] <= 0:
                todos_positivos = False
            else:
                producto *= valores[i]

        if todos_positivos:
            promedio_geo = producto ** (1.0 / n)

    return promedio_geo


def calcular_varianza(valores: list) -> float:
    """
    Calcula la varianza poblacional como medida de dispersión.
    """
    varianza = 0.0
    n = len(valores)

    if n > 0:
        media = calcular_promedio_aritmetico(valores)
        suma_cuadrados = 0.0
        for i in range(n):
            diferencia = valores[i] - media
            suma_cuadrados += diferencia ** 2
        varianza = suma_cuadrados / n

    return varianza


def calcular_mediana(valores: list) -> float:
    """
    Calcula la mediana (medida de posición central) ordenando previamente los datos.
    """
    ordenados = ordenar_burbuja(valores)
    n = len(ordenados)
    mitad = n // 2

    if n % 2 == 1:
        mediana = float(ordenados[mitad])
    else:
        mediana = (ordenados[mitad - 1] + ordenados[mitad]) / 2.0

    return mediana


def mostrar_frecuencias(valores: list) -> None:
    """
    Calcula y muestra la frecuencia absoluta y porcentual de cada valor único.
    """
    unicos = []
    total = len(valores)

    for i in range(total):
        ya_existe = False
        for k in range(len(unicos)):
            if valores[i] == unicos[k]:
                ya_existe = True
        if not ya_existe:
            unicos += [valores[i]]

    unicos_ordenados = ordenar_burbuja(unicos)

    print("\n--- Tabla de Conteos y Frecuencias ---")
    for k in range(len(unicos_ordenados)):
        valor_actual = unicos_ordenados[k]
        contador = 0
        for i in range(total):
            if valores[i] == valor_actual:
                contador += 1
        porcentaje = (contador * 100.0) / total
        print(f"  Valor {valor_actual}: aparece {contador} vez/veces ({porcentaje}% del total)")


def menu_punto_e_estadisticas(
    encabezados: list,
    tipos: list,
    matriz: list,
    fn_es_par: any,
    fn_es_primo: any,
    fn_es_multiplo: any
) -> None:
    """
    Ejecuta el submenú del Punto E sobre una columna numérica de la tabla.
    """
    cols_numericas = []
    for j in range(len(tipos)):
        if tipos[j] == "int":
            cols_numericas += [j]

    if len(cols_numericas) == 0:
        print("\nError: La tabla actual no tiene columnas numéricas ('int') para calcular estadísticas.")
        print("Use la opción C para configurar al menos una columna como entera ('int').")
    else:
        print("\n==========================================")
        print("PUNTO E: Módulo de Estadísticas")
        print("==========================================")
        print("Columnas numéricas disponibles:")
        for k in range(len(cols_numericas)):
            idx = cols_numericas[k]
            print(f"  {k + 1} -> {encabezados[idx]} (Columna {idx})")

        eleccion = pedir_entero_rango(f"Seleccione la columna a analizar (1 a {len(cols_numericas)}): ", 1, len(cols_numericas))
        col_elegida = cols_numericas[eleccion - 1]
        nombre_col = encabezados[col_elegida]
        valores = extraer_columna_numerica(matriz, col_elegida)

        print(f"\n¿Qué cálculo desea realizar sobre '{nombre_col}' ({valores})?")
        print("1 - Conteos y frecuencias")
        print("2 - Máximo y mínimo")
        print("3 - Medidas de tendencia central (Promedio aritmético y geométrico)")
        print("4 - Medidas de dispersión (Rango, Varianza y Desvío estándar)")
        print("5 - Medidas de posición (Mediana y lista ordenada)")
        print("6 - Analizar pares, números primos (recursivo) y múltiplos (Parte 2)")
        sub_op = pedir_entero_rango("Seleccione una opción (1 a 6): ", 1, 6)

        if sub_op == 1:
            mostrar_frecuencias(valores)
        elif sub_op == 2:
            max_val = calcular_maximo(valores)
            min_val = calcular_minimo(valores)
            print(f"\nResultados para '{nombre_col}':")
            print(f"  - Valor Máximo: {max_val}")
            print(f"  - Valor Mínimo: {min_val}")
        elif sub_op == 3:
            prom_arit = calcular_promedio_aritmetico(valores)
            prom_geo = calcular_promedio_geometrico(valores)
            print(f"\nMedidas de tendencia central para '{nombre_col}':")
            print(f"  - Promedio Aritmético: {prom_arit}")
            print(f"  - Promedio Geométrico: {prom_geo}")
        elif sub_op == 4:
            rango_datos = calcular_maximo(valores) - calcular_minimo(valores)
            varianza = calcular_varianza(valores)
            desvio = varianza ** 0.5
            print(f"\nMedidas de dispersión para '{nombre_col}':")
            print(f"  - Rango (Máx - Mín): {rango_datos}")
            print(f"  - Varianza: {varianza}")
            print(f"  - Desvío Estándar: {desvio}")
        elif sub_op == 5:
            ordenados = ordenar_burbuja(valores)
            mediana = calcular_mediana(valores)
            print(f"\nMedidas de posición para '{nombre_col}':")
            print(f"  - Datos ordenados de menor a mayor: {ordenados}")
            print(f"  - Mediana (Posición central): {mediana}")
        else:
            divisor_usuario = pedir_entero("Ingrese un divisor para comprobar múltiplos: ")
            pares = []
            primos = []
            multiplos = []
            for i in range(len(valores)):
                num = valores[i]
                if fn_es_par(num):
                    pares += [num]
                if fn_es_primo(num):
                    primos += [num]
                if fn_es_multiplo(num, divisor_usuario):
                    multiplos += [num]
            print(f"\nPropiedades numéricas de '{nombre_col}':")
            print(f"  - Números pares encontrados: {pares}")
            print(f"  - Números primos encontrados (recursivo): {primos}")
            print(f"  - Múltiplos de {divisor_usuario} encontrados: {multiplos}")