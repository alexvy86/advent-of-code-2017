''' Day 2 from Advent of Code 2017
'''

import utils
input_data = utils.read_file(2).read()
lines = [list(map(lambda x: int(x), line.split('\t'))) for line in input_data.split('\n')]

# Puzzle 1
line_checksums = [max(line)-min(line) for line in lines]
print(sum(line_checksums))

# Puzzle 2
line_checksums_2 = [n//m for line in lines for n in line for m in line if n > m and n % m == 0]
print(sum(line_checksums_2))
