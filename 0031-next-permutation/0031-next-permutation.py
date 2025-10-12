class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pinpoint = -1

        # Step 1: Find the first decreasing index from right
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                pinpoint = i
                break

        # Step 2: If no such index found, reverse all (last permutation → first)
        if pinpoint == -1:
            nums.reverse()
            return nums  # Important fix!

        # Step 3: Find element just larger than nums[pinpoint]
        for i in range(len(nums)-1, pinpoint, -1):
            if nums[i] > nums[pinpoint]:
                nums[i], nums[pinpoint] = nums[pinpoint], nums[i]
                break

        # Step 4: Reverse the part after pinpoint
        start, end = pinpoint + 1, len(nums) - 1
        while end > start:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        return nums
