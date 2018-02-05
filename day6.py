input_data = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]

def redistribute_blocks(input_list: list):
    blocks_to_be_distributed = max(input_list)
    bank_to_be_redistributed = input_list.index(blocks_to_be_distributed)
    input_list[bank_to_be_redistributed] = 0
    current_receiving_bank = bank_to_be_redistributed + 1
    
    while(blocks_to_be_distributed > 0):
        if (current_receiving_bank == len(input_list)):
            current_receiving_bank = 0
        input_list[current_receiving_bank] += 1
        current_receiving_bank += 1
        blocks_to_be_distributed -= 1
    
    return input_list

seen_states = []

# Initialize variables befor looping
redistributed_list = input_data.copy()
redist_string = str(redistributed_list)
redistributions = 0
print("{0} after {1} redistribution cycles".format(redist_string, redistributions))
while (redist_string not in seen_states):
    seen_states.append(redist_string)
    redistributed_list = redistribute_blocks(redistributed_list)
    redist_string = str(redistributed_list)
    redistributions += 1
    print("{0} after {1} redistribution cycles".format(redist_string, redistributions))

print('Repeated configuration after {0} redistribution cycles.'.format(redistributions))
print('Size of loop: {0}'.format(redistributions - seen_states.index(redist_string)))