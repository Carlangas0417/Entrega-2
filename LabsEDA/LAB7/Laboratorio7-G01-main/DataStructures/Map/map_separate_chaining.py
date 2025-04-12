import random
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import single_linked_list as sll


def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(int(num_elements / load_factor))
    
    table = {
        "elements": [sll.new_list() for _ in range(capacity)],
        "size": capacity
    }
    
    return {
        "prime": prime,
        "capacity": capacity,
        "scale": random.randint(1, prime - 1),
        "shift": random.randint(0, prime - 1),
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
    }


def default_compare(key, element):
    if key == me.get_key(element):
        return 0
    elif key > me.get_key(element):
        return 1
    return -1


def put(my_map, key, value):
    index = mf.hash_value(my_map, key)
    table = my_map['table']['elements']
    
    if table[index] is None:
        table[index] = sll.new_list()
    
    size_before = table[index]['size']
    
    for i in range(size_before):
        entry = sll.get_element(table[index], i)
        if default_compare(key, entry) == 0:
            entry['value'] = value
            return my_map
    
    entry = me.new_map_entry(key, value)
    sll.add_last(table[index], entry)
    my_map['size'] += 1
    
    my_map['current_factor'] = my_map['size'] / my_map['capacity']
    
    if my_map['current_factor'] > my_map['limit_factor']:
        my_map = rehash(my_map)
    
    return my_map


def contains(my_map, key):
    index = mf.hash_value(my_map, key)
    table = my_map['table']['elements']
    
    if table[index] is None:
        return False
    
    size_list = table[index]['size']
    for i in range(size_list):
        entry = sll.get_element(table[index], i)
        if default_compare(key, entry) == 0:
            return True
    
    return False

def remove(my_map, key):
    esta=contains(my_map,key)
    if esta:
        hash_value= mf.hash_value(key)
        single=my_map["table"]["elements"][hash_value]
        i=0
        removido=False
        node=single["first"]
        while i<sll.size(single) and not removido:
            if me.get_key(node["info"])==key:
                sll.delete_element(node, i)
                removido=True
            node=node["next"]
            i+=1
        my_map["size"]-=1
    return my_map
    
    
def get(my_map, key):
    
    "Obtiene el valor asociado a la llave"
    
    hash_value = mf.hash_value(key)
    single=my_map["table"]["elements"][hash_value]
    node=single["first"]
    obtenido=False
    value=None
    while not obtenido and node!=None:
        if me.get_key(node["info"])==key:
            value=me.get_value(node["info"])
            obtenido=True
        node=node["next"]
    return value

def size(my_map):
    return my_map['size']


def is_empty(my_map):
    return my_map['size'] == 0


def key_set(my_map):
    keys = sll.new_list()
    for bucket in my_map['table']['elements']:
        current = bucket['first']
        while current is not None:
            sll.add_last(keys, me.get_key(current['info']))
            current = current['next']
    return keys


def value_set(my_map):
    values = sll.new_list()
    for bucket in my_map['table']['elements']:
        node = bucket['first']
        while node is not None:
            sll.add_last(values, node['info']['value'])
            node = node['next']
    return values


def rehash(my_map):
    new_capacity = mf.next_prime(my_map['capacity'] * 2)
    new_table = new_map(new_capacity)
    
    for bucket in my_map['table']:
        if bucket:  
            for entry in bucket:  
                put(new_table, entry['key'], entry['value'])
    
    my_map.update(new_table)
    return my_map