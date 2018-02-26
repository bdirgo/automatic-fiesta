#  Problem 4.1 in elements of programming interviews
    # 0 | 0 = 0
    # 0 | 1 = 1
    # 1 | 0 = 1
    # 1 | 1 = 1

    # 0 ^ 0 = 0
    # 0 ^ 1 = 1
    # 1 ^ 0 = 1
    # 1 ^ 1 = 0
    
    # 0 & 0 = 0
    # 0 & 1 = 0
    # 1 & 0 = 0
    # 1 & 1 = 1

def parity(x):
    num_bits = 0
    while x:
        num_bits ^= x & 1
        x >>= 1
    return num_bits

print("Is the number odd (1) or even (0)")

x = 2**8-1
print(hex(x))
print("or " + str(x) + ":")
print("Odd/Even?")
print(parity(x))

def set_bit(x, position):
    print(bin(x))
    print(bin(position))
    mask = 1 << position
    print(bin(mask))
    result = x | mask
    print(bin(result))
    return result

def modify_bit(x, position, state):
    print(bin(x))
    print(bin(position))
    mask = 1 << position
    print(bin(mask))
    result = x | mask
    print(bin(result))
    return result

def flip_bit(x, position):
    print(bin(x))
    print(bin(position))
    mask = 1 << position
    print(bin(mask))
    result = x ^ mask
    print(bin(result))
    return result

def clear_bit(x, position):
    print(bin(x))
    print(bin(position))
    mask = 1 << position
    print(bin(mask))
    result = x & ~mask
    print(bin(result))
    return result

def is_bit_set(x, position):
    print(bin(x))
    print(bin(position))
    mask = x >> position
    print(bin(mask))
    result = mask & 1
    print(bin(result))
    return result
    
def count_different_bits(x,y):
    x_xor_y = x ^ y
    num_bits = 0
    while x_xor_y:
        num_bits += x_xor_y & 1
        x_xor_y  >>= 1
    return num_bits

print("Clear Bit")
print(clear_bit(6,2))
print(count_different_bits(4,19))