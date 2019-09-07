import sys
l="abcdefghijklmnopqrstuvwxyz"
u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n="1234567890"
s="!@#$%^&*(){}[]\|;:~`"
x=False
y=False
z=False
k=False
while True:
	s=raw_input("enter password :")
	if len(s) <8:
		print("you are far behind")
		continue
	else:
		for t in l:
			if t in s:
				x=True						
				break
			else:
				continue
		for t in u:
			if t in s:
				y=True						
				break
			else:
				continue
		for t in n:
			if t in s:
				z=True						
				break
			else:
				continue
		for t in s:
			if t in s:
				k=True						
				break
			else:
				continue
 
	if x and y and z and k :
		print("strenth is good")
		sys.exit()
	else:
		print("your password is weak")
