from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as lt

def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime((num_elements*(1/load_factor)))
    lista = lt.new_list()
    for i in range(capacity):
        lt.add_last(lista, sl.new_list())
    dic = {
        'prime': prime,
        'capacity': capacity,
        'scale': 1,
        'shift': 0,
        'table': lista,
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0
    }
    return dic

def put(my_map,key,value):
    hash = mf.hash_value(my_map,key)
    if contains(my_map,key):
        node = my_map["table"]["elements"][hash]["first"]
        for j in range(my_map["table"]["elements"][hash]["size"]):
            if key == node["info"]["key"]:
                node["info"]["value"] = value
                return my_map
    sl.add_last(my_map["table"]["elements"][hash], me.new_map_entry(key,value))
    my_map["size"] += 1
    my_map["current_factor"] = my_map["size"]/my_map["capacity"]
    if my_map["current_factor"] > my_map["limit_factor"]:
         rehash(my_map)
    return my_map

def default_compare(key, element):

   if (key == me.get_key(element)):
      return 0
   elif (key > me.get_key(element)):
      return 1
   return -1

def contains(my_map,key):
    hash = mf.hash_value(my_map,key)
    node = my_map["table"]["elements"][hash]["first"]
    for j in range(my_map["table"]["elements"][hash]["size"]):
        if key == node["info"]["key"]:
            return True
        node = node["next"]
    return False

def remove(my_map,key):
    hash = mf.hash_value(my_map,key)
    node = my_map["table"]["elements"][hash]["first"]
    if node == None:
        return my_map
    if node["info"]["key"] == key:
        sl.remove_first(my_map["table"]["elements"][hash])
        my_map["size"] -= 1
    for j in range(my_map["table"]["elements"][hash]["size"]-1):
        if key == node["next"]["info"]["key"]:
            node["next"] = node["next"]["next"]
            my_map["size"] -= 1
            return my_map
    return my_map

def get(my_map,key):
    hash = mf.hash_value(my_map,key)
    node = my_map["table"]["elements"][hash]["first"]
    for j in range(my_map["table"]["elements"][hash]["size"]):
        if key == node["info"]["key"]:
            return node["info"]["value"]
        node = node["next"]
    return None

def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    return my_map["size"] == 0

def key_set(my_map):
    lista = lt.new_list()
    for i in range(my_map['table']["size"]):
        node = my_map["table"]["elements"][i]["first"]
        for j in range(my_map["table"]["elements"][i]["size"]):
            lt.add_last(lista, node["info"]["key"])
            node = node["next"]
    return lista

def value_set(my_map):
    lista = lt.new_list()
    for i in range(my_map['table']["size"]):
        node = my_map["table"]["elements"][i]["first"]
        for j in range(my_map["table"]["elements"][i]["size"]):
            lt.add_last(lista, node["info"]["value"])
            node = node["next"]
    return lista

def rehash(my_map):
    old_table = my_map["table"]
    new_capacity = mf.next_prime(my_map["capacity"]*2)
    my_map["capacity"] = new_capacity
    tabla = lt.new_list()
    for i in range(new_capacity):
        lt.add_last(tabla, sl.new_list())
    my_map["table"] = tabla
    for j in range(lt.size(old_table)):
        node = old_table["elements"][j]["first"]
        for h in range(sl.size(old_table["elements"][j])):
            put(my_map, node["info"]["key"],node["info"]["value"])
            node = node["next"]
    return my_map