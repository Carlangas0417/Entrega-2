import doctest

def new_double_node(element):
    """
    Crea un nodo para una lista doblemente enlazada.
    """
    return {"info": element, "next": None, "prev": None}

def new_double_list():
    """
    Crea una lista doblemente enlazada vacía con nodos centinela.
    """
    header = {"info": None, "next": None, "prev": None}  # Nodo centinela inicial
    trailer = {"info": None, "next": None, "prev": header}  # Nodo centinela final
    header["next"] = trailer

    return {"header": header, "trailer": trailer, "size": 0}

def is_empty(my_list):
    """
    Verifica si la lista doblemente enlazada está vacía.
    """
    return my_list["size"] == 0

def size(my_list):
    """
    Retorna el tamaño de la lista doblemente enlazada.
    """
    return my_list["size"]

def add_last(my_list, element):
    """
    Agrega un elemento al final de la lista doblemente enlazada.
    """
    new_node = new_double_node(element)

    new_node["prev"] = my_list["trailer"]["prev"]
    new_node["next"] = my_list["trailer"]
    my_list["trailer"]["prev"]["next"] = new_node
    my_list["trailer"]["prev"] = new_node

    if my_list["size"] == 0:
        my_list["header"]["next"] = new_node
    my_list["size"] += 1
    return my_list

def get_element(my_list, pos):
    """
    Retorna la información del elemento en la posición especificada de la lista doblemente enlazada.
    """
    result = None
    if 0 <= pos < my_list["size"]:
        current = my_list["header"]["next"]
        for _ in range(pos):
            current = current["next"]
        result = current["info"]
    return result

def delete_element(my_list, pos):
    if 0 <= pos < my_list["size"]:
        current = my_list["header"]["next"]
        for _ in range(pos):
            current = current["next"]
    previous = current['prev']
    next = current['next']
    previous['next'] = next
    next['previous'] = previous
    my_list['size'] -= 1


def delete_element2(my_list, current):
    previous = current['prev']
    next = current['next']
    previous['next'] = next
    next['previous'] = previous
    my_list['size'] -= 1

def remove_duplicates(my_list):
    """
    Elimina los nodos duplicados *consecutivos* en una lista doblemente enlazada *ordenada*.
    No afecta el orden original de los elementos.
    
    La función modifica la lista *en sitio* y *no retorna nada*.

    :param my_list: Lista doblemente enlazada ordenada.
    :type my_list: dict

    >>> my_list = new_double_list()  # Caso 1: Lista vacía (no debe modificarse)
    >>> remove_duplicates(my_list)
    >>> is_empty(my_list)
    True

    >>> my_list = new_double_list()  # Caso 2: Lista con un solo elemento (no debe modificarse)
    >>> add_last(my_list, 10) is not None
    True
    >>> remove_duplicates(my_list)
    >>> get_element(my_list, 0) == 10
    True
    >>> size(my_list) == 1
    True

    >>> my_list = new_double_list()  # Caso 3: Lista sin duplicados (debe permanecer igual)
    >>> add_last(my_list, 1) is not None
    True
    >>> add_last(my_list, 2) is not None
    True
    >>> add_last(my_list, 3) is not None
    True
    >>> remove_duplicates(my_list)
    >>> get_element(my_list, 0) == 1
    True
    >>> get_element(my_list, 1) == 2
    True
    >>> get_element(my_list, 2) == 3
    True
    >>> size(my_list) == 3
    True

    >>> my_list = new_double_list()  # Caso 4: Lista con duplicados consecutivos (debe eliminarlos)
    >>> add_last(my_list, 1) is not None
    True
    >>> add_last(my_list, 2) is not None
    True
    >>> add_last(my_list, 2) is not None
    True
    >>> add_last(my_list, 3) is not None
    True
    >>> add_last(my_list, 3) is not None
    True
    >>> add_last(my_list, 3) is not None
    True
    >>> remove_duplicates(my_list)
    >>> get_element(my_list, 0) == 1
    True
    >>> get_element(my_list, 1) == 2
    True
    >>> get_element(my_list, 2) == 3
    True
    >>> size(my_list) == 3
    True

    >>> my_list = new_double_list()  # Caso 5: Lista con todos los elementos iguales (debe dejar solo uno)
    >>> add_last(my_list, 5) is not None
    True
    >>> add_last(my_list, 5) is not None
    True
    >>> add_last(my_list, 5) is not None
    True
    >>> remove_duplicates(my_list)
    >>> get_element(my_list, 0) == 5
    True
    >>> size(my_list) == 1
    True
    """
    if not(size(my_list) in [0,1]):
        current_node = my_list['header']['next']
        previous_node = my_list['header']
        while current_node != None: 
            if previous_node['info'] == current_node['info']:
                delete_element2(my_list, current_node)
            previous_node = current_node
            current_node = current_node['next']
doctest.run_docstring_examples(remove_duplicates, globals(), verbose=True)



