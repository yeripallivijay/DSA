import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# #Q1) Sum of First N Numbers
# class Solution:
#     def NnumbersSum(self, N):
        
#         if N == 0:
#             return 0
#         return  N + self.NnumbersSum(N-1)

# if __name__ == "__main__":
#     solution = Solution()
#     N = 10 
#     print(f"Sum of first {N} numbers is {solution.NnumbersSum(N)}")

# #Q2) Factorial of a Given Number
# class Solution:
#     def factorial(self, n):
#         if n<=1:
#             return 1
#         return n*self.factorial(n-1)

# if __name__ == "__main__":
#     solution = Solution()
#     N = 5 
#     print(f"Factorial of {N} is {solution.factorial(N)}")

# #Q3) Sum of Array Elements
# class Solution:
#     def factorial(self, n):
#         if n<=1:
#             return 1
#         return n*self.factorial(n-1)

# if __name__ == "__main__":
#     solution = Solution()
#     N = 5 
#     print(f"Factorial of {N} is {solution.factorial(N)}")
# #Q4) Reverse a String I
# class Solution:
#     def reverseString(self, s):
#         def reverse(s, left, right):
#             if left >= right:
#                 return
#             s[left], s[right] = s[right], s[left]
#             reverse(s, left + 1, right - 1)

#         reverse(s, 0, len(s) - 1)
#         return s

# if __name__ == "__main__":
#     solution = Solution()
#     s = ['h', 'e', 'l', 'l', 'o']
    
    
#     reversed_s = solution.reverseString(s)
#     print(reversed_s)

# #Q5) Check if String is Palindrome or Not
# class Solution:    
#     def palindromeCheck(self, s:str)->bool:
#         return self.isPalindrome(s,0,len(s)-1)
#     def isPalindrome(self,s:str,left:int,right:int)-> bool:
#         if left >= right:
#             return True
#         if s[left] != s[right]:
#             return False
#         return self.isPalindrome(s,left+1,right-1)

# if __name__ == "__main__":
#     solution = Solution()
#     print(solution.palindromeCheck("hannah"))  
#     print(solution.palindromeCheck("aabbaaa"))  
#     print(solution.palindromeCheck("aba"))

# #Q6) Check if a Number is Prime or Not
# class Solution:
#     def checkPrime(self, num):
#         if num <= 1:
#             return False
#         return self.prime(num,2)
#     def prime(self,num,x):
#         if x>num**0.5:
#             return True
#         if num % x == 0:
#             return False
#         return self.prime(num,x+1)

# if __name__ == "__main__":
#     solution = Solution()
#     num = 7  
#     result = solution.checkPrime(num)  
#     print(result) 

# #Q7) Reverse an array
# class Solution:
#     def reverseArray(self, nums):
#         self.reverse(nums,0,len(nums)-1)
#         return nums
#     def reverse(self,nums,left,right):
#         if left >= right:
#             return
#         nums[left],nums[right] = nums[right],nums[left]
#         self.reverse(nums,left+1,right-1)

# if __name__ == "__main__":
#     solution = Solution()
#     nums = [1, 2, 3, 4, 5]  
#     result = solution.reverseArray(nums)  
#     print(result) 

# #Q8) Check if the Array is Sorted II
# class Solution:
#     def isSorted(self, nums):
#         nums = list(nums)
#         if len(nums) <= 1:
#             return True
#         return self.sort(nums,0,1)
#     def sort(self,nums,left,right):
#         if right >= len(nums):
#             return True
#         if nums[left] > nums[right]:
#             return False
#         return self.sort(nums,left+1,right+1)

# if __name__ == "__main__":
#     solution = Solution()
#     nums = [1, 2, 3, 4, 5] 
#     result = solution.isSorted(nums) 
#     print("Array is sorted" if result else "Array is not sorted")

# #Q9) Sum of Digits in a Given Number
# class Solution:
#     def addDigits(self, num):
#         if num < 10:
#             return num
#         sum_digits = self.sumDigits(num)
#         return self.addDigits(sum_digits)
#     def sumDigits(self,num):
#         if num==0:
#             return 0
#         return self.sumDigits(num // 10) + (num % 10)

# if __name__ == "__main__":
#     solution = Solution()

    
#     num = 529

    
#     result = solution.addDigits(num)
#     print("Sum of digits:", result)

#Q10) Fibonacci Number
class Solution:
    def fib(self, n):
        if n == 0:
            return 0
        elif n==1:
            return 1
        return self.fib(n-1)+self.fib(n-2)
    
if __name__ == "__main__":
    solution = Solution()
    n = 6  
    print(f"Fibonacci number at position {n} is {solution.fib(n)}")