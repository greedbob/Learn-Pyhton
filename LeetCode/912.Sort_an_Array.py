class Solution:
    def sortArray(self, nums):
        if len(nums) < 2:
            return nums
        else:
            num = nums[0]
            right = [i for i in nums[1:] if i > num]
            left = [i for i in nums[1:] if i <= num]
            return self.sortArray(left) + [num] + self.sortArray(right)


arr = [5, 2, 3, 1]
solution = Solution()
ans = solution.sortArray(arr)
print(ans)
