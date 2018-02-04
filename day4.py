import utils
input_data = utils.read_lines(4)

def is_valid(passphrase):
    words = passphrase.split(' ')
    return len(words) == len(set(words))

print(len([passphrase for passphrase in input_data if is_valid(passphrase)]))