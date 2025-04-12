import time

import csv

import os

from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as al
from DataStructures.Queue import queue as qu
from DataStructures.Stack import stack as st

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

csv.field_size_limit(2147483647)

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    
    catalog = {'source': None,
               'commodity': None,
               'statical_category': None,
               'unit_measurement': None,
               'state_name': None,
               'location': None,
               'year_collection': None,
               'freq_collection': None,
               'reference_period': None,
               'load_time': None,
               'value': None}

    catalog['source'] = al.new_list()
    catalog['commodity'] = al.new_list()
    catalog['statical_category'] = al.new_list()
    catalog['unit_measurement'] = al.new_list()
    catalog['state_name'] = al.new_list()
    catalog["location"] = al.new_list()
    catalog["year_collection"] = al.new_list()
    catalog["freq_collection"] = al.new_list()
    catalog["reference_period"] = al.new_list()
    catalog["load_time"] = al.new_list()
    catalog["value"] = al.new_list()
    return catalog

def datos():
    """
    Crea una lista nativa de python por columna del archivo CSV, y la añade a un diccionario base, desde el cual se va a 
    pasar a llenar el catálogo.-
    """
    
    doc=(data_dir+"agricultural-100.csv")
    
    diccionario_base={}
    
    datos=open(doc,encoding="utf-8")
    lector=csv.reader(datos)
    columnas=next(lector)
    
    for columna in columnas:
        diccionario_base[columna]=[]
    
    for fila in lector:
        for i in range (len(columnas)):
            llave=columnas[i]
            dato=fila[i]
            diccionario_base[llave].append(dato)
            
    datos.close()
    
    return diccionario_base

# Funciones para la carga de datos

def carga(datos,catalog,columna:str):
    for i in datos[columna]:
        al.add_last(catalog[columna],i)
    

def load_data(catalog, datos):
    """
    Carga los datos del DataFrame en el catálogo.
    """
    carga(datos, catalog, 'source')
    
    source_size = catalog["source"]["size"]
    
    carga(datos, catalog, 'commodity')
    carga(datos, catalog, 'statical_category')
    carga(datos, catalog, 'unit_measurement')
    carga(datos, catalog, 'state_name')
    carga(datos, catalog, 'location')
    carga(datos, catalog, 'year_collection')
    carga(datos, catalog, 'freq_collection')
    carga(datos, catalog, 'reference_period')
    carga(datos, catalog, 'load_time')
    carga(datos, catalog, 'value')
    
    return source_size

def lesser_year(catalog):
    año=catalog["year_collection"]["elements"][0]
    for i in catalog["year_collection"]["elements"]:
        if año > i:
            año=i
    return año

def greater_year(catalog):
    año=catalog["year_collection"]["elements"][0]
    for i in catalog["year_collection"]["elements"]:
        if año < i:
            año=i
    return año

def primeros(catalog):
    final=[]
    transitoria=[]
    info = {'source': None,
               'unit_measurement': None,
               'state_name': None,
               'year_collection': None,
                "freq_collection":None,
               'load_time': None,
               'value': None,}
    for indice in range(0,5):
        for llave in catalog:
            transitoria.append(catalog[llave]["elements"][indice])
        info["source"]=transitoria[0]
        info["unit_measurement"]=transitoria[3]
        info["state_name"]=transitoria[4]
        info["year_collection"]=transitoria[6]
        info["load_time"]=transitoria[9]
        info["value"]=transitoria[10]
        final.append(info)
        transitoria=[]
    return final

def ultimos(catalog):
    final=[]
    transitoria=[]
    info = {'source': None,
               'unit_measurement': None,
               'state_name': None,
               'year_collection': None,
               'load_time': None,
               'value': None,}
    for indice in range(-6,-1):
        for llave in catalog:
            transitoria.append(catalog[llave]["elements"][indice])
        info["source"]=transitoria[0]
        info["unit_measurement"]=transitoria[3]
        info["state_name"]=transitoria[4]
        info["year_collection"]=transitoria[6]
        info["load_time"]=transitoria[9]
        info["value"]=transitoria[10]
        final.append(info)
        transitoria=[]
    return final
# Funciones de consulta sobre el catálogo



def req_1(catalog,anno):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    
    start_time=get_time()
    
    lista_fechas=[]
    info = {'source': None,
            'commodity': None,
               'unit_measurement': None,
               'state_name': None,
               'year_collection': None,
               'load_time': None,
               'value': None,}
    
    for i in range(catalog["year_collection"]["size"]):
        if int(catalog["year_collection"]["elements"][i]) == int(anno):
            lista_fechas.append(catalog["load_time"]["elements"][i])
    
    pasaron=len(lista_fechas)
    ultima=max(lista_fechas)
    
    print (ultima)
    
    for k in range(catalog["load_time"]["size"]):
        if (str(ultima) == catalog["load_time"]["elements"][k]) and (int(anno)==int(catalog["year_collection"]["elements"][k])):
            info["source"]=catalog["source"]["elements"][k]
            info["commodity"]=catalog["commodity"]["elements"][k]
            info["unit_measurement"]=catalog["unit_measurement"]["elements"][k]
            info["state_name"]=catalog["state_name"]["elements"][k]
            info["year_collection"]=catalog["year_collection"]["elements"][k]
            info["load_time"]=catalog["load_time"]["elements"][k]
            info["value"]=catalog["value"]["elements"][k]
    
    end_time=get_time()
    
    req_1_time=delta_time(start_time,end_time)
    
    return(info,req_1_time,pasaron)
    
    
            
        
    


def req_2(catalog, dep):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_time=get_time()
    
    lista_departamentos=[]
    info = {'source': None,
            'commodity': None,
               'unit_measurement': None,
               'state_name': None,
               'year_collection': None,
               'freq_collection': None,
               'load_time': None,
               'value': None,}
    
    for i in range(catalog["state_name"]["size"]):
        if catalog["state_name"]["elements"][i] == (dep):
            lista_departamentos.append(catalog["load_time"]["elements"][i])
    
    pasaron=len(lista_departamentos)
    ultima=max(lista_departamentos)
    
    for k in range(catalog["load_time"]["size"]):
        if (str(ultima) == catalog["load_time"]["elements"][k]) and ((dep)==catalog["state_name"]["elements"][k]):
            info["source"]=catalog["source"]["elements"][k]
            info["commodity"]=catalog["commodity"]["elements"][k]
            info["unit_measurement"]=catalog["unit_measurement"]["elements"][k]
            info["state_name"]=catalog["state_name"]["elements"][k]
            info["year_collection"]=catalog["year_collection"]["elements"][k]
            info["freq_collection"]=catalog["freq_collection"]["elements"][k]
            info["load_time"]=catalog["load_time"]["elements"][k]
            info["value"]=catalog["value"]["elements"][k]
    
    end_time=get_time()
    
    req_2_time=delta_time(start_time,end_time)
    
    return(info,req_2_time,pasaron)


def req_3(catalog,nombre,anno_i,anno_f):
    """
    Retorna el resultado del requerimiento 3
    
    anno_i (int): Año de inicio para hacer el filtro.
    
    anno_i (int): Año de finalización para hacer el filtro.
    
    
    POR SAMUEL VILLAMIL
    
    """
    # TODO: Modificar el requerimiento 3
    
    start_time=get_time()
    
    if anno_f<anno_i:
        return "No es un intervalo válido. Intente de nuevo..."    
    survey=0
    census=0
    
    info = {'source': None,
            'commodity': None,
               'unit_measurement': None,
               'state_name': None,
               'year_collection': None,
               'load_time': None,
               'freq_collection': None,}
    
    lista=al.new_list()
    
    for i in range(al.size(catalog["year_collection"])):
        if (catalog["state_name"]["elements"][i] == nombre) and (int(anno_i) <= int(catalog["year_collection"]["elements"][i]) <= int(anno_f)):
            info["source"]=catalog["source"]["elements"][i]
            info["commodity"]=catalog["commodity"]["elements"][i]
            info["unit_measurement"]=catalog["unit_measurement"]["elements"][i]
            info["state_name"]=catalog["state_name"]["elements"][i]
            info["year_collection"]=catalog["year_collection"]["elements"][i]
            info["load_time"]=catalog["load_time"]["elements"][i]
            info["freq_collection"]=catalog["freq_collection"]["elements"][i]

            al.add_last(lista,info)
            
            if catalog["source"]["elements"][i] == "SURVEY":
                survey+=1
            else:
                census+=1
            
            
    pasaron=al.size(lista)
    
    if pasaron > 20:
        nova_lista=al.new_list()
        for i in range(0,5):
            al.add_last(nova_lista,lista["elements"][i])
        for i in range(-6,-1):
            al.add_last(nova_lista,lista["elements"][i])
        lista=nova_lista
    
    end_time=get_time()
    
    req3_time=delta_time(start_time,end_time)
    
    return (lista,survey,census,pasaron,req3_time)
            
        
        
def req_4(catalog,product,anioi:int,aniof:int):
    """
    Retorna el resultado del requerimiento 4
    
    anno_i (int): Año de inicio para hacer el filtro.
    
    anno_i (int): Año de finalización para hacer el filtro.
    
    
    POR JUAN DIEGO GARCÍA
    
    """
    
    start_time = get_time()
    
    
    if anioi > aniof:
        return "Por favor revise la informacion ingresada."
    data = {
        "source": None,
        "year_collection":None,
        "load_time":None,
        "freq_collection":None,
        "state_name":None,
        "unit_measurement":None
    }
    s_count = 0
    c_count = 0
    
    size = al.size(catalog["year_collection"])
    result = al.new_list()
    
    for i in range(size):
        if catalog["commodity"]["elements"][i] == product and catalog["year_collection"]["elements"][i] > anioi and catalog["year_collection"]["elements"][i] < aniof:
            data["source"] = catalog["source"]["elements"][i]
            data["year_collection"] = catalog["year_collection"]["elements"][i]
            data["load_time"] = catalog["load_time"]["elements"][i]
            data["freq_collection"] = catalog["freq_collection"]["elements"][i]
            data["state_name"] = catalog["state_name"]["elements"][i]
            data["unit_measurement"] = catalog["unit_measurement"]["elements"][i]
            
            al.add_last(result, data)
    
    if catalog["source"]["elements"][i] == "SURVEY":
        s_count += 1
    else:
        c_count += 1
        
    count = int(al.size(result))
    
    if al.size(result) > 20:
        short_result = al.new_list()
        for i in range(0,5):
            al.add_last(short_result, result["elements"][i])
        for i in range(count-5,count):
            al.add_last(short_result, result["elements"][i])
        result = short_result
        
    end_time = get_time()
    time = delta_time(start_time,end_time)
    
    
    return (result, s_count, c_count, count, time)
    


def req_5(catalog, category, anno_i,anno_f):
    """
    Retorna el resultado del requerimiento 5
    
    
    
    POR TOMÁS APONTE
    """
    # TODO: Modificar el requerimiento 5
    start_time=get_time()
    
    if anno_f<anno_i:
        return "No es un intervalo válido. Intente de nuevo..."    
    survey=0
    census=0
    
    info = {'source': None,
            'commodity': None,
               'unit_measurement': None,
               'state_name': None,
               'year_collection': None,
               'load_time': None,
               'freq_collection': None,}
    
    lista=al.new_list()
    
    for i in range(al.size(catalog["year_collection"])):
        if (catalog["statical_category"]["elements"][i] == category) and (int(anno_i) <= int(catalog["year_collection"]["elements"][i]) <= int(anno_f)):
            info["source"]=catalog["source"]["elements"][i]
            info["commodity"]=catalog["commodity"]["elements"][i]
            info["unit_measurement"]=catalog["unit_measurement"]["elements"][i]
            info["state_name"]=catalog["state_name"]["elements"][i]
            info["year_collection"]=catalog["year_collection"]["elements"][i]
            info["load_time"]=catalog["load_time"]["elements"][i]
            info["freq_collection"]=catalog["freq_collection"]["elements"][i]
            info["statical_category"]=catalog["statical_category"]["elements"][i]

            al.add_last(lista,info)
            
            if catalog["source"]["elements"][i] == "SURVEY":
                survey+=1
            else:
                census+=1
            
            
    pasaron=al.size(lista)
    
    if pasaron > 20:
        nova_lista=al.new_list()
        for i in range(0,5):
            al.add_last(nova_lista,lista["elements"][i])
        for i in range(-6,-1):
            al.add_last(nova_lista,lista["elements"][i])
        lista=nova_lista
    
    end_time=get_time()
    
    req3_time=delta_time(start_time,end_time)
    
    return (lista,survey,census,pasaron,req3_time)



def req_6(catalog,fecha_i,fecha_f,dep):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    
    start_time=get_time()
    
    if fecha_f<fecha_i:
        return "No es un intervalo válido. Intente de nuevo..."    
    survey=0
    census=0
    
    info = {'source': None,
            'commodity': None,
               'unit_measurement': None,
               'state_name': None,
               'year_collection': None,
               'load_time': None,
               'freq_collection': None,}
    
    lista=al.new_list()
    
    for i in range(al.size(catalog["year_collection"])):
        if (catalog["state_name"]["elements"][i] == dep) and (fecha_i <= catalog["load_time"]["elements"][i][0:10] <= fecha_f):
            info["source"]=catalog["source"]["elements"][i]
            info["commodity"]=catalog["commodity"]["elements"][i]
            info["unit_measurement"]=catalog["unit_measurement"]["elements"][i]
            info["state_name"]=catalog["state_name"]["elements"][i]
            info["year_collection"]=catalog["year_collection"]["elements"][i]
            info["load_time"]=catalog["load_time"]["elements"][i]
            info["freq_collection"]=catalog["freq_collection"]["elements"][i]
            info["statical_category"]=catalog["statical_category"]["elements"][i]

            al.add_last(lista,info)
            
            if catalog["source"]["elements"][i] == "SURVEY":
                survey+=1
            else:
                census+=1
            
            
    pasaron=al.size(lista)
    
    if pasaron > 20:
        nova_lista=al.new_list()
        for i in range(0,5):
            al.add_last(nova_lista,lista["elements"][i])
        for i in range(-6,-1):
            al.add_last(nova_lista,lista["elements"][i])
        lista=nova_lista
    
    end_time=get_time()
    
    req3_time=delta_time(start_time,end_time)
    
    return (lista,survey,census,pasaron,req3_time)



def req_7(catalog,year0,year,dep):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start_time=get_time()    
    if year<year0:
        return "Por favor introduzca un intervalo de tiempo valido..."    
    survey_minn = 0
    survey_maxx = 0
    census_minn = 0
    census_maxx = 0
    lista_filtro = al.new_list()
    lista_minn = al.new_list()
    lista_maxx = al.new_list()
    info = {'source': None,
               'unit_measurement': None,
               'state_name': None,
               'year_collection': None,
               'load_time': None
               }

    
    for i in range(catalog["year_collection"]["size"]):
        if (catalog["state_name"]["elements"][i] == dep) and (year0 <= catalog["load_time"]["elements"][i][0:10] <= year):
            info = { 
            "state_name": catalog["state_name"]["elements"][i],
            "unit_measurement": catalog["unit_measurement"]["elements"][i],
            "year_collection": catalog["year_collection"]["elements"][i],
            "load_time": catalog["load_time"]["elements"][i]
            }
            al.add_last(lista_filtro, info)
            
    pasaron = al.size(lista_filtro)
    maxx = -99999999
    minn = 99999999
    year_maxx = 0
    year_minn = 0
    for k in range(pasaron):
        if (lista_filtro["unit_measurement"]["elements"][k] == "$"):
            if lista_filtro["value"]["elements"][k] > maxx:
                maxx = lista_filtro["value"]["elements"][k]
                year_maxx = lista_filtro["load_time"]["elements"][k]
            if lista_filtro["value"]["elements"][k] < minn:
                minn = lista_filtro["value"]["elements"][k]
                year_minn = lista_filtro["load_time"]["elements"][k]
    
    for k in range(pasaron):
        if lista_filtro["load_time"]["elements"][k] == year_maxx:
            al.add_last(lista_maxx, catalog["value"]["elements"][k])
            if lista_filtro["source"]["elements"][k] == "SURVEY":
                survey_maxx += 1
            else:
                census_maxx += 1
        if lista_filtro["load_time"]["elements"][k] == year_minn:
            al.add_last(lista_minn, catalog["value"]["elements"][k])
            if lista_filtro["source"]["elements"][k] == "SURVEY":
                survey_minn += 1
            else:
                census_minn += 1
    pasaron_minn = al.size(lista_minn)
    invalido_minn = abs(pasaron - pasaron_minn)
    pasaron_maxx = al.size(lista_maxx)
    invalido_maxx = abs(pasaron - pasaron_maxx)
    info_maxx = {'year_collection': year_maxx,
               'type': "MAYOR",
               'value': maxx,
               "filter": pasaron_maxx,
               "invalid": invalido_maxx,
               "survey": survey_maxx,
               "census": census_maxx,}
    info_min = {'year_collection': year_minn,
               'type': "MENOR",
               'value': minn,
               "filter": pasaron_minn,
               "invalid": invalido_minn,
               "survey": survey_minn,
               "census": census_minn,}
    
            

    
    end_time=get_time()
    
    req_7_time=delta_time(start_time,end_time)
    
    return (pasaron,info_maxx,info_min,req_7_time)


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


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
