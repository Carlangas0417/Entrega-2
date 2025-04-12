from DataStructures.List import list_node as ln

def new_list():
    '''Crea una lista (de tipo single_linked_list) vacía.
    La lista es creada con los siguientes atributos:
        - size: Tamaño actual de la lista, inicializado en 0.
        - first: Primer nodo de la lista, inicializado en None.
        - last: Último nodo de la lista, inicializado en None.
  
    :return: Lista vacía recien creada.
    :rtype: single_linked_list
    '''
    newlist = {
        'size' : 0,
        'first' : None,
        'last' : None
    }
    return newlist  


def add_first(my_list, element):
    '''Agrega un elemento al inicio de la lista.
    Agrega un nuevo nodo al inicio de la lista y aumenta el tamaño de la lista en 1. 
    En caso de que la lista esté vacía, el primer y último nodo de la lista serán el nuevo nodo.

    :param my_list: Lista a la cual se le agregará el elemento.
    :type my_list: single_linked_list
    :param element: Elemento a agregar.
    :type element: any

    :return: Lista con el elemento agregado al inicio.
    :rtype: single_linked_list
    '''
    nodo = ln.new_single_node(element)
    
    if my_list['size'] == 0:
        my_list['first'] = nodo
        my_list['last'] = nodo
    else:
        nodo['next'] = my_list['first']
        my_list['first'] = nodo
        
    my_list['size'] += 1
    return my_list
    

def add_last(my_list, element):
    '''Agrega un elemento al final de la lista.
    Inserta el elemento al final de la lista y aumenta el tamaño de la lista en 1.

    :param my_list: Lista a la cual se le agregará el elemento.
    :type my_list: single_linked_list
    :param element: Elemento a agregar.
    :type element: any

    :return: Lista con el elemento agregado al final.
    :rtype: single_linked_list
    '''
    nodo = ln.new_single_node(element)
    
    if my_list['size'] == 0:
        my_list['first'] = nodo
        my_list['last'] = nodo
    else:
        my_list['last']['next'] = nodo
        my_list['last'] = nodo
        
    my_list['size'] += 1
    return my_list


def is_empty(my_list):
    '''Verifica si la lista está vacía.
    Retorna True si la lista está vacía, en caso contrario retorna False.

    :param my_list: Lista a verificar.
    :type my_list: single_linked_list

    :return: True si la lista está vacía, False en caso contrario.
    :rtype: bool
    '''
    return my_list['size'] == 0
    

def size(my_list):
    '''Retorna el tamaño de la lista.

    :param my_list: Lista de la cual se obtendrá el tamaño.
    :type my_list: single_linked_list

    :return: Tamaño de la lista
    :rtype: int
    '''
    return my_list['size']


def first_element(my_list):
    '''Retorna el primer elemento de una lista no vacía.
    Retorna el primer elemento de la lista. Si la lista está vacía, 
    lanza un error IndexError: list index out of range. Esta función 
    no elimina el elemento de la lista.

    :param my_list: Lista de la cual se obtendrá el primer elemento.
    :type my_list: single_linked_list

    :return: Primer elemento de la lista.
    :rtype: any
    '''
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list['first']['info']


def last_element(my_list):
    if is_empty(my_list):
        raise IndexError("list index out of range")
    return my_list['last']['info']


def get_element(my_list, pos):
    '''Retorna el elemento en la posición dada.
    Retorna el elemento en la posición pos, la cual debe ser igual 
    o mayor a cero y menor al tamaño de la lista. 0 <= pos < size(my_list). 
    Si la posición no es válida, lanza un error IndexError: list index out of range. 
    Esta función no elimina el elemento de la lista.

    :param my_list: Lista de la cual se obtendrá el elemento.
    :type my_list: single_linked_list
    :param pos: Posición del elemento a obtener.
    :type pos: int

    :return: Elemento en la posición dada.
    :rtype: any
    '''
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]


def remove_first(my_list):
    '''Elimina el primer elemento de la lista enlazada.
    
    Si la lista no está vacía, elimina el primer nodo y actualiza el tamaño.
    Si la lista está vacía, lanza un IndexError.

    :param my_list: Lista de la cual se eliminará el primer elemento.
    :type my_list: single_linked_list

    :return: Elemento eliminado.
    :rtype: any
    '''
    if is_empty(my_list):
        raise IndexError("remove_first() called on an empty list")
    
    removed_element = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1

    if my_list["size"] == 0:
        my_list["last"] = None  # Si la lista queda vacía, actualiza "last"

    return removed_element


def remove_last(my_list):
    '''Elimina el último elemento de la lista enlazada.
    
    Si la lista no está vacía, elimina el último nodo y actualiza el tamaño.
    Si la lista está vacía, lanza un IndexError.

    :param my_list: Lista de la cual se eliminará el último elemento.
    :type my_list: single_linked_list

    :return: Elemento eliminado.
    :rtype: any
    '''
    if is_empty(my_list):
        raise IndexError("remove_last() called on an empty list")
    
    removed_element = my_list["last"]["info"]
    
    if my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
    else:
        current = my_list["first"]
        while current["next"] != my_list["last"]:
            current = current["next"]
        current["next"] = None
        my_list["last"] = current
    
    my_list["size"] -= 1
    return removed_element


def insert_element(my_list, element, pos):
    '''Inserta un elemento en una posición específica de la lista enlazada.
    
    Si la posición es válida (0 <= pos <= tamaño actual), inserta el elemento y actualiza el tamaño.
    Si la posición es inválida, lanza un IndexError.

    :param my_list: Lista en la cual se insertará el elemento.
    :type my_list: single_linked_list
    :param element: Elemento a insertar.
    :type element: any
    :param pos: Posición en la cual insertar el elemento.
    :type pos: int

    :return: Lista con el elemento insertado.
    :rtype: single_linked_list
    '''
    if pos < 0 or pos > my_list["size"]:
        raise IndexError("insert_element() position out of range")
    
    nodo = ln.new_single_node(element)
    
    if pos == 0:
        return add_first(my_list, element)
    elif pos == my_list["size"]:
        return add_last(my_list, element)
    
    current = my_list["first"]
    count = 0
    while count < pos - 1:
        current = current["next"]
        count += 1
    
    nodo["next"] = current["next"]
    current["next"] = nodo
    my_list["size"] += 1
    
    return my_list


def is_present(my_list, element, cmp_function):
    '''Verifica si un elemento está presente en la lista.
    Para comparar los elementos, se utiliza la función de comparación cmp_function. 
    Si el elemento está presente retorna su posición, en caso contrario retorna -1.
    
    :param my_list: Lista en la cual se buscará el elemento.
    :type my_list: single_linked_list
    :param element: Elemento a buscar.
    :type element: any
    :param cmp_function: Función de comparación.
    :type cmp_function: function

    :return: Posición del elemento si está presente, -1 en caso contrario.
    :rtype: int
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


def delete_element(my_list, pos):
    '''Elimina un elemento en la posición dada.
    Elimina el elemento en la posición pos, la cual debe ser igual o mayor a 
    cero y menor al tamaño de la lista. 0 <= pos < size(my_list) Si la posición 
    no es válida, lanza un error IndexError: list index out of range.
    
    :param my_list: Lista de la cual se eliminará el elemento.
    :type my_list: single_linked_list
    :param pos: Posición del elemento a eliminar.
    :type pos: int

    :return: Lista con el elemento eliminado.
    :rtype: single_linked_list
    '''
    if pos < 0 or pos >= my_list["size"]:
        raise Exception("IndexError: list index out of range")

    if pos == 0:
        eliminado = my_list["first"]
        my_list["first"] = eliminado["next"]
        if my_list["first"] is None:
            my_list["last"] = None
    else:
        i = 0
        nodo = my_list["first"]
        while i < pos - 1:
            nodo = nodo["next"]
            i += 1
        eliminado = nodo["next"]
        nodo["next"] = eliminado["next"]
        if nodo["next"] is None:
            my_list["last"] = nodo

    my_list["size"] -= 1
    return my_list


def change_info(my_list, pos, new_info):
    """
    Args:
        my_list (_type_): _description_
        pos (_type_): _description_
        new_info (_type_): _description_

    Returns: Lista con la informacion del elemento cambiada
    rtype: single_linked_list
    """
    node=my_list["first"]
    contador=0
    while contador<pos:
        node=node["next"]
        contador+=1
    node["info"]=new_info
    return my_list


def exchange(my_list, pos_1, pos_2):
    '''Intercambia la posición de dos elementos.
    Intercambia la posición de los elementos en las posiciones pos_1 y pos_2. 
    Si alguna de las posiciones no es válida, lanza un error IndexError: list index out of range.
    
    :param my_list: Lista en la cual se intercambiarán los elementos.
    :type my_list: single_linked_list
    :param pos_1: Posición del primer elemento a intercambiar.
    :type pos_1: int
    :param pos_2: Posición del segundo elemento a intercambiar.
    :type pos_2: int

    :return: Lista con los elementos intercambiados.
    :rtype: single_linked_list
    '''
    if pos_1 < 0 or pos_2 < 0:
        raise IndexError("list index out of range")
    
    primer_nodo = None
    segundo_nodo = None
    node = my_list["first"]
    contador = 0
    while node:
        if contador == pos_1:
            primer_nodo = node
        if contador == pos_2:
            segundo_nodo = node
        if primer_nodo and segundo_nodo:
            break
        node = node["next"]
        contador += 1
    if not primer_nodo or not segundo_nodo:
        raise IndexError("list index out of range")
    primer_nodo["info"], segundo_nodo["info"] = segundo_nodo["info"], primer_nodo["info"]
    return my_list


def sub_list(my_list, pos_i, num_elements):
    '''Retorna una sublista de la lista original.
    Retorna una sublista de la lista original que contiene num_elements 
    elementos a partir de la posición pos. Si la posición no es válida, 
    lanza un error IndexError: list index out of range.
    
    :param my_list: Lista de la cual se obtendrá la sublista.
    :type my_list: single_linked_list
    :param pos_i: Posición inicial de la sublista.
    :type pos_i: int
    :param num_elements: Número de elementos de la sublista.
    :type num_elements: int

    :return: Sublista de la lista original.
    :rtype: single_linked_list
    '''
    sub_list = new_list()
    nodo = my_list['first']
    i = 0
    while i < pos_i:
        nodo = nodo['next']
        i += 1
    contador = 0
    while nodo is not None and contador < num_elements:
        add_last(sub_list, nodo['info'])
        nodo = nodo['next']
        contador += 1
    return sub_list


def cmp_function(element1, element2):
    '''Función de comparación por defecto a modo de ejemplo.
    Esta función de comparación por defecto compara dos elementos y retorna 0 
    si son iguales, 1 si el element_1 es mayor que element_2 y -1 si element_1 
    es menor que element_2.
    
    :param element1: Primer elemento a comparar
    :type element1: any
    :param element2: Segundo elemento a comparar
    :type element2: any

    :return: 0 si los elementos son iguales, 1 si el primer elemento es mayor 
    que el segundo y -1 en caso contrario.
    :rtype: int
    '''
    if element1!=element2:
        if element1 > element2:
            return 1
        else:
            return -1
    else:
        return 0
