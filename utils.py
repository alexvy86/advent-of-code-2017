def read_file(day_number):
    """Opens the input file for day day_number and returns the handle"""
    return open(f"inputfiles/input{day_number}.txt")

def read_lines(day_number):
    all_data = read_file(day_number).read()
    return [line for line in all_data.split('\n')]