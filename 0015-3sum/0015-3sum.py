class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_len = len(nums)
        x = []

        for i in range(nums_len):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            first = nums[i]
            start = i + 1
            end = nums_len - 1
            target = 0 - first

            while end > start:
                if nums[start] + nums[end] > target:
                    end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    x.append([first, nums[start], nums[end]])
                    
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1

                    start += 1
                    end -= 1

        return x
