import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')


class Solution:
    def merge(self,arr,low,mid,high):
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left +=1
            else:
                temp.append(arr[right])
                right +=1
        while left <= mid:
            temp.append(arr[left])
            left +=1
        while right <= high:
            temp.append(arr[right])
            right +=1
        for i in range(low,high+1):
            arr[i] = temp[i-low]
    def mergeSortFinal(self,arr,low,high):
        if low >= high:
            return
        # mid = (low + high)//2
        mid = low + (high - low) //2
        self.mergeSortFinal(arr,low,mid)
        self.mergeSortFinal(arr,mid+1,high)
        self.merge(arr,low,mid,high)
    def mergeSort(self, nums):
        n = len(nums)
        self.mergeSortFinal(nums,0,n-1)
        return nums
        


if __name__ == "__main__":
    arr = [9, 4, 7, 6, 3, 1, 5]
    n = len(arr)

    print("Before Sorting Array: ")
    for i in range(n):
        print(arr[i], end=" ")
    print()

    
    sol = Solution()
    
    sortedArr = sol.mergeSort(arr)

    print("After Sorting Array: ")
    for i in range(n):
        print(sortedArr[i], end=" ")
    print()