# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json


def sum_input_file(filename):
    with open(filename) as f:
        return sum(int(line) for line in f.readlines())


def convert_json_to_tree(filename):
    with open(filename) as f:
        data = json.load(f)
        count = 0
        for item in data:
            children_recursive(item, count)


def children_recursive(item, count):
    print(item)
    if count == 0:
        print('- {0}'.format(item['value']))
    else:
        print('    ' * count, '- {0}'.format(item['value']))
    if len(item['children']) > 0:
        count += 1
        for child in item['children']:
            print(child)
            children_recursive(child, count)

'''
def transform_json_to_tree(filename):
    with open(filename) as f:
        data = json.load(f)
        roots = []
        graph = {value: set() for dic in data for value in dic}
        print(graph)
        for item in data:
            if item['parent'] is None:
                roots.append(item['value'])
            else:
                graph[item['parent']].add(item['value'])
        print(roots)
'''

def transform_json_to_tree(filename):
    with open(filename) as f:
        data = json.load(f)

        # Create list of classes
        classes = []
        for item in data:
            name = item['value']
            if name not in classes:
                classes.append(name)

        treenodes = {}
        root_node = None

        for item in data:  # Create  tree nodes
            item['children'] = []
            name = item['value']
            treenodes[name] = item
            parent = item['parent']
            if parent not in classes and parent not in treenodes:
                node = {'parent': None, 'children': [], 'value': parent}
                root_node = node
                treenodes[parent] = node

        ## Connect parents and children
        for item in data:  # Create  tree nodes
            parent = item['parent']
            parent_node = treenodes[parent]
            parent_node['children'].append(item)

        print(treenodes).to_json()

        for item in list(treenodes.values()):
            children_recursive(item, 0)






def display_node(node, indent=0):
    print('.'*indent, node['value'])
    indent += 3
    for child in node['children']:
        display_node(child, indent)




if __name__ == '__main__':
    #print(sum_input_file("foo.txt"))
    #convert_json_to_tree("hierarchy.json")
    transform_json_to_tree("hierarchy_2.json")
