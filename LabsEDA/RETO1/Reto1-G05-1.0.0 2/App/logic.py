import os
import csv
from datetime import datetime, date
import time
#import pandas as pd
#import matplotlib.pyplot as plt


from DataStructures.set import Set as st
from DataStructures.List import array_list as arr
from DataStructures.List import single_linked_list as sll
from DataStructures.Stack import stack as stk
from DataStructures.Queue import queue as q


csv.field_size_limit(2147483647) 

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Challenge1'


def new_logic():
    """
    Inicializa los datos y crea un catalogo vacio. 

    Para esta actividad, un catalogo es un diccionario donde se guardan
    las estructuras de datos que representan...


    :return: Catalogo inicializado
    :rtype: dict
    """

    # Creación del catalogo vacio
    catalog = {
        "registro": None
    }
    
    catalog["registro"] = arr.new_list()
    
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename: str)->tuple:
    '''Carga los datos del reto de los archivos propuestos de agricultural-100.csv

    :param DataStructure catalog: catalogo
    :param str filename: ruta al archivo
    :return tuple: el registro, menor_year, mayor_year, primeros5, ultimos5, time
    '''
    registro = catalog["registro"]
    registros_file = os.path.join(data_dir, filename)
    time = 0
    start = get_time()
    menor_year = 1000000
    mayor_year = 0
    head = []
    tail = []
    if (registro is not None and filename is not None):
        input_file = csv.DictReader(open(registros_file, encoding="utf-8"),
                                    delimiter=",")
        for line in input_file:
            arr.add_last(registro, line)
            if(int(line["year_collection"]) > mayor_year):
                mayor_year = int(line["year_collection"])
            if(int(line["year_collection"]) < menor_year):
                menor_year = int(line["year_collection"])
        head = arr.sub_list(registro, 0, 4)
        tail = arr.sub_list(registro, arr.size(registro)-5, 5)        
    end = get_time()
    time = round(delta_time(start, end),3)
    return catalog["registro"], menor_year, mayor_year, head, tail, time

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    return catalog["elements"][id]


def req_1(catalog, year: int) -> tuple:
    '''Identifica el último registro recopilado de la plataforma para mi año de 
    interés.
    
    utilice la fecha de carga del registro como referencia para 
    encontrar el registro más reciente. No es necesario hacer ordenamientos.

    :param DataStructure catalog: catalogo con la informacion
    :param int year: Anio
    :return tuple: registro_mas_reciente, tiempo, registros_que_pasaron_el_filtro
    '''
    time = 0
    start = get_time()
    reciente  = datetime.strptime("1040-12-31 23:59:59", "%Y-%m-%d %H:%M:%S")
    rta = None
    contador = 0
    elementos = catalog["registro"]
    for i in range(arr.size(catalog["registro"])):
        elemento = arr.get_element(elementos, i)
        anio_registro = int(elemento["year_collection"])
        fecha_registro = datetime.strptime(elemento["load_time"],"%Y-%m-%d %H:%M:%S")
        if anio_registro == int(year):
            contador += 1
            if fecha_registro >= reciente:
                reciente = fecha_registro
                rta = elemento
    end = get_time()
    time = round(delta_time(start, end),3)
    return rta, time, contador


def req_2(catalog, departamento: str) -> tuple:
    '''identificar el último registro cargado a la plataforma para mi 
    departamento de interés. 
    
    utilice la fecha de carga del registro como referencia para 
    encontrar el registro más reciente. No es necesario hacer ordenamientos.

    :param DataStructure catalog: catalogo
    :param str departamento: departamento
    :return tuple: ultimo_departamento_encontrado, tiempo, registros_que_pasaron_el_filtro
    '''
    time = 0
    start = get_time()
    reciente = datetime.strptime("1040-12-31 23:59:59", "%Y-%m-%d %H:%M:%S")
    rta = None
    contador = 0
    elementos = catalog["registro"]
    for i in range(arr.size(catalog["registro"])):
        elemento = arr.get_element(elementos, i)
        depto_registro = elemento["state_name"].lower()
        fecha_registro = datetime.strptime(elemento["load_time"],"%Y-%m-%d %H:%M:%S")
        if depto_registro == departamento.lower():
            contador += 1
            if fecha_registro >= reciente:
                reciente = fecha_registro
                rta = elemento
    end = get_time()
    time=round(delta_time(start, end),3)
    return rta, time, contador

#Req Alejo
def req_3(catalog, departamento: str, year_inicial: int, year_final: int) -> tuple:
    '''consulta los registros recopilados para mi departamento de interés 
    en un rango de años de recopilación dado.

    :param DataStructure catalog: catalogo
    :param str departamento: departamento
    :param int year_inicial: rango anio inicial
    :param int year_final: rango anio final 
    :return tuple: tiempo, contador_survey, contador_censo, registros_que_pasaron_el_filtro
    '''
    inicio = get_time()
    contador_surv = 0
    contador_censo = 0
    elementos = catalog["registro"]
    rta = q.new_queue()
    for i in range(arr.size(catalog["registro"])):
        elemento = arr.get_element(elementos, i)
        anio = int(elemento["year_collection"])
        if elemento["state_name"].lower() == departamento and year_inicial <= anio <= year_final:
            if elemento["source"] == "SURVEY":
                contador_surv += 1 
            else:
                contador_censo += 1
            q.enqueue(rta, elemento)
    final = get_time()  
    tiempo = round(delta_time(inicio, final), 3)
    return tiempo, contador_surv, contador_censo, rta
    

def req_4(catalog, tipo: str, year_inicial: int, year_final: int)->tuple:
    '''consultar los registros recopilados para un tipo de producto de mi 
    interés dado un rango de años de recopilación dado.

    :param DataStructure catalog: catalogo
    :param str tipo: tipo de registro
    :param int year_inicial: rango anio inicial
    :param int year_final: rango anio final
    :return tuple: registros_que_pasaron, survey_count, census_count, time
    '''
     #Implementación GABO
    time = 0
    start = get_time()
    results = q.new_queue()
    survey_count = 0
    census_count = 0
    elementos = catalog["registro"]
    for i in range(arr.size(catalog["registro"])):
        elemento = arr.get_element(elementos, i)
        if elemento["commodity"].lower() == tipo.lower() and int(year_inicial) <= int(elemento["year_collection"]) <= int(year_final):
            if elemento["source"] == "SURVEY":
                survey_count+=1
            else:
                census_count+=1
            q.enqueue(results, elemento)
    end = get_time()
    time = round(delta_time(start, end),3)
    return results, survey_count, census_count, time


def req_5(catalog, categoria: str, year_inicial: int, year_final: int)->tuple:
    '''consulta los registros recopilados para una categoría estadística de mi 
    interés entre un rango de años de recopilación dado. 

    :param DataStructure catalog: catalogo
    :param str categoria: categoria del registro
    :param int year_inicial: rango anio inicial
    :param int year_final: rango anio final
    :return tuple: registros_que_pasaron, survey_count, census_count, time
    '''
    time = 0
    start = get_time()
    results = q.new_queue()
    survey_count = 0
    census_count = 0
    elementos = catalog["registro"]
    for i in range(arr.size(catalog["registro"])):
        elemento = arr.get_element(elementos, i)
        if elemento["statical_category"].lower() == categoria.lower() and int(year_inicial) <= int(elemento["load_time"][:4]) <= int(year_final):
            if(elemento["source"] == "SURVEY"):
                survey_count+=1
            else:
                census_count+=1
            q.enqueue(results, elemento)
    end = get_time()
    time = round(delta_time(start, end),3)
    return results, survey_count, census_count, time

def convertirPeriodo(periodo: str)->int:
    fecha = periodo[0:10]
    fecha = fecha.split("-")
    fecha = int(fecha[0])*10000+ int(fecha[1])*100+int(fecha[2])
    return fecha
    

def req_6(catalog, departamento: str, periodo_inicial: str, periodo_final: str)->tuple:
    '''analiza la estadística del departamento de mi interés para un rango de 
    fechas de carga de los registros dado. 

    :param DataStructure catalog: catalogo
    :param str departamento: departamento
    :param str periodo_inicial: rango periodo inicial
    :param str periodo_final: randio periodo final
    :return tuple: registros_que_pasaron, survey_count, census_count, time
    '''
    time = 0
    start = get_time()
    results = q.new_queue()
    survey_count = 0
    census_count = 0
    elementos = catalog["registro"]
    for i in range(arr.size(catalog["registro"])):
        elemento = arr.get_element(elementos, i)
        fecha = datetime.strptime(elemento["load_time"][:10], "%Y-%m-%d")
        if elemento["state_name"].lower() == departamento.lower():
            if periodo_inicial <= fecha <= periodo_final:
                if(elemento["source"] == "SURVEY"):
                    survey_count+=1
                else:
                    census_count+=1
                q.enqueue(results, elemento)
    end = get_time()
    time=round(delta_time(start, end),3)
    return results, survey_count, census_count, time


def req_7(catalog, departamento: str, year_inicial: int, year_final: int)->tuple:
    '''  conocer el año con mayor y menor ingresos para un departamento en un 
    departamento de mi interés en un rango de fechas de recolección de los registros dado. Para esta consulta, tenga 
    en cuenta los registros cuya unidad de medida contenga un “$”.

    :param DataStructure catalog: catalogo
    :param str departamento: departamento
    :param int year_inicial: rango anio inicial
    :param int year_final: rango anio final
    :return tuple: registros_que_pasaron, survey_count, census_count, anioMaximo, anioMinimo, valorMaximo, valorMinimo, contador_valores_invalidos, time
    '''
    time = 0
    start = get_time()
    results = q.new_queue()
    year_data = {} #TODO cambiar array_list o single_linked, pero creo que no se puede, seria con HASHTABLE pero no cuenta para este proyecto
    survey_count = {}
    census_count = {}
    contador_invalido = {}
    elementos = catalog["registro"]["elements"]
    for i in range(arr.size(catalog["registro"])):
        if elementos[i]["state_name"].lower() == departamento.lower() and int(year_inicial) <= int(elementos[i]["year_collection"]) <= int(year_final):
            if(elementos[i]["source"] == "SURVEY"):
                    if(elementos[i]["year_collection"] in list(survey_count.keys())):
                        survey_count[elementos[i]["year_collection"]]+=1
                    else:
                        survey_count[elementos[i]["year_collection"]]=1
            elif (elementos[i]["source"] == "CENSUS"):
                    if(elementos[i]["year_collection"] in list(census_count.keys())):
                        census_count[elementos[i]["year_collection"]]+=1
                    else:
                        census_count[elementos[i]["year_collection"]]=1 
            if(elementos[i]["value"][0] != "(" and elementos[i]["value"][0] != '$'):
                valor = elementos[i]["value"]
                valor = valor.replace(",", "")
                valor = float(valor)
               
                if(elementos[i]["year_collection"] in list(year_data.keys())):
                    year_data[elementos[i]["year_collection"]] += valor
                else:
                    year_data[elementos[i]["year_collection"]] = valor
            else:
                if(elementos[i]["year_collection"] in list(contador_invalido.keys())):
                    contador_invalido[elementos[i]["year_collection"]]+=1
                else:
                    contador_invalido[elementos[i]["year_collection"]]=1
            q.enqueue(results, elementos[i])
    
    maxVal = list(year_data.keys())[0] #TODO MIRAR SI SE PUEDE CAMBIAR A TAD, es decir a array list o linked list o set o lo que sea sin usar diccionarios directamente.
    minVal = maxVal
    for k in list(year_data.keys()):
        if year_data[k] > year_data[maxVal]:
            maxVal = k
        if year_data[k] < year_data[minVal]:
            minVal = k
        
    end = get_time()
    time=round(delta_time(start, end),3)
    return results, survey_count[maxVal], survey_count[minVal], census_count[maxVal], survey_count[minVal], maxVal, minVal, year_data[maxVal], year_data[minVal], contador_invalido[maxVal], contador_invalido[minVal], time


def req_8(catalog):
    """
    conocer el cuál es el departamento con mayor diferencia promedio de 
    tiempo entre la recopilación de los registros y su carga a la plataforma de entre todos los registros. Para el cálculo 
    de los tiempos tenga en cuenta solo el año de la carga de datos y el año de recopilación de los datos.
    """
    time = 0
    start = get_time()
    departamentos = st.new_set()
    survey_count = 0
    census_count = 0
    menor_total=0
    mayor_total=0
    mediana=0
    elementos = catalog["registro"]["elements"]
    for i in range(arr.size(catalog["registro"])):
        fecha_menor= arr.new_list()
        fecha_mayor= arr.new_list()
        departamento=str(elementos[i]["state_name"].lower())
        nodo_departamento={departamento:arr.new_list()}
        st.add_element(departamentos, nodo_departamento)
        recopilacion = elementos[i]["load_time"][0:4]
        fecha_indicada = int(recopilacion[0])*1000+ int(recopilacion[1])*100+int(recopilacion[2])*10+int(recopilacion[3])
        promedio = abs(int(fecha_indicada) - int(elementos[i]["year_collection"]))
        fecha=elementos[i]["year_collection"].lower()
        if fecha_mayor["elements"][0]==None:
            fecha_mayor["elements"][0]=int(fecha)
        elif fecha>fecha_mayor["elements"][0]:
            fecha_mayor["elements"][0]=int(fecha)
        elif fecha_menor["elements"][0]==None:
            fecha_menor["elements"][0]=int(fecha)
        else:
            if fecha<fecha_menor["elements"][0]:
                fecha_menor["elements"][0]=int(fecha)
        if nodo_departamento["elements"][0]==None:
            nodo_departamento["elements"][0]=promedio
        else: 
            if nodo_departamento["elements"][0]<promedio:
               nodo_departamento["elements"][0]=promedio
        if nodo_departamento in departamentos["elements"]:
            arr.add_last(nodo_departamento, fecha_menor)
            arr.add_last(nodo_departamento, fecha_mayor)
            if fecha_mayor["elements"][0]>mayor_total:
                mayor_total=fecha_mayor["elements"][0]
            elif menor_total==0:
                menor_total=fecha_menor["elements"][0]
            else:
                if fecha_menor["elements"][0]<menor_total:
                    menor_total=fecha_menor["elements"][0]
        if(elementos[i]["source"] == "SURVEY"):
                survey_count+=1
        else:
                census_count+=1
    departamentos_totales=st.size(departamentos)
    for j in range(st.size(departamentos)):
        if departamentos["elements"][j]["elements"][0]>mediana:
            mediana=departamentos["elements"][j]["elements"][0]
    end = get_time()
    time=round(delta_time(start, end),3)
    
    inicio = get_time()
    info_retorno = {
        "time": 0, "contador_depto": 0, "prom_tiempo": 0, "menor_año": 10000, "mayor_año": 0, "info_depto": {}
    }
    deptos = {}
    elementos = catalog["registro"]
    for i in range(arr.size(elementos)):
        elemento = arr.get_element(elementos, i)  
        if elemento["value"] != "(D)" and elemento["value"] != "$":
            estado = elemento["state_name"]
            if elemento["state_name"] not in deptos:
                deptos[estado] = {
                    "registros": arr.new_list(),
                    "promedio_rec_carga": 0,
                    "tiempo": 0,
                    "menor_año": 100000, 
                    "mayor_año": 0,
                    "menor_diferencia": 1000000,
                    "mayor_diferencia": 0,
                    "survey": 0,
                    "census": 0
                    }
            depto = deptos[estado]
            arr.add_last(depto, elemento)
            if elemento["year_collection"] < depto["menor_año"]:
                depto["state_name"] = elemento["year_collection"]
            if elemento["year_collection"] > depto["mayor_año"]:
                depto["state_name"] = elemento["year_collection"]
            if elemento["year_collection"] < info_retorno["menor_año"]:
                elemento["state_name"] = elemento["year_collection"]
            if elemento["year_collection"] > info_retorno["mayor_año"]:
                elemento["state_name"] = elemento["year_collection"]
            
            if elemento["source"] == "SURVEY":
                depto["survey"] +=1
            else:
                depto["census"] += 1
                
            diferencia_carga =abs(elemento["year_collection"] - elemento["load_time"][:4])
            depto["tiempo"] += diferencia_carga
            
            if diferencia_carga < depto["menor_diferencia"]:
                depto["menor_diferencia"] = diferencia_carga
            if diferencia_carga > depto["mayor_diferencia"]:
                depto["mayor_diferencia"] = diferencia_carga
            
    peor_depto = ""
    peor_promedio = 0
    prom = 0
    for depto in deptos:
        nombre = depto
        depto = deptos[depto]
        depto["promedio_rec_carga"] = depto["tiempo"] / arr.size(depto["registros"])
        prom += depto["promedio_rec_carga"]
        if depto["promedio_rec_carga"] > peor_promedio:
            peor_promedio = depto["promedio_rec_carga"]
            peor_depto = nombre
    
    info_retorno["contador_depto"] = len(deptos)
    info_retorno["prom_tiempo"] = prom / len(deptos)
    
    
    
    fin = get_time()
    time = round(delta_time(inicio, fin),3)
    return departamentos, departamentos_totales, survey_count, census_count, time, menor_total, mayor_total, mediana



# Funciones para medir tiempos de ejecucion

def get_time():
    '''devuelve el instante tiempo de procesamiento en milisegundos

    :return float: tiempo en ms
    '''
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    '''devuelve la diferencia entre tiempos de procesamiento muestreados

    :param float start: inicio
    :param float end: final
    :return float: diferencia entre inicio y final
    '''
    elapsed = float(end - start)
    return elapsed
