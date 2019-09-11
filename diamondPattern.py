from __future__ import print_function
s=input("Enter : ")
n=int(s)
for i in range(0,n):
    print(" "*(n-i),end='')
    print("*"*(2*i+1))
for j in range(1,n):
    print(" "*(j+1),end='')
    print("*"*(2*n-2*j-1))
