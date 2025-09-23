class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        que = []
        res = []

        def helper(k,start,target):
            if k!=2: # finding sum till k-2 only using this recursive function "helper" there after problem will become a two sum 
                for i in range(start,len(nums)-k+1):
                    # len(nums)-k+1 -> because for k-sum you must have k numbers left over there, hence going to len(num)-k+1 only 
                    if i>start and nums[i]==nums[i-1]: # Skip duplicates at the same recursion level
                        continue
                    que.append(nums[i])
                    helper(k-1,i+1,target-nums[i])
                    que.pop() # let's say we have target = 2 and k =5 then: for first call let's say we have que = [-4,-2,-1] then we'll pop the last element and so that next element can be appended it will become [-4,-3,0]
                    # then it will become [-4,-2,1] then [-4,-2,3]
                return
            
            l = start
            r = len(nums)-1
            
            while r>l:
                if nums[l]+nums[r]<target:
                    l+=1
                elif nums[l]+nums[r]>target:
                    r-=1
                else:
                    res.append(que+[nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]: # Skip duplicate numbers on the left
                        l+=1
                        
        helper(4,0,target)
        return res
                    