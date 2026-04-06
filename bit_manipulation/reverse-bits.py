class Solution:
    def reverseBits(self, n: int) -> int:
        # reverse the bits of a given guven 32bits signed integer
        binary = bin(n)[2:].zfill(32)[::-1]
        return int(binary, 2)
        