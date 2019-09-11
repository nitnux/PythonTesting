co=0
def displayBoard(theBoard):
    count=0
    for c in theBoard.values():
        if count < 2:
            print(c+'|')
            count=count+1
        else:
            print('/n')
            count=0
def playerinput(chance,theBoard):
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
        if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )

	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	else
        
    if y == 'TM':
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	else
	        pass
    if y == 'TR':
 if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	else
	        pass
    if y == 'ML':
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	else
        	pass
    if y == 'MM':
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	else
        	pass
    if y == 'MR':
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	else
        	pass
    if y == 'LL':
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	else
        	pass
    if y == 'LM':
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	if int(theBoard['TL'] )^int(theBoard['TL'] ) ^int(theBoard['TL'] )
	else
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



