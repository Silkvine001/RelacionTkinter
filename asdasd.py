import tkinter
from tkinter import *
from tkinter import ttk

import sv_ttk

entry_a = 0
entry_b = 0
conjunto_a = 0
conjunto_b = 0
ListaSeleccion = 0
RelacionR = 0


def PropiedadesRel(RelacionR, Lista_a, Lista_b):
    for widget in frame2.winfo_children():
        widget.destroy()
    print("widgets eliminados \u2713")
    print(RelacionR)
    print(type(RelacionR))
    print(Lista_a)
    print(type(Lista_a))
    print(Lista_b)
    print(type(Lista_b))

    # Crea la matriz binaria vacía
    matriz_binaria_R = []
    matriz_binaria_R = [[0 for i in range(len(Lista_b))] for j in range(len(Lista_a))]

    # Completa la matriz binaria
    for i, elemento_a in enumerate(Lista_a):
        for j, elemento_b in enumerate(Lista_b):
            if (elemento_a, elemento_b) in RelacionR:
                matriz_binaria_R[i][j] = 1
            else:
                matriz_binaria_R[i][j] = 0

    # Imprime la matriz binaria
    print(f"La matriz binaria de la relación R es:")

    for i in range(len(Lista_b)):
        for j in range(len(Lista_a)):
            print(matriz_binaria_R[i][j])

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

    if Lista_a == Lista_b:
        if R_es_cuadrada:
            for i in range(len(matriz_binaria_R)):
                if matriz_binaria_R[i][i] != 1:
                    reflexividad_R = False
                    break
    else:
        reflexividad_R = False

    print(f"Reflexividad: {reflexividad_R}")

    if Lista_a == Lista_b:
        if R_es_cuadrada:
            for i in range(len(matriz_binaria_R)):
                if matriz_binaria_R[i][i] != 0:
                    irreflexivilidad_R = False
                    break
    else:
        irreflexivilidad_R = False

    print(f"Irreflexividad: {irreflexivilidad_R}")

    if Lista_a == Lista_b:
        if R_es_cuadrada:
            index = len(matriz_binaria_R) - 1
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

    if Lista_a == Lista_b:
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

    if Lista_a == Lista_b:
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


def GenerarArreglo(ListaSeleccion_f, titulo_relaciones):
    global RelacionR
    RelacionR = list(ListaSeleccion_f.get(0, "end"))

    for i in range(len(RelacionR)):
        temp = RelacionR[i]
        temp = temp[1:len(temp) - 1].split(", ")
        RelacionR[i] = (temp[0], temp[1])

    titulo_relaciones.config(text="R = " + str(RelacionR))
    print(RelacionR)

    LabelRelacion = ttk.Label(frame2, text="R = " + str(RelacionR))
    print("hola mundo")


def Enviaruno(ListaTuplas, ListaSeleccion_f):
    temp = list(ListaSeleccion_f.get(0, "end"))
    for i in range(len(ListaTuplas.curselection())):
        temp.append(ListaTuplas.get(ListaTuplas.curselection()[i]))
    temp.sort()
    ListaSeleccion_f.delete(0, "end")
    for i in range(len(temp)):
        ListaSeleccion_f.insert("end", temp[i])

    # Borramos los elementos de la lista previa
    for elements in reversed(ListaTuplas.curselection()):
        ListaTuplas.delete(elements)


def EnviarTodos(ListaTuplas, ListaSeleccion_f):
    if ListaSeleccion_f.size() == 0:
        for i in range(ListaTuplas.size()):
            ListaSeleccion_f.insert("end", ListaTuplas.get(i))
    else:

        temp = list(ListaSeleccion_f.get(0, "end"))
        for i in range(ListaTuplas.size()):
            temp.append(ListaTuplas.get(i))
        temp.sort()
        ListaSeleccion_f.delete(0, "end")
        for i in range(len(temp)):
            ListaSeleccion_f.insert("end", temp[i])

    # Borrar de la lista anterior
    ListaTuplas.delete(0, 'end')


# INSERION ELEMENTOS A LISTA
def relacionesLista(entry_a, entry_b, ListaTuplas):
    global Lista_a
    global Lista_b
    Lista_a = entry_a.get().split(",")
    Lista_b = entry_b.get().split(",")
    valor_a = entry_a.get()
    valor_b = entry_b.get()
    if not valor_a or not valor_b:
        Errorvacio = Toplevel()
        Errorvacio.geometry("380x160")
        Errorvacio.resizable(False, False)
        Errorvacio.transient(root)
        Errorvacio.grab_set_global()
        Errorvacio.focus_get()
        MsjError = ttk.Label(Errorvacio, text="El campo conjunto A o conjunto B estan vacios")
        MsjError.place(relx=0.5, rely=0.5, anchor="s")
        print("no pusiste nada pndj")
    else:
        conjunto_a = valor_a.split(",")
        conjunto_b = valor_b.split(",")
        print("el valor de a es", valor_a)
        print("el valor de b es", valor_b)

        print("el conjunto a es:", conjunto_a)
        print("el conjunto b es:", conjunto_b)
        ListaTuplas.delete(0, tkinter.END)

        # Rellenado de la listbox
        ListaTuplasLista = []
        for elemento_a in conjunto_a:
            for elemento_b in conjunto_b:
                ListaTuplasLista.append((elemento_a, elemento_b))
                ListaTuplas.insert("end", f"({elemento_a}, {elemento_b})")
        print(f"Las tuplas del conjunto A y B son:", ListaTuplasLista)


def click_boton():
    for widget in frame2.winfo_children():
        widget.destroy()
    print("widgets eliminados \u2713")


# VENTANA RELACIONES
def relaciones():
    # se remueve el texto de bienvenida
    for widget in frame2.winfo_children():
        widget.destroy()
    print("widgets anteriores eliminados")

    # caja de texto del conjunto a
    conjuntotitulo_a = ttk.LabelFrame(frame2, text="Conjunto A", style="Card.TFrame")
    conjuntotitulo_a.grid(padx=(10, 10), row=0, column=1)
    entry_a = ttk.Entry(conjuntotitulo_a)
    entry_a.grid(row=0, column=1, padx=10, pady=10)

    # caja de texto del conjunto b
    conjuntotitulo_b = ttk.LabelFrame(frame2, text="Conjunto B", style="Card.TFrame")
    conjuntotitulo_b.grid(padx=(10, 10), row=0, column=3)
    entry_b = ttk.Entry(conjuntotitulo_b)
    entry_b.grid(row=0, column=3, padx=10, pady=10)

    # recordatorio de que se debe separar con coma
    aviso_coma = tkinter.Label(frame2, text="*Separar con coma ( , )", fg="grey")
    aviso_coma.grid(row=0, column=2, padx=0, pady=(15, 0))

    # boton para subir la relacion
    boton_subir = ttk.Button(frame2, text="Enviar", style="Accent.TButton",
                             command=lambda: relacionesLista(entry_a, entry_b, ListaTuplas))
    boton_subir.grid(row=0, column=4, padx=(10, 0), pady=(15, 0))

    # Listbox Tuplas
    ListaTuplas = Listbox(frame2, selectmode="multiple")
    ListaTuplas.place(relx=0.22, rely=0.5, relwidth=0.40, relheight=0.65, anchor="center")
    # Scrollbar Tuplas
    scrolltuplas = ttk.Scrollbar(frame2, orient="vertical")
    ListaTuplas.config(yscrollcommand=scrolltuplas.set)
    scrolltuplas.config(command=ListaTuplas.yview)
    scrolltuplas.place(relx=0.44, rely=0.5, relheight=0.65, anchor="center")

    # Listbox relaciones
    ListaSeleccion_f = Listbox(frame2, width=40, height=18, selectmode="multiple")
    ListaSeleccion_f.place(relx=0.735, rely=0.5, relwidth=0.40, relheight=0.65, anchor="center")
    # Scrollbar relaciones
    scrollrelaciones = ttk.Scrollbar(frame2, orient="vertical")
    ListaSeleccion_f.config(yscrollcommand=scrollrelaciones.set)
    scrollrelaciones.config(command=ListaTuplas.yview)
    scrollrelaciones.place(relx=0.957, rely=0.5, relheight=0.65, anchor="center")

    # Titulos para cada frame

    # titulo tuplas
    titulo_tuplas_AXB = tkinter.Label(frame2, text="Tuplas de A x B", fg="white")
    titulo_tuplas_AXB.place(relx=0.215, rely=0.15, relheight=0.05, anchor="center")

    # titulo relaciones
    titulo_tuplas_AXB = tkinter.Label(frame2, text="Relacion R", fg="white")
    titulo_tuplas_AXB.place(relx=0.725, rely=0.15, relheight=0.05, anchor="center")

    # boton para enviar a la relacion
    Boton_enviar_uno = ttk.Button(frame2, text=">", style="Button.TButton",
                                  command=lambda: Enviaruno(ListaTuplas, ListaSeleccion_f))
    Boton_enviar_uno.place(relx=0.027, rely=0.85, relwidth=0.17)

    # boton para enviar todo
    Boton_enviar_todo = ttk.Button(frame2, text=">>", style="Button.TButton",
                                   command=lambda: EnviarTodos(ListaTuplas, ListaSeleccion_f))
    Boton_enviar_todo.place(relx=0.227, rely=0.85, relwidth=0.17)

    # boton para regresar de la relacion a la seleccion
    Boton_regresar_uno = ttk.Button(frame2, text="<", style="Button.TButton",
                                    command=lambda: Enviaruno(ListaSeleccion_f, ListaTuplas))
    Boton_regresar_uno.place(relx=0.547, rely=0.85, relwidth=0.17)

    # boton para regresar todo
    Boton_rergresar_todo = ttk.Button(frame2, text="<<", style="Button.TButton",
                                      command=lambda: EnviarTodos(ListaSeleccion_f, ListaTuplas))
    Boton_rergresar_todo.place(relx=0.747, rely=0.85, relwidth=0.17)

    # Boton para generar el arreglo y la matriz
    Boton_confirmar = ttk.Button(frame2, text="\u2713", style="Accent.TButton",
                                 command=lambda: GenerarArreglo(ListaSeleccion_f, titulo_relaciones))
    Boton_confirmar.place(relx=0.425, rely=0.85, relwidth=0.1)

    # Label para poner las relaciones abajo de los botones
    # label relaciones
    titulo_relaciones = tkinter.Label(frame2, text="R =", fg="white")
    titulo_relaciones.place(relx=0.475, rely=0.95, relheight=0.05, anchor="center")


# ventana principal
root = Tk()
root.title("Hecho por: Jonathan Salazar")
root.minsize(820, 650)
root.maxsize(1280, 720)
root.resizable(False, False)

root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# frame izquierdo que contiene los botones
frame1 = ttk.LabelFrame(root, text="Opciones", width=300, height=400, style="Card.TFrame")
frame1.grid(row=0, column=0, padx=20, pady=15, sticky="nsew")
# frame1.columnconfigure(0, weight=1)

# boton de crear relacion y propiedades, separados del resto
button = ttk.Button(frame1, text="Crear Relacion", style="Accent.TButton", command=relaciones)
button.grid(row=1, column=0, padx=10, pady=(85, 10), sticky="ew")
button = ttk.Button(frame1, text="Propiedades", style="Button.TButton",
                    command=lambda: PropiedadesRel(RelacionR, Lista_a, Lista_b))
button.grid(row=2, column=0, padx=10, pady=(10, 180), sticky="ew")

# label de texto para los otros botones
rep_lab = ttk.Label(frame1, text="Representaciones", anchor="center")
rep_lab.grid(row=3, column=0, padx=10, pady=10)

# el resto de los botones
button = ttk.Button(frame1, text="Matriz", style="Button.TButton", command=click_boton)
button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
button = ttk.Button(frame1, text="Sagital", style="Button.TButton", command=click_boton)
button.grid(row=5, column=0, padx=10, pady=10, sticky="ew")
button = ttk.Button(frame1, text="Grafo", style="Button.TButton", command=click_boton)
button.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

# segundo frame
frame2 = ttk.LabelFrame(root, text="Ventana Principal", padding=10)

frame2.grid(row=0, column=1, padx=20, pady=15, sticky="nsew")
label2 = ttk.Label(frame2, text="Bienvenido Usuario, seleccione una opcion para comenzar")
label2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# tema
sv_ttk.set_theme("dark")

# Fin
root.mainloop()
