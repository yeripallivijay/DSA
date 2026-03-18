import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')


class Solution:
    def insertionSort(self, nums):
        n = len(nums)
        for i in range(1,n):
            key=nums[i]
            j = i - 1
            while j>=0 and nums[j] > key:
                nums[j+1] = nums[j]
                j-=1
            nums[j+1] = key
        return nums
    

if __name__ == "__main__":
    
    solution = Solution()
    
    nums = [13, 46, 24, 52, 20, 9]
    
    print("Before Using Insertion Sort:")
    for num in nums:
        print(num, end=" ")
    print()
    
    
    nums = solution.insertionSort(nums)
    
    print("After Using Insertion Sort:")
    for num in nums:
        print(num, end=" ")
    print()