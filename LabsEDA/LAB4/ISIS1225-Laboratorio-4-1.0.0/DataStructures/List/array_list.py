def new_list():
    newlist = {'elements': [],
                'size': 0
            }
    return newlist

def get_element(my_list,index):
    if 0 <= index < len(my_list['elements']):
        return my_list['elements'][index]
    else:
        return None

def is_present(my_list,element,cmp_function):
    size = my_list['size']
    if size > 0:
        keyexist = False
        for keypos in range(0,size):
            info = my_list['elements'][keypos]
            if cmp_function(element,info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    if my_list['size'] == 0:
        my_list['elements'] = [element]
    else:
        my_list['elements'].insert(0,element)
    my_list['size'] +=1
    return my_list

def add_last(my_list, element):
    my_list['elements'].insert(-1,element)
    my_list['size']+=1
    return my_list

def size(my_list):
    return my_list['size']

def first_element(my_list):
    return my_list['elements'][0]

def is_empty(my_list):
    return my_list["size"] == 0

def remove_first(my_list):
    if not is_empty(my_list):
        elemento = my_list['elements'].pop(0)
        my_list["size"] -= 1
        return elemento
    else:
        raise Exception


def remove_last(my_list):
    if not is_empty(my_list):
        elemento = my_list['elements'].pop(-1)
        my_list["size"] -= 1
        return elemento
    else:
        raise Exception

def delete_element(my_list,pos):
    my_list['elements'].pop(pos)
    return my_list

def insert_element(my_list,pos, element):
    my_list['elements'].insert(pos,element)
    return my_list

def change_info(my_list, pos, element):
    my_list['elements'][pos]= element
    return my_list

def exchange(my_list,pos_1,pos_2):
    el_1 = my_list['elements'][pos_1]
    el_2 = my_list['elements'][pos_2]
    my_list['elements'][pos_1] = el_2
    my_list['elements'][pos_2] = el_1
    return my_list

def sub_list(my_list,pos_i,num_elements):
    list = my_list['elements'][pos_i:pos_i+num_elements]
    return {'size': len(list),'elements': list}