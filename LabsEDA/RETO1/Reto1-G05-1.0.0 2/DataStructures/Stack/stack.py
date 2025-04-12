import DataStructures.List.array_list as arr

def new_stack()->dict:
    return arr.new_list()
def is_empty(stk:dict)->bool:
    return arr.is_empty(stk)
def size(stk:dict)->int:
    return arr.size(stk)
def push(stk: dict, element: any) -> dict:
    return arr.add_last(stk, element)
def pop(stk:dict)->any:
    if is_empty(stk):
        raise Exception('EmptyStructureError: stack is empty')
    return arr.remove_last(stk)
def top(stk: dict)->any:
    if is_empty(stk):
        raise Exception('EmptyStructureError: stack is empty')
    return arr.last_element(stk)