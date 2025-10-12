class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = (low+high)//2

            if nums[mid]== target:
                return mid
            
            if nums[low]<=nums[mid]:
                # If the left half is sorted part
                if nums[low]<=target and target<=nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            
            else:
                # If right part is sorted
                if nums[mid]<=target and target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1