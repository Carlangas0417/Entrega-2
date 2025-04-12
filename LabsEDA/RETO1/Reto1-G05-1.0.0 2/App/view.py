import sys
import App.logic as logic
from tabulate import tabulate
from DataStructures.Queue import queue as q
from datetime import datetime, date
from DataStructures.List import array_list as arr

default_limit = 1000 
sys.setrecursionlimit(default_limit*10) 


def new_logic():
    '''Se crea una instancia del controlador

    :return dict: catalogo
    '''
    control = logic.new_logic()
    return control

def print_menu():
    '''imprime el menu
    '''
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

def load_data(control, filename: str)->tuple:
    '''Carga los datos

    :param DataStructure control: catalogo
    :param str filename: ruta al archivo
    :return tuple: registro, menor_year, mayor_year, primeros5, ultimos5
    '''
    registro, menor_year, mayor_year, head, tail, time = logic.load_data(control, filename)
    if arr.size(registro) != 0:
        print(f'Se tardo {time}ms en cargar')
        print(f"Hay un total de: {arr.size(registro)} registros")
        print(f"El año mas antiguo donde se tomo un registro fue en: {menor_year} ")
        print(f"El año mas reciente donde se tomo un registro fue en: {mayor_year} ")
        print("Primeros 5 registros: ")
        header = ["Año Recopilación", "Fecha Carga", "Departamento", "Tipo Fuente", "Unidad de Medición", "Valor del Registro"]
        table = []
        for dicci in head["elements"]:
            row = [
            dicci["year_collection"], dicci["load_time"], dicci["state_name"], dicci["source"], dicci["unit_measurement"], dicci["value"]]
            table.append(row)
        print(tabulate(table, headers= header, tablefmt= "grid"))
        print("\n...")
        print("...")
        print("...")
        
        table2 = []
        for dicci in tail["elements"]:
            row = [
            dicci["year_collection"], dicci["load_time"], dicci["state_name"], dicci["source"], dicci["unit_measurement"], dicci["value"]]
            table2.append(row)
        print("Ultimos 5 registros:")
        print(tabulate(table2, headers= header, tablefmt= "grid"))
        
        return registro, menor_year, mayor_year, head, tail
    else:
        return ("La carga de los datos no fue exitosa, intentelo nuevamente")


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control, year: int):
    '''Función que imprime la solución del Requerimiento 1 en consola

    :param DataStructure control: catalogo
    :param int year: anio
    '''
    resultado, time, contador = logic.req_1(control, year)
    if resultado is not None:
        print(f"El tiempo que se tardo en ejecutar fue de: {time} ms")
        print(f"El numero total de registros que cumplieron fue de: {contador}")
        head = ["Año Recolección", "Fecha Carga", "Tipo Fuente", "Frecuencia Recolección", "Departamento", "Tipo Producto", "Unidad de Medida", "Valor del Registro"]
        table = []
        row = [
            resultado["year_collection"], resultado["load_time"], resultado["source"], resultado["freq_collection"], resultado["state_name"], resultado["commodity"], resultado["unit_measurement"], resultado["value"]
        ]
        table.append(row)
        print(tabulate(table, headers =head, tablefmt = "simple_outline"))
    else:
        print("No se encontró ningún resultado con los parámetros ingresados")
        

def print_req_2(control, departamento: str):
    '''Función que imprime la solución del Requerimiento 2 en consola

    :param Datastructure control: catalogo
    :param str departamento: departamento
    '''
    resultado, time, contador = logic.req_2(control, departamento)
    if resultado is not None:
        print(f"El tiempo que se tardo en ejecutar fue de: {time} ms")
        print(f"El número total de registros que cumplieron fue de: {contador}")
        head = ["Año Recolección", "Fecha Carga", "Tipo Fuente", "Frecuencia Recolección", "Departamento", "Tipo Producto", "Unidad de Medida", "Valor del Registro"]
        table = []
        row = [
            resultado["year_collection"], resultado["load_time"], resultado["source"], resultado["freq_collection"], resultado["state_name"], resultado["commodity"], resultado["unit_measurement"], resultado["value"]
        ]
        table.append(row)
        print(tabulate(table, headers =head, tablefmt = "simple_outline"))
    else:
        print("No se encontró ningún resultado con los parámetros ingresados")

#Alejo
def print_req_3(control, departamento: str, year_inicial: int, year_final: int):
    '''        Función que imprime la solución del Requerimiento 3 en consola


    :param DataStructure control: catalogo
    :param str departamento: departamento
    :param int year_inicial: anio inicial
    :param int year_final: anio final
    '''
    departamento = departamento.lower()
    year_final = int(year_final)
    year_inicial = int(year_inicial)
    tiempo, survey, censo, rta = logic.req_3(control, departamento, year_inicial, year_final)
    print(f"El tiempo que se tardo en ejecutar fue de: {tiempo} ms")
    total = survey + censo
    print(f"La cantidad de registros que pasaron el filtro fueron: {total}")
    print(f"La cantidad de registros tipo SURVEY fueron: {survey}")
    print(f"La cantidad de registros tipo CENSUS fueron: {censo}")
    
    if q.size(rta) != 0:
        if total < 20:
            header = ["Tipo Registro", "Año Recopilación", "Fecha Carga", "Frecuencia Recolección", "Tipo Producto", "Unidad de Medición"]
            table = []
            reg = q.dequeue(rta)
            for i in range(q.size(rta)):
                fila = [
                    reg["source"], reg["year_collection"], reg["load_time"], reg["freq_collection"], reg["commodity"], reg["unit_measurement"]
                ]
                table.append(fila)
                reg = q.dequeue(rta)
            print(tabulate(table, headers= header, tablefmt= "grid"))
        else:
            print("Primeros 5 registros")
            header = ["Tipo Registro", "Año Recopilación", "Fecha Carga", "Frecuencia Recolección", "Tipo Producto", "Unidad de Medición"]
            table = []
            reg = q.dequeue(rta)
            for i in range(0,5):
                fila = [
                    reg["source"], reg["year_collection"], reg["load_time"], reg["freq_collection"], reg["commodity"], reg["unit_measurement"]
                ]
                reg = q.dequeue(rta)
                table.append(fila)
            print(tabulate(table, headers= header, tablefmt= "grid"))
            print("\n ...")
            print("...")
            print("...")
            for i in range(0, q.size(rta)-5):
                reg = q.dequeue(rta)
            print("Últimos 5 registros")
            table = []
            for i in range(q.size(rta)):
                reg = q.dequeue(rta)
                fila = [
                    reg["source"], reg["year_collection"], reg["load_time"], reg["freq_collection"], reg["commodity"], reg["unit_measurement"]
                ]
                table.append(fila)
            print(tabulate(table, headers= header, tablefmt= "grid"))
            

def print_req_4(control, tipo: str, year_inicial: int, year_final: int):
    '''Función que imprime la solución del Requerimiento 4 en consola

    :param DataStructure control: catalogo
    :param str tipo: tipo de dato
    :param int year_inicial: anio inicial
    :param int year_final: anio final
    '''
    resultado, survey_count, census_count, time = logic.req_4(control, tipo, year_inicial, year_final)
    total = survey_count + census_count
    print(f"El tiempo que se tardo en ejecutar fue de : {time} ms")
    print(f"La cantidad de registros que pasaron el filtro fueron: {total}")
    print(f"La cantidad de registros tipo SURVEY fueron: {survey_count}")
    print(f"La cantidad de registros tipo CENSUS fueron: {census_count}")
    if q.is_empty(resultado):
        print("No se encontraron registros que pasen el filtro.")
    elif total < 20:
        header = ["Tipo Registro", "Año Recopilación", "Fecha Carga", "Frecuencia Recolección", "Departamento", "Unidad de Medición"]
        table = []
        reg = q.dequeue(resultado)
        for i in range(q.size(resultado)):
            fila = [
                reg["source"], reg["year_collection"], reg["load_time"], reg["freq_collection"], reg["state_name"], reg["unit_measurement"]
                ]
            table.append(fila)
            reg = q.dequeue(resultado)
        print(tabulate(table, headers= header, tablefmt= "grid"))
    else:
        print("Primeros 5 registros")
        header = ["Tipo Registro", "Año Recopilación", "Fecha Carga", "Frecuencia Recolección", "Tipo Producto", "Unidad de Medición"]
        table = []
        reg = q.dequeue(resultado)            
        for i in range(0,5):
            fila = [
                reg["source"], reg["year_collection"], reg["load_time"], reg["freq_collection"], reg["commodity"], reg["unit_measurement"]
                ]
            reg = q.dequeue(resultado)
            table.append(fila)
        print(tabulate(table, headers= header, tablefmt= "grid"))
        print("\n ...")
        print("...")
        print("...")
        for i in range(0, q.size(resultado)-5):
            reg = q.dequeue(resultado)
        print("Últimos 5 registros")
        table2 = []
        for i in range(q.size(resultado)):
            reg = q.dequeue(resultado)
            fila = [
                reg["source"], reg["year_collection"], reg["load_time"], reg["freq_collection"], reg["commodity"], reg["unit_measurement"]
                ]
            table2.append(fila)
        print(tabulate(table2, headers= header, tablefmt= "grid"))



def print_req_5(control, categoria: str, year_inicial: int, year_final: int):
    '''        Función que imprime la solución del Requerimiento 5 en consola


    :param DataStructure control: catalogo
    :param str categoria: categoria de dato
    :param int year_inicial: anio inicial
    :param int year_final: anio final
    '''
    resultado, survey_count, census_count, time = logic.req_5(control, categoria, year_inicial, year_final)
    size = logic.q.size(resultado)
    print(f"El tiempo que se tardo en ejecutar fue de : {time}ms")
    print(f"La cantidad de registros que pasaron el filtro fueron: {size}")
    print(f"La cantidad de registros tipo SURVEY fueron: {survey_count}")
    print(f"La cantidad de registros tipo CENSUS fueron: {census_count}")
    if q.is_empty(resultado):
        print("No se encontraron registros que pasen el filtro.")
    elif size < 20 :
        header = ["Tipo Registro", "Año Recopilación", "Fecha Carga", "Frecuencia Recolección", "Departamento", "Unidad de Medición", "Tipo de Producto"]
        table = []
        reg = q.dequeue(resultado)
        for i in range(q.size(resultado)):
            fila = [
                reg["source"], reg["year_collection"], reg["load_time"], reg["freq_collection"], reg["state_name"], reg["unit_measurement"], reg ["commodity"]
                ]
            table.append(fila)
            reg = q.dequeue(resultado)
        print(tabulate(table, headers= header, tablefmt= "grid"))
    else:
        print("Primeros 5 registros")
        header = ["Tipo Registro", "Año Recopilación", "Fecha Carga", "Frecuencia Recolección", "Tipo Producto", "Unidad de Medición", "Tipo de Producto"]
        table = []
        reg = q.dequeue(resultado)            
        for i in range(0,5):
            fila = [
                reg["source"], reg["year_collection"], reg["load_time"], reg["freq_collection"], reg["commodity"], reg["unit_measurement"], reg ["commodity"]
                ]
            reg = q.dequeue(resultado)
            table.append(fila)
        print(tabulate(table, headers= header, tablefmt= "grid"))
        print("\n...")
        print("...")
        print("...")
        for i in range(0, q.size(resultado)-5):
            reg = q.dequeue(resultado)
        print("Últimos 5 registros")
        table2 = []
        for i in range(q.size(resultado)):
            reg = q.dequeue(resultado)
            fila = [
                reg["source"], reg["year_collection"], reg["load_time"], reg["freq_collection"], reg["commodity"], reg["unit_measurement"], reg ["commodity"]
                ]
            table2.append(fila)
        print(tabulate(table2, headers= header, tablefmt= "grid"))


def print_req_6(control, departamento: str, fecha_inicial: int, fecha_final: int):
    '''        Función que imprime la solución del Requerimiento 6 en consola


    :param Datastructure control: catalogo
    :param str departamento: departamento
    :param int fecha_inicial: anio inicial
    :param int fecha_final: anio final
    '''     
    fecha_final = datetime.strptime(fecha_final, "%Y-%m-%d")
    fecha_inicial = datetime.strptime(fecha_inicial, "%Y-%m-%d")
    resultado, survey_count, census_count, time = logic.req_6(control, departamento, fecha_inicial, fecha_final)
    total = survey_count + census_count
    print(f"El tiempo que se tardo en ejecutar fue de : {time}ms")
    print(f"La cantidad de registros que pasaron el filtro fueron: {total}")
    print(f"La cantidad de registros tipo SURVEY fueron: {survey_count}")
    print(f"La cantidad de registros tipo CENSUS fueron: {census_count}")
    if q.is_empty(resultado):
        print("No se encontraron registros que pasen el filtro.")
    if q.size(resultado) != 0:
        if total < 20:
            header = ["Tipo Registro", "Año Recopilación", "Fecha Carga", "Frecuencia Recolección", "Departamento", "Unidad de Medición", "Tipo Producto"]
            table = []
            reg = q.dequeue(resultado)
            for i in range(q.size(resultado)):
                fila = [
                    reg["source"], reg["year_collection"], reg["load_time"], reg["freq_collection"], reg["state_name"], reg["unit_measurement"], reg["commodity"]
                    ]
                table.append(fila)
                reg = q.dequeue(resultado)
            print(tabulate(table, headers= header, tablefmt= "grid"))
        else:
            print("Primeros 5 registros")
            header = ["Tipo Registro", "Año Recopilación", "Fecha Carga", "Frecuencia Recolección", "Departamento", "Unidad de Medición", "Tipo Producto"]
            table = []
            reg = q.dequeue(resultado)
            for i in range(0,5):
                fila = [
                    reg["source"], reg["year_collection"], reg["load_time"], reg["freq_collection"], reg["state_name"], reg["unit_measurement"], reg["commodity"]
                    ]
                table.append(fila)
                reg = q.dequeue(resultado)
            print(tabulate(table, headers= header, tablefmt= "grid"))
            print("\n ...")
            print("...")
            print("...")
            for i in range(0, q.size(resultado)-5):
                reg = q.dequeue(resultado)
            print("Últimos 5 registros")
            header = ["Tipo Registro", "Año Recopilación", "Fecha Carga", "Frecuencia Recolección", "Departamento", "Unidad de Medición", "Tipo Producto"]
            table = []
            for i in range(q.size(resultado)):
                reg = q.dequeue(resultado)
                fila = [
                    reg["source"], reg["year_collection"], reg["load_time"], reg["freq_collection"], reg["state_name"], reg["unit_measurement"], reg["commodity"]
                    ]
                table.append(fila)
            print(tabulate(table, headers= header, tablefmt= "grid"))


def print_req_7(control, departamento: str, year_inicial: int, year_final: int):
    '''Función que imprime la solución del Requerimiento 7 en consola

    :param DataStructure control: catalogo
    :param str departamento: departamento
    :param int year_inicial: anio inicial
    :param int year_final: anio final
    '''
    resultado, survey_countmax, survey_countmin, census_countmax, census_countmin, maxYear, minYear, maxValue, minValue, contador_invalidomax, contador_invalidomin, time = logic.req_7(control, departamento, year_inicial, year_final)
    total = q.size(resultado)
    print(f"El tiempo que se tardo en ejecutar fue de : {time}ms")
    print(f"Los datos que pasaron son: {total}")
    

    if q.is_empty(resultado):
        print("No se encontraron registros que pasen el filtro.")
    if q.size(resultado) != 0:
        
        header = ["Año con mayor ingreso", "Valor mayor ingreso", "Datos Invalidos", "Survey", "Census"]#, "Registros que pasaron el filtro", "Registros con valores no validos", "Registros SURVEY", "Registros CENSUS"
        table = []
        fila = [maxYear, maxValue, contador_invalidomax, survey_countmax, census_countmax] # total, contador_invalido, survey_count, census_count
        table.append(fila)
        header2 = ["Año con menor ingreso", "Valor menor ingreso", "Datos Invalidos", "Survey", "Census"]#
        table2 = []
        fila2 = [minYear, minValue, contador_invalidomin, survey_countmin, census_countmin] # 
        table2.append(fila2)
        print('Año con mayor ingreso')
        print(tabulate(table, headers= header, tablefmt= "grid"))
        print('Año con menor ingreso')
        print(tabulate(table2, headers= header2, tablefmt= "grid"))
        
        

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    data = None
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if inputs == 'a':
            logic.req_9(control)
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control, "agricultural-100.csv")
            
        elif int(inputs) == 2:
            year = int(input("Ingrese el año a buscar: "))
            print_req_1(control, year)

        elif int(inputs) == 3:
            departamento = input("Ingrese el departamento a buscar: ")
            print_req_2(control, departamento)

        elif int(inputs) == 4:
            departamento = input("Ingrese el departamento a buscar: ")
            year_inicial = int(input("Ingrese el año inicial: "))
            year_final = int(input("Ingrese el año final: "))        
            print_req_3(control, departamento, year_inicial, year_final)

        elif int(inputs) == 5:
            tipo = input("Ingrese el tipo a buscar: ")
            year_inicial = int(input("Ingrese el año inicial: "))
            year_final = int(input("Ingrese el año final: ")) 
            print_req_4(control, tipo, year_inicial, year_final)

        elif int(inputs) == 6:
            categoria = input("Ingrese la categoria a buscar: ")
            year_inicial = int(input("Ingrese el año inicial: "))
            year_final = int(input("Ingrese el año final: ")) 
            print_req_5(control, categoria, year_inicial, year_final)

        elif int(inputs) == 7:
            departamento = input("Ingrese el departamento a buscar: ")
            fecha_inicial = input("Ingrese la fecha inicial (en formato AAAA-MM-DD): ")
            fecha_final = input("Ingrese la fecha final (en formato AAAA-MM-DD): ")
            print_req_6(control, departamento, fecha_inicial, fecha_final)

        elif int(inputs) == 8:
            departamento = input("Ingrese el departamento a buscar: ")
            year_inicial = int(input("Ingrese el año inicial: "))
            year_final = int(input("Ingrese el año final: "))    
            print_req_7(control, departamento, year_inicial, year_final)

        elif int(inputs) == 9:
            print_req_8(control)
        

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
