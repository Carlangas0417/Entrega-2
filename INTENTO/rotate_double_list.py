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

def add_first(my_list, element):
    """
    Agrega un elemento al inicio de la lista doblemente enlazada.
    """
    new_node = new_double_node(element)

    new_node["next"] = my_list["header"]["next"]
    new_node["prev"] = my_list["header"]
    my_list["header"]["next"]["prev"] = new_node
    my_list["header"]["next"] = new_node

    if my_list["size"] == 0:
        my_list["trailer"]["prev"] = new_node

    my_list["size"] += 1

    return my_list

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

def first_element(my_list):
    """
    Retorna la información del primer elemento de la lista doblemente enlazada.
    """
    return None if is_empty(my_list) else my_list["header"]["next"]["info"]

def last_element(my_list):
    """
    Retorna la información del último elemento de la lista doblemente enlazada.
    """
    return None if is_empty(my_list) else my_list["trailer"]["prev"]["info"]

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

def size(my_list):
    """
    Retorna el tamaño de la lista doblemente enlazada.
    """
    return my_list["size"]


def last_element_node(my_list):
    """
    Retorna la información del último elemento de la lista doblemente enlazada.
    """
    return None if is_empty(my_list) else my_list["trailer"]["prev"]

def rotate_double_list(my_list, k):
    """
    Rota la lista doblemente enlazada `k` posiciones a la derecha si `k` es positivo,
    o a la izquierda si `k` es negativo.

    :param my_list: Lista doblemente enlazada.
    :type my_list: dict
    :param k: Número de posiciones a rotar (positivo para la derecha, negativo para la izquierda).
    :type k: int

    >>> my_list = new_double_list()  # Caso 1: Lista vacía, no debe modificarse
    >>> rotate_double_list(my_list, 3)
    >>> is_empty(my_list)
    True

    >>> my_list = new_double_list()  # Caso 2: Lista con un solo elemento, no cambia
    >>> add_last(my_list, 42) is not None
    True
    >>> rotate_double_list(my_list, 2)
    >>> first_element(my_list) == 42 and last_element(my_list) == 42
    True

    >>> my_list = new_double_list()  # Caso 3: Lista con 2 elementos, rotar más veces que su tamaño (equivalente a 1 rotación)
    >>> add_last(my_list, 1) is not None
    True
    >>> add_last(my_list, 2) is not None
    True
    >>> rotate_double_list(my_list, 3)  # 3 % 2 = 1 rotación efectiva
    >>> first_element(my_list) == 2 and last_element(my_list) == 1
    True

    >>> my_list = new_double_list()  # Caso 4: Lista con 3 elementos, rotación normal (1 posición)
    >>> add_last(my_list, 1) is not None
    True
    >>> add_last(my_list, 2) is not None
    True
    >>> add_last(my_list, 3) is not None
    True
    >>> rotate_double_list(my_list, 1)
    >>> first_element(my_list) == 3 and get_element(my_list, 1) == 1 and last_element(my_list) == 2
    True

    >>> my_list = new_double_list()  # Caso 5: Lista con 3 elementos, rotación negativa (izquierda)
    >>> add_last(my_list, 'A') is not None
    True
    >>> add_last(my_list, 'B') is not None
    True
    >>> add_last(my_list, 'C') is not None
    True
    >>> rotate_double_list(my_list, -1)
    >>> first_element(my_list) == 'B' and get_element(my_list, 1) == 'C' and last_element(my_list) == 'A'
    True

    >>> my_list = new_double_list()  # Caso 6: Lista con 4 elementos, rotación de tamaño completo (sin cambios)
    >>> add_last(my_list, 10) is not None
    True
    >>> add_last(my_list, 20) is not None
    True
    >>> add_last(my_list, 30) is not None
    True
    >>> add_last(my_list, 40) is not None
    True
    >>> rotate_double_list(my_list, 4)  # 4 % 4 = 0, lista queda igual
    >>> first_element(my_list) == 10 and last_element(my_list) == 40
    True
    """
    #TODO: Implemente la función tal y como se describe en la documentación.
    if not(size(my_list) <= 1) and (k % size(my_list) != 0):
        #derecha 
        k = k % size(my_list) 
        i = 0
        current_node = my_list['header']['next']
        while i != size(my_list)-k:
            current_node = current_node['next']
        last_node = last_element_node(my_list)
        last_node['next'] = None
        my_list['header']['next'] = current_node
        previous = current_node['prev']
        previous['next'] = 




#doctest.run_docstring_examples(rotate_double_list, globals(), verbose=True)