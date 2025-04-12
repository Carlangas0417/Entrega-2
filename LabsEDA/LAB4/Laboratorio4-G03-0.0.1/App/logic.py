"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones
 *
 * Dario Correal
 """

import csv
import os
import time
from DataStructures.List import array_list as lt
from DataStructures.Queue import queue as q
# TODO Importar las librerías correspondientes para el manejo de pilas y colas

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_logic():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'books': None,
               'authors': None,
               'tags': None,
               'book_tags': None,
               'books_to_read': None,
               'book_sublist': None}

    catalog['books'] = lt.new_list()
    catalog['authors'] = lt.new_list()
    catalog['tags'] = lt.new_list()
    catalog['book_tags'] = lt.new_list()
    # TODO Implementar la inicialización de la lista de asociación de libros y tags
    catalog['books_to_read'] = None
    catalog["book_sublist"] = None
    return catalog


# Funciones para la carga de datos


def load_data(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    books, authors = load_books(catalog)
    tag_size = load_tags(catalog)
    book_tag_size = load_books_tags(catalog)
    # TODO Cargar los datos de libros para leer
    return books, authors, tag_size, book_tag_size, books_to_read


def load_books(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    booksfile = data_dir + '/books.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for book in input_file:
        add_book(catalog, book)
    return book_size(catalog), author_size(catalog)


def load_tags(catalog):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    tagsfile = data_dir + '/tags.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for tag in input_file:
        add_tag(catalog, tag)
    return tag_size(catalog)


def load_books_tags(catalog):
    """
    Carga la información que asocia tags con libros.
    """
    bookstagsfile = data_dir + '/book_tags-small.csv'
    input_file = csv.DictReader(open(bookstagsfile, encoding='utf-8'))
    for booktag in input_file:
        add_book_tag(catalog, booktag)
    return book_tag_size(catalog)


def load_books_to_read(catalog):
    """
    Carga la información del archivo to_read y los agrega a la lista de libros por leer
    """
    # TODO Implementar la carga de los libros por leer del archivo to_read
    return books_to_read_size(catalog)

# Funciones de consulta sobre el catálogo


def get_books_stack_by_user(catalog, user_id):
    """
    Retorna una pila con los libros que un usuario tiene por leer.
    """
    books_stack = st.new_stack()

    # TODO Completar la función que retorna los libros por leer de un usuario. Se debe usar el TAD Pila para resolver el requerimiento

    return books_stack


def get_user_position_on_queue(catalog, user_id, book_id):
    """
    Retorna la posición de un usuario en la cola para leer un libro.
    """
    queue = q.new_queue()

    # TODO Completar la función que retorna la posición de un usuario en la cola para leer un libro. Se debe usar el TAD Cola para resolver el requerimiento.

    return position

# Funciones para agregar informacion al catalogo


def add_book(catalog, book):
    # Se adiciona el libro a la lista de libros
    book["goodreads_book_id"] = int(book["goodreads_book_id"])
    lt.add_last(catalog['books'], book)
    # Se obtienen los autores del libro
    authors = book['authors'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for author in authors:
        add_book_author(catalog, author.strip(), book)
    return catalog


def add_book_author(catalog, author_name, book):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    authors = catalog['authors']
    pos_author = lt.is_present(authors, author_name, compare_authors)
    if pos_author > 0:
        author = lt.get_element(authors, pos_author)
    else:
        author = new_author(author_name)
        lt.add_last(authors, author)
    lt.add_last(author['books'], book)
    return catalog


def add_tag(catalog, tag):
    """
    Adiciona un tag a la lista de tags
    """
    t = new_tag(tag['tag_name'], tag['tag_id'])
    lt.add_last(catalog['tags'], t)
    return catalog


def add_book_tag(catalog, book_tag):
    """
    Adiciona un tag a la lista de tags
    """
    t = new_book_tag(book_tag['tag_id'],
                     book_tag['goodreads_book_id'], book_tag['count'])
    lt.add_last(catalog['book_tags'], t)
    return catalog


def add_book_to_read(catalog, book_to_read):
    """
    Adiciona un libro a la lista de libros por leer
    """
    t = new_book_to_read(book_to_read['user_id'], book_to_read['book_id'])
    lt.add_last(catalog['books_to_read'], t)
    return catalog

# Funciones para creacion de datos


def new_author(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    author = {'name': "", "books": None,  "average_rating": 0}
    author['name'] = name
    author['books'] = lt.new_list()
    return author


def new_tag(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    tag = {'name': '', 'tag_id': ''}
    tag['name'] = name
    tag['tag_id'] = id
    return tag


def new_book_tag(tag_id, book_id, count):
    """
    Esta estructura crea una relación entre un tag y
    los libros que han sido marcados con dicho tag.
    """
    book_tag = {'tag_id': tag_id, 'book_id': book_id, 'count': count}
    return book_tag


def new_book_to_read(user_id, book_id):
    """
    Esta estructura crea una relación entre un tag y
    los libros que han sido marcados con dicho tag.
    """
    book_to_read = {'user_id': user_id, 'book_id': book_id}
    return book_to_read


def book_size(catalog):
    return lt.size(catalog['books'])


def author_size(catalog):
    return lt.size(catalog["authors"])


def tag_size(catalog):
    return lt.size(catalog["tags"])


def book_tag_size(catalog):
    return lt.size(catalog["book_tags"])


def books_to_read_size(catalog):
    # TODO Implementar la función que retorna el tamaño de la lista de libros por leer
    pass

# Funciones utilizadas para comparar elementos dentro de una lista


def compare_authors(author_name1, author):
    if author_name1.lower() == author['name'].lower():
        return 0
    elif author_name1.lower() > author['name'].lower():
        return 1
    return -1


def compare_tag_names(name, tag):
    if (name == tag['name']):
        return 0
    elif (name > tag['name']):
        return 1
    return -1


def set_book_sublist(catalog, size):
    """
    Crea una sublista de libros de tamaño size
    """
    algo = lt.sub_list(catalog["books"], 0, size)
    catalog["book_sublist"] = algo
    return catalog


def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


def measure_queue_performance(catalog):
    """
    Mide el desempeño de las operaciones de la cola
    """

    queue = q.new_queue()

    # Medir enqueue
    start_time = get_time()
    for pos in range(lt.size(catalog["book_sublist"])):
        book = lt.get_element(catalog["book_sublist"], pos)
        q.enqueue(queue, book)
    end_time = get_time()
    enqueue_time = delta_time(start_time, end_time)

    # Medir peek
    start_time = get_time()
    next = q.peek(queue)
    end_time = get_time()
    peek_time = delta_time(start_time, end_time)

    # Medir dequeue
    start_time = get_time()
    while not q.is_empty(queue):
        q.dequeue(queue)
    end_time = get_time()
    dequeue_time = delta_time(start_time, end_time)

    return {
        "enqueue_time": enqueue_time,
        "peek_time": peek_time,
        "dequeue_time": dequeue_time
    }


def measure_stack_performance(catalog):
    """
    Mide el desempeño de las operaciones de la pila
    """

    stack = st.new_stack()

    # Medir push
    start_time = get_time()
    # TODO Implementar la medición de tiempo para la operación push

    # Medir top
    start_time = get_time()
    # TODO Implementar la medición de tiempo para la operación top
    end_time = get_time()
    top_time = delta_time(start_time, end_time)

    # Medir dequeue
    # TODO Implementar la medición de tiempo para la operación pop

    return {
        "push_time": push_time,
        "top_time": top_time,
        "pop_time": pop_time
    }
