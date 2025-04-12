import csv


def new_set():
    """
    Crea un conjunto (set) vacio el cuál permite almacenar elementos únicos sin un orden específico.

    El conjunto (set) es creado con los siguientes atributos inicializados:

    - **size:** Tamaño del conjunto, inicializado en 0.
    - **elements:** Lista de elementos del conjunto. Inicializada como ``array`` vacio.

    :returns: Conjuto vacío creado recien inicializado
    :rtype: :ref:`set<set.py>`
    """
    my_new_set = {
        'size': 0,
        'elements': []
    }
    return my_new_set


def add_element(my_set, element):
    """
    Añade un elemento no existente al conjunto.

    Si el elemento ya existe en el conjunto, no se añadirá. De lo contrario, se añadirá al conjunto (se inserta al array) y se incrementará el tamaño del conjunto.

    :param my_set: Conjunto al que se le añadirá un elemento.
    :type my_set: :ref:`set<set.py>`
    :param element: Elemento que se añadirá al conjunto.
    :type element: any

    :returns: Conjunto con el elemento añadido.
    :rtype: :ref:`set<set.py>`
    """
    if element not in my_set['elements']:
        my_set['elements'].append(element)
        my_set['size'] += 1
    return my_set


def remove_element(my_set, element):
    """
    Elimina un elemento del conjunto.

    Si el elemento no existe en el conjunto, no se eliminará. De lo contrario, se eliminará del conjunto (se elimina del array) y se decrementará el tamaño del conjunto.

    :param my_set: Conjunto al que se le eliminará un elemento.
    :type my_set: :ref:`set<set.py>`
    :param element: Elemento que se eliminará del conjunto.
    :type element: any

    :returns: Conjunto con el elemento eliminado.
    :rtype: :ref:`set<set.py>`
    """
    if element in my_set['elements']:
        my_set['elements'].remove(element)
        my_set['size'] -= 1
    return my_set


def load_set(my_set, filename):
    """Carga un set a partir de un archivo csv

    :param my_set: Set al que se le agregaran los elementos
    :type my_set: set
    :param filename: Nombre del archivo csv
    :type filename: str

    :returns: Set con los elementos cargados
    :rtype: set
    """
    menor_year = 1000000
    mayor_year = 0
    head = []
    tail = []
    if (my_set is not None and filename is not None):
        input_file = csv.DictReader(open(filename, encoding="utf-8"),
                                    delimiter=",")
        for line in input_file:
            add_element(my_set, line)
            if(int(line["year_collection"]) > mayor_year):
                mayor_year = int(line["year_collection"])
            if(int(line["year_collection"]) < menor_year):
                menor_year = int(line["year_collection"])
            print(size(my_set))
        head = my_set["elements"][:5]
        tail = my_set["elements"][-6:-1]
            
    return (my_set, menor_year, mayor_year, head, tail)


def size(my_set):
    """Obtiene el tamaño del set

    :param my_set: Set del que se obtendra el tamaño
    :type my_set: set

    :returns: Tamaño del set
    :rtype: int
    """
    return my_set['size']


def is_empty(my_set):
    """Verifica si el set esta vacio

    :param my_set: Set a verificar
    :type my_set: set

    :returns: True si el set esta vacio, False en caso contrario
    :rtype: bool
    """
    return my_set['size'] == 0

def get_first_element(my_set):
    """Retorna el primer elemento del set

    :param my_set: Set a verificar
    :type my_set: set

    :returns: El primer libro del set con toda su informacion
    :rtype: dict
    """
    return  my_set['elements'][0]

def get_last_element(my_set):
    """Retorna el ultimo elemento del set

    :param my_set: Set a verificar
    :type my_set: set

    :returns: El ultimo libro del set con toda su informacion
    :rtype: dict
    """
    return  my_set['elements'][-1]