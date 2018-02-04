import utils
input_data = [int(i) for i in utils.read_lines(5)]

current_index = 0
steps = 0
while (current_index >= 0 and current_index < len(input_data)):
    steps += 1
    new_index = current_index + input_data[current_index]
    input_data[current_index] += 1
    current_index = new_index
    
print('Escaped in {0} steps'.format(steps))