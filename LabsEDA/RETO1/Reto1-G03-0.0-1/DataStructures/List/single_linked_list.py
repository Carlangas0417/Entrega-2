from DataStructures.List import list_node as ln

def new_list():
    newlist={"size":0,"first":None,"last":None,}
    return(newlist)

def get_element (my_list,pos):
    searchpos=0
    node=my_list["first"]
    while searchpos < pos:
        node=node["next"]
        searchpos +=1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp= my_list["first"]
    count=0
    while not is_in_array and temp is not None:
        if cmp_function(element,temp["info"]) == 0:
            is_in_array = True
        else:
            temp =temp["next"]
            count+=1
    if not is_in_array:
        count=-1
    return (count)


def add_first(my_list,element):
    """
    Añade un elemento al principio de la estructura de datos: single linked list.
    """
    new_node=ln.new_single_node(element)
    new_node["next"]=my_list["first"]
    my_list["first"]=new_node
    
    if my_list["size"] == 0:
        my_list["last"]=new_node
        
    my_list["size"]+=1
    return(my_list)

def add_last(my_list,element):
    """
    Añade un elemento al final de la estructura de datos
    """
    new_node=ln.new_single_node(element)
    my_list["last"]=new_node
    
    if my_list["size"]==0:
        my_list["first"]=new_node
    
    my_list["size"]+=1
    
    return my_list
def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if size(my_list) == 0:
        raise Exception('IndexError: list index out of range')
    return my_list["first"]

def is_empty(my_list):
    return my_list["size"]==0

def last_element(my_list):
    
    if is_empty(my_list)==True:
        raise Exception('IndexError: list index out of range')
    return my_list["last"]

def remove_first(my_list):
    if is_empty(my_list)==True:
        my_list["last"]=None
    node=my_list["first"]
    removed_info=node["info"]
    
    my_list["first"]=node["next"]
    my_list["size"]-=1
    
    return removed_info

def remove_last(my_list):
    removed_info=0
    if is_empty(my_list)==True:
         raise Exception('IndexError: list index out of range')
    else:
         if size(my_list)==1:
             removed_info=remove_first(my_list)
         else:
             current=my_list["first"]
             removed_info=my_list["last"]
             while current != my_list["last"]:
                 current=current["next"]
                 if current["next"]==my_list["last"]:
                    current["next"]=None
                    my_list["last"]=current
                    my_list["size"]-=1
    return removed_info

def insert_element(my_list,element,pos):
    conteo=0
    a_cambiar={"info":element,"next":None}
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    elif pos==0:
        add_first(my_list,element)
    else:
        actual=my_list["first"]
        while conteo < pos-1:
            conteo+=1
            actual=actual["next"]
        a_cambiar["next"]=actual["next"]
        actual["next"]=a_cambiar
    return my_list

def delete_element(my_list,pos):
    conteo=0
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    elif pos==0:
        remove_first(my_list)
    else:
        actual=my_list["first"]
        while conteo < pos-1:
            conteo+=1
            actual=actual["next"]
        actual["next"]=actual["next"]["next"]
    return my_list
            
def change_info(my_list,pos,new_info):
    conteo=0
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        actual=my_list["first"]
        while conteo < pos-1:
            conteo+=1
            actual=actual["next"]
        actual["info"]=actual["info"]
    return my_list

def exchange(my_list,pos1,pos2):
    conteo=0
    if (pos1 < 0 or pos1 > size(my_list)) or (pos2 < 0 or pos2 > size(my_list)):
        raise Exception('IndexError: list index out of range')
    else:
        primero=my_list["first"]
        segundo=my_list["first"]
        while conteo < pos1-1:
            conteo+=1
            primero=primero["next"]
        while conteo < pos2-1:
            conteo+=1
            segundo=segundo["next"]
        primero["next"]=segundo["next"]
        segundo["next"]=primero["next"]
    return my_list



def sub_list(my_list,pos,num_elements):
    conteo=0
    conteo2=0
    nueva_lista=new_list()
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        actual=my_list["first"]
        while conteo < pos-1:
            conteo+=1
            actual=actual["next"]
        nueva_lista["first"]=actual
        while conteo2 < num_elements:
            conteo2+=1
            actual=actual["next"]
            if actual==None:
                return nueva_lista
            nueva_lista=add_last(actual)
            