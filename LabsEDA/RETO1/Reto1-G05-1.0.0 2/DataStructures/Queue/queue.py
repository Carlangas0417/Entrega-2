import DataStructures.List.single_linked_list as sll

def new_queue()->dict:
    return sll.new_list()

def is_empty(cola: dict)->bool:
    return sll.is_empty(cola)
def size(cola: dict)->int:
    return sll.size(cola)
def enqueue(cola: dict, elemento: any)-> dict:
    return sll.add_last(cola, elemento)
def dequeue(cola: dict) -> any:
    return sll.remove_first(cola)
def peek(cola: dict)->any:
    return sll.first_element(cola)
