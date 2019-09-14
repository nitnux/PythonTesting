import sys

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
    if y == 'TL' or y=='TM' or y=='TR' or y=='ML' or y=='MM' or y=='MR' or y=='LL' or y=='LM' or y=='LR':

        if theBoard.get(y) == ' ':
            updateBoard(x,y,theBoard)
            print(y)
            if co > 4 and co < 9:
                declareResult(y,chance,theBoard)
        else:
            print('value is initialise')
    else:
        pass
def declareResult(y,chance,theBoard):
    print(y)
    if y == 'TL':
        if theBoard[y] == theBoard['TM'] == theBoard['TR']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif theBoard[y] == theBoard['MM'] == theBoard['LR']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif theBoard[y] == theBoard['ML'] == theBoard['LL']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    elif y == 'TM':
        if  theBoard[y] == theBoard['TL'] == theBoard['TR']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif theBoard[y] == theBoard['MM'] == theBoard['LM'] :
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    elif y == 'TR':
        if theBoard[y] == theBoard['TM'] == theBoard['TL']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif theBoard[y] == theBoard['LR'] == theBoard['MR']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif theBoard[y] == theBoard['MM'] == theBoard['LL']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    elif y == 'ML':
        if theBoard[y] == theBoard['TL'] == theBoard['LL']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif theBoard[y] == theBoard['MM'] == theBoard['MR']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    elif y == 'MM':
        if theBoard[y] == theBoard['TL'] == theBoard['LR']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif theBoard[y] == theBoard['TM'] == theBoard['LM']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif theBoard[y] == theBoard['LL'] == theBoard['TR']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif theBoard[y] == theBoard['ML'] == theBoard['MR']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    elif y == 'MR':
        if theBoard[y] == theBoard['LR'] == theBoard['TR']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif theBoard[y] == theBoard['ML'] == theBoard['MM']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    elif y == 'LL':
        if theBoard[y] == theBoard['ML'] == theBoard['TL']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif theBoard[y] == theBoard['LM'] == theBoard['LR']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif theBoard[y] == theBoard['MM'] == theBoard['TR']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    elif y == 'LM':
        if theBoard[y] == theBoard['TM'] == theBoard['MM']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif theBoard[y] == theBoard['LL'] == theBoard['LR']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    elif y == 'LR':
        if theBoard[y] == theBoard['MR'] == theBoard['TR']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif theBoard[y] == theBoard['MM'] == theBoard['TL']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif theBoard[y] == theBoard['LM'] == theBoard['LL']:
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    else:
        pass

if __name__ == '__main__' :
    theBoard =  {'TL':' ','TM':' ','TR':' ',
            'ML':' ','MM':' ','MR':' ',
            'LL':' ','LM':' ','LR':' '
            }
    
    displayBoard(theBoard)
    count=0
    co=0
    while co != 9:
        if count ==2:
            count=0
        else:
            co=co+1
            count=count+1
            if playerInput(co,count,theBoard):
                pass
            else:
                co=count-1
                count=count-1



