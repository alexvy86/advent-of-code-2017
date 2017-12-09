''' Day 2 from Advent of Code 2017
'''

def calculate_total(data, step):
    '''Calculates the sum of the digits that are equal to their 'sibling',
    which is <step> positions ahead in the circular list''' 
    total = 0
    length = len(input_data)
    for i in range(0, length - 1):
        if data[i] == data[(i+step) % length]:
            total += int(data[i])
    return total

import utils
input_data = utils.read_file(2).read()
lines = [list(map(lambda x: int(x), line.split('\t'))) for line in input_data.split('\n')]

# print(lines)
line_checksums = [max(line)-min(line) for line in lines]
# print(line_checksums)
print(sum(line_checksums))
