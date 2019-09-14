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
            print(co)
            if co > 4 and co < 9:
                declareResult(y,chance,theBoard)
        else:
            print('value is initialise')
            return False
        return True
    else:
        return False
def declareResult(y,chance,theBoard):

    if y == 'TL':
        print('TL')
        if  not bool(ord(theBoard[y]) ^ ord(theBoard['TM']) & ord(theBoard['TR']) ):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif  not bool(ord(theBoard[y]) ^ ord(theBoard['MM']) & ord(theBoard['LR'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif  not bool(ord(theBoard[y]) ^ ord(theBoard['ML']) & ord(theBoard['LL']) ):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    elif y == 'TM':
        print('TM')
        if  not bool(ord(theBoard[y]) ^ ord(theBoard['TL']) & ord(theBoard['TR'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif  not bool(ord(theBoard[y]) ^ ord(theBoard['MM']) & ord(theBoard['LM'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    elif y == 'TR':
        print('TR')
        if  not bool(ord(theBoard[y]) ^ ord(theBoard['TM']) & ord(theBoard['TL'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif  not bool(ord(theBoard[y]) ^ ord(theBoard['LR']) & ord(theBoard['MR'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif  not bool(ord(theBoard[y]) ^ ord(theBoard['MM']) & ord(theBoard['LL'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    elif y == 'ML':
        print('ML')
        if  not bool(ord(theBoard[y]) ^ ord(theBoard['TL']) & ord(theBoard['LL'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif  not bool(ord(theBoard[y]) ^ ord(theBoard['MM']) & ord(theBoard['MR'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    elif y == 'MM':
        print('MM')
        if  not bool(ord(theBoard[y]) ^ ord(theBoard['TL']) & ord(theBoard['LR'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif  not bool(ord(theBoard[y]) ^ ord(theBoard['TM']) & ord(theBoard['LM'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif  not bool(ord(theBoard[y]) ^ ord(theBoard['LL']) & ord(theBoard['TR'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif  not bool(ord(theBoard[y]) ^ ord(theBoard['ML']) & ord(theBoard['MR'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    elif y == 'MR':
        print('MR')
        if  not bool(ord(theBoard[y]) ^ ord(theBoard['LR']) & ord(theBoard['TR'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif  not bool(ord(theBoard[y]) ^ ord(theBoard['ML']) & ord(theBoard['MM'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    elif y == 'LL':
        print('LL')
        if  not bool(ord(theBoard[y]) ^ ord(theBoard['ML']) & ord(theBoard['TL'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif  not bool(ord(theBoard[y]) ^ ord(theBoard['LM']) & ord(theBoard['LR'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif  not bool(ord(theBoard[y]) ^ ord(theBoard['MM']) & ord(theBoard['TR'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    elif y == 'LM':
        print('LM')
        if  not bool(ord(theBoard[y]) ^ ord(theBoard['TM']) & ord(theBoard['MM'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif  not bool(ord(theBoard[y]) ^ ord(theBoard['LL']) & ord(theBoard['LR'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        else:
            pass
    elif y == 'LR':
        print('LR')
        if  not bool(ord(theBoard[y]) ^ ord(theBoard['MR']) & ord(theBoard['TR'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif  not bool(ord(theBoard[y]) ^ ord(theBoard['MM']) & ord(theBoard['TL'])):
            print('player {chance}win'.format(chance=chance))
            sys.exit()
        elif  not bool(ord(theBoard[y]) ^ ord(theBoard['LM']) & ord(theBoard['LL'])):
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
    while co < 9:
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




