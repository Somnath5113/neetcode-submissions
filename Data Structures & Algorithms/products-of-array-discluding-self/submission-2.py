class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum=math.prod(nums)
        ans=[]
        for i,j in enumerate(nums):
            val=0
            if j!=0:
                val=sum//j
            if j==0:
                val=math.prod(nums[:i]+nums[i+1:])

            ans.append(val)
        return ans

        