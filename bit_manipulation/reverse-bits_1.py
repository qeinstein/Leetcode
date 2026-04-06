class Solution:
    def reverseBits(self, n: int) -> int:
        # reverse the bits of a given guven 32bits signed integer

        bits = []
        rev = 0
        i = 0

        while i < 32:
            bits.append(bool(n%2))
            n //= 2
            i += 1
        
        i = 31
        cnt = 0
        while i >= 0:
            rev += (bits[i] * pow(2, cnt))
            cnt += 1
            i -= 1

        return rev
