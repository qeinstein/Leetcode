class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        min_time = float('inf')

        for i in range(len(landDuration)):
            for j in range(len(waterDuration)):
                endforland = landDuration[i] + landStartTime[i]
                waterstraland = max(endforland, waterStartTime[j])
                total = waterstraland + waterDuration[j]

                endforwater = waterDuration[j] + waterStartTime[j]
                landstrawater = max(endforwater, landStartTime[i])
                total2 = landstrawater + landDuration[i]
                
                min_time = min(min_time, total, total2)

        return min_time