from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
from DataStructures.List import array_list as lt

def default_compare(key, entry):
    if type(key) != type(me.get_key(entry)):
        return -1
    if key == me.get_key(entry):
        return 0
    elif key > me.get_key(entry):
        return 1
    return -1

def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime((num_elements*(1/load_factor)))
    lista = lt.new_list()
    for i in range(capacity):
        lt.add_last(lista, {'key':None, 'value':None})
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

def put(my_map, key, value):
    hash = mf.hash_value(my_map,key)
    pos = find_slot(my_map,key,hash)[1]
    my_map["table"]["elements"][pos] = me.new_map_entry(key,value)
    my_map["size"] += 1
    my_map["current_factor"] = my_map["size"]/my_map['capacity']
    if my_map["current_factor"] > my_map["limit_factor"]:
        rehash(my_map)
    return my_map

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = lt.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def is_available(table, pos):
   entry = lt.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def contains(my_map,key):
    hash = mf.hash_value(my_map,key)
    i = hash
    while i < lt.size(my_map["table"]):
        if my_map["table"]["elements"][hash]["key"] == key:
            return True
        i += 1
        if i == lt.size(my_map["table"]):
            i = 0
        if i == hash:
            return False
    
def remove(my_map,key):
    hash = mf.hash_value(my_map,key)
    i = hash
    while i < lt.size(my_map["table"]):
        if my_map["table"]["elements"][hash]["key"] == key:
            my_map["table"]["elements"][hash]["key"] = "__EMPTY__"
            my_map["table"]["elements"][hash]["value"] = "__EMPTY__"
            my_map["size"] -= 1
            my_map["current_factor"] = my_map["size"]/my_map["capacity"]
            break
        i += 1
        if i == lt.size(my_map["table"]):
            i = 0
        if i == hash:
            break
    return my_map
def size(my_map):
    return my_map["size"]

def get(my_map,key):
    hash = mf.hash_value(my_map,key)
    i = hash
    while i < lt.size(my_map["table"]):
        if my_map["table"]["elements"][hash]["key"] == key:
            return my_map["table"]["elements"][hash]["value"]
        i += 1
        if i == lt.size(my_map["table"]):
            i = 0
        if i  == hash:
            return None

def is_empty(my_map):
    return my_map["size"] == 0

def key_set(my_map):
    lista = lt.new_list()
    for i in range(my_map["capacity"]):
        if my_map["table"]["elements"][i]["key"] != None and my_map["table"]["elements"][i]["key"] != "__EMPTY__":
            lt.add_last(lista,my_map["table"]["elements"][i]["key"])
    return lista

def value_set(my_map):
    lista = lt.new_list()
    for i in range(my_map["capacity"]):
        if my_map["table"]["elements"][i]["value"] != None and my_map["table"]["elements"][i]["value"] != "__EMPTY__":
            lt.add_last(lista, my_map["table"]["elements"][i]["value"])
    return lista

def rehash(my_map):
    old_table = my_map["table"]
    new_capacity = mf.next_prime(my_map["capacity"]*2)
    my_map["capacity"] = new_capacity
    tabla = lt.new_list()
    for i in range(new_capacity):
        lt.add_last(tabla, {'key':None, 'value':None})
    my_map["table"] = tabla
    my_map["size"] = 0
    for j in range(lt.size(old_table)):
        if old_table["elements"][j]["key"] != None and old_table["elements"][j]["key"] != "__EMPTY__":
            put(my_map,old_table["elements"][j]["key"],old_table["elements"][j]["value"])
    return my_map