import sys
from App import logic
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Map import map_separate_chaining as sc
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from tabulate import tabulate

def new_logic():
    """
        Se crea una instancia del controlador
    """
    return logic.new_logic()

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    filename = input("ingrese el nombre del archivo en formato csv (incluya el .csv): ")
    res = logic.load_data(control,filename)
    print(f"El tiempo de ejecucion fue: {res["tiempo"]} ms")
    print(f"El total de registros cargados fue: {res["total"]}")
    print(f"El menor año de recoleccion fue: {res["menor"]}")
    print(f"El mayor año de recoleccion fue: {res["mayor"]}")
    lista_menores = sc.get(res["catalog"]["año de carga"], res["menor_carga"])
    lista_menores_2 = sc.get(res["catalog"]["año de carga"], res["menor_carga"]+1)
    lista_mayores = sc.get(res["catalog"]["año de carga"], res["mayor_carga"])
    lista_ultimos = []
    lista_primeros = []
    for i in range(3):
        lista_ultimos.append(al.get_element(lista_menores,i))
    h = al.size(lista_menores_2)-2
    for p in range(2):
        lista_ultimos.append(al.get_element(lista_menores_2,h))
        h +=1
    k = 4
    for j in range(5):
        lista_primeros.append(al.get_element(lista_mayores,k))
        k -= 1
    print("primeros 5 cargados: ")
    print(tabulate(lista_ultimos, headers="keys", tablefmt="fancy_grid"))
    print("\nultimos 5 cargados: ")
    print(print(tabulate(lista_primeros, headers="keys", tablefmt="fancy_grid")))
    return res["catalog"]
       


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    año = int(input("ingrese el año a filtrar: "))
    res = logic.req_1(control,año)
    if res == None:
        print("No se encontraron registros")
    else:
        print(f"El tiempo de ejecucion fue: {res["tiempo"]} ms")
        print(f"El total de registros que pasaron el filtro fue: {res["total"]}")
        print(f"El registro encontrado fue: ")
        print(tabulate([res["registro"]], headers="keys", tablefmt="fancy_grid"))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    departamento = input("ingrese el departamento a filtrar: ").upper()
    n = int(input("Ingrese la cantidad de registros que desea obtener: "))
    res = logic.req_2(control,departamento, n)
    if res == None:
        print("No se encontraron registros")
    else:
        print(f"El tiempo de ejecucion fue: {res["tiempo"]} ms")
        print(f"El total de registros que pasaron el filtro fue: {res["total"]}")
        print(tabulate(res["registros"]["elements"], headers="keys", tablefmt="fancy_grid"))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    departamento = input("ingrese el departamento a filtrar: ").upper()
    año_inicial = int(input("ingrese el año inicial del rango: "))
    año_final = int(input("ingrese el año final del rango: "))
    if año_final < año_inicial:
        aux = año_inicial
        año_inicial = año_final
        año_final = aux
    res = logic.req_3(control,departamento, año_inicial, año_final)
    if res == None:
        print("No se encontraron registros")
    else:
        print(f"El tiempo de ejecucion fue: {res["tiempo"]} ms")
        print(f"El total de registros que pasaron el filtro fue: {res["size"]}")
        print(f"La cantidad de registros con SURVEY fue: {res["survey"]}")
        print(f"La cantidad de registrso con CENSUS fue: {res["census"]}")
        if res["size"] > 20:
            lista_primeros =[]
            lista_ultimos = []
            j = res["size"] -1
            for i in range(5):
                lista_primeros.append(al.get_element(res["registros"],i))
                lista_ultimos.append(al.get_element(res["registros"],j))
                j -= 1
            print("los 5 primeros son: ")
            print(tabulate(lista_primeros, headers="keys", tablefmt="fancy_grid"))
            print("\nlos 5 ultimos son: ")
            print(tabulate(lista_ultimos, headers="keys", tablefmt="fancy_grid"))
        else:
            print(tabulate(res["registros"]["elements"], headers="keys", tablefmt="fancy_grid"))



def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    tipo = input("ingrese el tipo de producto a filtrar: ").upper()
    año_inicial = int(input("ingrese el año inicial del rango: "))
    año_final = int(input("ingrese el año final del rango: "))
    if año_final < año_inicial:
        aux = año_inicial
        año_inicial = año_final
        año_final = aux
    res = logic.req_4(control,tipo, año_inicial, año_final)
    if res == None:
        print("No se encontraron registros")
    else:
        print(f"El tiempo de ejecucion fue: {res["tiempo"]} ms")
        print(f"El total de registros que pasaron el filtro fue: {res["size"]}")
        print(f"La cantidad de registros con SURVEY fue: {res["survey"]}")
        print(f"La cantidad de registrso con CENSUS fue: {res["census"]}")
        if res["size"] > 20:
            lista_primeros =[]
            lista_ultimos = []
            j = res["size"] -1
            for i in range(5):
                lista_primeros.append(al.get_element(res["registros"],i))
                lista_ultimos.append(al.get_element(res["registros"],j))
                j -= 1
            print("los 5 primeros son: ")
            print(tabulate(lista_primeros, headers="keys", tablefmt="fancy_grid"))
            print("\nlos 5 ultimos son: ")
            print(tabulate(lista_ultimos, headers="keys", tablefmt="fancy_grid"))
        else:
            print(tabulate(res["registros"]["elements"], headers="keys", tablefmt="fancy_grid"))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    estadistica = input("ingrese la estadistica a filtrar: ").upper()
    año_inicial = int(input("ingrese el año inicial del rango: "))
    año_final = int(input("ingrese el año final del rango: "))
    if año_final < año_inicial:
        aux = año_inicial
        año_inicial = año_final
        año_final = aux
    res = logic.req_5(control,estadistica, año_inicial, año_final)
    if res == None:
        print("No se encontraron registros")
    else:
        print(f"El tiempo de ejecucion fue: {res["tiempo"]} ms")
        print(f"El total de registros que pasaron el filtro fue: {res["size"]}")
        print(f"La cantidad de registros con SURVEY fue: {res["survey"]}")
        print(f"La cantidad de registrso con CENSUS fue: {res["census"]}")
        if res["size"] > 20:
            lista_primeros =[]
            lista_ultimos = []
            j = res["size"] -1
            for i in range(5):
                lista_primeros.append(al.get_element(res["registros"],i))
                lista_ultimos.append(al.get_element(res["registros"],j))
                j -= 1
            print("los 5 primeros son: ")
            print(tabulate(lista_primeros, headers="keys", tablefmt="fancy_grid"))
            print("\nlos 5 ultimos son: ")
            print(tabulate(lista_ultimos, headers="keys", tablefmt="fancy_grid"))
        else:
            print(tabulate(res["registros"]["elements"], headers="keys", tablefmt="fancy_grid"))


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    departamento = input("Ingrese el departamento a filtrar: ").upper()
    carga_inicial = input("Ingrese el tiempo de carga en formato %Y-%M-%D en el que inicia el periodo: ")
    carga_final = input("Ingrese el tiempo de carga en formato %Y-%M-%D en el que finaliza el periodo: ")
    res = logic.req_6(control,departamento,carga_inicial,carga_final)
    if res == None:
        print("No se encontraron registros")
    else:
        print(f"El tiempo de ejecucion fue: {res["tiempo"]} ms")
        print(f"El total de registros que pasaron el filtro fue: {res["size"]}")
        print(f"La cantidad de registros con SURVEY fue: {res["survey"]}")
        print(f"La cantidad de registrso con CENSUS fue: {res["census"]}")
        if res["size"] > 20:
            lista_primeros =[]
            lista_ultimos = []
            j = res["size"] -1
            for i in range(5):
                lista_primeros.append(al.get_element(res["registros"],i))
                lista_ultimos.append(al.get_element(res["registros"],j))
                j -= 1
            print("los 5 primeros son: ")
            print(tabulate(lista_primeros, headers="keys", tablefmt="fancy_grid"))
            print("\nlos 5 ultimos son: ")
            print(tabulate(lista_ultimos, headers="keys", tablefmt="fancy_grid"))
        else:
            print(tabulate(res["registros"]["elements"], headers="keys", tablefmt="fancy_grid"))

def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    departamento = input("ingrese el departamento a filtrar: ").upper()
    año_inicial = int(input("ingrese el año inicial del rango: "))
    año_final = int(input("ingrese el año final del rango: "))
    if año_final < año_inicial:
        aux = año_inicial
        año_inicial = año_final
        año_final = aux
    orden = input("ascendente o descendete: ").upper()
    res = logic.req_7(control,departamento, año_inicial, año_final, orden)
    if res == None:
        print("No se encontraron registros")
    else:
        print(f"El tiempo de ejecucion fue: {res["tiempo"]} ms")
        print(f"El total de registros que pasaron el filtro fue: {res["size"]}")
        if año_final - año_inicial > 15:
            lista_primeros =[]
            lista_ultimos = []
            j = res["size"] -1
            h = 4
            for i in range(5):
                lista_primeros.append(al.get_element(res["registros"],h))
                lista_ultimos.append(al.get_element(res["registros"],j))
                h -= 1
                j -= 1
            print("los 5 primeros son: ")
            print(tabulate(lista_primeros, headers="keys", tablefmt="fancy_grid"))
            print("\nlos 5 ultimos son: ")
            print(tabulate(lista_ultimos, headers="keys", tablefmt="fancy_grid"))
        else:
            print(tabulate(res["registros_años"]["elements"], headers="keys", tablefmt="fancy_grid"))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    n = int(input("ingrese el numero de departamento que desea que se muestren: "))
    orden = input("ascendente o descendente: ").upper()
    res = logic.req_8(control, orden)
    print(f"El tiempo fue: {res["tiempo"]}")
    print(f"El numero de departamentos fue: {res["cantidad"]}")
    print(f"El tiempo promedio de carga fue: {res["promedio"]}")
    print(f"El menor año de recoleccion fue: {res["menor año"]}")
    print(f"El mayor año de recoleccion fue: {res["mayor año"]}")
    if n > 20:
        lista_primeros =[]
        lista_ultimos = []
        j = res["size"] -1
        h = 4
        for i in range(5):
            lista_primeros.append(al.get_element(res["inf_deptos"],h))
            lista_ultimos.append(al.get_element(res["inf_deptos"],j))
            h -= 1
            j -= 1
        print("los 5 primeros son: ")
        print(tabulate(lista_primeros, headers="keys", tablefmt="fancy_grid"))
        print("\nlos 5 ultimos son: ")
        print(tabulate(lista_ultimos, headers="keys", tablefmt="fancy_grid"))
    else:
        print(tabulate(res["inf_deptos"]["elements"], headers="keys", tablefmt="fancy_grid"))

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
