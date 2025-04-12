
from DataStructures.List import array_list as al #Importa el módulo array_list
from DataStructures.Utils import error as er #Importa el módulo error

def new_stack():
    
    """Crea y retorna una nueva pila vacía."""
    
    return al.new_list()


def is_empty(stack):
    
    """Devuelve True si la pila está vacía, False en caso contrario."""
    
    return al.is_empty(stack)


def size(stack):
    
    """Retorna el número de elementos en la pila."""
    
    return al.size(stack)

def push(stack, element):
    
    """Añade un elemento al tope de la pila."""
    
    if element is None:
        er.error("Element is None") #Lanza un error si el elemento es None.
    else:
        al.add_last(stack, element) #Agrega el elemento al final de la lista.
    
    
def pop(stack):
    
    """Elimina y retorna el último elemento agregado a la pila"""
    
    return al.remove_last(stack) #Elimina el último elemento de la lista.

def top(stack):
    
    """Devuelve el último elemento de la pila sin eliminarlo."""
    
    return al.get_element(stack, al.size(stack) - 1) # Obtiene el último elemento de la lista.

