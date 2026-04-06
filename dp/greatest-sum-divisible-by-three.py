class Solution(object):
    def maxSumDivThree(self, nums):
        summ=sum(nums)
        rem = summ%3
        onenum=0
        twonums = []
        nums.sort()
        #print(nums,rem)
        if rem == 0:
            return summ

        for i in nums:
            if onenum>0 and len(twonums)==2:
                break
            if i%3==rem and onenum==0:
                onenum=i
            if rem==1:
                if i%3==2 and len(twonums)<2:
                    twonums.append(i)
            if rem==2:
                if i%3==1 and len(twonums)<2:
                    twonums.append(i)

        #print(onenum, twonums)
        if len(twonums)==2 and onenum>0:
            if sum(twonums)>onenum:
                summ-=onenum
            else:
                summ-=sum(twonums)
        else:
            if len(twonums)==2:
                summ-=sum(twonums)
            else:
                summ-=onenum
        return summ