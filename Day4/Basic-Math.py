import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')


# # Q1) Count all Digits of a Number
# class Solution:
#     def countDigit(self,n):
#         if n==0:
#             return 1
        
#         count = 0

#         while n>0:
#             count = count + 1
#             n = n // 10

#         return count

# n = 4

# sol = Solution()
# ans = sol.countDigit(n)

# print(f"The count of digits in the given number is: {ans}")

# # Q2) Count number of oddDigits in the given numbers
# class Solution:
#     def countOddDigit(self,n):
#         oddDigits = 0

#         while n>0:
#             lastDigit = n%10

#             if lastDigit % 2 == 1:
#                 oddDigits = oddDigits + 1
            
#             n = n // 10

#         return oddDigits

# n = 5627

# sol = Solution()
# ans = sol.countOddDigit(n)

# print(f"The count of odd digits in the given number is: {ans}")

# # Q3) Reverse a Number
# class Solution:
#     def reverseNumber(self,n):
#         reverseNum = 0

#         while n>0:
#             lastDigit = n%10
#             reverseNum = (reverseNum * 10) + lastDigit
#             n = n // 10
#         return reverseNum

# if __name__ == "__main__":
#     n = 6678


# sol = Solution()
# ans = sol.reverseNumber(n)

# print("The reverse of given number is:", ans)

# # Q4) Palindrome Number
# class Solution:
#     def isPalindrome(self,n):
#         copy = n

#         reverseNum = 0

#         while n>0:
#             lastDigit = n%10

#             reverseNum = (reverseNum * 10) + lastDigit
#             n = n // 10

#         return reverseNum == copy

# if __name__ == "__main__":
#     n = 6678


# sol = Solution()
# ans = sol.isPalindrome(n)

# if ans:
#     print("The given number is a palindrome")
# else:
#     print("The given number is not a palindrome")

# # Q5) Find Largest Number
# class Solution:
#     def largestDigit(self,n):
#         largestDigit = 0

#         while n>0:
#             lastDigit = n % 10
#             if lastDigit > largestDigit:
#                 largestDigit = lastDigit
#             n = n//10
#         return largestDigit

# if __name__ == "__main__":
#     n = 99


# sol = Solution()
# ans = sol.largestDigit(n)

# print("The largest digit in the number is:", ans)

# # Q6) Find Factorial Number
# class Solution:
#     def factorial(self,n):
#         if n == 0:
#             return 1
#         ans = 1
#         for i in range(1,n+1):
#             ans = ans * i
#         return ans

# if __name__ == "__main__":
#     n = 3


# sol = Solution()
# ans = sol.factorial(n)

# print("The factorial of given number is:", ans)

# # Q7) Check if the number is Armstrong or not
# import math
# class Solution:
#     def countDigit(self,n):
#         if n==0:
#             return 1
#         count = int(math.log10(n))+1
#         return count
    
#     def isArmstrong(self,n):
#         count = self.countDigit(n)
#         sum = 0
#         copy = n
#         while n>0:
#             lastDigit = n % 10
#             sum = sum + pow(lastDigit,count)
#             n=n//10
        
#         if sum == copy:
#             return True
#         return False

# if __name__ == "__main__":
#     n = 153


# sol = Solution()
# ans = sol.isArmstrong(n)

# if ans:
#     print(f"{n} is an Armstrong number.")
# else:
#     print(f"{n} is not an Armstrong number.")

# # Q8) Check for perfect number

# class Solution:
#     def isPerfect(self,n):
#         total = 0
#         for i in range(1,n):
#             if n%i == 0:
#                 total = total + i
#         return total==n

# if __name__ == "__main__":
#     n = 4
#     sol = Solution()
#     ans = sol.isPerfect(n)
#     if ans:
#         print(f"{n} is a perfect number.")
#     else:
#         print(f"{n} is not a perfect number.")

# # Q9) Check for prime number

# class Solution:
#     def isPrime(self,n):
#         if n<2:
#             return False
#         for i in range(2,n):
#             if n %i==0:
#                 return False
#         return True
# if __name__ == "__main__":
#     n = 3
#     sol = Solution()
#     ans = sol.isPrime(n)
#     if ans:
#         print(f"{n} is a prime number.")
#     else:
#         print(f"{n} is not a prime number.")

# # Q10) Count of Prime Numbers till N

# class Solution:
    
#     def isPrime(self, n):
#         count = 0
#         for i in range(1,n+1):
#             if n%i==0:
#                 count = count + 1
#         if count == 2:
#             return True
#         return False
    
#     def primeUptoN(self,n):
#         count = 0
#         for i in range(2,n+1):
#             if self.isPrime(i):
#                 count = count + 1
#         return count
    
# if __name__ == "__main__":
#     n = 3
#     sol = Solution()
#     ans = sol.primeUptoN(n)
#     print("The count of primes till", n, "is:", ans)

# # Q11) GCD of TWO Numbers

# class Solution:
    
#     def GCD(self, n1,n2):
#         gcd = 1
#         for i in range(1,min(n1,n2)+1):
#             if n1 % i == 0 and n2 % i == 0:
#                 gcd = i
#         return gcd
    
# if __name__ == "__main__":
#     n1 = 9
#     n2 = 8

#     sol = Solution()
#     ans = sol.GCD(n1, n2)

#     print(f"GCD of {n1} and {n2} is: {ans}")

# # Q12)LCM of two numbers
# class Solution:
    
#     def LCM(self, n1,n2):
#         lcm = 0
#         n = max(n1,n2)
#         i = 1

#         while True:
#             mul = n*i
#             if mul % n1 == 0 and mul % n2 == 0:
#                 lcm = mul
#                 break
#             i = i+1
#         return lcm
    
# if __name__ == "__main__":
#     n1 = 4
#     n2 = 6

#     sol = Solution()
#     ans = sol.LCM(n1, n2)
#     print("The LCM of", n1, "and", n2, "is:", ans)

# Q13)Divisors of a Number
class Solution:
    
    def divisors(self,n):
        ans = []
        for i in range(1,n+1):
            if n%i==0:
                ans.append(i)
        return ans
    
if __name__ == "__main__":
    n=6
    sol = Solution()
    ans = sol.divisors(n)

print(f"The divisors of {n} are: ", end="")
for i in range(len(ans)):
    print(ans[i], end=" ")




