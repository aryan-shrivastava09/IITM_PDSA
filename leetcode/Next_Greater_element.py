class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for i in range(len(nums1)):
            pos = nums2.index(nums1[i])
            flag = None
            for j in range(pos,len(nums2)):
                if nums2[j]>nums1[i]:
                    flag = j
                    break
                else:
                    flag = None
            if flag == None:
                output.append(-1)
            else:
                output.append(nums2[flag])
                
                        
        return output