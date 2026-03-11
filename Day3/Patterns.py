import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

class Solution:
    
    def pattern1(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print()
    def pattern2(self,n):
        for i in range(n):
            for j in range(i + 1):
                print("*",end="")
            print()
    def pattern3(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end="")
            print()
    def pattern4(self,n):
        for  i in range(1,n+1):
            for j in range(1,i+1):
                print(i,end="")
            print()
    def pattern5(self,n):
        for i in range(n):
            for j in range(n-i):
                print("*",end="")
            print()
    def pattern6(self,n):
        for i in range(n):
            for  j in range(0,n-i):
                print(j+1,end="")
            print()
    def pattern7(self,n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end="")
            for j in range(2*i+1):
                print("*",end="")
            print()
    def pattern8(self,n):
        for i in range(n):
            for j in range(i):
                print(" ",end="")
            for j in range(2*n-(2*i+1)):
                print("*",end="")
            print()
    def pattern9(self,n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end="")
            for j in range(2*i+1):
                print("*",end="")
            print()
        for  i in range(n):
            for j in range(i):
                print(" ",end="")
            for j in range(2*n-(2*i+1)):
                print("*",end="")
            print()
    def pattern10(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*",end="")
            print()
        for i in range(1,n):
            for j in range(n-i):
                print("*",end="")
            print()
    def pattern11(self,n):
        start = 1
        for i in range(n):
            if i%2==0:
                start = 1
            else:
                start = 0
            for j in range(i + 1):
                print(start, end=" ")
                start = 1 - start
            print()
    def pattern12(self,n):
        spaces = 2*(n-1)
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end="")
            for j in range(1, spaces +1):
                print(" ",end="")
            for j in range(i, 0, -1):
                print(j, end="")
            print()
            spaces -= 2
    def pattern13(self,n):
        num = 1
        for i in range(1,n+1):
            for  j in range(1,i+1):
                print(num,end=" ")
                num += 1
            print()
    def pattern14(self,n):
        for i in range(n):
            char = ord('A')
            for ch in range(char,char + i + 1):
                print(chr(ch),end="")
            print()
    def pattern15(self,n):
        for i in range(n):
            char = ord('A')
            for j in range(char,char + n - i):
                print(chr(j),end="")
            print()
    def pattern16(self,n):
        for i in range(n):
            ch = chr(ord('A') + i)
            for j in range(i + 1):
                print(ch,end="")
            print()
    def pattern17(self,n):
        for i in range(n):
            for  j in range(n-i-1):
                print(" ",end="")
            ch = 'A'
            pyramid = (2*i+1)//2
            for j in range(1,2*i+2):
                print(ch,end="")
                if j <= pyramid:
                    ch = chr(ord(ch) + 1)
                else:
                    ch = chr(ord(ch) - 1)
            print()
    def pattern18(self,n):
        for i in range(n):
            char = ord('A')
            for ch in range(char + n-1-i,char + n):
                print(chr(ch),end=" ")    
            print()
    def pattern19(self,n):
        #Upper Half  Pattern
        upperSpace = 0
        for i in range(n):
            for  j in range(n-i):
                print("*",end="")
            for j in range(upperSpace):
                print(" ",end="")
            for j in range(n-i):
                print("*",end="")
            upperSpace +=2
            print()
        #Lower Half Pattern
        lowerSpace = 2 * n - 2
        for i in range(1,n+1):
            for j in range(i):
                print("*",end="")
            for j in range(lowerSpace):
                print(" ",end="")
            for j in range(i):
                print("*",end="")
            lowerSpace -= 2
            print()
    def pattern20(self,n):
        
        spaces = 2 * n - 2
        for i in range(1, 2 * n):
            stars = i
            if i > n:
                stars = 2 * n - i
            for j in range(stars):
                print("*",end="")
            for j in range(spaces):
                print(" " , end="")
            for j in range(stars):
                print("*",end="")
            print()
            if i < n:
                spaces -= 2
            else:
                spaces += 2
    def pattern21(self,n):
        for i in range(n):
            for j in range(n):
                if i==0 or i==n-1:
                    print("*",end="")
                elif j==0 or j==n-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()       
    def pattern22(self,n):
        for i in range(2*n-1):
            for j in range(2*n-1):
                top = i
                left = j
                right = (2*n-2)-j
                bottom = (2*n-2)-i
                print((n - min(min(top, bottom), min(left, right))), end=" ")
            print()
    def main(self):
        N = int(input())
        sol = Solution()
        # sol.pattern1(N)
        # sol.pattern2(N)
        # sol.pattern3(N)
        # sol.pattern4(N)
        # sol.pattern5(N)
        # sol.pattern6(N)
        # sol.pattern7(N)
        # sol.pattern8(N)
        # sol.pattern9(N)
        # sol.pattern10(N)
        # sol.pattern11(N)
        # sol.pattern12(N)
        # sol.pattern13(N)
        # sol.pattern14(N)
        # sol.pattern15(N)
        # sol.pattern16(N)
        # sol.pattern17(N)
        # sol.pattern18(N)
        # sol.pattern19(N)
        # sol.pattern20(N)
        # sol.pattern21(N)
        sol.pattern22(N)



if __name__ == "__main__":
    Solution().main()