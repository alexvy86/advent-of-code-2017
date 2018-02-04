''' Day 2 from Advent of Code 2017
'''

input_data = 277678

def get_closest_first_number_in_ring(target_number):
    '''
    Returns a tuple (ring_number, first_item) that indicates the ring where target_number
    lives, and first_item is the lowest number in that ring (the first one to "enter" the
    ring when creating the spiral)
    '''

    # lowest number in each ring, starting at ring 0
    # 1, 2, 10, 26, 50
    # lowest_number_n = 1 for n = 0
    # lowest_number_n = 2 for n = 1
    #                 = lowest_number_n-1 + 8*(n-1), for n >= 2

    current_first_number = 1
    ring_number = 0
    while True:
        next_first_number = 2 if ring_number == 0 else current_first_number + 8*ring_number
        if (next_first_number > target_number):
            break
        ring_number += 1
        current_first_number = next_first_number
    return (ring_number, current_first_number)

def sequence_for_ring(ring_number):
    '''
    Returns the sequence whose entries are the number of steps required to reach "home" for all numbers
    in ring n, starting at the lowest number in the ring
    '''

    # Number of steps for each number, starting from the first number that gets into the ring (1,2,10,26)
    # 0,
    # 1,2,1,2,1,2,1,2
    # 3,2,3,4,3,2,3,4,3,2,3,4,3,2,3,4
    # 5,4,3,4,5,6,5,4,3,4,5,6,5,4,3,4,5,6,5,4,3,4,5,6
    # For each ring n, create a sequence that goes from n to 2*n, then back to n+1, and repeats 4 times. Starting with
    #  ring 2, the last (n-1) items of the sequence need to be shifted to the beginning (this accounts for the fact)
    #  that in general the lowest number in a ring is not the one directly to the right of 1, but (n-1) steps below it.

    if ring_number == 0:
        return [0]
    else:
        first_part = list(range(ring_number, 2*ring_number))
        pyramid_without_last_item = (first_part + [2*ring_number] + list(reversed(first_part))[:-1]) # Remove last entry in the reversed list
        full_sequence = pyramid_without_last_item * 4  # Repeat it four times
        if (ring_number >= 2):
            for _ in range(1, ring_number):
                full_sequence.insert(0, full_sequence.pop()) # Rotate the last item to the front of the list
        return full_sequence

# if n is the ring number (starts at 0)
# - Min num in sequence of steps required to reach 1 is n (for the numbers directly in line with the center 1 in any direction)
# - Max num in sequence of steps required to reach 1 is 2*n (for the numbers in any corner of the ring)
# - There's n+1 different amounts of steps required for numbers in that ring
# - Ring 0 is an edge case

# Algorithm to calculate necessary steps for X:
# - Get the largest ring N whose lowest number M is less than or equal to X
# - Calculate the sequence whose items are the number of steps required to reach 1, for each number in ring N, starting from the lowest number in the ring
# - Return the (X-M)'th entry from the sequence

print(('Input', 'N (ring number)', 'M (first number in ring)', 'index in output sequence', 'output'))
(N, M) = get_closest_first_number_in_ring(input_data)
sequence_of_number_of_required_steps = sequence_for_ring(N)
index = (input_data - M)
print((input_data, N, M, index, sequence_of_number_of_required_steps[index]))