def has_unique_chars(string):
    my_set = set()
    for char in string:
        if char in my_set:
            return False
        my_set.add(char)
    return True




print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False