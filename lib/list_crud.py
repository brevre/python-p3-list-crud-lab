def create_an_empty_list():
    return []

def create_a_list():
    return ["apples", "oranges", "grapes", "bananas"]

def add_element_to_end_of_list(lst, melons):
    lst.append(melons)
    return lst

def add_element_to_start_of_list(lst, passion_fruits):
    lst.insert(0, passion_fruits)
    return lst

def remove_element_from_end_of_list(lst):
    lst.pop()
    return lst

def remove_element_from_start_of_list(lst):
    del lst[0]
    return lst

def retrieve_first_element_from_list(lst):
    return lst[0]

def retrieve_element_from_index(lst, index):
    return lst[index]

def retrieve_last_element_from_list(lst):
    return lst[-1]
