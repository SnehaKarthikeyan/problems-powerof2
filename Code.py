Coding:

def is_Power_of_two(n):
        return n > 0 and (n & (n - 1)) == 0
n=int(input())
if (is_Power_of_two(n)==True):
    print("YES")
else:
    print("NO")
