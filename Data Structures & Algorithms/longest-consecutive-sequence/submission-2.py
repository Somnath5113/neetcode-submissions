class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        long=0
        for i in nums:
            if (i-1) not in num:
                loo=1
                while (loo+i) in num:
                    loo+=1
                long=max(loo,long)
        return long
                

        