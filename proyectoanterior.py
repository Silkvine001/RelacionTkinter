# defino conjunto A y B
map_a = ["a", "c"]
map_b = ["b", "d"]
map_r = ["r", "s"]


def crear_conjunto(conjunto):
    conjunto_a = []
    conjunto_b = []
    relacion_r = []
    while True:
        try:
            input_a = input(f"Ingrese la lista de terminos que desea incluir al conjunto {map_a[conjunto]}, separados por coma" "\n")
            if not input_a:
                raise ValueError("no ha ingresado ningun valor")
            conjunto_a = list(map(int, input_a.split(",")))
            break
        except ValueError as error:
            print(f"Error: {error}")

    print("\n")

    while True:
        try:
            input_b = input(f"Ingrese la lista de terminos que desea incluir al conjunto {map_b[conjunto]}, separados por coma" "\n")
            if not input_b:
                raise ValueError("no ha ingresado ningun valor")
            conjunto_b = list(map(int, input_b.split(",")))
            break
        except ValueError as error:
            print(f"Error: {error}")

    print("\n")

    print(f"el conjunto {map_a[conjunto]} es" "\n", conjunto_a, "\n")
    print(f"el conjunto {map_b[conjunto]} es" "\n", conjunto_b, "\n")

    R = []
    for elemento_a in conjunto_a:
        for elemento_b in conjunto_b:
            R.append((elemento_a, elemento_b))
    print(f"Las tuplas de {map_a[conjunto].upper()} y {map_b[conjunto].upper()} son:" "\n", R, "\n")

    for i in range(len(R)):
        print(f"la tupla de {map_r[conjunto].upper()} en la posicion", i, "es de")
        print(R[i])
        while True:
            eleccion = input(f"Desea incluir esta tupla en la relacion {map_r[conjunto].upper()}? (s/n)""\n")
            if eleccion.lower() == 's':
                relacion_r.append(R[i])
                print(f"Se ha añadido la tupla a la relación {map_r[conjunto].upper()}")
                break
            elif eleccion.lower() == 'n':
                print(f"La tupla no se ha añadido a la relacion {map_r[conjunto].upper()}")
                break
            else:
                print("caracter no valido")

    print("Se han añadido todas las tuplas seleccionadas""\n")
    print(f"La relacion {map_r[conjunto].upper()} esta conformada por:""\n", relacion_r)
    print(type(relacion_r))

    m_binaria = propiedades(conjunto_a, conjunto_b, relacion_r, conjunto)
    return m_binaria


def propiedades(conjunto_a, conjunto_b, relacion_r, conjunto):
    # Crea la matriz binaria vacía
    matriz_binaria_R = [[0 for i in range(len(conjunto_b))] for j in range(len(conjunto_a))]

    # Completa la matriz binaria
    for i, elemento_a in enumerate(conjunto_a):
        for j, elemento_b in enumerate(conjunto_b):
            if (elemento_a, elemento_b) in relacion_r:
                matriz_binaria_R[i][j] = 1
            else:
                matriz_binaria_R[i][j] = 0

    # Imprime la matriz binaria
    print(f"La matriz binaria de la relación {map_r[conjunto].upper()} es:")

    # Imprime la matriz binaria con plantilla ajustable
    print(map_r[conjunto].upper(), end=" | ") #imprime el encabezado R separado con un "|"
    for elemento_b in conjunto_b:
        print(elemento_b, end=" | ") #imprime los elementos de b como encabezado, usando "|" como separador
    print() #pasa a la siguiente linea sin dejar espacios

    for i, fila in enumerate(matriz_binaria_R):
        print(conjunto_a[i], end=" | ")
        for elemento in fila:
            print(elemento, end=" | ")
        print()

    print("Propiedades de la matriz:")

    R_es_cuadrada = True
    reflexividad_R = True
    irreflexivilidad_R = True
    transitividad_R = True
    simetria_R = True
    antisimetria_R = True

    if len(matriz_binaria_R) == len(matriz_binaria_R[0]):
        reflexividad_R = True
        R_es_cuadrada = True
    else:
        reflexividad_R = False
        R_es_cuadrada = False

    if conjunto_a == conjunto_b:
        if R_es_cuadrada:
            for i in range(len(matriz_binaria_R)):
                if matriz_binaria_R[i][i] != 1:
                    reflexividad_R = False
                    break
    else:
        reflexividad_R = False

    print(f"Reflexividad: {reflexividad_R}")

    if conjunto_a == conjunto_b:
        if R_es_cuadrada:
            for i in range(len(matriz_binaria_R)):
                if matriz_binaria_R[i][i] != 0:
                    irreflexivilidad_R = False
                    break
    else:
        irreflexivilidad_R = False

    print(f"Irreflexividad: {irreflexivilidad_R}")

    if conjunto_a == conjunto_b:
        if R_es_cuadrada:
            index = len(matriz_binaria_R)-1
            pos = True
            if matriz_binaria_R[1][1] == matriz_binaria_R[0][0]:
                pos = False

            if matriz_binaria_R[0][0] == matriz_binaria_R[index][index] and pos == False:
                transitividad_R = True 
            else:
                transitividad_R = False

    else:
        transitividad_R = False

    print(f"Transitividad: {transitividad_R}")


    if conjunto_a == conjunto_b:
        if R_es_cuadrada:

            rev = list(reversed(matriz_binaria_R))
            for i in range(len(rev)):
                rev[i] = list(reversed(rev[i]))
                
            if matriz_binaria_R != rev:
                simetria_R = False


    else:
        simetria_R = False

    print(f"Simetria: {simetria_R}")
    print(f"Asimetria: {not simetria_R}")

    if conjunto_a == conjunto_b:
        if R_es_cuadrada:
            last = matriz_binaria_R[0][0]
            for i in range(len(matriz_binaria_R)):
                
                if matriz_binaria_R[i][i] != last and last != 0:
                    antisimetria_R = False
                    break
                last = matriz_binaria_R[i][i]
    else:
        antisimetria_R = False

    print(f"Antisimetria: {antisimetria_R}""\n")
    return matriz_binaria_R
print("\n")

def union(rel_r, rel_s):
    matriz_binaria_T = [[0 for i in range(len(rel_s))] for j in range(len(rel_r))]

    for i in range(len(rel_r)):
        for j in range(len(rel_r)):
            if rel_s[i][j] | rel_r[i][j]:
                matriz_binaria_T[i][j] = 1
            else:
                matriz_binaria_T[i][j] = 0
    # Imprime la matriz binaria

    tuplas_union = []
    for i in range(len(matriz_binaria_T)):
        for j in range(len(matriz_binaria_T)):
            if matriz_binaria_T[i][j] == 1:
                tuplas_union.append((i+1, j+1))

    tuplas_union_sin_corchetes = str(tuplas_union).replace("[", "").replace("]", "")
    print("RUS = {", tuplas_union_sin_corchetes, "}")
    print("La matriz binaria de la union R y S es:")

    # Imprime la matriz binaria con plantilla ajustable
    print("RUS", end=" | ") #imprime el encabezado R separado con un "|"
    for i in range(len(rel_s)):
        print(i+1, end=" | ") #imprime los elementos de b como encabezado, usando "|" como separador
    print() #pasa a la siguiente linea sin dejar espacios

    for i, fila in enumerate(matriz_binaria_T):
        print(i+1, end="   | ")
        for elemento in fila:
            print(elemento, end=" | ")
        print()

def interseccion(rel_r, rel_s):
    matriz_binaria_T = [[0 for i in range(len(rel_s))] for j in range(len(rel_r))]

    for i in range(len(rel_r)):
        for j in range(len(rel_r)):
            if rel_s[i][j] & rel_r[i][j]:
                matriz_binaria_T[i][j] = 1
            else:
                matriz_binaria_T[i][j] = 0

    tuplas_interseccion = []
    for i in range(len(matriz_binaria_T)):
        for j in range(len(matriz_binaria_T)):
            if matriz_binaria_T[i][j] == 1:
                tuplas_interseccion.append((i+1, j+1))

    tuplas_interseccion_sin_corchetes = str(tuplas_interseccion).replace("[", "").replace("]", "")
    print("RnS = {", tuplas_interseccion_sin_corchetes, "}")

    # Imprime la matriz binaria
    print("La matriz binaria de la interseccion R y S es:")

    # Imprime la matriz binaria con plantilla ajustable
    print("RnS", end=" | ") #imprime el encabezado R separado con un "|"
    for i in range(len(rel_s)):
        print(i+1, end=" | ") #imprime los elementos de b como encabezado, usando "|" como separador
    print() #pasa a la siguiente linea sin dejar espacios

    for i, fila in enumerate(matriz_binaria_T):
        print(i+1, end="   | ")
        for elemento in fila:
            print(elemento, end=" | ")
        print()

def diferencia(rel_r, rel_s):
    matriz_binaria_T = [[0 for i in range(len(rel_s))] for j in range(len(rel_r))]

    for i in range(len(rel_r)):
        for j in range(len(rel_r)):
            if rel_r[i][j] - rel_s[i][j] <= 0:
                matriz_binaria_T[i][j] = 0
            else:
                matriz_binaria_T[i][j] = 1

    tuplas_dif = []
    for i in range(len(matriz_binaria_T)):
        for j in range(len(matriz_binaria_T)):
            if matriz_binaria_T[i][j] == 1:
                tuplas_dif.append((i+1, j+1))

    tuplas_dif_sc = str(tuplas_dif).replace("[", "").replace("]", "")
    print("R-S = {", tuplas_dif_sc, "}")

    # Imprime la matriz binaria
    print("La matriz binaria de la diferencia R y S es:")

    # Imprime la matriz binaria con plantilla ajustable
    print("R-S", end=" | ") #imprime el encabezado R separado con un "|"
    for i in range(len(rel_s)):
        print(i+1, end=" | ") #imprime los elementos de b como encabezado, usando "|" como separador
    print() #pasa a la siguiente linea sin dejar espacios

    for i, fila in enumerate(matriz_binaria_T):
        print(i+1, end="   | ")
        for elemento in fila:
            print(elemento, end=" | ")
        print()

def dif_simetri(rel_r, rel_s):
    matriz_binaria_T = [[0 for i in range(len(rel_s))] for j in range(len(rel_r))]

    for i in range(len(rel_r)):
        for j in range(len(rel_r)):
            
            if rel_r[i][j] ^ rel_s[i][j]:
                matriz_binaria_T[i][j] = 1
            else:
                matriz_binaria_T[i][j] = 0

    tuplas_dif_s = []
    for i in range(len(matriz_binaria_T)):
        for j in range(len(matriz_binaria_T)):
            if matriz_binaria_T[i][j] == 1:
                tuplas_dif_s.append((i+1, j+1))

    tuplas_dif_s_sc = str(tuplas_dif_s).replace("[", "").replace("]", "")
    print("R^S = {", tuplas_dif_s_sc, "}")

    # Imprime la matriz binaria
    print("La matriz binaria de la diferencia simetrica de R y S es:")

    # Imprime la matriz binaria con plantilla ajustable
    print("R^S", end=" | ") #imprime el encabezado R separado con un "|"
    for i in range(len(rel_s)):
        print(i+1, end=" | ") #imprime los elementos de b como encabezado, usando "|" como separador
    print() #pasa a la siguiente linea sin dejar espacios

    for i, fila in enumerate(matriz_binaria_T):
        print(i+1, end="   | ")
        for elemento in fila:
            print(elemento, end=" | ")
        print()

def complemento(rel_r, rel_s):
    matriz_binaria_T = [[0 for i in range(len(rel_s))] for j in range(len(rel_r))]

    for i in range(len(rel_r)):
        for j in range(len(rel_r)):
            
            if rel_r[i][j] == 1:
                matriz_binaria_T[i][j] = 0
            else:
                matriz_binaria_T[i][j] = 1

    tuplas_comp = []
    for i in range(len(matriz_binaria_T)):
        for j in range(len(matriz_binaria_T)):
            if matriz_binaria_T[i][j] == 1:
                tuplas_comp.append((i+1, j+1))

    tuplas_comp_sc = str(tuplas_comp).replace("[", "").replace("]", "")
    print("~R = {", tuplas_comp_sc, "}")

    # Imprime la matriz binaria
    print("La matriz binaria del complemento de R es:")

    # Imprime la matriz binaria con plantilla ajustable
    print("~R", end=" | ") #imprime el encabezado R separado con un "|"
    for i in range(len(rel_s)):
        print(i+1, end=" | ") #imprime los elementos de b como encabezado, usando "|" como separador
    print() #pasa a la siguiente linea sin dejar espacios

    for i, fila in enumerate(matriz_binaria_T):
        print(i+1, end="  | ")
        for elemento in fila:
            print(elemento, end=" | ")
        print()

def inversa(rel_r, rel_s):
    matriz_binaria_T = [[0 for i in range(len(rel_s))] for j in range(len(rel_r))]
           
    rev = list(reversed(rel_r))
    for i in range(len(rev)):
        rev[i] = list(reversed(rev[i]))
        matriz_binaria_T = rev

    tuplas_inv = []
    for i in range(len(matriz_binaria_T)):
        for j in range(len(matriz_binaria_T)):
            if matriz_binaria_T[i][j] == 1:
                tuplas_inv.append((i+1, j+1))

    tuplas_inv_sc = str(tuplas_inv).replace("[", "").replace("]", "")
    print("~R = {", tuplas_inv_sc, "}")

    # Imprime la matriz binaria
    print("La matriz binaria de la inversa de R es:")

    # Imprime la matriz binaria con plantilla ajustable
    print("R-1", end=" | ") #imprime el encabezado R separado con un "|"
    for i in range(len(rel_s)):
        print(i+1, end=" | ") #imprime los elementos de b como encabezado, usando "|" como separador
    print() #pasa a la siguiente linea sin dejar espacios

    for i, fila in enumerate(matriz_binaria_T):
        print(i+1, end="   | ")
        for elemento in fila:
            print(elemento, end=" | ")
        print()

def composicion(rel_r, rel_s):
    matriz_binaria_T = [[0 for i in range(len(rel_s))] for j in range(len(rel_r))]
    R = []
    for i in range(len(rel_r)):
        for j in range(len(rel_s)):
            last = 0
            for k in range(len(rel_s)):
                if k == len(rel_s)-1:
                    R.append((rel_r[i][k] * rel_s[k][j]) + last)
                last = rel_r[i][k] * rel_s[k][j] + last

    num=0

    for i in range(len(rel_r)):
        for j in range(len(rel_r)):

            if R[num] >= 1:
                matriz_binaria_T[i][j] = 1
            else:
                matriz_binaria_T[i][j] = 0
            num+=1

    tuplas_compos = []
    for i in range(len(matriz_binaria_T)):
        for j in range(len(matriz_binaria_T)):
            if matriz_binaria_T[i][j] == 1:
                tuplas_compos.append((i+1, j+1))

    tuplas_compos_sc = str(tuplas_compos).replace("[", "").replace("]", "")
    print("R*S = {", tuplas_compos_sc, "}")

    # Imprime la matriz binaria
    print("La matriz binaria de la composicion de R y S es:")

    # Imprime la matriz binaria con plantilla ajustable
    print("R*S", end=" | ") #imprime el encabezado R separado con un "|"
    for i in range(len(rel_s)):
        print(i+1, end=" | ") #imprime los elementos de b como encabezado, usando "|" como separador
    print() #pasa a la siguiente linea sin dejar espacios

    for i, fila in enumerate(matriz_binaria_T):
        print(i+1, end="   | ")
        for elemento in fila:
            print(elemento, end=" | ")
        print()



relacion_r = crear_conjunto(0)
relacion_s = crear_conjunto(1)

union(relacion_r, relacion_s)
interseccion(relacion_r, relacion_s)
diferencia(relacion_r, relacion_s)
dif_simetri(relacion_r, relacion_s)
complemento(relacion_r, relacion_s)
inversa(relacion_r, relacion_s)
composicion(relacion_r, relacion_s)