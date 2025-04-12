def new_list():
    '''Crea una lista (de tipo array_list) vacía.
    La lista es creada con los siguientes atributos:
        - size: Tamaño actual de la lista, inicializado en 0.
        - elements: Lista de elementos, inicializada en una lista vacía.
        
    :return: Lista vacía recien creada.
    :rtype: array_list
    '''
    newlist = {
        'size' : 0,
        'elements' : []
    }
    return newlist


def add_first(my_list, element):
    '''Agrega un elemento al inicio de la lista.
    Inserta el elemento al inicio de la lista y actualiza el tamaño de la lista en 1.

    :param my_list: Lista a la cual se le agregará el elemento.
    :type my_list: array_list
    :param element: Elemento a agregar.
    :type element: any

    :return: Lista con el elemento agregado al inicio.
    :rtype: array_list
    '''
    my_list['elements'].insert(0, element)
    my_list['size'] += 1
    return my_list


def add_last(my_list, element):
    '''Agrega un elemento al final de la lista.
    Inserta el elemento al final de la lista y aumenta el tamaño de la lista en 1.

    :param my_list: Lista a la cual se le agregará el elemento.
    :type my_list: array_list
    :param element: Elemento a agregar.
    :type element: any

    :return: Lista con el elemento agregado al final.
    :rtype: array_list
    '''
    my_list['elements'].append(element)
    my_list['size'] += 1
    return my_list


def is_empty(my_list):
    '''Verifica si la lista está vacía.
    Retorna True si la lista está vacía, en caso contrario retorna False.

    :param my_list: Lista a verificar.
    :type my_list: array_list

    :return: True si la lista está vacía, False en caso contrario.
    :rtype: bool
    '''
    return my_list['size'] == 0


def size(my_list):
    '''Retorna el tamaño de la lista.

    :param my_list: Lista de la cual se obtendrá el tamaño.
    :type my_list: array_list

    :return: Tamaño de la lista
    :rtype: int
    '''
    print(f"Debug: my_list = {my_list}, type = {type(my_list)}")
    return my_list['size']


def first_element(my_list):
    '''Retorna el primer elemento de una lista no vacía.
    Retorna el primer elemento de la lista. Si la lista está vacía, 
    lanza un error IndexError: list index out of range. Esta función 
    no elimina el elemento de la lista.

    :param my_list: Lista de la cual se obtendrá el primer elemento.
    :type my_list: array_list

    :return: Primer elemento de la lista.
    :rtype: any
    '''
    return my_list['elements'][0]
        

def last_element(my_list):
    '''Retorna el último elemento de la lista no vacía.
    Retorna el último elemento de la lista. Si la lista está vacía, 
    lanza un error IndexError: list index out of range. Esta función 
    no elimina el elemento de la lista.

    :param my_list: Lista de la cual se obtendrá el último elemento.
    :type my_list: array_list

    :return: Último elemento de la lista.
    :rtype: any
    '''
    return my_list['elements'][-1]
    

def get_element(my_list, index):
    '''Retorna el elemento en la posición dada.
    Retorna el elemento en la posición pos, la cual debe ser igual o 
    mayor a cero y menor al tamaño de la lista. 0 <= pos < size(my_list). 
    Si la posición no es válida, lanza un error IndexError: list index out of range. 
    Esta función no elimina el elemento de la lista.

    :param my_list: Lista de la cual se obtendrá el elemento.
    :type my_list: array_list
    :param pos: Posición del elemento a obtener.
    :type pos: int

    :return: Elemento en la posición dada.
    :rtype: any
    '''
    return my_list['elements'][index]


def remove_first(my_list):
    '''Elimina el primer elemento de la lista.
    Elimina el primer elemento de la lista y disminuye el tamaño de la lista en 1. 
    Si la lista está vacía, lanza un error IndexError: list index out of range.
    
    :param my_list: Lista de la cual se eliminará el primer elemento.
    :type my_list: array_list

    :return: Elemento recien eliminado.
    :rtype: any
    '''
    if is_empty(my_list):
        raise IndexError("list index out of range")
    elemento = my_list['elements'].pop(0)
    my_list['size'] -= 1
    return elemento


def remove_last(my_list):
    '''Elimina el último elemento de la lista.
    Elimina el último elemento de la lista y disminuye el tamaño de la lista en 1. 
    Si la lista está vacía, lanza un error IndexError: list index out of range.
    c
    :param my_list: Lista de la cual se eliminará el último elemento.
    :type my_list: array_list

    :return: Elemento recien eliminado.
    :rtype: any
    '''
    if is_empty(my_list):
        raise IndexError("list index out of range")
    elemento = my_list['elements'].pop(-1)
    my_list['size'] -= 1
    return elemento


def insert_element(my_list, element, pos):
    '''Inserta un elemento en la posición dada.
    Inserta el elemento en la posición pos. La lista puede estar vacia o 
    tener elementos. Se incrementa el tamaño de la lista en 1.
    
    :param my_list: Lista en la cual se insertará el elemento.
    :type my_list: array_list
    :param element: Elemento a insertar.
    :type element: any
    :param pos: Posición en la cual se insertará el elemento.
    :type pos: int

    :return: Lista con el elemento insertado.
    :rtype: array_list
    '''
    if is_empty(my_list):
        add_last(my_list, element)
    else:
        my_list['elements'].insert(pos, element)
        my_list['size'] += 1
    return my_list


def is_present(my_list, element, cmp_function):
    '''Verifica si un elemento está presente en la lista.
    Para comparar los elementos, se utiliza la función de comparación cmp_function. 
    Si el elemento está presente retorna su posición, en caso contrario retorna -1.
    
    :param my_list: Lista en la cual se buscará el elemento.
    :type my_list: array_list
    :param element: Elemento a buscar.
    :type element: any
    :param cmp_function: Función de comparación.
    :type cmp_function: function

    :return: Posición del elemento si está presente, -1 en caso contrario.
    :rtype: int
    '''
    size = my_list['size']
    if size > 0:
        key_exist = False
        for key_pos in range(0, size):
            info = my_list['elements'][key_pos]
            if cmp_function(element, info) == 0:
                key_exist = True
                break
        if key_exist:
            return key_pos
    return -1


def delete_element(my_list, pos):
    '''Elimina el elemento en la posición dada.
    Elimina el elemento en la posición pos, la cual debe ser igual o mayor a 
    cero y menor al tamaño de la lista. 0 <= pos < size(my_list). Si la posición 
    no es válida, lanza un error IndexError: list index out of range.

    :param my_list: Posición del elemento a eliminar.
    :type my_list: array_list
    :param pos: Elemento a buscar.
    :type pos: int

    :return: Lista con el elemento eliminado.
    :rtype: array_list
    '''
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    
    my_list["elements"].pop(pos)
    my_list["size"] -= 1
    return my_list


def change_info(my_list, pos, new_info):
    """
    Args:
        my_list (_type_): _description_
        pos (_type_): _description_
        new_info (_type_): _description_

    Returns: Lista con la informacion del elemento cambiada
    rtype: array_list
    """
    my_list["elements"][pos]=new_info
    return my_list


def exchange(my_list, pos_1, pos_2):
    """
    Args:
        my_list (_type_): _description_
        pos_1 (_type_): _description_
        pos_2 (_type_): _description_
    Returns: Lista con la informacion de los elementos cambiada
    rtype: array_list
    """
    primer_elemento=my_list["elements"][pos_1]
    segundo_elemento=my_list["elements"][pos_2]
    my_list["elements"][pos_1]=segundo_elemento
    my_list["elements"][pos_2]=primer_elemento
    return my_list


def sub_list(my_list, pos_i, num_elements):
    """Retorna una sublista de la lista original.
    Retorna una sublista de la lista original que inicia en la posición pos_i 
    y contiene num_elements elementos. Si la posición inicial no es válida, 
    lanza un error IndexError: list index out of range.
    
    :param my_list: Lista de la cual se obtendrá la sublista.
    :type my_list: array_list
    :param pos_i: Posición inicial de la sublista.
    :type pos_i: int
    :param num_elements: Número de elementos de la sublista.
    :type num_elements: int

    :return: Sublista de la lista original.
    :rtype: array_list
    """
    sub_list = new_list()
    if num_elements <= size(my_list):
        for i in range(pos_i, num_elements-1 + pos_i):
            sub_list = add_last(sub_list, my_list['elements'][i])
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
