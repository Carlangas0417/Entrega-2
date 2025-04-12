import time
import csv
import os
from datetime import datetime

from DataStructures.List import array_list as lt

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {
        'registros' : None
    }
    catalog['registros'] = lt.new_list()
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    regs = load_registros(catalog, filename)
    min_year = get_min_year(catalog)
    max_year = get_max_year(catalog)
    first5 = sorted_by_load_time(catalog)[:5]
    last5 = sorted_by_load_time(catalog)[-5:]
    return regs, min_year, max_year, first5, last5


def load_registros(catalog, filename):
    '''
    Carga los registros del reto y los ordena por 'load_time'
    '''
    agricultural_file = data_dir + 'Challenge-1/' + filename
    input_file = csv.DictReader(open(agricultural_file, encoding='utf-8'))
    for registro in input_file:
        lt.add_last(catalog['registros'], registro)
    return lt.size(catalog['registros'])


def get_min_year(catalog):
    '''
    Retorna el año menor del catalogo
    '''
    registros = catalog['registros']['elements']
    min_year = float('inf')
    for registro in registros:
        year = int(registro['year_collection'])
        if year < min_year:
            min_year = year
    return min_year if min_year != float('inf') else None

def get_max_year(catalog):
    '''
    Retorna el año mayor del catalogo
    '''
    registros = catalog['registros']['elements']
    max_year = 0
    for registro in registros:
        year = int(registro['year_collection'])
        if year > max_year:
            max_year = year
    return max_year if max_year != 0 else None


def get_load_time(registro):
    return registro['load_time']

def sorted_by_load_time(catalog):
    '''
    Crea una lista organizada según fecha de carga (load_time)
    '''
    registros = catalog['registros']['elements']
    return sorted(registros, key=get_load_time)


# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    pos_data = lt.is_present(catalog['registros'], id)
    if pos_data > 0:
        data = lt.get_element(catalog['registros'], pos_data)
        return data
    return None


# Requerimiento 1
def ultimo_registro_anio(catalog, anio):
    """
    Retorna el ultimo registro recopilado según un año de interes.
    
    :param catalog: Catalogo con los registros 
    :type catalog: array_list
    :param anio: Año de interés a filtrar (con el formato “YYYY”. Ej. “2007”)
    :type anio: int

    :return: Tupla con el registro segun año de interes y el número total 
        de registros que cumplieron el filtro por año de recopilación.
    :rtype: tuple
    """
    start_time = get_time()
    
    ultimo_registro = None
    total_registros = 0
    for registro in catalog['registros']['elements']:
        if anio == int(registro['year_collection']):
            ultimo_registro = registro
            total_registros += 1
            
    end_time = get_time()
    tiempo_ejecucion = delta_time(start_time, end_time)
    return tiempo_ejecucion, total_registros, ultimo_registro


# Requerimiento 2
def ultimo_registro_depto(catalog, depto):
    """
    Retorna el ultimo registro cargado dado un departamento (estado) de interés.
    
    :param catalog: Catalogo con los registros de produccion agrícola.
    :type catalog: array_list
    :param depto: Nombre del departamento a filtrar (ej.: “NEW MEXICO”, “CALIFORNIA” o “COLORADO”)
    :type depto: str

    :return: Tupla con el tiempo de ejecucion, total de registros que cumplieron el 
    filtro por año de recopilación y el registro segun año de interes.
    :rtype: tuple
    """
    start_time = get_time()
    
    ultimo_registro_depto = None
    fecha_max = None
    total_registros = 0
    for registro in catalog['registros']['elements']:
        if registro['state_name'].upper() == depto.upper():
            fecha_actual = datetime.strptime(registro['load_time'], "%Y-%m-%d %H:%M:%S") # 2012-01-01 00:00:00
            if fecha_max is None or fecha_actual > fecha_max:
                fecha_max = fecha_actual
                ultimo_registro_depto = registro
            total_registros += 1

    end_time = get_time()
    tiempo_ejecucion = delta_time(start_time, end_time)
    return tiempo_ejecucion, total_registros, ultimo_registro_depto


# Requerimiento 3
def filtrar_deptos_por_periodo(catalog, depto, anio_inicial, anio_final):
    """
    Listar los registros recopilados según el nombre del departamento para 
    un periodo de tiempo de interés
    
    :param catalog: Catalogo con los registros de produccion agrícola.
    :type catalog: array_list
    :param depto: Nombre del departamento a filtrar (ej.: “NEW MEXICO”, “CALIFORNIA” o “COLORADO”)
    :type depto: str
    :param anio_inicial: Año inicial del periodo a consultar (con formato "YYYY ", ej.: “2007”)
    :type anio_inicial: int
    :param anio_final: Año final del periodo a consultar (con formato "YYYY", ej.: “2010”)
    :type anio_final: int

    :return: Tupla con el tiempo de ejecucion, numero total de registros que cumplieron con el filtro,
        total de resgistros con 'source' SURVEY, total de registros con 'source' CENSUS y 
        listado de registros filtrados resultantes.
    :rtype: tuple
    """
    start_time = get_time()
    
    filtrados = lt.new_list()
    count_survey = 0
    count_census = 0
    for registro in catalog['registros']['elements']:
        if (depto.upper() == registro['state_name'].upper() 
        and anio_inicial <= int(registro['year_collection']) <= anio_final):
            lt.add_last(filtrados, registro)
            if registro['source'] == 'SURVEY':
                count_survey += 1
            elif registro['source'] == 'CENSUS':
                count_census += 1
    total_registros = lt.size(filtrados)     
    
    end_time = get_time()
    tiempo_ejecucion = delta_time(start_time, end_time)
    return tiempo_ejecucion, total_registros, count_survey, count_census, filtrados


# Requerimiento 4
def filtrar_commodity_por_periodo(catalog, commodity, anio_inicial, anio_final):
    """
    Listar los registros recopilados según el tipo de producto para un periodo de tiempo de interés
    
    :param catalog: Catalogo con los registros de produccion agrícola.
    :type catalog: array_list
    :param commodity: Tipo de producto a filtrar (ej.: “HOGS”, “SHEEP”, etc.)
    :type commodity: str
    :param anio_inicial: Año inicial del periodo a consultar (con formato "YYYY ", ej.: “2007”)
    :type anio_inicial: int
    :param anio_final: Año final del periodo a consultar (con formato "YYYY", ej.: “2010”)
    :type anio_final: int

    :return: Tupla con el tiempo de ejecucion, número total de registros que cumplieron con el filtro,
        total de resgistros con 'source' SURVEY, total de registros con 'source' CENSUS y 
        listado de registros filtrados resultantes.
    :rtype: tuple
    """
    start_time = get_time()
    
    filtrados = lt.new_list()
    count_survey = 0
    count_census = 0
    for registro in catalog['registros']['elements']:
        categories = registro['commodity'].upper().split(', ')
        if (commodity.upper() in categories
        and anio_inicial <= int(registro['year_collection']) <= anio_final):
            lt.add_last(filtrados, registro)
            if registro['source'] == 'SURVEY':
                count_survey += 1
            elif registro['source'] == 'CENSUS':
                count_census += 1
    total_registros = lt.size(filtrados)     
    
    end_time = get_time()
    tiempo_ejecucion = delta_time(start_time, end_time)
    return tiempo_ejecucion, total_registros, count_survey, count_census, filtrados


# Requerimiento 5
def filtrar_category_por_periodo(catalog, category, anio_inicial, anio_final):
    """
    Listar los registros cargados según su categoría estadística para un rango de tiempo de interés.
    
    :param catalog: Catalogo con los registros de produccion agrícola.
    :type catalog: array_list
    :param category: Categoría estadística para filtrar (ej.: “INVENTORY”, “SALES”, etc.)
    :type category: str
    :param anio_inicial: Año inicial del periodo a consultar (con formato "YYYY ", ej.: “2007”)
    :type anio_inicial: int
    :param anio_final: Año final del periodo a consultar (con formato "YYYY", ej.: “2010”)
    :type anio_final: int

    :return: Tupla con el tiempo de ejecucion, número total de registros que cumplieron con el filtro,
        total de resgistros con 'source' SURVEY, total de registros con 'source' CENSUS y 
        listado de registros filtrados resultantes.
    :rtype: tuple
    """
    start_time = get_time()
    
    filtrados = lt.new_list()
    count_survey = 0
    count_census = 0
    for registro in catalog['registros']['elements']:
        categories = registro['statical_category'].upper().split(', ')
        if (category.upper() in categories
        and anio_inicial <= int(registro['load_time'].split("-")[0]) <= anio_final):
            lt.add_last(filtrados, registro)
            if registro['source'] == 'SURVEY':
                count_survey += 1
            elif registro['source'] == 'CENSUS':
                count_census += 1
    total_registros = lt.size(filtrados) 

    end_time = get_time()
    tiempo_ejecucion = delta_time(start_time, end_time)
    return tiempo_ejecucion, total_registros, count_survey, count_census, filtrados


# Requerimiento 6
def analizar_deptos_por_periodo(catalog, depto, fecha_inicio, fecha_fin):
    """
    Analiza los registros de un departamento en un rango de fechas y calcula estadísticas.

    :param catalogo: Estructura de datos con la información de los registros.
    :type catalogo: dict o lista de diccionarios
    :param departamento: Nombre del departamento a filtrar (ej.: "NEW MEXICO", "CALIFORNIA", "COLORADO").
    :type departamento: str
    :param fecha_inicio: Fecha inicial del periodo a consultar en formato "%Y-%m-%d" (ej.: "1998-01-20").
    :type fecha_inicio: str
    :param fecha_fin: Fecha final del periodo a consultar en formato "%Y-%m-%d" (ej.: "2004-01-20").
    :type fecha_fin: str

    :return: Tupla con (tiempo de ejecución en ms, total de registros filtrados, total "SURVEY", 
              total "CENSUS", lista de registros seleccionados).
    :rtype: tuple(int, int, int, int, list[dict])
    """
    start_time = get_time()
    
    filtrados = lt.new_list()
    count_survey = 0
    count_census = 0
    for registro in catalog['registros']['elements']:
        fecha_registro = datetime.strptime(registro['load_time'], "%Y-%m-%d %H:%M:%S").date()
        if (fecha_inicio <= fecha_registro <= fecha_fin
            and registro['state_name'].upper() == depto.upper()):
            lt.add_last(filtrados, registro)
            if registro['source'] == 'SURVEY':
                count_survey += 1
            elif registro['source'] == 'CENSUS':
                count_census += 1
    total_registros = lt.size(filtrados)
    
    end_time = get_time()
    tiempo_ejecucion = delta_time(start_time, end_time)
    return tiempo_ejecucion, total_registros, count_survey, count_census, filtrados


# Requerimiento 7
def ingresos_depto_por_periodo(catalog, depto, anio_inicial, anio_final):
    """
    Analiza el periodo con mayores y menores ingresos para un departamento dentro de un rango de tiempo.
    Retorna el año con mayor y menor ingresos sumados.

    :param catalog: Estructura de datos con la información de los registros.
    :type catalog: dict (con 'registros' -> 'elements' como lista de diccionarios)
    :param depto: Nombre del departamento a filtrar (ej.: "NEW MEXICO", "CALIFORNIA").
    :type depto: str
    :param anio_inicial: Año inicial del periodo a consultar (ej.: 2007).
    :type anio_inicial: int
    :param anio_final: Año final del periodo a consultar (ej.: 2010).
    :type anio_final: int

    :return: Diccionario con el tiempo de ejecución, total de registros filtrados, 
             año con mayor ingresos (y total acumulado) y año con menor ingresos (y total acumulado).
    :rtype: dict
    """
    start_time = get_time()

    cumple_filtro = 0
    ingresos_periodo = 0
    cumple_periodo = 0
    valor_invalido = 0
    count_survey = 0
    count_census = 0
    
    anio_max, ingreso_max = None, float('-inf')
    anio_min, ingreso_min = None, float('inf')

    anio_actual = None
    ingreso_actual = 0

    for registro in catalog['registros']['elements']:
        if (depto.upper() == registro['state_name'].upper() 
            and anio_inicial <= int(registro['year_collection']) <= anio_final
            and registro['unit_measurement'] == '$'):
            
            value = registro['value'].replace(',', '')
            if value.replace('.', '', 1).isdigit():
                ingreso = float(value)
                anio = int(registro['year_collection'])

                if anio_actual is None or anio_actual != anio:
                    if anio_actual is not None:
                        if ingreso_actual > ingreso_max:
                            ingreso_max = ingreso_actual
                            anio_max = anio_actual
                        if ingreso_actual < ingreso_min:
                            ingreso_min = ingreso_actual
                            anio_min = anio_actual

                    anio_actual = anio
                    ingreso_actual = 0

                ingreso_actual += ingreso
                cumple_filtro += 1
                ingresos_periodo += ingreso
            else:
                valor_invalido += 1
                
            if registro['source'] == 'SURVEY':
                count_survey += 1
            elif registro['source'] == 'CENSUS':
                count_census += 1
                    
            cumple_periodo += 1

    if anio_actual is not None:
        if ingreso_actual > ingreso_max:
            ingreso_max = ingreso_actual
            anio_max = anio_actual
        if ingreso_actual < ingreso_min:
            ingreso_min = ingreso_actual
            anio_min = anio_actual

    if ingreso_max == float('-inf'):
        anio_max, ingreso_max = None, 0
    if ingreso_min == float('inf'):
        anio_min, ingreso_min = None, 0

    end_time = get_time()
    time = delta_time(start_time, end_time)
    return {
        'tiempo_ejecucion': time,
        'cumple_filtro': cumple_filtro,
        'anio_max': anio_max,
        'anio_min': anio_min,
        'ingreso_max': ingreso_max,
        'ingreso_min': ingreso_min,
        'ingresos_periodo': ingresos_periodo,
        'cumple_periodo': cumple_periodo,
        'valor_invalido': valor_invalido,
        'survey_count': count_survey,
        'census_count': count_census
    }


# Requerimiento 8
def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    :param : 
    :type : 

    :return: 
    :rtype: 
    """
    start_time=get_time()
    deps={}
    registros=catalog["registros"]["elements"]
    mayor_inicial=30
    menor_inical=2500
    total_registros=0
    total_anios=0
    for registro in registros:
        if int(registro["year_collection"])>mayor_inicial:
            mayor_inicial=int(registro["year_collection"])
        elif int(registro["year_collection"])<menor_inical:
            menor_inical=int(registro["year_collection"])
        if registro["state_name"] in deps.keys():
            diferencia=int(registro["load_time"][:4])-int(registro["year_collection"])
            deps[registro["state_name"]]["total_anios"]+= diferencia
            deps[registro["state_name"]]["total_registros"]+=1
            if registro["source"]=="CENSUS":
                deps[registro["state_name"]]["total_census"]+=1
            elif registro["source"]=="SURVEY":
                deps[registro["state_name"]]["total_survey"]+=1
            if deps[registro["state_name"]]["menor_anio"]>registro["year_collection"]:
                deps[registro["state_name"]]["menor_anio"]=registro["year_collection"]
            elif deps[registro["state_name"]]["mayor_anio"]<registro["year_collection"]:
                deps[registro["state_name"]]["mayor_anio"]=registro["year_collection"]
            if diferencia>deps[registro["state_name"]]["mayor_tiempo"]:
                deps[registro["state_name"]]["mayor_tiempo"]=diferencia
            elif diferencia<deps[registro["state_name"]]["menor_tiempo"]:
                deps[registro["state_name"]]["menor_tiempo"]=diferencia
        else:
            deps[registro["state_name"]]={"state_name":registro["state_name"],
                                          "total_anios":0,
                                          "total_registros":0,
                                          "menor_anio":"2000",
                                          "mayor_anio":"1900",
                                          "menor_tiempo":3000,
                                          "mayor_tiempo":0,
                                          "total_census":0,
                                          "total_survey":0}

        total_anios+=int(registro["load_time"][:4])-int(registro["year_collection"])
        total_registros+=1
    dep_mayor_tiempo={"total_anios":1,
                      "total_registros":1}
    prom_dep_mayor=dep_mayor_tiempo["total_anios"]/dep_mayor_tiempo["total_registros"]
    for dep in deps:
        promedio=deps[dep]["total_anios"]/deps[dep]["total_registros"]
        deps[dep]["promedio_dep"]=promedio
        if promedio>prom_dep_mayor:
            dep_mayor_tiempo=deps[dep]
            prom_dep_mayor=promedio
    promedio_total=total_anios/total_registros
    finish_time=get_time()
    time=delta_time(start_time,finish_time)
    return time,len(deps),promedio_total,menor_inical,mayor_inicial,dep_mayor_tiempo


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
