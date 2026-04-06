class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # 1. Handle leading whitespace
        if not s:
            return 0

        i = 0
        sign = 1
        
        # 2. Handle sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        result = 0
        
        # 3. Read digits and build the number
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            # 4. Check for integer overflow before adding the next digit
            # For positive numbers
            if sign == 1 and (result > 214748364 or (result == 214748364 and digit >= 7)):
                return 2147483647 # 2**31 - 1
            # For negative numbers
            if sign == -1 and (result > 214748364 or (result == 214748364 and digit >= 8)):
                return -2147483648 # -2**31
            
            result = result * 10 + digit
            i += 1
        
        return sign * result