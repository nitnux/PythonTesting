from __future__ import print_function
co=0
def displayBoard(theBoard):
    count=0
    for c in theBoard.values():
        if count < 2:
            print(c+'|',end='')
            count=count+1
        else:
	    
	    print("")
	    while count > 0:
		print('--',end='')
            	count=count-1
	    print("")

def playerInput(chance,theBoard):
    x=input('Enter player{chance} choice  '.format(chance))
    y=input('Enter player{chance} posiion '.format(chance))
    updateBoard(x,y,theBoard)
    co=co+1
    if co > 4:
        declareResult(y,chance,theBoard)
def updateBoard(x,y,theBoard):
    theBoard[y]=x
    dislayBoard(theBoard)
def declareResult(y,chance,theBoard):
    if y == 'TL':
        if int(theBoard['TL'] )^int(theBoard['TM'] ) ^int(theBoard['TR'] ):
		pass
	elif int(theBoard['TL'] )^int(theBoard['TM'] ) ^int(theBoard['LL'] ):
		pass
	elif int(theBoard['TL'] )^int(theBoard['MM'] ) ^int(theBoard['LR'] ):
		pass
	else:
		pass
        
    elif y == 'TM':
	if int(theBoard['TM'] )^int(theBoard['TL'] ) ^int(theBoard['TR'] ):
		pass
	elif int(theBoard['TM'] )^int(theBoard['MM'] ) ^int(theBoard['LM'] ):
		pass
	else:
	        pass
    elif y == 'TR':
	if int(theBoard['TR'] )^int(theBoard['TM'] ) ^int(theBoard['TL'] ):
		pass
	elif int(theBoard['TR'] )^int(theBoard['MM'] ) ^int(theBoard['LL'] ):
		pass
	elif int(theBoard['TR'] )^int(theBoard['MR'] ) ^int(theBoard['LR'] ):
		pass
	else:
	        pass
    elif y == 'ML':
	if int(theBoard['ML'] )^int(theBoard['TL'] ) ^int(theBoard['LL'] ):
		pass
	elif int(theBoard['ML'] )^int(theBoard['MM'] ) ^int(theBoard['MR'] ):
		pass
	else:
        	pass
    elif y == 'MM':
	if int(theBoard['MM'] )^int(theBoard['TL'] ) ^int(theBoard['LR'] ):
		pass
	elif int(theBoard['MM'] )^int(theBoard['TR'] ) ^int(theBoard['LL'] ):
		pass
	elif int(theBoard['MM'] )^int(theBoard['TM'] ) ^int(theBoard['LM'] ):
		pass
	elif int(theBoard['MM'] )^int(theBoard['ML'] ) ^int(theBoard['MR'] ):
		pass
	else:
        	pass
    elif y == 'MR':
	if int(theBoard['MR'] )^int(theBoard['TR'] ) ^int(theBoard['LR'] ):
		pass
	elif int(theBoard['MR'] )^int(theBoard['MM'] ) ^int(theBoard['ML'] ):
		pass
	else:
        	pass
    elif y == 'LL':
	if int(theBoard['LL'] )^int(theBoard['ML'] ) ^int(theBoard['TL'] ):
		pass
	elif int(theBoard['LL'] )^int(theBoard['MM'] ) ^int(theBoard['TR'] ):
		pass
	elif int(theBoard['LL'] )^int(theBoard['LM'] ) ^int(theBoard['LR'] ):
		pass
	else:
        	pass
    elif y == 'LM':
	if int(theBoard['LM'] )^int(theBoard['MM'] ) ^int(theBoard['TM'] ):
		pass
	elif int(theBoard['LM'] )^int(theBoard['LL'] ) ^int(theBoard['LR'] ):
		pass
	else:
        	pass
    else :
        pass
if __name__ == '__main__' :
    theBoard =  {'TL':'','TM':'','TR':'',
                'ML':'','MM':'','MR':'',
                'LL':'','LM':'','LR':''
            }
    displayBoard(theBoard)
    count=0
    while True:
        if count ==2:
            count=0
        else:
            count=count+1
            playerInput(count,theBoard)




