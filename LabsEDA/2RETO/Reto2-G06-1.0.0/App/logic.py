import time
import csv
import os
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Map import map_separate_chaining as sc
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from tabulate import tabulate
from datetime import datetime, date
import sys
csv.field_size_limit(2147483647)
default_limit = 1000
sys.setrecursionlimit(default_limit*100)

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Challenge-2/'
def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """ 
    catalogo = {
        "año de recoleccion": sc.new_map(200,3),
        "departamento": sc.new_map(100, 3),
        "año de carga": sc.new_map(100,3),
        "año y depto": sc.new_map(100,3),
        "año y tipo": sc.new_map(100,3),
        "año y estadistica": sc.new_map(100,3),
    }
    return catalogo
# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    menor = 3000
    mayor = 0
    menor_año_carga = 3000
    mayor_año_carga = 0
    start_time = get_time()
    total = 0
    file = data_dir + filename
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for row in input_file:
        load_time = datetime.strptime(row["load_time"], "%Y-%m-%d %H:%M:%S")
        row["year_collection"] = int(row["year_collection"])
        registro = {
            "source": row["source"],
            "commodity": row["commodity"],
            "statical_category": row["statical_category"],
            "unit_measurement": row["unit_measurement"],
            "state_name": row["state_name"],
            'location': row["location"],
            "year_collection": row["year_collection"],
            "freq_collection" : row["freq_collection"],
            "reference_period": row["reference_period"],
            "load_time": load_time,
            "value": row["value"]
        }
        if sc.contains(catalog["año de recoleccion"], row["year_collection"]):
            array_list = sc.get(catalog["año de recoleccion"], row["year_collection"])
            insert_data_sorted(array_list,registro)
        else:
            lista = al.new_list()
            al.add_last(lista, registro)
            sc.put(catalog["año de recoleccion"], row["year_collection"], lista)

        if sc.contains(catalog["departamento"], row["state_name"]):
            array_list = sc.get(catalog["departamento"], row["state_name"])
            insert_data_sorted(array_list,registro)
            mapa_año = sc.get(catalog["año y depto"],row["state_name"])
            if sc.contains(mapa_año, row["year_collection"]):
                array_list_año = sc.get(mapa_año, row["year_collection"])
                insert_data_sorted(array_list_año,registro)
            else:
                lista = al.new_list()
                al.add_last(lista,registro)
                sc.put(mapa_año, row["year_collection"], lista)
        else:
            lista = al.new_list()
            al.add_last(lista, registro)
            sc.put(catalog["departamento"], row["state_name"], lista)
            new_map = sc.new_map(200,3)
            new_list = al.new_list()
            al.add_last(new_list, registro)
            sc.put(new_map, row["year_collection"], new_list)
            sc.put(catalog["año y depto"], row["state_name"], new_map)
        
        if sc.contains(catalog["año de carga"], int(row["load_time"][:4])):
            array_list = sc.get(catalog["año de carga"], int(row["load_time"][:4]))
            insert_data_sorted(array_list,registro)
        else:
            lista = al.new_list()
            al.add_last(lista, registro)
            sc.put(catalog["año de carga"], int(row["load_time"][0:4]), lista)
        
        if sc.contains(catalog["año y tipo"], row["commodity"]):
            mapa_años = sc.get(catalog["año y tipo"],row["commodity"])
            if sc.contains(mapa_años, row["year_collection"]):
                array_list_año = sc.get(mapa_años, row["year_collection"])
                insert_data_sorted(array_list_año,registro)
            else:
                lista = al.new_list()
                al.add_last(lista,registro)
                sc.put(mapa_años, row["year_collection"], lista)
        else:
            new_map = sc.new_map(200,3)
            new_list = al.new_list()
            al.add_last(new_list, registro)
            sc.put(new_map, row["year_collection"], new_list)
            sc.put(catalog["año y tipo"], row["commodity"], new_map)

        if sc.contains(catalog["año y estadistica"],row["statical_category"]):
            mapa_años = sc.get(catalog["año y estadistica"],row["statical_category"])
            if sc.contains(mapa_años, row["year_collection"]):
                array_list_año = sc.get(mapa_años, row["year_collection"])
                insert_data_sorted(array_list_año,registro)
            else:
                lista = al.new_list()
                al.add_last(lista,registro)
                sc.put(mapa_años, row["year_collection"], lista)
        else:
            new_map = sc.new_map(200,3)
            new_list = al.new_list()
            al.add_last(new_list, registro)
            sc.put(new_map, row["year_collection"], new_list)
            sc.put(catalog["año y estadistica"], row["statical_category"], new_map)
        
        if row["year_collection"] > mayor:
            mayor = row["year_collection"]
        if row["year_collection"] < menor:
            menor = row["year_collection"]
        
        if int(row["load_time"][:4]) > mayor_año_carga:
            mayor_año_carga = int(row["load_time"][:4])
        if int(row["load_time"][:4]) < menor_año_carga:
            menor_año_carga = int(row["load_time"][:4])
        total += 1
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    respuesta = {
        "tiempo":tiempo,
        "total":total,
        "menor":menor,
        "mayor": mayor,
        "catalog":catalog,
        "menor_carga":menor_año_carga,
        "mayor_carga":mayor_año_carga
    }
    return respuesta

def insert_data_sorted(array_list, registro, parametro1 = "load_time", parametro2 = "state_name", orden = "DESCENDENTE"):
    e = True
    if orden == "DESCENDENTE":
        for i in range(al.size(array_list)):
            if al.get_element(array_list,i)[parametro1] < registro[parametro1]:
                al.insert_element(array_list,registro,i)
                e = False
                break
            elif al.get_element(array_list,i)[parametro1] == registro[parametro1]:
                if al.get_element(array_list,i)[parametro2] <= registro[parametro2]:
                    al.insert_element(array_list,registro,i)
                    e = False
                    break
        if e:
            al.add_last(array_list,registro)
    else:
        for i in range(al.size(array_list)):
            if al.get_element(array_list,i)[parametro1] > registro[parametro1]:
                al.insert_element(array_list,registro,i)
                e = False
                break
            elif al.get_element(array_list,i)[parametro1] == registro[parametro1]:
                if al.get_element(array_list,i)[parametro2] <= registro[parametro2]:
                    al.insert_element(array_list,registro,i)
                    e = False
                    break
        if e:
            al.add_last(array_list,registro)




# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog,año_de_interes):
    """
    Retorna el resultado del requerimiento 1
    """
    start_time = get_time()
    array_list = sc.get(catalog["año de recoleccion"],año_de_interes)
    if array_list == None:
        return None
    registro = al.first_element(array_list)
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    respuesta = {
        "tiempo": tiempo,
        "total": al.size(array_list),
        "registro": {
            "año de recoleccion": registro["year_collection"],
            "fecha de carga": registro["load_time"],
            "tipo de fuente": registro["source"],
            "frecuencia": registro["freq_collection"],
            "departamento": registro["state_name"],
            "tipo de producto": registro["commodity"],
            "unidad de medicion": registro["unit_measurement"],
            "valor de medicion": registro["value"]
        }
    }
    return respuesta

def req_2(catalog, departamento, n):
    """
    Retorna el resultado del requerimiento 2
    """
    start_time = get_time()
    registros = al.new_list()
    array_list = sc.get(catalog["departamento"],departamento)
    if array_list == None:
        return None
    for i in range(n):
        registro = al.get_element(array_list,i)
        registro = {
            "año de recoleccion": registro["year_collection"],
            "fecha de carga": registro["load_time"],
            "tipo de fuente": registro["source"],
            "frecuencia": registro["freq_collection"],
            "departamento": registro["state_name"],
            "tipo de producto": registro["commodity"],
            "unidad de medicion": registro["unit_measurement"],
            "valor de medicion": registro["value"]
        }
        al.add_last(registros, registro)
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    respuesta = {
        "tiempo": tiempo,
        "total": al.size(array_list),
        "registros": registros
    }
    return respuesta



def req_3(catalog,  departamento, año_inicial, año_final):
    """
    Retorna el resultado del requerimiento 3
    """
    start_time = get_time()
    mapa_años = sc.get(catalog["año y depto"], departamento)
    if mapa_años == None:
        return None
    
    año = año_inicial 
    total_size = 0
    survey = 0
    census = 0
    registros = al.new_list()
    while año <= año_final:
        array_list_año = sc.get(mapa_años, año)
        if array_list_año != None:
            total_size += al.size(array_list_año)
            for registro in array_list_año["elements"]:
                new_registro = {
                    "año de recoleccion": registro["year_collection"],
                    "fecha de carga": registro["load_time"],
                    "tipo de fuente": registro["source"],
                    "frecuencia": registro["freq_collection"],
                    "tipo de producto": registro["commodity"],
                    "unidad de medicion": registro["unit_measurement"],
                    }
                insert_data_sorted(registros,new_registro, "fecha de carga", "año de recoleccion")
                if registro["source"] == "SURVEY":
                    survey += 1
                else:
                    census += 1
        año += 1
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    respuesta = {
        "tiempo": tiempo,
        "size": total_size,
        "registros": registros,
        "survey": survey,
        "census":census
    }
    return respuesta

def req_4(catalog, tipo, año_inicial, año_final):
    """
    Retorna el resultado del requerimiento 4
    """
    start_time = get_time()
    mapa_años = sc.get(catalog["año y tipo"], tipo)
    if mapa_años == None:
        return None
    año = año_inicial 
    total_size = 0
    registros = al.new_list()
    survey = 0
    census = 0
    while año <= año_final:
        array_list_año = sc.get(mapa_años, año)
        if array_list_año != None:
            total_size += al.size(array_list_año)
            for registro in array_list_año["elements"]:
                new_registro = {
                    "año de recoleccion": registro["year_collection"],
                    "fecha de carga": registro["load_time"],
                    "tipo de fuente": registro["source"],
                    "frecuencia": registro["freq_collection"],
                    "departamento": registro["state_name"],
                    "unidad de medicion": registro["unit_measurement"],
                    }
                insert_data_sorted(registros,new_registro, "fecha de carga", "año de recoleccion")
                if registro["source"] == "SURVEY":
                    survey += 1
                else:
                    census += 1
        año += 1
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    respuesta = {
        "tiempo": tiempo,
        "size": total_size,
        "registros": registros,
        "survey": survey,
        "census":census
    }
    return respuesta


def req_5(catalog, cat_est, año_inicial, año_final):
    """
    Retorna el resultado del requerimiento 5
    """
    start_time = get_time()
    mapa_años = sc.get(catalog["año y estadistica"], cat_est)
    if mapa_años == None:
        return None
    año = año_inicial 
    total_size = 0
    registros = al.new_list()
    survey = 0
    census = 0
    while año <= año_final:
        array_list_año = sc.get(mapa_años, año)
        if array_list_año != None:
            total_size += al.size(array_list_año)
            for registro in array_list_año["elements"]:
                new_registro = {
                    "año de recoleccion": registro["year_collection"],
                    "fecha de carga": registro["load_time"],
                    "tipo de fuente": registro["source"],
                    "frecuencia": registro["freq_collection"],
                    "tipo de producto": registro["commodity"],
                    "unidad de medicion": registro["unit_measurement"],
                    "departamento": registro["state_name"]
                    }
                insert_data_sorted(registros,new_registro, "fecha de carga", "año de recoleccion")
                if registro["source"] == "SURVEY":
                    survey += 1
                else:
                    census += 1
        año += 1
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    respuesta = {
        "tiempo": tiempo,
        "size": total_size,
        "registros": registros,
        "survey": survey,
        "census":census
    }
    return respuesta

def req_6(catalog, departamento, carga_inicial, carga_final):
    """
    Retorna el resultado del requerimiento 6
    """
    start_time = get_time()
    array_list = sc.get(catalog["departamento"],departamento)
    if array_list == None:
        return None
    registros = al.new_list()
    census = 0
    survey = 0
    total_size = 0
    for registro in array_list["elements"]:
        new_registro = {
                    "año de recoleccion": registro["year_collection"],
                    "fecha de carga": registro["load_time"],
                    "tipo de fuente": registro["source"],
                    "frecuencia": registro["freq_collection"],
                    "tipo de producto": registro["commodity"],
                    "unidad de medicion": registro["unit_measurement"],
                    "departamento": registro["state_name"]
                    }
        if (((registro["load_time"]).date()) >= datetime.strptime(carga_inicial, "%Y-%m-%d").date()) and (registro["load_time"].date() <= datetime.strptime(carga_final, "%Y-%m-%d").date()):
            al.add_last(registros, new_registro)
            total_size += 1
            if registro["source"] == "SURVEY":
                survey += 1
            else:
                census += 1
        if (registro["load_time"].date() < datetime.strptime(carga_inicial, "%Y-%m-%d").date()):
            break
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    respuesta = {
        "tiempo": tiempo,
        "size": total_size,
        "survey": survey,
        "census": census,
        "registros": registros
    }
    return respuesta
    


def req_7(catalog, departamento, año_inicial, año_final, orden = "ASCENDENTE"):
    """
    Retorna el resultado del requerimiento 7
    """
    start_time = get_time()
    mapa_años = sc.get(catalog["año y depto"], departamento)
    if mapa_años == None:
        return None
    total_size = 0
    año = año_inicial
    inf_años = al.new_list()
    while año <= año_final:
        array_list_año = sc.get(mapa_años, año)
        if array_list_año != None:
            ingresos = 0
            no_valido = 0
            survey = 0
            census = 0
            total_año = 0
            for registro in array_list_año["elements"]:
                if "$" in registro["unit_measurement"]:
                    total_size += 1
                    total_año += 1
                    if "(" not in registro["value"]:
                        ingresos += float(registro["value"].replace(",",""))
                    else:
                        no_valido += 1
                    if registro["source"] == "SURVEY":
                        survey += 1
                    else:
                        census += 1
            inf_año = {
            "año": año,
            "mayor_o_menor": "MITAD",
            "ingresos": ingresos,
            "total_año": total_año,
            "no_valido": no_valido,
            "survey": survey,
            "census": census
            }
            insert_data_sorted(inf_años,inf_año, "ingresos", "total_año", orden)
        año += 1
    al.get_element(inf_años,0)["mayor_o_menor"] = "MAYOR"
    al.get_element(inf_años,al.size(inf_años)-1)["mayor_o_menor"] = "MENOR"
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    respuesta = {
        "tiempo": tiempo,
        "size":total_size,
        "registros_años": inf_años,
    }
    return respuesta

def req_8(catalog, orden):
    """
    Retorna el resultado del requerimiento 8
    """
    start_time = get_time()
    lista = sc.key_set(catalog["departamento"])
    inf_deptos = al.new_list()
    menor_año_general = 3000
    mayor_año_general = 0
    promedio_general = 0
    for i in lista["elements"]:
        array_list = sc.get(catalog["departamento"],i)
        promedio = 0
        menor_tiempo = 10000
        mayor_tiempo = -1
        mayor_año = 0
        menor_año = 3000
        census = 0
        survey = 0
        for j in range(al.size(array_list)):
            registro = al.get_element(array_list,j)
            dif = registro["load_time"].year - registro["year_collection"]
            promedio += dif
            if dif < menor_tiempo:
                menor_tiempo = dif
            if dif > mayor_tiempo:
                mayor_tiempo = dif
            if registro["year_collection"] > mayor_año:
                mayor_año = registro["year_collection"]
            if registro["year_collection"] < menor_año:
                menor_año = registro["year_collection"]
            if registro["source"] == "SURVEY":
                survey += 1
            else:
                census += 1
        inf_depto = {
            "nombre": i,
            "promedio": round(promedio/al.size(array_list),2),
            "registros": al.size(array_list),
            "menor_año": menor_año,
            "mayor_año": mayor_año,
            "menor_tiempo": menor_tiempo,
            "mayor_tiempo": mayor_tiempo,
            "survey": survey,
            "census": census
        }
        if mayor_año > mayor_año_general:
            mayor_año_general = mayor_año
        if menor_año < menor_año_general:
            menor_año_general = menor_año
        promedio_general += promedio
        insert_data_sorted(inf_deptos, inf_depto, "promedio", "departamento", orden)
    promedio_general = promedio_general/al.size(lista)
    end_time = get_time()
    tiempo = delta_time(start_time,end_time)
    respuesta = {
        "tiempo": tiempo,
        "cantidad": al.size(lista),
        "promedio": promedio_general,
        "menor año": menor_año_general,
        "mayor año": mayor_año_general,
        "inf_deptos": inf_deptos
    }
    return respuesta




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
