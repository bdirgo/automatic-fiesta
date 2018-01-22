#  Problem 4.1 in elements of programming interviews

def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

print("Number of '1's' in the bits representing these numbers")

x = 2**64 -1
print(hex(x))
print("or " + str(x) + ":")
print("Count bits:")
print(count_bits(x))
