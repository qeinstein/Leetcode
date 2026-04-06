class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        result = self.dfs(stickers, target, 0, {})
        return result if result != float("inf") else -1
    
    def dfs(self, stickers, target, idx, memo):
        if target == "":
            return 0

        if idx == len(stickers):
            return float("inf")

        key = (idx, target)
        if key in memo:
            return memo[key]
        
        result = self.dfs(stickers, target, idx+1, memo)

        # choice 2 try to take the current sticker
        currentSticker = stickers[idx]
        newTarget = target
        somethingRemoved = False
        for c in currentSticker:
            idxToRemove = newTarget.find(c)
            if idxToRemove != -1:
                newTarget = newTarget[:idxToRemove] + newTarget[idxToRemove+1:]
                somethingRemoved = True
        if somethingRemoved:
            result = min(result, 1 + self.dfs(stickers, newTarget, idx, memo))

        #cache the result
        memo[key] = result
        return result
