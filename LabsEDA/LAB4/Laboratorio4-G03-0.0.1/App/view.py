"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

import sys
import App.logic as logic

"""
La vista se encarga de la interacción con el usuario
Presenta el menú de opciones y por cada selección
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_logic():
    """
    Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control


def print_menu():
    """
    Menu de usuario
    """
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar la pila de libros por leer de un usuario")
    print("3- Consultar la posición del usuario en la cola para leer un libro")
    print("4- Ejecutar pruebas de rendimiento")
    print("0- Salir")


def load_data(control):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    books, authors, tags, book_tags, books_to_read = logic.load_data(control)
    return books, authors, tags, book_tags, books_to_read


def print_books_to_read(results):
    # TODO Imprimir los libros por leer
    pass


def print_tests_results(queue_results, stack_results):
    """
    Imprime los resultados de las pruebas de rendimiento
    """
    print("\nTiempos de ejecución para Cola: \n")

    print("Tiempo de ejecución para enqueue:",
          f"{queue_results['enqueue_time']:.3f}", "[ms]")
    print("Tiempo de ejecución para peek:",
          f"{queue_results['peek_time']:.3f}", "[ms]")
    print("Tiempo de ejecución para dequeue:",
          f"{queue_results['dequeue_time']:.3f}", "[ms]")

    print("\nTiempos de ejecución para Pila: \n")

    # TODO Imprimir los resultados de las pruebas de rendimiento de la pila


# Se crea el controlador asociado a la vista
control = new_logic()


# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    # ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 1:
            print("Cargando información de los archivos ....")
            bk, at, tg, bktg, tr = load_data(control)
            print('Libros cargados: ' + str(bk))
            print('Autores cargados: ' + str(at))
            print('Géneros cargados: ' + str(tg))
            print('Libros por leer cargados: ' + str(tr))
            print('Asociación de Géneros a Libros cargados: ' +
                  str(bktg))

        elif int(inputs[0]) == 2:
            user_id = input("Ingrese el id del usuario: ")
            result = logic.get_books_stack_by_user(control, int(user_id))
            print_books_to_read(result)

        elif int(inputs[0]) == 3:
            user_id = input("Ingrese el id del usuario: ")
            book_id = input("Ingrese el id del libro: ")

            result = logic.get_user_position_on_queue(
                control, int(user_id), int(book_id))
            # TODO Imprimir la posición del usuario en la cola

        elif int(inputs[0]) == 4:
            size = input("Indique tamaño de la muestra: ")
            size = int(size)
            logic.set_book_sublist(control, size)

            print("Ejecutando pruebas de rendimiento...")
            queue_result = logic.measure_queue_performance(control)
            stack_result = logic.measure_stack_performance(control)
            print_tests_results(queue_result, stack_result)

        elif int(inputs[0]) == 0:
            working = False
            print("\nGracias por utilizar el programa.")

        else:
            continue
    sys.exit(0)
