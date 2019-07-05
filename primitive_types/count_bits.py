"""
This function count the number of ones in the integer binary
"""


def count_bits(x: int) -> int:
    count_bit = 0
    while x:
        count_bit += x & 1
        x >>= 1
    return count_bit


print(count_bits(12))
