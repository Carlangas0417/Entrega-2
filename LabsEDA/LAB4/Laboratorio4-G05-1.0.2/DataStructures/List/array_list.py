def new_list()->dict:
    '''Crea un nuevo array list

    :return dict: array list
    '''
    newlist = {
        "elements": [],
        "size": 0
    }
    return newlist

def get(lst: dict, element: any)->list:
    '''devuelve los indices del elemento encontrado

    :param dict lst: lista
    :param any element: elemento a buscar
    :return int: indice del elemento
    '''
    i = 0
    elementos = []
    while i < size(lst):
        if lst["elements"][i] == element:
            elementos.append(element)
        i+=1
    return elementos

def get_element(my_list: dict, pos: int)->any:
    '''Retorna el elemento en dado indice

    :param dict my_list: array list
    :param int index: indice
    :return any: elemento en el indice del array list
    '''
    
    if 0 <= pos < size(my_list):
        return my_list["elements"][pos]
    else:
        raise Exception ("IndexError: list index out of range")

def cmp_function(element_1: any, element_2: any) -> int:
    '''funcion complementaria que compara 2 elementos

    :param any element_1: elemento 1
    :param any element_2: elemento 2
    :return int: retorna un entero dependiendo de quien es mas grande
    '''
    if element_1 > element_2:
        return 1
    elif element_1 < element_2:
        return -1
    return 0

def is_present(my_list: dict, element:any, cmp_function:any)->int:
    '''Encuentra la cantidad de ocurrencias de un elemento

    :param dict my_list: array list
    :param any element: elemento a buscar
    :param any cmp_function: funcion complementaria
    :return int: cuenta del elemento
    '''
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos 
    return -1

def is_empty(lst: dict)->bool:
    '''Determina si el array list esta vacio

    :param dict lst: array list
    :return bool: retorna si esta vacio o no
    '''
    return lst["size"] == 0

def add_first(lst: dict, element: any)-> dict:
    '''agrega al inicio del array list

    :param dict lst: array list
    :param any element: elemento a agregar
    :return dict: array list actualizado
    '''
    lst["elements"].insert(0, element)
    lst["size"] += 1
    return lst

def add_last(lst:dict, element:any)->dict:
    '''agrega al final del array list

    :param dict lst: array list
    :param any element: elemento a agregar
    :return dict: array list actualizado
    '''
    lst["elements"].append(element)
    lst["size"] += 1
    return lst

def size(lst: dict)->int:
    '''Tamanio del array list

    :param dict lst: array list
    :return int: tamanio
    '''
    return lst["size"]

def first_element(lst: dict)->any:
    '''Encuentra el primer elemento del array list

    :param dict lst: array list
    :raises Exception: si esta vacio, no hay primer elemento
    :return any: el primer elemento
    '''
    resultado = None
    if is_empty(lst):
        raise Exception('IndexError: list index out of range')
    else:
        resultado = lst["elements"][0]
    return resultado

def last_element(lst: dict)->any:
    '''Encuentra el ultimo elemento del array list

    :param dict lst: array list
    :raises Exception: si esta vacio, no hay ultimo elemento
    :return any: el ultimo elemento
    '''
    resultado = None
    if is_empty(lst):
        raise Exception('IndexError: list index out of range')
    else:
        resultado = lst["elements"][-1]
    return resultado

def remove_first(lst: dict)->int:
    '''Quita el primer elemento del array list

    :param dict lst: array list
    :raises Exception: si esta vacio, no hay que quitar
    :return int: devuelve el elemento que quitamos
    '''
    if is_empty(lst):
        raise Exception('IndexError: list index out of range')
    else:
        lst["size"] -= 1
        rta = lst["elements"].pop(0)
        return rta

def remove_last(lst: dict)->int:
    '''Quita el ultimo elemento del array list

    :param dict lst: array list
    :raises Exception: si esta vacio, no hay que quitar
    :return int: devuelve el elemento que quitamos
    '''
    if is_empty(lst):
        raise Exception('IndexError: list index out of range')
    else:
        lst["size"] -= 1
        rta = lst["elements"].pop(-1) 
        return rta

def insert_element(lst: dict, element: any, pos: int)->dict:
    '''Inserta un elemento en un indice dado

    :param dict lst: array list
    :param any element: elemento a insertar
    :param int pos: indice a insertar
    :raises Exception: si el indice es no valido, retorna error
    :return dict: array list actualizado
    '''
    if pos <= 0 or pos > size(lst):
        raise Exception('IndexError: list index out of range')
    else:
        lst["elements"].insert(pos, element)
        lst["size"] += 1
    return lst

def delete_element(lst: dict, pos: int)-> dict:
    '''Quita un elemento dado un indice

    :param dict lst: array list
    :param int pos: indice a remover
    :raises Exception: si el indice no es valido, retorna error
    :return dict: array list actualizado
    '''
    if pos <= 0 or pos > size(lst):
        raise Exception('IndexError: list index out of range')
    else:
        lst["elements"].pop(pos)
        lst["size"] -= 1
    return lst

def change_info(lst: dict, pos: int, new_info: any)->dict:
    '''Intercambia la informacion del indice con una info nueva

    :param dict lst: array list
    :param int pos: indice
    :param any new_info: la nueva info con la que vamos a reemplazar
    :raises Exception: si la posicion no es valida, lanza error
    :return dict: array list actualizada
    '''
    if pos <= 0 or pos > size(lst):
        raise Exception('IndexError: list index out of range')
    else:
        lst["elements"][pos] = new_info
    return lst

def exchange(lst: dict, pos1: int, pos2: int)->dict:
    '''Intercambia los datos de pos1 con pos 2 y viceversa

    :param dict lst: array list
    :param int pos1: posicion dato1
    :param int pos2: posicion dato2
    :raises Exception: si las posiciones no son validas, retorna error
    :return dict: array list actualizada
    '''
    if pos1 < 0 or pos1 >= size(lst) or pos2 < 0 or pos2 >= size(lst):
        raise Exception('IndexError: list index out of range')
    else:
        element1 = lst["elements"][pos1]
        element2 = lst["elements"][pos2]
        
        lst["elements"][pos1] = element2
        lst["elements"][pos2] = element1
        
    return lst

def sub_list(lst: dict, pos: int, num_elements: int) -> dict:
    '''Genera una sublista array desde el indice pos con los elementos consecuentes hasta llegar a num_elements

    :param dict lst: array list
    :param int pos: indice donde empieza
    :param int num_elements: cantidad de elementos a agregar
    :raises Exception: lanza error si la posicion no es valida
    :return dict: array sublist
    '''
    sublist = {
        "size": 0,
        "elements": []
    }
    if pos < 0 or pos >= size(lst):
        raise Exception('IndexError: list index out of range')
    else:
        for i in range(pos, pos + num_elements + 1):
            sublist["elements"].append(lst["elements"][i])
            sublist["size"] += 1
    return sublist