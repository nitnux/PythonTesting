import os
from argparse import ArgumentParser
if __name__ == '__main__':
    parser=ArgumentParser(prog="renameFile")
    parser.add_argument('--dir',type=str)
    parser.add_argument('--projcode',type=str)
    args=parser.parse_args()
    os.system('ls -rt {arg} > tmp.txt'.format(arg=args.dir))
    os.system('mkdir {arg} '.format(arg=args.projcode))
    projcode=args.projcode
    cwd=os.getcwd()
    d=open('tmp.txt','r')
    count=0
    g= list(d.read().splitlines())[:-1]
    d.close()
    os.chdir("./{arg}".format(arg=args.dir))
    for r in g:
        if os.path.isdir(r):
            os.system('ls -rt {f} > ./{f}/tmp1.txt'.format(f=r))
            os.chdir("./{f}".format(f=r))
            d=open('tmp1.txt','r')
            s= list(d.read().splitlines())[:-1]
            d.close()
            for i in s:
                os.rename(i,projcode+str(count))
                os.system("mv {projcode}{count} {cwd}/{projcode}".format(count=count,cwd=cwd,projcode=projcode))
                count=count+1

            os.chdir("{cwd}/{arg}".format(arg=args.dir,cwd=cwd))

        elif  os.path.isfile(r):
            os.rename(r,projcode+str(count))
            os.system("mv {projcode}{count} {cwd}/{projcode}".format(count=count,cwd=cwd,projcode=projcode))
            count=count+1
        else:
            continue

