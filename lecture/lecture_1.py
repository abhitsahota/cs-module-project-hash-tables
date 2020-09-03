def my_hash(s):
    sb = s.encode()
    total = 0
    for b in sb:
        total += b
    return total

# This is what the hash table will use to store values
my_array = [None] * 8
print(f'my array {my_array}')


# Storing a value
hash_index = my_hash('hello world') % 8
print(f'hash index {hash_index}')

my_array[hash_index] = 'my value'
print(f'my array {my_array}')

# Getting a value
hash_index = my_hash('hello world') % 8
print(my_array[hash_index])