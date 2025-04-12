from DataStructures.List import single_linked_list as sl
from DataStructures.Utils import error as er


def new_queue():
    """
    Crea una nueva cola vacía.
    """
    
    return sl.new_list()


def enqueue(my_queue, element):
    
    """
    Agrega un elemento a la cola.
    """
    
    sl.add_last(my_queue, element)
    
    return my_queue

def dequeue(my_queue):
    
    """
    Elimina y retorna el elemento al frente de la cola.
    """
    
    if my_queue is sl.is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty')
    else:
        return sl.remove_first(my_queue)
        
    
    
def peek(my_queue):
    
    """
    Retorna el elemento al frente de la cola.
    """
    if my_queue is sl.is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty')
    else:
        return sl.first_element(my_queue)

def is_empty(my_queue):
    
    """
    Retorna True si la cola está vacía, False de lo contrario.
    """
    return sl.is_empty(my_queue)  


def size(my_queue):
    
    """
    Retorna el número de elementos en la cola.
    """
    
    return sl.size(my_queue)

