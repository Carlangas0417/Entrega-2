import doctest
def new_list():
    '''
    Retorna una lista Enlaza simple vacia
    '''
    new_list = {
        'first': None,
        'last': None, 
        'size': 0,
    } #Complejidad O(1)
    return new_list

def size(lst: dict)->int:
    '''El tamanio de la lista enlazada simple

    :param dict lst: lista enlazada simple
    :return int: tamanio de la lista enlazada simple
    '''
    return lst["size"]

def is_empty(lst):
    '''
    Verifica si esta vacia
    '''
    
    return lst['size'] == 0 #Complejidad O(1)

def new_single_node(element):
    '''
    Creacion de un nodo
    '''
    
    return {'info': element, 'next': None} #Complejidad O(1)

def get_element(node):
    '''
    retorna la info del nodo
    '''
    resultado = None
    if node is not None:
        resultado = node["info"]
    return resultado #Complejidad O(1)

def add_first(lst, elemento):
    '''
    Agrega un elemento al inicio de la lista enlaada simple
    
    CREAR PRUEBAS
    >>> my_list = {'first': None, 'last': None, 'size': 0}
    >>> add_first(my_list, 10)
    {'first': {'info': 10, 'next': None}, 'last': {'info': 10, 'next': None}, 'size': 1}
    >>> add_first(my_list, 20)
    {'first': {'info': 20, 'next': {'info': 10, 'next': None}}, 'last': {'info': 10, 'next': None}, 'size': 2}
    >>> add_first(my_list, 'A')
    {'first': {'info': 'A', 'next': {'info': 20, 'next': {'info': 10, 'next': None}}}, 'last': {'info': 10, 'next': None}, 'size': 3}
    '''
    nuevo_nodo = new_single_node(elemento)
    nuevo_nodo['next'] = lst['first']
    lst['first'] = nuevo_nodo
    
    if lst['size'] == 0:
        lst['last'] = nuevo_nodo
    lst['size'] += 1
    
    return lst #Complejidad O(1)

def add_last(lst, elemento):
    '''
    Añade al final
    
    PRUEBAS
    >>> my_list = {'first': None, 'last': None, 'size': 0}
    >>> add_last(my_list, 10)
    {'first': {'info': 10, 'next': None}, 'last': {'info': 10, 'next': None}, 'size': 1}
    
    >>> add_last(my_list, 20)
    {'first': {'info': 10, 'next': {'info': 20, 'next': None}}, 'last': {'info': 20, 'next': None}, 'size': 2}
    
    >>> add_last(my_list, 'A')
    {'first': {'info': 10, 'next': {'info': 20, 'next': {'info': 'A', 'next': None}}}, 'last': {'info': 'A', 'next': None}, 'size': 3}
    
    '''
    nuevo_nodo = new_single_node(elemento)
    
    if lst['size'] == 0:
        lst['first'] = nuevo_nodo
        lst['last'] = nuevo_nodo
    else:
        lst["last"]["next"] = nuevo_nodo  # Se enlaza el último nodo con el nuevo nodo solo si tail NO es None
        lst["last"] = nuevo_nodo

        
    lst['size'] += 1
    
    return lst


def first_element(lst: dict)-> dict:
    '''devuelve el primer nodo

    :param dict lst: lista enlazada simple
    :raises Exception: si la lista esta vacia retorna error
    :return dict: lista enlazada simple actualizada
    '''
    resultado = None
    if is_empty(lst):
        raise Exception('IndexError: list index out of range')
    else:
        resultado = lst["first"]
    return resultado

def last_element(lst: dict)->dict:
    '''retorna el ultimo nodo de la lista enlazada simple

    :param dict lst: lista enlazada simple
    :raises Exception: si la lista esta vacia retorna error
    :return dict: lista enlazada simple actualizada
    '''
    resultado = None
    if is_empty(lst):
        raise Exception('IndexError: list index out of range')
    else:
        resultado = lst["last"]
    return resultado

def remove_first(lst: dict)->int:
    '''Quita el primer nodo de la lista enlazada simple

    :param dict lst: lista enlazada simple
    :raises Exception: Error si esta vacia la lista enlazada simple
    :return int: Los tests piden que se devuelva un Int, entonces devolvemos el nuevo tamanio de la lista enlazada simple
    '''
    valor = None
    if is_empty(lst):
        raise Exception('IndexError: list index out of range')
    else:
        valor = lst["first"]
        nuevo_first = lst["first"]["next"]
        lst["first"] = nuevo_first
        lst["size"] -= 1
    return valor["info"] #Devuelvo el valor que quitamos

def remove_last(lst: dict)->int:
    '''Quita el ultimo nodo de la lista enlazada simple

    :param dict lst: lista enlazada simple
    :raises Exception: envia error si la lista enlazada simple esta vacia
    :return int: devolvemos el nuevo tamanio de la lista enlazada simple
    '''
    valor = None
    if is_empty(lst):
        raise Exception('IndexError: list index out of range')
    else:
        nuevo_last = lst["first"]
        for i in range(lst["size"]-2):
            nuevo_last = nuevo_last["next"]
        lst["last"] = nuevo_last
        nuevo_last["next"] = None
        lst["size"] -= 1
        lst
    return nuevo_last["info"]


def recorrido_total(lst):
    '''
    >>> list = {'first': {'info': '10', 'next': {'info': 20, 'next': {'info': 'A', 'next': None}}}, 'last': {'info': 'A', 'next': None}, 'size': 3}
    >>> recorrido_total(list)
    10
    20
    A
    '''
    if lst["size"] > 0:
        current_node = lst["first"]
        while current_node is not None:
            print(current_node["info"])
            current_node = current_node["next"]
    pass

def get(lst, pos):
    '''
    Acceso por indices (pos)
    
    >>> my_list = {'first': None, 'last': None, 'size': 0}
    >>> get(my_list, 0)

    
    >>> my_list = {'first': {'info': 10, 'next': {'info': 20, 'next': None}}, 'last': {'info': 20, 'next': None}, 'size': 2}
    >>> get(my_list, 0)
    10
    >>> get(my_list, 1)
    20
    
    >>> my_list = {'first': {'info': 10, 'next': {'info': 20, 'next': {'info': 'A', 'next': None}}}, 'last': {'info': 'A', 'next': None}, 'size': 3}
    >>> get(my_list, 2)
    'A'
    '''
    nodo_actual = None
    if lst["first"] is not None and 0 <= pos <= lst["size"]:
        nodo_actual = lst["first"]
        
        indice = 0
        while indice < pos:
            nodo_actual=nodo_actual["next"]
            indice+=1
            
    return get_element(nodo_actual)

def find(lst, elemento):
    '''
    Encuentra el indice de la primera ocurrencia del elemento
    >>> my_list = {'first': None, 'last': None, 'size': 0}
    >>> find(my_list, 0)

    
    >>> my_list = {'first': {'info': 10, 'next': {'info': 20, 'next': None}}, 'last': {'info': 20, 'next': None}, 'size': 2}
    >>> find(my_list, 10)
    0
    >>> find(my_list, 20)
    1
    
    >>> my_list = {'first': {'info': 10, 'next': {'info': 20, 'next': {'info': 'A', 'next': None}}}, 'last': {'info': 'A', 'next': None}, 'size': 3}
    >>> find(my_list, "A")
    2
    '''
    indice = None
    encontrado = False
    if lst["first"] is not None :
        nodo_actual = lst["first"]

        indice = 0
        while indice <= lst["size"] and not encontrado:
            if get_element(nodo_actual) == elemento:
                encontrado = True
            else:
                nodo_actual=nodo_actual["next"]
                indice+=1
            
    return indice
            


def insert_element(lst: dict, element: dict, pos: int)->dict:
    '''_summary_

    :param dict lst: _description_
    :param dict element: _description_
    :param int pos: _description_
    :raises Exception: _description_
    :return dict: _description_
    
    >>> my_list = {'first': None, 'last': None, 'size': 0}
    >>> insert_element(my_list, 10,0)
    {'first': {'info': 10, 'next': None}, 'last': {'info': 10, 'next': None}, 'size': 1}
    >>> insert_element(my_list, 20, 1)
    {'first': {'info': 10, 'next': {'info': 20, 'next': None}}, 'last': {'info': 20, 'next': None}, 'size': 2}
    >>> insert_element(my_list, 'A', 2)
    {'first': {'info': 10, 'next': {'info': 20, 'next': {'info': 'A', 'next': None}}}, 'last': {'info': 'A', 'next': None}, 'size': 3}
    >>> insert_element(my_list, 0, 2)
    {'first': {'info': 10, 'next': {'info': 20, 'next': {'info': 0, 'next': {'info': 'A', 'next': None}}}}, 'last': {'info': 'A', 'next': None}, 'size': 4}

    >>> insert_element(my_list, 60, 1)
    {'first': {'info': 10, 'next': {'info': 60, 'next': {'info': 20, 'next': {'info': 0, 'next': {'info': 'A', 'next': None}}}}}, 'last': {'info': 'A', 'next': None}, 'size': 5}

    '''
    if pos < 0 or pos > lst["size"]:
        raise Exception('IndexError: list index out of range')
    elif pos == 0:
        add_first(lst, element)
    elif pos == lst["size"] or lst["size"] == 0:
        add_last(lst, element)
    else:
        nodo_indice = lst["first"]
        for i in range(pos-1):
            nodo_indice = nodo_indice["next"]
        #Insertar nodo
        element_node = new_single_node(element)
        element_node["next"] = nodo_indice["next"]
        nodo_indice["next"] = element_node
        lst["size"] +=1
    return lst

def delete_element(lst: dict, pos: int)->dict:
    '''elimina el elemento en el indice pos

    :param dict lst: lista enlazada simple
    :param int pos: indice a eliminar
    :raises Exception: retorna error si el indice esta por fuera del rango de la lista
    :return dict: lista enlazada simple actualizada

    >>> my_list = {'first': None, 'last': None, 'size': 0}
    >>> insert_element(my_list, 10,0)
    {'first': {'info': 10, 'next': None}, 'last': {'info': 10, 'next': None}, 'size': 1}
    >>> insert_element(my_list, 20, 1)
    {'first': {'info': 10, 'next': {'info': 20, 'next': None}}, 'last': {'info': 20, 'next': None}, 'size': 2}
    >>> insert_element(my_list, 'A', 2)
    {'first': {'info': 10, 'next': {'info': 20, 'next': {'info': 'A', 'next': None}}}, 'last': {'info': 'A', 'next': None}, 'size': 3}
    >>> insert_element(my_list, 0, 2)
    {'first': {'info': 10, 'next': {'info': 20, 'next': {'info': 0, 'next': {'info': 'A', 'next': None}}}}, 'last': {'info': 'A', 'next': None}, 'size': 4}

    >>> insert_element(my_list, 60, 1)
    {'first': {'info': 10, 'next': {'info': 60, 'next': {'info': 20, 'next': {'info': 0, 'next': {'info': 'A', 'next': None}}}}}, 'last': {'info': 'A', 'next': None}, 'size': 5}


    >>> delete_element(my_list, 4)
    {'first': {'info': 10, 'next': {'info': 60, 'next': {'info': 20, 'next': {'info': 0, 'next': None}}}}, 'last': {'info': 0, 'next': None}, 'size': 4}
    >>> delete_element(my_list, 0)
    {'first': {'info': 60, 'next': {'info': 20, 'next': {'info': 0, 'next': None}}}, 'last': {'info': 0, 'next': None}, 'size': 3}
    >>> delete_element(my_list, 1)
    {'first': {'info': 60, 'next': {'info': 0, 'next': None}}, 'last': {'info': 0, 'next': None}, 'size': 2}
    '''
    if pos < 0 or pos > lst["size"] or is_empty(lst):
        raise Exception('IndexError: list index out of range')
    elif pos == 0:
        remove_first(lst)
    elif pos == lst["size"]-1:
        remove_last(lst)
    else:
        nodo_indice = lst["first"]
        for i in range(pos-1):
            nodo_indice = nodo_indice["next"]
        #Insertar nodo
        nodo_indice["next"] = nodo_indice["next"]["next"]
        lst["size"] -=1
    return lst

def change_info(lst: dict, pos: int, new_info: dict)->dict:
    '''Cambia informacion en un indice dado (pos)

    :param dict lst: lista enlazada simple
    :param int pos: indice a cambiar la info
    :param dict new_info: la informacion nueva
    :raises Exception: Retorna error si el indice esta por fuera del rango de la lista
    :return dict: lista enlazada simple actualizada
    >>> my_list = {'first': None, 'last': None, 'size': 0}
    >>> insert_element(my_list, 10,0)
    {'first': {'info': 10, 'next': None}, 'last': {'info': 10, 'next': None}, 'size': 1}
    >>> insert_element(my_list, 20, 1)
    {'first': {'info': 10, 'next': {'info': 20, 'next': None}}, 'last': {'info': 20, 'next': None}, 'size': 2}
    >>> insert_element(my_list, 'A', 2)
    {'first': {'info': 10, 'next': {'info': 20, 'next': {'info': 'A', 'next': None}}}, 'last': {'info': 'A', 'next': None}, 'size': 3}
    >>> insert_element(my_list, 0, 2)
    {'first': {'info': 10, 'next': {'info': 20, 'next': {'info': 0, 'next': {'info': 'A', 'next': None}}}}, 'last': {'info': 'A', 'next': None}, 'size': 4}

    >>> insert_element(my_list, 60, 1)
    {'first': {'info': 10, 'next': {'info': 60, 'next': {'info': 20, 'next': {'info': 0, 'next': {'info': 'A', 'next': None}}}}}, 'last': {'info': 'A', 'next': None}, 'size': 5}

    >>> change_info(my_list, 0, 5)
    {'first': {'info': 5, 'next': {'info': 60, 'next': {'info': 20, 'next': {'info': 0, 'next': {'info': 'A', 'next': None}}}}}, 'last': {'info': 'A', 'next': None}, 'size': 5}
    >>> change_info(my_list, 1, 15)
    {'first': {'info': 5, 'next': {'info': 15, 'next': {'info': 20, 'next': {'info': 0, 'next': {'info': 'A', 'next': None}}}}}, 'last': {'info': 'A', 'next': None}, 'size': 5}
    >>> change_info(my_list, 2, 25)
    {'first': {'info': 5, 'next': {'info': 15, 'next': {'info': 25, 'next': {'info': 0, 'next': {'info': 'A', 'next': None}}}}}, 'last': {'info': 'A', 'next': None}, 'size': 5}
    >>> change_info(my_list, 4, 30)
    {'first': {'info': 5, 'next': {'info': 15, 'next': {'info': 25, 'next': {'info': 0, 'next': {'info': 30, 'next': None}}}}}, 'last': {'info': 30, 'next': None}, 'size': 5}

    '''
    if pos < 0 or pos > lst["size"] or is_empty(lst):
        raise Exception('IndexError: list index out of range')
    elif pos == 0:
        lst["first"]["info"] = new_info
    elif pos == lst["size"]-1:
        lst["last"]["info"] = new_info
    else:
        nodo_indice = lst["first"]
        for i in range(pos):
            nodo_indice = nodo_indice["next"]
        #cambiar info de nodo
        nodo_indice["info"] = new_info
    return lst

def exchange(lst: dict, pos1: int, pos2: int)->dict:
    '''intercambia los valores de la posicion1 con los de la posicion2

    :param dict lst: lista enlazada simple
    :param int pos1: indice 1
    :param int pos2: indice 2
    :raises Exception: si alguna de las 2 posiciones esta fuera del rango de la lista retorna error
    :return dict: lista enlazada simple actualizada

    >>> my_list = {'first': None, 'last': None, 'size': 0}
    >>> add_last(my_list, 10)
    {'first': {'info': 10, 'next': None}, 'last': {'info': 10, 'next': None}, 'size': 1}
    >>> add_last(my_list, 20)
    {'first': {'info': 10, 'next': {'info': 20, 'next': None}}, 'last': {'info': 20, 'next': None}, 'size': 2}
    >>> add_last(my_list, 'A')
    {'first': {'info': 10, 'next': {'info': 20, 'next': {'info': 'A', 'next': None}}}, 'last': {'info': 'A', 'next': None}, 'size': 3}
    >>> exchange(my_list, 0, 2)
    {'first': {'info': 'A', 'next': {'info': 20, 'next': {'info': 10, 'next': None}}}, 'last': {'info': 10, 'next': None}, 'size': 3}
    >>> exchange(my_list, 0, 1)
    {'first': {'info': 20, 'next': {'info': 'A', 'next': {'info': 10, 'next': None}}}, 'last': {'info': 10, 'next': None}, 'size': 3}
    '''
    if pos1 < 0 or pos1 > size(lst) or pos2 < 0 or pos2 > size(lst):
        raise Exception('IndexError: list index out of range')
    elif (pos1 == 0 and pos2 == size(lst)) or (pos2 == 0 and pos1 == size(lst)):
        primero = get_element(lst["first"])
        ultimo = get_element(lst["last"])
        remove_first(lst)
        remove_last(lst)
        add_first(lst, primero)
        add_last(ultimo)
    else:
        primer_elemento = lst["first"]
        segundo_elemento = lst["first"]

        for i in range(pos1):
            primer_elemento = primer_elemento["next"]
        for k in range(pos2):
            segundo_elemento = segundo_elemento["next"]
        info1 = primer_elemento["info"]
        info2 = segundo_elemento["info"]
        primer_elemento["info"] = info2
        segundo_elemento["info"] = info1
        if(pos2 == size(lst)-1):
            lst["last"]["info"] = segundo_elemento["info"]
    return lst

def sub_list(lst: dict, pos: int, num_elements: int)->dict:
    '''Genera sublista a partir del indice pos por una cantidad de elementos definida

    :param dict lst: lista enlazada simple
    :param int pos: indice donde empieza la sublista
    :param int num_elements: elementos consecuentes a aniadir
    :raises Exception: si la posicion no es valida retorna error
    :return dict: sublista enlazada simple
    '''
    if pos < 0 or pos >= lst["size"]:
        raise Exception('IndexError: list index out of range')
    else:
        sublist = {
            "first": None,
            "last": None,
            "size": 0
        }
        nodo_indice = lst["first"]
        for i in range(0, pos):
            nodo_indice = nodo_indice["next"]
        
        for j in range(pos, pos + num_elements):
            add_last(sublist, nodo_indice)
            nodo_indice = nodo_indice["next"]
            sublist["size"] += 1
    return sublist