#python3 code
import os
print("enter the domain with ip to ping\n")
while True:

    option=input("\ndo you want to continue?:")
    if option == 'y':
        ip=input('ip:')
        domain=input('domain:')
        host=open("/etc/hosts",'a+')
        hostdomain=open("./hostdomain.txt","a+")
        host.write('\n'+ip+'\t'+domain+'\n').close()
        hostdomain.write('\n'+domain).close()
    else:
        break

with open("./hostdomain.txt") as domain:
    read=domain.read()
    for dom in read.splitlines():
        os.system("ping {dom}".format(dom=dom))

