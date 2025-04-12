import time
import csv
import os
import sys
from datetime import datetime
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Map import map_separate_chaining as mc


import time
from operator import itemgetter

csv.field_size_limit(2147483647)
default_limit=1000
sys.setrecursionlimit(default_limit*10)


data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'
def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {
        "registros" : al.new_list(),
        "map_by_state" : lp.new_map(100, 0.7),
        "map_by_category" : lp.new_map(1000, 0.7),
        "map_by_year" : lp.new_map(1000, 0.7),
        "map_by_commodity" : lp.new_map(1000, 0.7),
    }
    return catalog

# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    nombre = data_dir + filename
    archivo = csv.DictReader(open(nombre, encoding="utf-8"))
    for registro in archivo:
        fecha = datetime.strptime(registro["load_time"], "%Y-%m-%d %H:%M:%S")
        registro_data = {
        "source": registro["source"],
        "commodity": registro["commodity"],
        "statical_category": registro["statical_category"],
        "unit_measurement": registro["unit_measurement"],
        "state_name": registro["state_name"],
        "location": registro["location"],
        "year_collection": registro["year_collection"],
        "freq_collection": registro["freq_collection"],
        "reference_period": registro["reference_period"],
        "load_time": fecha,
        "value": registro["value"]
        }
        al.add_last(catalog["registros"], registro_data)
        update_bystate(catalog, registro_data)
        update_bycategory(catalog, registro_data)
        update_byyear(catalog, registro_data)
        update_bycommodity(catalog, registro_data)

    al.merge_sort(catalog["registros"], comp_fechas)
    
    return catalog

def menor_año_recoleccion(catalog):
    
    anio = al.get_element(catalog["registros"], 0)["year_collection"]
    
    for i in range(1, al.size(catalog["registros"])):
        registro = al.get_element(catalog["registros"], i)
        if registro["year_collection"] < anio:
            anio = registro["year_collection"]
    return anio
    
    
def mayor_año_recoleccion(catalog):
    
    anio = al.get_element(catalog["registros"], 0)["year_collection"]
    
    for i in range(1, al.size(catalog["registros"])):
        registro = al.get_element(catalog["registros"], i)
        if registro["year_collection"] > anio:
            anio = registro["year_collection"]
    return anio
        
        
def update_bystate(catalog, registro):
    """
    Agrega un dato al mapa por estado
    """
    
    state_value = lp.contains(catalog['map_by_state'],registro['state_name'])
    if state_value:
        state_list = lp.get(catalog['map_by_state'],registro['state_name'])
        al.add_last(state_list,registro)
    else:
        state_list = al.new_list()
        al.add_last(state_list, registro)
        lp.put(catalog['map_by_state'], registro['state_name'], state_list)
        
    return catalog


def update_bycategory(catalog, registro):
    """
    Agrega un dato al mapa por estado
    """
    
    category_value = lp.contains(catalog['map_by_category'],registro['statical_category'])
    if category_value:
        category_list = lp.get(catalog['map_by_category'],registro['statical_category'])
        al.add_last(category_list,registro)
    else:
        category_list = al.new_list()
        al.add_last(category_list, registro)
        lp.put(catalog['map_by_category'], registro['statical_category'], category_list)
        
    return catalog


def update_byyear(catalog, registro):
    """
    Agrega un dato al mapa por estado
    """

    year_value = lp.contains(catalog['map_by_year'],registro['year_collection'])
    if year_value:
        year_list = lp.get(catalog['map_by_year'],registro['year_collection'])
        al.add_last(year_list,registro)
    else:
        year_list = al.new_list()
        al.add_last(year_list, registro)
        lp.put(catalog['map_by_year'], registro['year_collection'], year_list)
        
    return catalog

def update_bycommodity(catalog, registro):
    """
    Agrega un dato al mapa por commodity
    """

    commodity_value = lp.contains(catalog['map_by_commodity'],registro['commodity'])
    if commodity_value:
        commodity_list = lp.get(catalog['map_by_commodity'],registro['commodity'])
        al.add_last(commodity_list,registro)
    else:
        commodity_list = al.new_list()
        al.add_last(commodity_list, registro)
        lp.put(catalog['map_by_commodity'], registro['commodity'], commodity_list)
        
    return catalog


def comp_fechas(registro1, registro2):
    """
    Compara dos fechas
    """
    f1 = registro1["load_time"]
    f2 = registro2["load_time"]
    if f1 == f2:
        return registro1["state_name"] < registro2["state_name"]
    else:
        return f1 > f2
    
def comp_fechas_asc(registro1, registro2):
    """
    Compara dos fechas
    """
    f1 = registro1["promedio"]
    f2 = registro2["promedio"]
    if f1 == f2:
        return registro1["state_name"] < registro2["state_name"]
    else:
        return f1 < f2
def comp_fechas_desc(registro1, registro2):
    """
    Compara dos fechas
    """
    f1 = registro1["promedio"]
    f2 = registro2["promedio"]
    if f1 == f2:
        return registro1["state_name"] < registro2["state_name"]
    else:
        return f1 > f2

# Funciones de consulta sobre el catálogo

def req_1(catalog, year):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start_time = get_time()

    registros = lp.get(catalog["map_by_year"], year)

    if not registros or al.size(registros) == 0:
        return {"tiempo_ejecucion": delta_time(start_time, get_time()), "total_registros": 0, "ultimo_registro": None}

    registros = al.merge_sort(registros, comp_fechas)

    ultimo_registro = al.get_element(registros, 0)

    return {
        "tiempo_ejecucion": delta_time(start_time, get_time()),
        "total_registros": al.size(registros),
        "ultimo_registro": {
            "Año de recolección": ultimo_registro["year_collection"],
            "Fecha de carga": ultimo_registro["load_time"].strftime("%Y-%m-%d"),
            "Fuente": ultimo_registro["source"],
            "Frecuencia": ultimo_registro["freq_collection"],
            "Departamento": ultimo_registro["state_name"],
            "Producto": ultimo_registro["commodity"],
            "Unidad de medición": ultimo_registro["unit_measurement"],
            "Valor": ultimo_registro["value"]
        }
    }


def req_2(catalog, state, n_registros):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    list_state = lp.get(catalog["map_by_state"], state)
    lista = al.new_list()
    list_state = al.merge_sort(list_state, comp_fechas)
    
    if n_registros > al.size(list_state):
        n_registros = al.size(list_state)
    for i in range(0, n_registros):
        al.add_last(lista, list_state["elements"][i])
    return lista, al.size(list_state)


def req_3(catalog, department, start_year, end_year):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    list_deptos = lp.get(catalog["map_by_state"], department)
    lista = al.new_list()
    survey = 0
    census = 0
    list_deptos = al.merge_sort(list_deptos, comp_fechas)
    for i in range(al.size(list_deptos)):
        registro = al.get_element(list_deptos, i)
        if start_year <= int(registro["year_collection"]) and int(registro["year_collection"]) <= end_year:
            al.add_last(lista, registro)
            if registro["source"] == "SURVEY":
                survey += 1
            if registro["source"] == "CENSUS":
                census += 1
    
    return lista, al.size(lista), survey, census


def req_4(catalog, producto, anio_inicio, anio_fin):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    
    start = get_time()
    total_census = 0
    total_survey = 0
    total_registros = 0

    registros_producto = lp.get(catalog["map_by_commodity"], producto)
    filtrados = al.new_list()

    for i in range(al.size(registros_producto)):
        registro = al.get_element(registros_producto, i)
        anio = int(registro["year_collection"])

        if anio_inicio <= anio <= anio_fin:
            al.add_last(filtrados, registro)
            total_registros += 1
            if registro["source"] == "CENSUS":
                total_census += 1
            elif registro["source"] == "SURVEY":
                total_survey += 1

    al.merge_sort(filtrados, comp_fechas)

    if total_registros > 20:
        primeros = al.sub_list(filtrados, 0, 5)
        ultimos = al.sub_list(filtrados, al.size(filtrados) - 5, 5)
        resultado = al.new_list()
        for i in range(al.size(primeros)):
            al.add_last(resultado, al.get_element(primeros, i))
        for i in range(al.size(ultimos)):
            al.add_last(resultado, al.get_element(ultimos, i))
    else:
        resultado = filtrados

    tiempo = delta_time(start, get_time())
    return tiempo, total_registros, total_census, total_survey, resultado


def req_5(catalog, category, year_ini, year_fin):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    list_category = lp.get(catalog["map_by_category"], category)
    lista = al.new_list()
    survey = 0
    census = 0
    list_category = al.merge_sort(list_category, comp_fechas)
    for i in range(al.size(list_category)):
        registro = al.get_element(list_category, i)
        if year_ini <= int(registro["year_collection"]) and int(registro["year_collection"]) <= year_fin:
            al.add_last(lista, registro)
            if registro["source"] == "SURVEY":
                survey += 1
            if registro["source"] == "CENSUS":
                census += 1
    
    return lista, al.size(lista), survey, census


def req_6(catalog, department, start_date, end_date):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = get_time()

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    list_depto = lp.get(catalog["map_by_state"], department)
    lista = al.new_list()
    survey = 0
    census = 0
    list_depto = al.merge_sort(list_depto, comp_fechas)
    for i in range(al.size(list_depto)):
        registro = al.get_element(list_depto, i)
        if start_date <= registro["load_time"] and registro["load_time"] <= end_date:
            al.add_last(lista, registro)
            if registro["source"] == "SURVEY":
                survey += 1
            if registro["source"] == "CENSUS":
                census += 1
                
    return lista, al.size(lista), census, survey
    

def req_7(catalog, estado, anio_inicio, anio_final, orden):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
   
    start = get_time()
    total_filtrados = 0
    resumen = al.new_list()

    registros_estado = lp.get(catalog["map_by_state"], estado)
    ingresos_por_anio = lp.new_map(100, 0.5)
    invalidos = ["(D)", "(Z)", "(Y)", "(X)", "(NA)"]
    for i in range(al.size(registros_estado)):
        registro = al.get_element(registros_estado, i)
        anio = int(registro["year_collection"])
        if anio_inicio <= anio <= anio_final and "$" in registro["unit_measurement"]:
            valor = registro["value"]
            fuente = registro["source"]
            total_filtrados += 1

            if not lp.contains(ingresos_por_anio, anio):
                lp.put(ingresos_por_anio, anio, {
                    "anio": anio,
                    "ingresos": 0,
                    "registros": 0,
                    "invalidos": 0,
                    "survey": 0,
                    "census": 0
                })

            datos = lp.get(ingresos_por_anio, anio)

            if valor in invalidos:
                datos["invalidos"] += 1
            else:
                datos["ingresos"] += float(valor.replace(",", ""))

            datos["registros"] += 1
            if fuente == "SURVEY":
                datos["survey"] += 1
            elif fuente == "CENSUS":
                datos["census"] += 1

    resumen = lp.value_set(ingresos_por_anio)

    if orden.upper() == "ASCENDENTE":
        al.merge_sort(resumen, comparar_ingresos_asc)
    else:
        al.merge_sort(resumen, comparar_ingresos_desc)

    if al.size(resumen) > 0:
        al.get_element(resumen, 0)["indicador"] = "MAYOR" if orden.upper() == "DESCENDENTE" else "MENOR"
        al.get_element(resumen, al.size(resumen) - 1)["indicador"] = "MENOR" if orden.upper() == "DESCENDENTE" else "MAYOR"

    if al.size(resumen) > 20:
        top_5 = al.sub_list(resumen, 0, 5)
        bottom_5 = al.sub_list(resumen, al.size(resumen) - 5, 5)
        nuevo_resumen = al.new_list()
        for i in range(al.size(top_5)):
            al.add_last(nuevo_resumen, al.get_element(top_5, i))
        for i in range(al.size(bottom_5)):
            al.add_last(nuevo_resumen, al.get_element(bottom_5, i))
        resumen = nuevo_resumen

    tiempo = delta_time(start, get_time())
    return tiempo, total_filtrados, resumen


def req_8(catalog, num_estados, orden):
    """
    Retorna el resultado del requerimiento 8
    
    # TODO: Modificar el requerimiento 8
    """
    start = get_time()
    list_state_names = lp.key_set(catalog["map_by_state"])
    array_list = al.new_list()
    invalidos = ["QUE"]

    deptos = {}
    for i in list_state_names["elements"]:

        list_registros = lp.get(catalog["map_by_state"], i)

        for registro in list_registros["elements"]:
            if registro["unit_measurement"] == "$" and registro["value"] in invalidos:
                continue
            if registro["state_name"] not in deptos:
                deptos[registro["state_name"]] = {
                    "state_name": registro["state_name"],
                    "diferencia": 0,
                    "menor_anio": int(registro["year_collection"]),
                    "mayor_anio": int(registro["year_collection"]),
                    "menor_tp": registro["load_time"].year - int(registro["year_collection"]),
                    "mayor_tp": registro["load_time"].year - int(registro["year_collection"]),
                    "survey": 0,
                    "census": 0,
                    "total_registros": 0,
                    "promedio": 0
                }  
            depto_stats = deptos[registro["state_name"]]
            diferencia = registro["load_time"].year - int(registro["year_collection"])
        
            deptos[registro["state_name"]]["diferencia"] += diferencia
            deptos[registro["state_name"]]["total_registros"] += 1

            if registro["source"] == "SURVEY":
                deptos[registro["state_name"]]["survey"] += 1
            elif registro["source"] == "CENSUS":
                deptos[registro["state_name"]]["census"] += 1

            deptos[registro["state_name"]]["menor_tp"] = min(depto_stats["menor_tp"], diferencia)
            deptos[registro["state_name"]]["mayor_tp"] = max(depto_stats["mayor_tp"], diferencia)
            deptos[registro["state_name"]]["menor_anio"] = min(depto_stats["menor_anio"], int(registro["year_collection"]))
            deptos[registro["state_name"]]["mayor_anio"] = max(depto_stats["mayor_anio"], int(registro["year_collection"]))
    
    tiempo_promedio = 0

    for depto in deptos:
        deptos[depto]["promedio"] = round((deptos[depto]["diferencia"] / deptos[depto]["total_registros"]), 2)
        tiempo_promedio += deptos[depto]["promedio"]
        
    tiempo_promedio = tiempo_promedio / len(deptos)    
    
    for depto in deptos:
        al.add_last(array_list, deptos[depto])

    if orden == "desc":
        array_list = al.merge_sort(array_list, comp_fechas_desc)
    elif orden == "asc":
        array_list = al.merge_sort(array_list, comp_fechas_asc)
    
    if num_estados > al.size(list_state_names):
        num_estados = al.size(list_state_names)
    lista_n_deptos = al.sub_list(array_list, 0, num_estados)
    
    end = get_time()
    tiempo_total = delta_time(start, end)
    
    return tiempo_total, len(deptos), tiempo_promedio, menor_año_recoleccion(catalog), mayor_año_recoleccion(catalog), lista_n_deptos

# Funciones auxiliares para trabajar con el mapa
def menor_año_recoleccion_map(map_data):
    """
    Encuentra el año de recolección mínimo en los registros del mapa
    """
    min_year = float('inf')
    table = map_data["table"]
    
    for entry in table["elements"]:
        if entry["key"] is not None and entry["value"] is not None:
            records = entry["value"]
            for i in range(al.size(records)):
                year = int(al.get_element(records, i)["year_collection"])
                if year < min_year:
                    min_year = year
    return min_year if min_year != float('inf') else 0

def mayor_año_recoleccion_map(map_data):
    """
    Encuentra el año de recolección máximo en los registros del mapa
    """
    max_year = -float('inf')
    table = map_data["table"]
    
    for entry in table["elements"]:
        if entry["key"] is not None and entry["value"] is not None:
            records = entry["value"]
            for i in range(al.size(records)):
                year = int(al.get_element(records, i)["year_collection"])
                if year > max_year:
                    max_year = year
    return max_year if max_year != -float('inf') else 0

def comparar_ingresos_desc(a, b):
    if a["ingresos"] > b["ingresos"]:
        x = True
    elif a["ingresos"] == b["ingresos"]:
        x = a["registros"] > b["registros"]
    else:
        x = False
    return x


def comparar_ingresos_asc(a, b):
    if a["ingresos"] < b["ingresos"]:
        x = True
    elif a["ingresos"] == b["ingresos"]:
        x = a["registros"] < b["registros"]
    else:
        x = False
    return x

def comparar_por_fecha_estado_desc(a, b):
    if a["load_time"] > b["load_time"]:
        x = True
    elif a["load_time"] == b["load_time"]:
        x = a["state_name"] < b["state_name"]
    else:
        x = False
    return x

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
