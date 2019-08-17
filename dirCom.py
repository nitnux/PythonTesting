



import os
from argparse import ArgumentParser
parser=ArgumentParser(prog="dirCom")
parser.add_argument('--dir',type=str)
parser.add_argument('--cdir',type=str)
args=parser.parse_args()
os.system('ls {arg} > tmp.txt'.format(arg=args.dir))
os.system('ls {arg} > tmp1.txt'.format(arg=args.cdir))

d=open('tmp.txt','r')
c=open('tmp1.txt','r')
li=list(c.read().splitlines())
print(li)
dub=[]
for s in d.read().splitlines():
    for r  in li:
        if s == r:
            if bool(os.system('diff {arg}/{s} {arg1}/{r}'.format(arg=args.dir,s=s,arg1=args.cdir,r=r))) != True :
                print("duplicate")
                dub.append(s)
            else:
                continue
        else:
            continue
print(dub)
