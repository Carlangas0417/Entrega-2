import DataStructures.List.array_list as arr
import DataStructures.List.single_linked_list as sll


def new_stack()->dict:
    return sll.new_list()#arr.new_list()
def is_empty(stk:dict)->bool:
    return sll.is_empty(stk)#arr.is_empty(stk)
def size(stk:dict)->int:
    return sll.size(stk) #arr.size(stk)
def push(stk: dict, element: any) -> dict:
    return sll.add_last(stk, element) # arr.add_last(stk, element)
def pop(stk:dict)->any:
    if is_empty(stk):
        raise Exception('EmptyStructureError: stack is empty')
    return sll.remove_last(stk) #arr.remove_last(stk)
def top(stk: dict)->any:
    if is_empty(stk):
        raise Exception('EmptyStructureError: stack is empty')
    return sll.last_element(stk) #arr.last_element(stk)