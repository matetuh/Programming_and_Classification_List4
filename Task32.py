def hash_function(x):
    x = int(x,2)
    p = 50
    return x % p

print(hash_function('0010111'))