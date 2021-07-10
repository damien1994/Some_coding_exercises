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
    if len(item['children']) > 0:
        count += 1
        for child in item['children']:
            children_recursive(child, count)


def flat_list_to_hierarchical_tree(filename):
    with open(filename) as f:
        data = json.load(f)
        values = []
        parents = []
        for item in data:
            values.append(item['value'])
            parents.append(item['parent'])

    # get root nodes
    root_nodes = [item['value'] for item in data if item['parent'] is None]

    # result
    result = [get_nodes(data, root) for root in root_nodes]
    for item in result:
        children_recursive(item, 0)


def get_nodes(data, node):
    d = {'value': node}
    children = get_children(data, node)
    print(children)
    if children:
        d['children'] = [get_nodes(data, child) for child in children]
    else:
        d['children'] = []
    return d


def get_children(input, node):
    return [item['value'] for item in input if item['parent'] == node]
