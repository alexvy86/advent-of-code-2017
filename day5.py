import utils
input_data = [int(i) for i in utils.read_lines(5)]

# input_data = [0,3,0,1,-3]

current_index = 0
steps = 0
while (current_index >= 0 and current_index < len(input_data)):
    steps += 1
    new_index = current_index + input_data[current_index]
    # input_data[current_index] += 1
    if (input_data[current_index] >= 3):
        input_data[current_index] -= 1
    else:
        input_data[current_index] += 1
    current_index = new_index
    
print('Escaped in {0} steps'.format(steps))
# print(input_data)