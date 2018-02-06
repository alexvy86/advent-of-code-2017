import utils
input_data = utils.read_lines(7)

class ProgramData:
    def __init__(self, name: str, weight: int, children: [str]):
        self.name = name
        self.weight = weight
        self.children = children
        self.childrenObjects = []

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