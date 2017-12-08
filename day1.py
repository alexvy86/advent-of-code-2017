''' Puzzle 1 from Advent of Code 2017
'''
import utils
input_data = utils.read_file(1).read()

# Add first character at the end so we can analyze all pairs of characters
input_data = input_data + input_data[0]

total = 0
for i in range(0, len(input_data) - 1):
    if input_data[i] == input_data[i+1]:
        total += int(input_data[i])

print(total)
