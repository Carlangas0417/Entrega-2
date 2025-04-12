import sys
from tabulate import tabulate
from datetime import datetime
import App.logic as logic

# Limite de recursion
default_limit = 1000
sys.setrecursionlimit(default_limit*10)


def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Obtener último registro recopilado según año")
    print("3- Obtener último registro cargado según departamento")
    print("4- Obtener registros recopilados según departamento y periodo")
    print("5- Obtener registros recopilados según tipo de producto y periodo")
    print("6- Obtener registros cargados según categoria estadística y periodo")
    print("7- Obtener la estadística de un departamento en un periodo")
    print("8- Obtener mayores y menores ingresos de un departamento en un periodo")
    print("9- Obtener departamento con mayor diferencia promedio \n   de tiempo de recolección y publicación de registros.")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    regs, min_year, max_year, first5, last5 = logic.load_data(control, 'agricultural-100.csv')
    return regs, min_year, max_year, first5, last5

def print_first_last_records_tabulate(data):
    columns = ['year_collection', 'load_time', 'state_name', 'source', 'unit_measurement', 'value']
    tabla = []
    for item in data:
        fila = [item.get(columna, '') for columna in columns]
        tabla.append(fila)
    print(tabulate(tabla, headers=columns, tablefmt='grid'), '\n')

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = logic.get_data(control, id)
    if data:
        print("Dato encontrado:")
        print(data)
    else:
        print(f"No se encontró un registro con el ID {id}")

def print_tabulate(data: list, columns: list):
    '''
    Imprime una tabla con los datos de una lista de diccionarios.
    '''
    tabla = []
    for item in data:
        fila = [item.get(columna, '') for columna in columns]
        tabla.append(fila)
    print(tabulate(tabla, headers=columns, tablefmt='grid'), '\n')
    

# Imprimir requerimiento 1
def print_ultimo_registro_anio(control, anio):
    """
        Funcion que imprime el tiempo de la ejecución del requerimiento en milisegundos, 
        el úmero total de registros que cumplieron el filtro por año de recopilación 
        y una tabla del ultimo registro recopilado según un año de interes.
    """
    tiempo, total_registros, ultimo_registro = logic.ultimo_registro_anio(control, anio)
    print(f'Tiempo de ejecución: {tiempo:.3f} ms')
    if ultimo_registro:
        print(f'Total de registros que cumplieron el filtro por año de recopilación: {total_registros}')
        data = []
        data.append(ultimo_registro)
        columns = ['year_collection', 'load_time', 'source', 'freq_collection', 'state_name', 'commodity', 'unit_measurement', 'value']
        print_tabulate(data, columns)
    else:
        print(f"No hay registros del año {anio}.\n")
    

# Imprimir requerimiento 2
def print_ultimo_registro_depto(control, depto):
    """
        Funcion que imprime el tiempo de la ejecución del requerimiento en milisegundos, 
        el número total de registros que cumplieron el filtro por nombre de departamento 
        y una tabla con la informacion del ultimo registro recopilado según el deparpamento de interes.
    """
    tiempo, total_registros, ultimo_registro = logic.ultimo_registro_depto(control, depto)
    print(f'Tiempo de ejecución: {tiempo:.3f} ms')
    if ultimo_registro:
        print(f'Total de registros que cumplieron el filtro por departamento: {total_registros}')
        data = []
        data.append(ultimo_registro)
        columns = ['year_collection', 'load_time', 'source', 'freq_collection', 'state_name', 'commodity', 'unit_measurement', 'value']
        print_tabulate(data, columns)
    else:
        print(f"No hay registros del departamento {depto}.\n")


# Imprimir requerimiento 3
def print_filtrar_depto_por_periodo(control, depto, anio_inicial, anio_final):
    """
        Funcion que imprime el tiempo de la ejecución del requerimiento en milisegundos, 
        el número total de registros que cumplieron el filtro, número total de registros 
        con tipo de fuente/origen 'SURVEY' y 'CENSUS' y una tabla con el listado de registros 
        recopilados según el nombre del departamento para un periodo de tiempo de interés.
        Si el listado de registros tiene mas de 20 elementos, se imprimen los primeros 5
        y últimos 5.
    """
    tiempo, total_registros, survey, census, filtrados = logic.filtrar_deptos_por_periodo(control, depto, anio_inicial, anio_final)
    print(f'Tiempo de ejecución: {tiempo:.3f} ms')
    if total_registros > 0:
        print(f'Total de registros que cumplieron el filtro: {total_registros}')
        print(f'Total de registros con tipo de fuente/origen “SURVEY”: {survey}')
        print(f'Total de registros con tipo de fuente/origen “CENSUS”: {census}')
        
        columns = ['source', 'year_collection', 'load_time', 'freq_collection', 'commodity', 'unit_measurement']
        if total_registros > 20:
            filtrados_20 = filtrados['elements'][:5] + filtrados['elements'][-5:]
            print_tabulate(filtrados_20, columns)
        else:
            print_tabulate(filtrados['elements'], columns)
    else:
        print(f"No hay registros del departamento {depto} en el periodo de {anio_inicial} a {anio_final}.\n")


# Imprimir requerimiento 4
def print_filtrar_commodity_por_periodo(control, commodity, anio_inicial, anio_final):
    """
        Funcion que imprime el tiempo de la ejecución del requerimiento en milisegundos, 
        el número total de registros que cumplieron el filtro, Número total de registros 
        con tipo de fuente/origen 'SURVEY' y 'CENSUS' y una tabla con el listado de registros 
        recopilados según el tipo de producto para un periodo de tiempo de interés.
        Si el listado de registros tiene mas de 20 elementos, se imprimen los primeros 5
        y últimos 5.
    """
    tiempo, total_registros, survey, census, filtrados = logic.filtrar_commodity_por_periodo(control, commodity, anio_inicial, anio_final)
    print(f'Tiempo de ejecución: {tiempo:.3f} ms')
    if total_registros > 0:
        print(f'Total de registros que cumplieron el filtro: {total_registros}')
        print(f'Total de registros con tipo de fuente/origen “SURVEY”: {survey}')
        print(f'Total de registros con tipo de fuente/origen “CENSUS”: {census}')
        
        columns = ['source', 'year_collection', 'load_time', 'freq_collection', 'state_name', 'unit_measurement', 'commodity']
        if total_registros > 20:
            filtrados_20 = filtrados['elements'][:5] + filtrados['elements'][-5:]
            print_tabulate(filtrados_20, columns)
        else:
            print_tabulate(filtrados['elements'], columns)
    else:
        print(f"No hay registros del tipo de producto {commodity} en el periodo de {anio_inicial} a {anio_final}.\n")


# Imprimir requerimiento 5
def print_filtrar_category_por_periodo(control, category, anio_inicial, anio_final):
    """
        Funcion que imprime el tiempo de la ejecución del requerimiento en milisegundos, 
        el número total de registros que cumplieron el filtro, Número total de registros 
        con tipo de fuente/origen 'SURVEY' y 'CENSUS' y una tabla con el listado de registros 
        recopilados según el tipo de producto para un periodo de tiempo de interés.
        Si el listado de registros tiene mas de 20 elementos, se imprimen los primeros 5
        y últimos 5.
    """
    tiempo, total_registros, survey, census, filtrados = logic.filtrar_category_por_periodo(control, category, anio_inicial, anio_final)
    print(f'Tiempo de ejecución: {tiempo:.3f} ms')
    if total_registros > 0:
        print(f'Total de registros que cumplieron el filtro: {total_registros}')
        print(f'Total de registros con tipo de fuente/origen “SURVEY”: {survey}')
        print(f'Total de registros con tipo de fuente/origen “CENSUS”: {census}')
        
        columns = ['source', 'year_collection', 'load_time', 'freq_collection', 'state_name', 'unit_measurement', 'commodity']
        if total_registros > 20:
            filtrados_20 = filtrados['elements'][:5] + filtrados['elements'][-5:]
            print_tabulate(filtrados_20, columns)
        else:
            print_tabulate(filtrados['elements'], columns)
    else:
        print(f"No hay registros de la categoria estadistica {category} en el periodo de {anio_inicial} a {anio_final}.\n")


# Imprimir requerimiento 6
def print_analizar_deptos_por_periodo(control, depto, fecha_inicio, fecha_fin):
    """
        Funcion que imprime el tiempo de la ejecución del requerimiento en milisegundos, 
        el número total de registros que cumplieron el filtro, el número total de registros 
        con tipo de fuente/origen 'SURVEY' y 'CENSUS' y una tabla con cada registro cargado 
        para un departamento para un rango de tiempo dado que contiene:
            - Tipo de fuente/origen (ej.: "CENSUS", "SURVEY")
            - Año de recopilación
            - Fecha de carga en la plataforma (formato "%Y-%m-%d")
            - Frecuencia de la recopilación (ej.: "ANNUAL", "WEEKLY")
            - Nombre del departamento
            - Unidad de medición del registro (ej.: "HEAD", "$")
            - Tipo de producto (ej.: "HOGS", "SHEEP")
        Si el listado de registros tiene mas de 20 elementos, se imprimen los primeros 5 y últimos 5.
    """
    try:
        if isinstance(fecha_inicio, str):
            fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
        if isinstance(fecha_fin, str):
            fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
    except ValueError:
        print("Error: Las fechas ingresadas no tienen el formato correcto (YYYY-MM-DD).")
        return
    
    tiempo, total_registros, survey, census, filtrados = logic.analizar_deptos_por_periodo(control, depto, fecha_inicio, fecha_fin)
    print(f'Tiempo de ejecución: {tiempo:.3f} ms.')
    if total_registros > 0:
        print(f'Total de registros que cumplieron el filtro: {total_registros}')
        print(f'Total de registros con tipo de fuente/origen “SURVEY”: {survey}')
        print(f'Total de registros con tipo de fuente/origen “CENSUS”: {census}')
        
        columns = ['source', 'year_collection', 'load_time', 'freq_collection', 'state_name', 'unit_measurement', 'commodity']
        if total_registros > 20:
            filtrados_20 = filtrados['elements'][:5] + filtrados['elements'][-5:]
            print_tabulate(filtrados_20, columns)
        else:
            print_tabulate(filtrados['elements'], columns)
    else:
        print(f"No hay registros cargados para {depto} en el periodo de {fecha_inicio} a {fecha_fin}.\n")
    

# Imprimir requerimiento 7
def print_ingresos_depto_por_periodo(control, depto, anio_inicial, anio_final):
    """
    Imprime el tiempo de ejecución, total de registros filtrados, 
    el año con mayor y menor ingresos y la suma total de ingresos por año.
    """
    resultado = logic.ingresos_depto_por_periodo(control, depto, anio_inicial, anio_final)

    print(f"\nTiempo de ejecución: {resultado['tiempo_ejecucion']:.3f} ms")

    if resultado['cumple_filtro'] > 0:
        print(f'Total de registros que cumplieron el periodo del filtro: {resultado['cumple_filtro']}\n')
        
        print(f'El año con MAYOR ingresos en {depto.upper()} fue {resultado['anio_max']} '
              f'con ingresos de ${resultado['ingreso_max']:.2f}')
        print(f'El año con MENOR ingresos en {depto.upper()} fue {resultado['anio_min']} '
              f'con ingresos de ${resultado['ingreso_min']:.2f}\n')
        
        print(f'El total de ingresos del periodo fue de ${resultado['ingresos_periodo']}')
        
        print(f'Total de registros que cumplieron el periodo del filtro: {resultado['cumple_periodo']}')
        print(f'Total de registros con unidad de medida "$" con valor inválido: {resultado['valor_invalido']}\n')
        print(f'Total de registros con tipo de fuente/origen "SURVEY": {resultado['survey_count']}')
        print(f'Total de registros con tipo de fuente/origen "CENSUS": {resultado['census_count']}\n')
    else:
        print(f'\nNo hay registros para el departamento {depto} en el periodo de {anio_inicial} a {anio_final}.\n')


# Imprimir requerimiento 8
def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    time,deps,promedio_total,menor_inicial,mayor_inicial,dep_mayor_tiempo=logic.req_8(control)
    print("El tiempo que se demoró el requerimiento en completarse fue: "+str(time))
    print("El total número de departamentos fue "+str(deps)+"\n"+"El tiempo promedio de carga de todos los departamentos fueron "+str(promedio_total)+
          "años\n"+"El menor año de recopilación de los registros fue "+str(menor_inicial)+"\n"+"El mayor año de recopilación de los registros fue "+str(mayor_inicial)+"\n"+
          "El departamento con mayor tiempo promedio fue "+dep_mayor_tiempo["state_name"]+", con un promedio de: "+str(dep_mayor_tiempo["promedio_dep"])+"\n"+
          "El total de registros de este departamento fue "+str(dep_mayor_tiempo["total_registros"])+", el menor año de recopilacion del departamento fue "+str(dep_mayor_tiempo["menor_anio"])+
          " y el mayor "+str(dep_mayor_tiempo["mayor_anio"])+"\n"+"El menor tiempo entre recopilación del departamento fue "+str(dep_mayor_tiempo["menor_tiempo"])+
          " y el mayor "+str(dep_mayor_tiempo["mayor_tiempo"])+"\n"+"El total de registros del departamento de tipo censo fue "+str(dep_mayor_tiempo["total_census"])+
          " y de encuestas fue "+str(dep_mayor_tiempo["total_survey"]))


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
            regs, min_year, max_year, first5, last5 = load_data(control)
            print('Total de registros cargados: ' + str(regs))
            print('Menor año de recolección de registro: ' + str(min_year))
            print('Mayor año de recolección de registro: ' + str(max_year))
            print('Los primeros registros cargados fueron:')
            print_first_last_records_tabulate(first5)
            print('Los últimos registros cargados fueron:')
            print_first_last_records_tabulate(last5)
        elif int(inputs) == 2:
            anio = int(input('Ingrese el año de interés: '))
            print_ultimo_registro_anio(control, anio)

        elif int(inputs) == 3:
            depto = input('Ingrese el departamento de interés: ')
            print_ultimo_registro_depto(control, depto)

        elif int(inputs) == 4:
            depto = input('Ingrese el departamento de interés: ')
            anio_inicial = int(input('Ingrese el año inicial: '))
            anio_final = int(input('Ingrese el año final: '))
            print_filtrar_depto_por_periodo(control, depto, anio_inicial, anio_final)

        elif int(inputs) == 5:
            commodity = input('Ingrese el tipo de producto de interés: ')
            anio_inicial = int(input('Ingrese el año inicial: '))
            anio_final = int(input('Ingrese el año final: '))
            print_filtrar_commodity_por_periodo(control, commodity, anio_inicial, anio_final)

        elif int(inputs) == 6:
            category = input('Ingrese la categoria estadística de interés: ')
            anio_inicial = int(input('Ingrese el año inicial: '))
            anio_final = int(input('Ingrese el año final: '))
            print_filtrar_category_por_periodo(control, category, anio_inicial, anio_final)

        elif int(inputs) == 7:
            depto = input('Ingrese el departamento de interés: ')
            fecha_inicio = input('Ingrese la fecha inicial en el formato "YYYY-MM-DD": ')
            fecha_fin = input('Ingrese la fecha final en el formato "YYYY-MM-DD": ')
            print_analizar_deptos_por_periodo(control, depto, fecha_inicio, fecha_fin)

        elif int(inputs) == 8:
            depto = input('Ingrese el departamento de interés: ')
            anio_inicial = int(input('Ingrese el año inicial del periodo: '))
            anio_final = int(input('Ingrese el año final del periodo: '))
            print_ingresos_depto_por_periodo(control, depto, anio_inicial, anio_final)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
    
    # comentario
