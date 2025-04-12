from DataStructures.List import list_node as ln
def new_list():
    newlist={
        "first":None,
        "last":None,
        "size":0
    }
    return newlist

def get_element(my_list, pos):
    searchpos=0
    node=my_list["first"]
    while searchpos<pos:
        node=node["next"]
        searchpos+=1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array=False
    temp=my_list["first"]
    count=0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"])==0:
            is_in_array=True
        else: 
            temp=temp["next"]
            count+=1
    if not is_in_array:
        count=-1
    return count

def size (my_list):
    return my_list['size']

def first_element(my_list):
    return my_list['first']["info"]

def last_element(my_list):
    return my_list['last']["info"]

def add_first(my_list,element):
    new_node = ln.new_single_node(element)
    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
        my_list["size"] = 1
        return my_list
    new_node["next"] = my_list["first"]
    my_list["first"] = new_node
    my_list["size"] += 1
    return my_list

def add_last(my_list,element):
    new_node = ln.new_single_node(element)
    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
        my_list["size"] = 1
        return my_list
    my_list["last"]["next"] = new_node
    my_list["last"] = new_node
    my_list["size"] += 1
    return my_list

def is_empty(my_list):
    return my_list["size"]==0

def remove_first(my_list):    
    first_node = my_list["first"]
    my_list["first"] = first_node["next"]
    my_list["size"] -= 1
    
    return first_node["info"]

def remove_last(my_list):
    
    last_node = my_list["first"]
    while last_node["next"]:
        next_node = last_node["next"]
        if not next_node["next"]:
            my_list["last"] = last_node
            last_node["next"] = None
        last_node = next_node
    
    my_list["size"] -= 1
    return last_node["info"] 

def insert_element(my_list, element, pos):
    new_node = ln.new_single_node(element)
    busqueda_pos = 0
    node = my_list["first"]
    while busqueda_pos < pos-1:
        node = node["next"]
        busqueda_pos += 1
    new_node["next"] = node["next"]
    node["next"] = new_node
    my_list["size"] += 1
    return my_list
def delete_element(my_list, pos):
    if pos == 0:
        deleted_node = my_list["first"]
        my_list["first"] = deleted_node["next"]
        
        if my_list["size"] == 1:
            my_list["last"] = None
        
        my_list["size"] -= 1
        return deleted_node
    
    busqueda_pos = 0
    node = my_list["first"]
    while busqueda_pos < pos - 1:
        node = node["next"]
        busqueda_pos += 1
    
    deleted_node = node["next"]
    node["next"] = deleted_node["next"]

    if node["next"] is None:
        my_list["last"] = node
    
    my_list["size"] -= 1
    return deleted_node

def change_info(my_list, pos, new_info):
    busqueda_pos = 0
    node = my_list["first"]
    while busqueda_pos < pos:
        node = node["next"]
        busqueda_pos += 1
    node["info"] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    if pos_1 > pos_2:
        pos_1, pos_2 = pos_2, pos_1
    
    nodo_1_anterior = None
    nodo_1 = my_list["first"]
    for i in range(pos_1):
        nodo_1_anterior = nodo_1
        nodo_1 = nodo_1["next"]
    
    nodo_2_anterior = None
    nodo_2 = my_list["first"]
    for i in range(pos_2):
        nodo_2_anterior = nodo_2
        nodo_2 = nodo_2["next"]
    
    if nodo_1_anterior:
        nodo_1_anterior["next"] = nodo_2
    else:
        my_list["first"] = nodo_2

    if nodo_2_anterior:
        nodo_2_anterior["next"] = nodo_1
    else:
        my_list["first"] = nodo_1

    nodo_1["next"], nodo_2["next"] = nodo_2["next"], nodo_1["next"]
    
    if nodo_1["next"] is None:
        my_list["last"] = nodo_1
    elif nodo_2["next"] is None:
        my_list["last"] = nodo_2
    
    return my_list

def sub_list(my_list, pos, num_elements):
    sub_list_head = None
    sub_list_tail = None
    
    nodo = my_list["first"]
    for i in range(pos):
        nodo = nodo["next"]
    
    for i in range(num_elements):
        nuevo_nodo = {"info": nodo["info"], "next": None}
        if sub_list_head is None:
            sub_list_head = nuevo_nodo
            sub_list_tail = sub_list_head
        else:
            sub_list_tail["next"] = nuevo_nodo
            sub_list_tail = sub_list_tail["next"]
     
        nodo = nodo["next"]
    return {"first": sub_list_head, "last": sub_list_tail, "size": num_elements}

def default_sort_criteria(element_1,element_2):
    if element_1 < element_2:
        return True
    return False

def selection_sort(my_list, crit):
    node = my_list["first"]
    for i in range(my_list["size"]):
        min_index_node = node
        min_index_element = node["info"]
        key = node['next']
        for j in range(i+1, my_list["size"]):
            if crit(key["info"], min_index_element):
                min_index_node = key["next"]
                min_index_element = key["next"]["info"]
            key = key["next"]
        min_index_node["info"], node["info"] = node["info"], min_index_element
    return my_list