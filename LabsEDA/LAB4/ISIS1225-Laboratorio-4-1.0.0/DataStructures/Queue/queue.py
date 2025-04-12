from DataStructures.List import single_linked_list as sgl
def new_queue():
    return sgl.new_list()

def enqueue(my_queue,element):
    if is_empty(my_queue):
        sgl.add_first(my_queue,element)
        my_queue['last'] = my_queue['first']
    else:
        sgl.add_last(my_queue,element)
    return my_queue

def is_empty(my_queue):
    return bool(my_queue['size']== 0)

def size(my_queue):
    return sgl.size(my_queue)

def dequeue(my_queue):
    dev = sgl.get_element(my_queue,0)
    sgl.remove_first(my_queue)
    return dev

def peek(my_queue):
    if not is_empty(my_queue):
        return my_queue['first']['info']
    else:
        raise Exception
