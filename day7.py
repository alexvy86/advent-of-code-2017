import utils
input_data = utils.read_lines(7)

class ProgramData:
    def __init__(self, name: str, weight: int, children: [str]):
        self.name = name
        self.weight = weight
        self.children = children
        self.childrenObjects = []
        self.tower_weight = 0

def transform_line_to_program_data(line: str):
    first_split = line.split(" -> ")
    if (len(first_split) == 1):
        tokens = first_split[0].split(" ")
        return ProgramData(tokens[0], tokens[1].replace("(","").replace(")",""), [])
    else:
        tokens = first_split[0].split(" ")
        return ProgramData(tokens[0], tokens[1].replace("(","").replace(")",""), first_split[1].split(", "))

programs = [transform_line_to_program_data(line) for line in input_data ]
# print([ "{0},{1},{2}".format(o.name, o.weight, o.children) for o in programs])

tree = programs.pop()

def insert_into_tree(item: ProgramData, tree: ProgramData):
    if (tree.name in item.children):
        item.childrenObjects.append(tree)
        return (item, True)
    elif (item.name in tree.children):
        tree.childrenObjects.append(item)
        return (tree, True)
    else:
        for child in tree.childrenObjects:
            (maybe_updated_child, could_update_child) = insert_into_tree(item, child)
            if (could_update_child):
                tree.childrenObjects.remove(child)
                tree.childrenObjects.append(maybe_updated_child)
                return (tree, True)
        return (tree, False)

steps = 0
while(len(programs) > 0):
    processing_item = programs.pop(0)
    (tree, could_insert) = insert_into_tree(processing_item, tree)
    if (could_insert):
        print("{0} steps so far. Inserted program {1}. {2} programs left to insert.".format(steps, processing_item.name, len(programs)))
    else:
        programs.append(processing_item)
    steps += 1

print(tree.name)

def calculate_tower_weight(node: ProgramData):
    node.tower_weight = node.weight + sum([calculate_tower_weight(child) for child in node.childrenObjects])

def find_wrong_node_and_return_correct_weight(node: ProgramData):
    (wrong_child, expected_weight) = get_correct_weight(node.childrenObjects)
    if (wrong_child == None):
        print('Found wrong node! {0} with tower_weight {1}'.format(node.name, node.tower_weight))
        return node.name
    else:
        return find_wrong_node_and_return_correct_weight(wrong_child)

def get_correct_weight(items: [ProgramData]):
    # By design of the challenge, items will always have 3 or more items
    # (because it's impossible to determine which of two distinct elements)
    # is the wrong one; either could be corrected up or down)
    if (len(items) == 0):
        return (None, 0)
    
    if (len(items) <= 2):
        return (None, items[0].tower_weight)
    
    correct_weight = items[0].tower_weight if items[0].tower_weight == items[1].tower_weight \
                                           else (items[0].tower_weight if items[0].tower_weight == items[2].tower_weight \
                                                                       else items[1].tower_weight)
    wrong_items = [i for i in items if i.tower_weight != correct_weight]
    if (len(wrong_items) > 0):
        return (wrong_items[0], correct_weight)
    return (None, correct_weight)

print(calculate_tower_weight(tree))
