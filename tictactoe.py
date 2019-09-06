def displayBoard(theBoard):
    count=0
    for c in theBoard.values():
        if count < 2:
            print(c+'|')
            count=count+1
        else:
            print('/n')
            count=0
def displayBoard(x,y,theBoard):
    count=0
    for c in theBoard.values():
        if count < 2:
            print(c+'|')
            count=count+1
        else:
            print('/n')
            count=0
def updateBoard(x,y,theBoard):
    dislayBoard(x,y,theBoard)
def declareResult(x,y,theBoard):
    updateBoard(x,y,theBoard)
if __name__ == '__main__' :
    theBoard =  {'TL':'','TM':'','TR':'',
                'ML':'','MM':'','MR':'',
                'LL':'','LM':'','LR':''
            }
    displayBoard(x,y,theBoard)
    x=input('Enter your choice  ')
    y=input('Enter your posiion ')
    declareResult(x,y,theBoard)

