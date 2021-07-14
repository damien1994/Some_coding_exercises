import json


def sum_input_file(filename: str) -> int:
    """
    Read a file and returns the sum of each line
    :param filename: a string which specifies the name of the file to load
    :return: an integer which is the sum of each line (if integer)
    """
    with open(filename) as f:
        return sum(int(line) for line in f.readlines())


def convert_json_to_tree(filename: str):
    """
    Read a json file and returns a specific print of the input
    :param filename: A string which defines the name of the json file
    :return: A specific print
    """
    with open(filename) as f:
        data = json.load(f)
        count = 0
        for item in data:
            children_recursive(item, count)


def children_recursive(item: dict, count: int):
    """
    A recursive function
    A counter is initialized to 0 and is passed as argument to the function
    This function takes each item of the dict passed in input and
    relatively to the value of the counter will return a specific print
    The value of the counter changes if the value children is not null.
    We can interpret the children value as a level of the dictionary.
    :param item: A dict which contains (key, value) nested within (key, values)
    The value has to be named "children"
    :param count: A counter which represents the "level"/depth of the dictionary
    :return: A print
    """
    print('    ' * count, '- {0}'.format(item['value']))
    if item['children']:
        count += 1
        for child in item['children']:
            children_recursive(child, count)


def flat_list_to_hierarchical_tree(filename: str):
    """
    Function to answer to question 3
    This function transforms a flat list to an hierarchical tree.
    The first objective is to transform the flat list to a hierarchy of tags
    (like the 2nd exercise) and after to apply the children recursive function.
    This function defines the root nodes and thanks to a recursive function get
    the children corresponding to the node until the node has no more children.
    :param filename: A string which defines the path to the input/json file
    :return: A print which represents an hierarchical tree
    """
    with open(filename) as f:
        data = json.load(f)
        print(type(data))

    # get root nodes
    root_nodes = [item['value'] for item in data if item['parent'] is None]

    # result
    result = [get_nodes(data, root) for root in root_nodes]
    for item in result:
        children_recursive(item, 0)


def get_nodes(data: list, node: str) -> dict:
    """
    Recursive function
    Takes in input the flat list and the node corresponding to the level of the
    tree.
    We take at the beginning the root of the tree. We apply the get_children function
    to see if the node has children : if it's true, we apply again the get_nodes function
    (recursive function) until there are no more children to represent.
    :param data: The list which represents the flat list loaded
    :param node: The level of the tree
    :return: A dict which represent the hierarchy in the tree between parents and
    children
    """
    d = {'value': node}
    children = get_children(data, node)
    if children:
        d['children'] = [get_nodes(data, child) for child in children]
    else:
        d['children'] = []
    return d


def get_children(data: list, node: str) -> list:
    """
    This function returns the children corresponding to the parent node (value)
    :param data: The list which represents the flat list loaded
    :param node: The node which represents the level of the tree
    :return: A list which contains the children corresponding
    """
    return [item['value'] for item in data if item['parent'] == node]
