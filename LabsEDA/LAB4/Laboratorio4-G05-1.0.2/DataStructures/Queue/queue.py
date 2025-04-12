import DataStructures.List.single_linked_list as sll
import DataStructures.List.array_list as arr


def new_queue()->dict:
    return arr.new_list() #sll.new_list()

def is_empty(cola: dict)->bool:
    return arr.is_empty(cola)#sll.is_empty(cola)
def size(cola: dict)->int:
    return arr.size(cola)#sll.size(cola)
def enqueue(cola: dict, elemento: any)-> dict:
    return arr.add_last(cola, elemento)#sll.add_last(cola, elemento)
def dequeue(cola: dict) -> any:
    return arr.remove_first(cola)#sll.remove_first(cola)
def peek(cola: dict)->any:
    return arr.first_element(cola)#sll.first_element(cola)
