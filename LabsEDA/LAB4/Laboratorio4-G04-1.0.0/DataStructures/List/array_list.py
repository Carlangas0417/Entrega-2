
def new_list():
    """
    Esta funcion crea una nueva lista vacia con la estructura de array list.

    Parameters:
    None

    Returns:
    dict: A dictionary representing the new array list with the following keys
    """
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist


def add_first(my_list, element):
    """
    Adds an element to the beginning of the array list.

    Parameters:
    my_list (dict): The array list to which the element will be added. It should have the following keys:
        'elements' (list): A list containing the elements of the array list.
        'size' (int): The number of elements in the array list.

    element (any): The element to be added to the array list.

    Returns:
    None. The function modifies the array list in-place.
    """
    my_list["elements"].insert(0, element)
    my_list["size"] += 1

    
def add_last(my_list, element):
    """
    Adds an element to the end of the array list.

    Parameters:
    my_list (dict): The array list to which the element will be added. It should have the following keys:
        'elements' (list): A list containing the elements of the array list.
        'size' (int): The number of elements in the array list.

    element (any): The element to be added to the array list.

    Returns:
    None. The function modifies the array list in-place.
    """
    my_list["elements"].append(element)
    my_list["size"] += 1


def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else: 
        return False
    
def size(my_list):
    return my_list["size"]
    
def first_element(my_list):
    if is_empty(my_list):
        return None
    else:
        return my_list["elements"][0]

def last_element(my_list):
    if is_empty(my_list):
        return None
    else:
        return my_list["elements"][my_list["size"] - 1]


def get_element(my_list, index):
    
    return my_list["elements"][index]


def is_present(my_list, element, cmp_function):
    
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

def remove_first(my_list):
    if my_list["size"] !=0:
        elemento_borrado = my_list["elements"].pop(0)
        my_list["size"] = my_list["size"] - 1
        return elemento_borrado
    else:
        return None
    
def remove_last(my_list):
    if my_list["size"] !=0:
        elemento_borrado = my_list["elements"].pop(-1)
        my_list["size"] = my_list["size"] - 1
        return elemento_borrado
    else:
        return None
    
def insert_element(my_list, element, pos):
    my_list["elements"].insert(pos ,element)
    my_list["size"] = len(my_list["elements"])
    return my_list

def delete_element(my_list, pos):
    if my_list["size"] !=0:
        if pos >=0 and pos <= len(my_list["elements"]):
            elemento_borrado = my_list["elements"].pop(pos) 
            my_list["size"] = my_list["size"] - 1
            return my_list
    else:
        return None
    
def change_info(my_list, pos, new_info):
    my_list["elements"][pos] = new_info
    return my_list


def exchange(my_list, pos1,pos2):
    my_list["elements"][pos1], my_list["elements"][pos2] = my_list["elements"][pos2], my_list["elements"][pos1]
    return my_list


def sub_list(my_list, pos, numelem):
    posicion = pos
    contador = 0
    new_list = {"elements":[],"size":0,"type": "ARRAY_LIST"}

    while posicion < len(my_list["elements"]) and contador < numelem:
        new_list["elements"].append(my_list["elements"][posicion])
        posicion +=1
        contador +=1
    
    new_list["size"] = len(new_list["elements"])
    return new_list