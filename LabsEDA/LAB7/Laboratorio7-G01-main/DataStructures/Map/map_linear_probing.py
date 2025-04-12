import random
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as arr



def new_map(num_elements, load_factor, prime=109345121):
    """ 
    
    """
    capacity = mf.next_prime(num_elements // load_factor)
    map = {
        "capacity": capacity,
        "prime": prime,
        "scale": random.randint(1, prime - 1),
        "shift": random.randint(0, prime - 1),
        "table": arr.new_list(),
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
    }

    for _ in range(capacity):
        arr.add_last(map["table"], me.new_map_entry(None, None))

    return map

def size(my_map):
    '''
    Obtiene la cantidad de elementos en la tabla de simbolos.
    '''
    return my_map['size']

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   hash_value= hash(key) % my_map["capacity"] 
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = arr.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, arr.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def is_available(table, pos):

    entry = arr.get_element(table, pos)
    
    if entry is None:
        return True
    key = me.get_key(entry)
    return key is None or key == "__EMPTY__"

def contains(my_map, key):
    
    hash_code= hash(key) % my_map["capacity"]
    ocupied, first_avail = find_slot(my_map, key, hash_code)
    return ocupied

def remove(my_map, key):
    
    esta= contains(my_map,key)
    if esta == True:
        hash= hash(key) % my_map["capacity"]
        ocupied, first_avail= find_slot(my_map, key, hash)
        
        if ocupied:
            entry = arr.get_element(my_map["table"], first_avail)
            me.set_key(entry, "__EMPTY__")
            me.set_value(entry, None)
            my_map["size"] -= 1
            return my_map
        else:
            return my_map
    else:
        return my_map
    
    
def get(my_map, key):
    
    "Obtiene el valor asociado a la llave"
    
    hash_value = hash(key) % my_map["capacity"]
    occupied, position = find_slot(my_map, key, hash_value)
    if occupied:
        entry = arr.get_element(my_map["table"], position)
        return me.get_value(entry)
    return None
            
            
def is_empty(my_map):
    
    if my_map["size"] == 0:
        return True 
    else: 
        return False

def key_set(my_map):
    keys = arr.new_list()
    for i in range(my_map["capacity"]):
        entry = arr.get_element(my_map["table"], i)
        if entry is not None and me.get_key(entry) is not None and me.get_key(entry) != "__EMPTY__":
            arr.add_last(keys, me.get_key(entry))
    return keys

def value_set(my_map):
    values = arr.new_list()
    for i in range(my_map["capacity"]):  
        entry = arr.get_element(my_map["table"], i)  
        if entry is not None and me.get_value(entry) is not None:
            arr.add_last(values, me.get_value(entry))  
    return values
            
def rehash(my_map):
    values = []
    for i in range(my_map["capacity"]):
        entry = arr.get_element(my_map["table"], i)
        if entry is not None and me.get_key(entry) is not None and me.get_key(entry) != "__EMPTY__":
            values.append((me.get_key(entry), me.get_value(entry)))
    
    new_capacity = mf.next_prime(my_map["capacity"] * 2)
    new_map_instance = new_map(new_capacity, my_map["limit_factor"])
    
    for key, value in values:
        put(new_map_instance, key, value)
    
    my_map["capacity"] = new_map_instance["capacity"]
    my_map["prime"] = new_map_instance["prime"]
    my_map["scale"] = new_map_instance["scale"]
    my_map["shift"] = new_map_instance["shift"]
    my_map["table"] = new_map_instance["table"]
    my_map["current_factor"] = new_map_instance["current_factor"]
    my_map["size"] = new_map_instance["size"]

    return my_map
    
def put(my_map, key, value):
    
    hash_value = hash(key) % my_map["capacity"]
    occupied, position = find_slot(my_map, key, hash_value)
    entry = arr.get_element(my_map["table"], position)
    if occupied:
        me.set_value(entry, value)
    else:
        me.set_key(entry, key)
        me.set_value(entry, value)
        my_map["size"] += 1

        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

        if my_map["current_factor"] > my_map["limit_factor"]:
            new_map_instance = rehash(my_map)
            my_map.update(new_map_instance)
    