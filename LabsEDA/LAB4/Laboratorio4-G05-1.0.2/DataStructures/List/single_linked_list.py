import DataStructures.List.list_node as list_node

def new_list()->dict:
    '''Crea una nueva lista enlazada simple

    :return dict: devuelve la lista enlazada simple
    '''
    newlist = {
        "first": None,
        "last": None,
        "size": 0
    }
    return newlist

def cmp_function(element_1: any, element_2: any) -> int:
    '''Funcion complementaria que compara si un elemento es mayor o menor que el otro

    :param any element_1: elemento 1 a comparar
    :param any element_2: elemento 2 a comparar
    :return int: retorna 1 si es mayor el 1 con el 2, y -1 si es menor el 1 con el 2.
    '''
    if element_1 > element_2:
        return 1
    elif element_1 < element_2:
        return -1
    return 0

def get_element(my_list: dict, pos: int)->any:
    '''Encuentra el elemento en dada posicion

    :param dict my_list: lista enlazada simple
    :param int pos: indice a buscar
    :return any: devuelve la info del nodo en el indice
    '''
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list: dict, element:dict, cmp_function)->int:
    '''determina si un elemento esta presente en la lista enlazada simple

    :param dict my_list: lista enlazada simple
    :param dict element: elemento a buscar
    :param _type_ cmp_function: funcion complementaria
    :return int: retorna la cantidad de veces que el elemento se encontro
    '''
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    
    if not is_in_array:
        count = -1
    return count

def is_empty(lst: dict)->bool:
    '''determina si la lista enlazada simple esta vacia

    :param dict lst: lista enlazada simple
    :return bool: booleano que determina si esta vacia o no
    '''
    return lst["size"] == 0


def size(lst: dict)->int:
    '''El tamanio de la lista enlazada simple

    :param dict lst: lista enlazada simple
    :return int: tamanio de la lista enlazada simple
    '''
    return lst["size"]

def add_first(lst: dict, element: dict)->dict:
    '''Agrega un nodo al inicio

    :param dict lst: lista enlazada simple
    :param dict element: elemento a agregar
    :return dict: devuelve la lista enlazada simple actualizada
    '''
    nuevo_nodo = list_node.new_single_node(element)
    nuevo_nodo['next'] = lst['first']
    lst['first'] = nuevo_nodo
    
    if lst['size'] == 0:
        lst['last'] = nuevo_nodo
    lst['size'] += 1
    
    return lst #Complejidad O(1)

def add_last(lst: dict, element: dict)->dict:
    '''Agrega un nodo al final

    :param dict lst: lista enlazada simple
    :param dict element: elemento a agregar
    :return dict: devuelve la lista lista enlazada simple actualizada
    '''
    nuevo_nodo = list_node.new_single_node(element)
    
    if lst['size'] == 0:
        lst['first'] = nuevo_nodo
        lst['last'] = nuevo_nodo
    else:
        lst["last"]["next"] = nuevo_nodo  # Se enlaza el último nodo con el nuevo nodo solo si tail NO es None
        lst["last"] = nuevo_nodo

    lst['size'] += 1
    
    return lst

def first_element(lst: dict)-> dict:
    '''devuelve el primer elemento (info)

    :param dict lst: lista enlazada simple
    :raises Exception: si la lista esta vacia retorna error
    :return dict: lista enlazada simple actualizada
    '''
    resultado = None
    if is_empty(lst):
        #raise Exception('IndexError: list index out of range')
        resultado = None
    else:
        resultado = lst["first"]["info"]
    return resultado

def last_element(lst: dict)->dict:
    '''retorna el ultimo elemento (info) de la lista enlazada simple

    :param dict lst: lista enlazada simple
    :raises Exception: si la lista esta vacia retorna error
    :return dict: lista enlazada simple actualizada
    '''
    resultado = None
    if is_empty(lst):
        raise Exception('IndexError: list index out of range')
    else:
        resultado = lst["last"]["info"]
    return resultado

def remove_first(lst: dict)->int:
    '''Quita el primer nodo de la lista enlazada simple

    :param dict lst: lista enlazada simple
    :raises Exception: Error si esta vacia la lista enlazada simple
    :return int: Los tests piden que se devuelva un Int, entonces devolvemos el nuevo tamanio de la lista enlazada simple
    '''
    if is_empty(lst):
        raise Exception('IndexError: list index out of range')
    else:
        elemento_a_eliminar = lst["first"]["info"]
        nuevo_first = lst["first"]["next"]
        lst["first"] = nuevo_first
        lst["size"] -= 1
    return elemento_a_eliminar #Devuelvo size porque los tests piden un int

def remove_last(lst: dict)->int:
    '''Quita el ultimo nodo de la lista enlazada simple

    :param dict lst: lista enlazada simple
    :raises Exception: envia error si la lista enlazada simple esta vacia
    :return int: devolvemos el nuevo tamanio de la lista enlazada simple
    '''
    if is_empty(lst):
        raise Exception('IndexError: list index out of range')
    else:
        nuevo_last = lst["first"]
        for i in range(lst["size"]):
            nuevo_last = nuevo_last["next"]
        lst["last"] = nuevo_last
        lst["size"] -= 1
    return lst["size"] #Devuelvo size porque los tests piden un int

def insert_element(lst: dict, element: dict, pos: int)->dict:
    '''inserta un elemento en el indice pos dentro de la lista enlazada simple

    :param dict lst: lista enlazada simple
    :param dict element: elemento a insertar
    :param int pos: indice a insertar
    :raises Exception: retorna error si la posicion es mayor al tamanio de la lista
    :return dict: lista enlazada simple actualizada
    '''
    newlst = {
        "first": None,
        "last": None,
        "size": 0
    }
    if pos < 0 or pos > lst["size"]:
        raise Exception('IndexError: list index out of range')
    elif pos == 0:
        add_first(lst, element)
    elif pos == lst["size"]:
        add_last(lst, element)
    else:
        nodo_indice = lst["first"]
        for i in range(1, pos):
            add_last(newlst, get_element(nodo_indice))
            nodo_indice = nodo_indice["next"]
        #Insertar nodo
        element_node = {"info": element, "next": nodo_indice["next"]}
        nodo_indice["next"] = element_node
        for j in range(pos, lst["size"]+2): #Terminar de copiar los nodos siguientes
            '''O(N) Completo en todos los casos, 
            intente hacerle asignación a los next después de insertar pero se daña el formato del diccionario'''
            
            add_last(newlst, get_element(nodo_indice))
            nodo_indice = nodo_indice["next"]
    return newlst

def delete_element(lst: dict, pos: int)->dict:
    '''elimina el elemento en el indice pos

    :param dict lst: lista enlazada simple
    :param int pos: indice a eliminar
    :raises Exception: retorna error si el indice esta por fuera del rango de la lista
    :return dict: lista enlazada simple actualizada
    '''
    newlst = {
        "first": None,
        "last": None,
        "size": 0
    }
    if pos < 0 or pos > lst["size"]:
        raise Exception('IndexError: list index out of range')
    elif pos == 0:
        remove_first(lst)
    elif pos == lst["size"]:
        remove_last(lst)
    else:
        nodo_indice = lst["first"]
        for i in range(1, pos):
            add_last(newlst, get_element(nodo_indice))
            nodo_indice = nodo_indice["next"]
        #Eliminar nodo
        nodo_indice["next"] = nodo_indice["next"]["next"]
        for j in range(pos, lst["size"]+2): #Terminar de copiar los nodos siguientes
            '''O(N) Completo, intente hacerle asignación a los next después de insertar pero se daña el orden del diccionario'''
            
            add_last(newlst, get_element(nodo_indice))
            nodo_indice = nodo_indice["next"]
    return newlst

def change_info(lst: dict, pos: int, new_info: dict)->dict:
    '''Cambia informacion en un indice dado (pos)

    :param dict lst: lista enlazada simple
    :param int pos: indice a cambiar la info
    :param dict new_info: la informacion nueva
    :raises Exception: Retorna error si el indice esta por fuera del rango de la lista
    :return dict: lista enlazada simple actualizada
    '''
    newlst = {
        "first": None,
        "last": None,
        "size": 0
    }
    if pos < 0 or pos > lst["size"]:
        raise Exception('IndexError: list index out of range')
    elif pos == 0:
        lst["first"]["info"] = new_info
    elif pos == lst["size"]:
        lst["last"]["info"] = new_info
    else:
        nodo_indice = lst["first"]
        for i in range(1, pos):
            add_last(newlst, get_element(nodo_indice))
            nodo_indice = nodo_indice["next"]
        #cambiar info de nodo
        nodo_indice["info"] = new_info
        for j in range(pos, lst["size"]+2): #Terminar de copiar los nodos siguientes
            '''O(N) Completo, intente hacerle asignación a los next después de insertar pero se daña el orden del diccionario'''
            
            add_last(newlst, get_element(nodo_indice))
            nodo_indice = nodo_indice["next"]
    return newlst

def exchange(lst: dict, pos1: int, pos2: int)->dict:
    '''intercambia los valores de la posicion1 con los de la posicion2

    :param dict lst: lista enlazada simple
    :param int pos1: indice 1
    :param int pos2: indice 2
    :raises Exception: si alguna de las 2 posiciones esta fuera del rango de la lista retorna error
    :return dict: lista enlazada simple actualizada
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
        pass
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
        
        for j in range(pos, num_elements + 1):
            add_last(sublist, nodo_indice)
            nodo_indice = nodo_indice["next"]
            sublist["size"] += 1
    return sublist