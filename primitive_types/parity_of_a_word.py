"""
This function calculates the parity of a word
here XOR operation is used for only remembering the last bits value.
"""


def determine_parity(x: int) -> int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


print(determine_parity(4))
# In the above fun 4 is represented as 0100 which has parity of 1