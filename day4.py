import utils
input_data = utils.read_lines(4)

def is_valid(passphrase):
    words = passphrase.split(' ')
    return len(words) == len(set(words))

def is_valid_stronger(passphrase):
    words = passphrase.split(' ')
    words_with_sorted_letters = [''.join(sorted(w)) for w in words]
    return len(words_with_sorted_letters) == len(set(words_with_sorted_letters))

print(len([passphrase for passphrase in input_data if is_valid(passphrase)]))
print(len([passphrase for passphrase in input_data if is_valid_stronger(passphrase)]))