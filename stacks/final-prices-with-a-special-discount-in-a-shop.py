class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:


        mono_stack = []
        answer = []
        for price in prices:
            answer.append(price)
        n = len(prices)
        if n == 0:
            return []
        # elif prices == sorted(prices):
        #     return prices
        

        for i in range(n-1, -1, -1):
            while mono_stack and (prices[mono_stack[-1]] > prices[i]):
                mono_stack.pop()
            
            # mono_stack.append(i)
            
            if mono_stack:
                answer[i] -= prices[mono_stack[-1]]
                mono_stack.append(i)
            else:
                mono_stack.append(i)

        return answer

        
        