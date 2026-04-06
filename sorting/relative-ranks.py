class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        #just five numbers
        # score = score.sort()
        score_dict = {value : index for index, value in enumerate(score)}
        score_sorted = sorted(score) #.sort()
        n = len(score)
        answer = ["0"] * n

        count = 1
        for i in range(n-1, -1, -1):
            if count == 1:
                answer[score_dict[score_sorted[i]]] = "Gold Medal"
                count += 1
            elif count == 2:
                answer[score_dict[score_sorted[i]]] = "Silver Medal"
                count += 1
            elif count == 3:
                answer[score_dict[score_sorted[i]]] = "Bronze Medal"
                count += 1
            else:
                answer[score_dict[score_sorted[i]]] = str(count)
                count += 1

        print(answer)
        return answer



        
        
        