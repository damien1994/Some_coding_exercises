# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from utils import sum_input_file, convert_json_to_tree, flat_list_to_hierarchical_tree


if __name__ == '__main__':
    print(sum_input_file("input_data/foo.txt"))
    convert_json_to_tree("input_data/hierarchy.json")
    flat_list_to_hierarchical_tree("input_data/hierarchy_2.json")
