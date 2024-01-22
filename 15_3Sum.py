class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        triplets = set()
        length = len(nums)
        nums.sort()
        for i in range(length - 2):
            first = nums[i]
            
            if i > 0 and first == nums[i - 1]:
                continue
            
            left, right = i + 1, length - 1            
            
            while left < right:
                second, third = nums[left], nums[right]                
                sum = first + second + third
                
                if sum == 0:
                    triplets.add((first, second, third))
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left -1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum < 0:
                    left += 1
                else: 
                    right -= 1

        out = list(triplets)        
        return out