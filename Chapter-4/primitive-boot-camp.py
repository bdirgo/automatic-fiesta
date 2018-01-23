# Primative types boot camp from elements of programming interviews

def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

print("Number of '1's' in the bits representing these numbers")

for x in range(1,100):
    print(str(x) + ":")
    print(count_bits(x))
    print(hex(x))

