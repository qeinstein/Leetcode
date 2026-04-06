class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # find the no of occurences or R, L, U, D
        # return R == L and U == D
        R, L, U, D = moves.count('R'), moves.count('L'), moves.count('U'), moves.count('D')

        return R == L and U == D
        