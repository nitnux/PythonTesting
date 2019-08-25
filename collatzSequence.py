#if no is even print num/2
#if no. is odd print 3*num +1
#check input validation  for integer
import sys
def collatz(num):
    if num % 2 == 0:
        return num / 2
    elif num % 2 == 1:
        return 3*num+1
    else:
        pass
if __name__ == "__main__":
    try:
        s=int(input("enter the no."))
    except:
        print("wrong input  please enter  integer")
        sys.exit(0)
    print(collatz(s))

