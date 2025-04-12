def get_element(my_list, index):
    return my_list['elements'][index]

def is_present(my_list, element, cmp_function):
    
    size = my_list['size']
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list['elements'][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1
            
def new_list():
    newlist={
        'elements':[],
        'size':0
    }
    return newlist

def add_first(my_list,element):
    my_list["elements"].insert(0,element)
    my_list["size"] += 1
    return my_list

def add_last(my_list,element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list['size']

def first_element(my_list):
    if len(my_list['elements']) == 0:
        raise IndexError("list index out of range")
    return my_list['elements'][0]

def is_empty(my_list):
    return my_list['size']==0

def insert_element(my_list, element, pos):
    my_list['elements'].insert(pos, element)
    my_list['size'] += 1
    return my_list

def delete_element(my_list, pos):
    if pos > 0 and pos <= my_list['size']:
        if my_list['size'] > 0:
            del my_list['elements'][pos-1]
            my_list['size'] -= 1
            return my_list
        
def remove_first(my_list):
    if my_list['size']==0:
        raise IndexError("list index out of range")
    removed = my_list['elements'].pop(0)
    my_list['size'] -= 1
    return removed

def remove_last(my_list):
    if my_list['size']==0:
        raise IndexError("list index out of range")
    removed = my_list['elements'].pop(-1)
    my_list['size'] -= 1
    return removed

def change_info(my_list, pos, new_info):
    my_list['elements'][pos-1] = new_info
    return my_list

def exchange(my_list, pos1, pos2):
    my_list['elements'][pos1-1],  my_list['elements'][pos2-1] = my_list['elements'][pos2-1],  my_list['elements'][pos1-1]
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i > my_list['size'] or num_elements < 0:
        raise IndexError("list index out of range")
    final= pos_i + num_elements
    sub_elements = my_list['elements'][pos_i:final]
    sub_list = new_list()
    sub_list['elements'] = sub_elements
    sub_list['size'] = len(sub_list)
    return sub_list

def default_sort_criteria(element1, element2):
    is_sorted=False
    if element1 < element2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, crit):
    for i in range(0, my_list['size']-1):
        min_pos = i
        for j in range(i+1, my_list['size']):
            if crit(my_list['elements'][j], my_list['elements'][min_pos]):
                min_pos = j
        exchange(my_list, i+1, min_pos+1)
    return my_list

def insertion_sort(my_list, crit):
    for i in range(1, my_list["size"]-1):
        j = i - 1
        while j >= 0 and crit(my_list["elements"][j], my_list["elements"][i]):
            my_list["elements"][j + 1] = my_list["elements"][j]
            j -= 1
        my_list["elements"][j + 1] = my_list["elements"][i]
    return my_list

def shell_sort(my_list, crit):
    h = 1
    while h < my_list["size"] // 3:
        h = 3 * h +1
    while h > 0:
        for i in range(h, my_list["size"]):
            j = i
            while j >= h and my_list["elements"][j - h] > my_list["elements"][i]:
                my_list["elements"][j] = my_list["elements"][j-h]
                j -= h
            my_list["elements"][j] = my_list["elements"][i]
        h //= 3
    return my_list