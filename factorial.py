import sys
sys.setrecursionlimit(10**6)
def factorial(n):
    if n < 0 and int(n) != n:
      print("NA")
    if n == 1 or n == 0:
        return 1
    else:
       return n*factorial(n-1)
f = int(input("ENTER YOUR NUMBER: "))
print(factorial(f))