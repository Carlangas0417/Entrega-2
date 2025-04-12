
def new_list():
    
    """Crea y retorna una nueva lista vacía."""
    
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    
    return newlist

def insert_element(my_list, element, pos):
    
    """Inserta un elemento en una posición específica dentro de la lista."""
    
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    nodo = my_list["first"]
    for i in range(pos - 2):
        nodo = nodo["next"]
        nodo["next"] = {
            "info": element,
            "next": nodo["next"]
        }
    return my_list
    
def get_element(my_list, pos):
    
    """Obtiene el elemento en la posición indicada."""
    
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    
    """Verifica si un elemento está en la lista usando una función de comparación."""
    
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

def add_first(my_list, element):
    
    """Agrega un elemento al inicio de la lista."""
    
    node = {
        "info": element,
        "next": None
    }
    if my_list["size"] == 0:
        my_list["first"] = node
        my_list["last"] = node
    else:
        node["next"] = my_list["first"]
        my_list["first"] = node
    my_list["size"] += 1
    
def add_last(my_list, element):
    
    """Agrega un elemento al final de la lista."""
    
    node = {
        "info": element,
        "next": None
    }
    if my_list["size"] == 0:
        my_list["first"] = node
        my_list["last"] = node
    else:
        my_list["last"]["next"] = node
        my_list["last"] = node
    my_list["size"] += 1
    
def is_empty(my_list):
    
    """Verifica si la lista está vacía."""
    
    return my_list["size"] == 0

def size(my_list):
    
    """Devuelve el tamaño de la lista."""
    
    return my_list["size"]

def first_element(my_list):
    
    """Devuelve el primer elemento de la lista."""
    
    return my_list["first"]["info"]

def last_element(my_list):
    
    """Devuelve el último elemento de la lista."""
    
    return my_list["last"]["info"]

def remove_first(my_list):
    
    """Elimina y devuelve el primer elemento de la lista."""
    
    if my_list["size"] == 0:
        return None
    element = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1
    if my_list["size"] == 0:
        my_list["last"] = None
    return element

def remove_last(my_list):
    
    """Elimina y devuelve el último elemento de la lista."""
    
    if my_list["size"] == 0:
        return None
    element = my_list["last"]["info"]
    if my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
    else:
        temp = my_list["first"]
        while temp["next"] != my_list["last"]:
            temp = temp["next"]
        temp["next"] = None
        my_list["last"] = temp
    my_list["size"] -= 1
    return element

  

def clear(my_list):
    
    """Elimina todos los elementos de la lista, dejándola vacía."""
    
    my_list["first"] = None
    my_list["last"] = None
    my_list["size"] = 0


def delete_element(my_list, pos):
    
    """Elimina un elemento en una posición específica."""

    if pos == 0:
        my_list['first'] = my_list['first']['next']
        if my_list['size'] == 1:
            my_list['last'] = None
            
    else:
        node = my_list['first']
        for i in range(pos - 1):
            node = node['next']
        node['next'] = node['next']['next']
        if pos == my_list['size'] - 1:
            my_list['last'] = node
    my_list['size'] -= 1
    
    return my_list


def change_info(my_list, pos, new_info):
    
    """Modifica el valor de un nodo en una posición específica."""
    
    first = my_list["first"]
    i = 0
    
    while i < pos:
        first = first["next"]
        i += 1
    first["info"] = new_info
    
    return my_list


def exchange(my_list, pos1, pos2):
    
    """Intercambia dos elementos en la lista."""
    
    if pos1 == pos2:
        return my_list
    n1 = my_list["first"]
    n2 = my_list["first"]
    i = 0
    
    while i < pos1:
        n1 = n1["next"]
        i += 1
    i = 0
    
    while i < pos2:
        n2 = n2["next"]
        i += 1
    info = n1["info"]
    n1["info"] = n2["info"]
    n2["info"] = info
    
    return my_list


def sub_list(my_list, pos, num_elem):
    
    """Crea y retorna una sublista a partir de una posición dada y un número de elementos."""
    
    sublst = new_list()
    cont = 0
    while cont < num_elem:
        elem = get_element(my_list, pos)
        add_last(sublst, elem)
        pos += 1
        cont += 1
    return sublst