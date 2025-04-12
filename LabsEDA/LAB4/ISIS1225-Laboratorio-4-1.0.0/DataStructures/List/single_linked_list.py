def new_list ():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    
    return newlist

def is_empty(my_list):
    return my_list["size"] == 0

        
def new_single_node(element):
    
    return {"info": element, "next": None}

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
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
    nodo = new_single_node(element)
    
    nodo["next"] = my_list["first"]
    my_list["first"] = nodo
    
    if my_list["size"] == 0:
        my_list["last"] = my_list["first"]
        
    my_list["size"] += 1
 
    return my_list

def add_last(my_list, element):
    new_node=new_single_node(element)
    
    if my_list["size"] == 0:
        my_list["first"] = new_node
    else:
        my_list["last"]["next"] = new_node

    my_list["last"] = new_node

    
    my_list["size"] += 1  
    
    return my_list

def size(my_list):
    size = my_list["size"]
    return size

def first_element(my_list):
    if is_empty(my_list):
        raise Exception
    element=None
    if my_list["first"] is not None:
        element=my_list["first"]
    return element

def last_element(my_list):
    result = None
    
    if my_list["last"] is not None:
        current_node = my_list["last"]
        result = current_node["info"]
        
    return result

def remove_first(my_list):
    removed_info = None
    
    if my_list["size"] > 0:
        node = my_list["first"]
        removed_info = node["info"]
        my_list['first']= node['next']
    my_list['size']-=1
        
    return removed_info

def remove_last(my_list):
    removed_info = None
    
    if my_list["size"] > 0:
        if my_list["first"] == my_list ["last"]:
            removed_info = remove_first(my_list)
            my_list['first']=None
            my_list['last']=None
            
        else:
            current_node = my_list["first"]
                                   
            while current_node["next"] != my_list["last"]:
                current_node = current_node["next"]
            removed_info = my_list['last']['info']
            current_node['next']=None
            my_list['last']=current_node
    my_list['size']-=1
    return removed_info

def insert_element(my_list, element, pos):
    searchpos = 0
    node = my_list["first"]
    current_node = node
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
        current_node = node["info"]
    
    nuevo_nodo = new_single_node(element)
    
    current_node["next"] = nuevo_nodo["info"]
        
    my_list["size"] += 1
 
    return my_list

def delete_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    current_node = node
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
        current_node = node["info"]
    current_node = current_node["next"]
        
    my_list["size"] -= 1
 
    return my_list

def change_info(my_list, pos, new_info):
    searchpos = 0
    node = my_list["first"]
    current_node = node
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
        current_node = node["info"]
    current_node["info"] = new_info
 
    return my_list

def exchange(my_list, pos_1, pos_2):
    searchpos1 = 0
    node = my_list["first"]
    current_node1 = node
    while searchpos1 < pos_1:
        node = node["next"]
        searchpos1 += 1
        current_node1 = node["info"]
    
    searchpos2 = 0
    node = my_list["first"]
    current_node2 = node
    while searchpos2 < pos_2:
        node = node["next"]
        searchpos2 += 1
        current_node2 = node["info"]
 
    informacion1 = current_node1["info"] 
    informacion2 = current_node2["info"] 
    
    current_node1["info"] = informacion2
    current_node2["info"] = informacion1
    
    return my_list

def sub_list(my_list, pos, num_elements):
    sublist = new_list()  
    if pos < 0 or pos >= my_list["size"]:
        sublist=None
    current = my_list["first"]  
    for _ in range(pos):
        current = current["next"]
    count = 0  
    while current is not None and count < num_elements:
        if sublist["size"] == 0:
            sublist = add_first(sublist, current["info"])  
        else:
            sublist = add_last(sublist, current["info"])  
        current = current["next"]  
        count += 1  
    return sublist
        
        
