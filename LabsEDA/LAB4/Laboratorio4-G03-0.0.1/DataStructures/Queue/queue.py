from DataStructures.List import array_list as al

def new_queue():
    return al.new_list()

def peek(my_queue):
    first = al.first_element(my_queue)
    return first

def is_empty(my_queue):
    x = al.is_empty(my_queue)
    return x


def dequeue(my_queue):
    elemento1 = my_queue["elements"][0]
    my_queue["elements"].pop(0)
    return elemento1

def size(my_queue):
    return my_queue["size"]


def enqueue(my_queue,element):
    
    nueva_cola=al.add_last(my_queue,element)
    return nueva_cola