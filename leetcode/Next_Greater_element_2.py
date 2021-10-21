class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            j = i+1
            if j == len(nums):
                j=0
            flag = None
            while j!=i:
                if j==len(nums):
                    j=0
                elif nums[j]>nums[i]:
                    flag = j
                    break
                else:
                    flag = None
                    j=j+1
            if flag ==None:
                output.append(-1)
            else:
                output.append(nums[flag])
        return output