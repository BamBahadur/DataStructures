class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(n) for n in nums]
        nums.sort()
        return str(nums[-k])