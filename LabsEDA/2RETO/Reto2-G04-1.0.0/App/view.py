import sys
from App import logic as log
from tabulate import tabulate
from DataStructures.List import array_list as al



def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    return log.new_logic()


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
    #TODO: Realizar la carga de datos
    file = "/agricultural-100.csv"
    start_time = log.get_time()
    
    catalogo = log.load_data(control, file)
    
    end_time = log.get_time()
    tiempo_ejecucion = log.delta_time(start_time, end_time)

    print("El tiempo de ejecucion es: ", tiempo_ejecucion)
    print("Se cargaron " + str(al.size(catalogo["registros"])) + " registros")
    print("El mayor año de recoleccion de registro fue: ", log.mayor_año_recoleccion(catalogo))

    primeros_ultimos(catalogo["registros"], al.size(catalogo["registros"]))

def print_registros(registros):
    """
        Función que imprime los datos de la carga de datos
    """
    rows = []
    for registro in registros["elements"]:

        rows.append([
            registro["year_collection"],
            registro["load_time"],
            registro["state_name"],
            registro["source"],
            registro["unit_measurement"],
            registro["value"],
        ])

    # Encabezados de la tabla
    headers = [
        "Año de recoleccion", 
        "Fecha de carga", 
        "Departamento", 
        "Tipo de fuente", 
        "Unidad de medicion", 
        "Valor de medicion",        
    ]
    
    print((tabulate(rows, headers=headers, tablefmt="pretty")))

def primeros_ultimos(lista, total_registros):
    
    if total_registros >= 20:
        primeras = al.sub_list(lista, 0, 5)
        ultimas = al.sub_list(lista, -5, 5)
        print("\nPrimeros 5 registros:")
        print_reqs(primeras)
        print("\nUltimos 5 registros:")
        print_reqs(ultimas)
    else:
        primeras = lista
        print_reqs(primeras)
    
def print_reqs(registros):
    """
        Función que imprime los datos de los reqs
    """
    rows = []
    for registro in registros["elements"]:
        fecha = registro["load_time"].date()
        rows.append([
            registro["source"],
            registro["year_collection"],
            fecha,
            registro["freq_collection"],
            registro["state_name"],
            registro["unit_measurement"],
            registro["commodity"],
            registro["value"]
        ])

    # Encabezados de la tabla
    headers = [
        "Tipo de fuente",
        "Año de recoleccion", 
        "Fecha de carga", 
        "Frecuencia de recolección",
        "Departamento", 
        "Unidad de medicion", 
        "Tipo del producto",
        "Valor de medicion",        
    ]
    
    print((tabulate(rows, headers=headers, tablefmt="pretty")))

def print_bono(registros):
    """
        Función que imprime los datos del bono
    """
    rows = []
    for registro in registros["elements"]:
        rows.append([
            registro["state_name"],
            registro["promedio"],
            registro["total_registros"],
            registro["menor_anio"],
            registro["mayor_anio"],
            registro["menor_tp"],
            registro["mayor_tp"],
            registro["survey"],
            registro["census"]
        ])

    # Encabezados de la tabla
    headers = [
        "Estado",
        "Tiempo promedio", 
        "Total registros", 
        "Menor año",
        "Mayor año",
        "Menor tiempo de diferencia",
        "Mayor tiempo de diferencia",
        "Survey",
        "Census"     
    ]
    
    print((tabulate(rows, headers=headers, tablefmt="pretty")))

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    year = input("Ingrese el año de interés (formato YYYY): ")

    resultado = log.req_1(control, year)

    print(f"\nTiempo de ejecución: {resultado['tiempo_ejecucion']} ms")
    print(f"Número total de registros encontrados: {resultado['total_registros']}")

    if resultado["total_registros"] == 0:
        print("No se encontraron registros para el año solicitado.")
    else:
        ultimo = resultado["ultimo_registro"]
        print("\nÚltimo registro recopilado:")
        for key, value in ultimo.items():
            print(f"  - {key}: {value}")


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    state = input("Ingrese el nombre del estado a filtrar: ")
    n_registros = int(input("Ingrese el número de registros a mostrar: "))
    
    start_time = log.get_time()
    
    lista, total_registros = log.req_2(control, state, n_registros)
    
    end_time = log.get_time()
    tiempo_ejecucion = log.delta_time(start_time, end_time)

    print("\nTiempo de ejecución:", tiempo_ejecucion, "ms")
    print("Total de registros encontrados:", total_registros)
    print_reqs(lista)


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    department = input("Ingrese el nombre del departamento a filtrar: ").upper()
    start_year = int(input("Ingrese el año inicial del periodo a consultar (YYYY): "))
    end_year = int(input("Ingrese el año final del periodo a consultar (YYYY): "))

    start_time = log.get_time()
    lista, total_registros, survey, census = log.req_3(control, department, start_year, end_year)

    end_time = log.get_time()
    tiempo_ejecucion = log.delta_time(start_time, end_time)
    
    print("\nTiempo de ejecución:", tiempo_ejecucion, "ms")
    print("\nTotal de registros encontrados:", total_registros)
    print(f"Total de registros con fuente 'SURVEY': ", survey)
    print(f"Total de registros con fuente 'CENSUS': ", census)
    
    primeros_ultimos(lista, total_registros)

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    
    producto = input("Ingrese el nombre del producto a filtrar: ").upper()
    anio_ini = int(input("Ingrese el año inicial (YYYY): "))
    anio_fin = int(input("Ingrese el año final (YYYY): "))

    tiempo, total, census, survey, registros = log.req_4(control, producto, anio_ini, anio_fin)

    print(f"\nTiempo de ejecución: {tiempo} ms")
    print(f"Total de registros encontrados: {total}")
    print(f"Total con fuente 'CENSUS': {census}")
    print(f"Total con fuente 'SURVEY': {survey}")

    if al.size(registros) == 0:
        print("No se encontraron registros.")
        return

    headers = ["Fuente", "Año", "Fecha de carga", "Frecuencia", "Departamento", "Unidad"]
    tabla = []

    for i in range(al.size(registros)):
        reg = al.get_element(registros, i)
        tabla.append([
            reg["source"],
            reg["year_collection"],
            reg["load_time"].strftime("%Y-%m-%d"),
            reg["freq_collection"],
            reg["state_name"],
            reg["unit_measurement"]
        ])

    print("\nListado de registros:")
    print(tabulate(tabla, headers=headers, tablefmt="grid"))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    category = input("Ingrese la categoría a filtrar: ")
    year_ini = int(input("Ingrese el año de recoleccion inicial: "))
    year_fin = int(input("Ingrese el año de recoleccion final: "))
    
    start_time = log.get_time()
    
    lista, total_registros, survey, census = log.req_5(control, category, year_ini, year_fin)
    
    end_time = log.get_time()
    tiempo_ejecucion = log.delta_time(start_time, end_time)
    
    print("\nTiempo de ejecución:", tiempo_ejecucion, "ms")
    print("\nTotal de registros encontrados:", total_registros)
    print(f"Total de registros con fuente 'SURVEY': ", survey)
    print(f"Total de registros con fuente 'CENSUS': ", census)
    
    primeros_ultimos(lista, total_registros)
    
    
def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    department = input("Ingrese el nombre del departamento a filtrar: ").upper()
    start_date = input("Ingrese la fecha inicial del periodo a consultar (YYYY-MM-DD): ")
    end_date = input("Ingrese la fecha final del periodo a consultar (YYYY-MM-DD): ")

    start_time = log.get_time()
    lista, total_registros, survey, census = log.req_6(control, department, start_date, end_date)
    
    end_time = log.get_time()
    tiempo_ejecucion = log.delta_time(start_time, end_time)
    
    print("\nTiempo de ejecución:", tiempo_ejecucion, "ms")
    print("\nTotal de registros encontrados:", total_registros)
    print(f"Total de registros con fuente 'SURVEY': ", survey)
    print(f"Total de registros con fuente 'CENSUS': ", census)
    
    primeros_ultimos(lista, total_registros)

def print_req_7(control):
    """
    Imprime la solución del Requerimiento 7 en consola
    """
        # TODO: Imprimir el resultado del requerimiento 6
    estado = input("Ingrese el nombre del estado/departamento: ").upper()
    anio_inicio = int(input("Ingrese el año inicial (YYYY): "))
    anio_final = int(input("Ingrese el año final (YYYY): "))
    orden = input("Ingrese el tipo de ordenamiento (ASCENDENTE/DESCENDENTE): ").upper()

    tiempo, total_filtrados, resumen = log.req_7(control, estado, anio_inicio, anio_final, orden)

    print(f"\nTiempo de ejecución: {tiempo} ms")
    print(f"Total de registros válidos encontrados: {total_filtrados}\n")

    if al.size(resumen) == 0:
        print("No se encontraron registros con los criterios dados.")
        return

    headers = ["Año", "Etiqueta", "Ingresos ($)", "# Registros", "# Inválidos", "# Survey", "# Census"]
    tabla = []

    for i in range(al.size(resumen)):
        dato = al.get_element(resumen, i)
        tabla.append([
            dato["anio"],
            dato.get("indicador", ""),
            round(dato["ingresos"], 2),
            dato["registros"],
            dato["invalidos"],
            dato["survey"],
            dato["census"]
        ])

    print(tabulate(tabla, headers=headers, tablefmt="grid"))



def print_req_8(catalog):
    """
    Función que imprime los resultados del requerimiento 8
    """
    # Ejecutamos la función principal
    num_estados = int(input("Ingrese el número de departamentos a mostrar: "))
    orden = input("Ingrese el orden de los departamentos (asc para ascendente o desc paradescendente): ")
    tiempo_total, num_deptos, tiempo_promedio, menor_año, mayor_año, lista_n_deptos = log.req_8(catalog, num_estados, orden)
    
    print("El tiempo total del requerimiento fue: ", tiempo_total, "ms")
    print("Se encontraron ", num_deptos, " departamentos")
    print("El tiempo promedio de carga de todos los departamentos fue: ", round(tiempo_promedio, 3))
    print("El menor año de inicio de recolección fue: ", menor_año)
    print("El mayor año de inicio de recolección fue: ", mayor_año)
    
    if num_estados >= 15:
        primeras = al.sub_list(lista_n_deptos, 0, 5)
        print(lista_n_deptos)
        ultimas = al.sub_list(lista_n_deptos, -5, 5)
        
        print("\nListado de los primeros 5 departamentos:")
        print_bono(primeras)
        print("\nListado de los últimos 5 departamentos:")
        print_bono(ultimas)
    else:
        primeras = lista_n_deptos
        print("\nListado de departamentos:")
        print_bono(primeras)

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
