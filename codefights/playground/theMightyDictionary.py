# import _dictinfo
from timeit import timeit
def bits(n):
	n += 2**32
	return bin(n)[-32:] # remove '0b'

print(bits(1))
print(bits(-1))
