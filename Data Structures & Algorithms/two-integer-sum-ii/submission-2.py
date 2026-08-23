class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hel={}
        for i,j in enumerate(numbers):
            diff=target-j
            if diff in hel:
                return [hel[diff]+1,i+1]
            hel[j]=i
            
        