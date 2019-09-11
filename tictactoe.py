def displayBoard(theBoard):
    count=0
    li=list(theBoard.keys())
    for c in li:
         print(theBoard[c]+'|',end='')
         count=count+1
         if count > 2:
            print("")
            while count > 0:
                print('--',end='')
                count=count-1
            print("")

def updateBoard(x,y,theBoard):
    theBoard[y]=x
    print(theBoard)
    displayBoard(theBoard)
def playerInput(co,chance,theBoard):
    
    print('Enter player{chance} choice  '.format(chance=chance))
    x=input()
    print('Enter player{chance} posiion '.format(chance=chance))
    y=input()
    updateBoard(x,y,theBoard)
    if co > 4:
        declareResult(y,chance,theBoard)
def declareResult(y,chance,theBoard):
if __name__ == '__main__' :
    theBoard =  {'TL':'','TM':'','TR':'',
            'ML':'','MM':'','MR':'',
            'LL':'','LM':'','LR':''
            }
    displayBoard(theBoard)
    count=0
    co=0
    while True:
        if count ==2:
            count=0
        else:
            co=co+1
            count=count+1
            playerInput(co,count,theBoard)
        



