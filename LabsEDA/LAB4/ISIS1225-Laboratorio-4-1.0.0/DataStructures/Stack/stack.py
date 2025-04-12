from DataStructures.List import array_list as arr    
def new_stack():
    return arr.new_list()

def is_empty(my_stack):
    return len(my_stack["elements"]) == 0

def pop(my_stack):
    if not is_empty(my_stack):
        return arr.remove_first(my_stack)
    else:
        raise Exception

def top(my_stack):
    return arr.first_element(my_stack)

def size(my_stack):
    return arr.size(my_stack)

def push(my_stack, element):
    if is_empty(my_stack):
        arr.add_first(my_stack, element)
    else:
        my_stack = arr.add_last(my_stack, element)
    return my_stack
