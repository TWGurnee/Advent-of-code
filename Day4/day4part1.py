#input list contains line of number called and boxes
import numpy as np

winBox = []
def checkBingo(box): #boc is np.arrays from boxList.
    win =['X','X','X','X','X']
    global winBox
    boxL=box.tolist()
    colList = list(zip(*boxL[0]))
    for col in colList:
        if col == ('X','X','X','X','X'):# == ['X','X','X','X','X']
            if box not in winBox:winBox.append(box)
            return True
    for row in boxL[0]:
        if win == row:
            if box not in winBox:winBox.append(box)
            return True
    else: return False

end = False
def crossNumber(x):#Take call as arg and find in each box, then replace that index with str 'X'
    global boxList
    global end
    for box in boxList:
        for cell in np.nditer(box,op_flags=['readwrite']):
            if cell == str(x):
                cell[...] = 'X'
        if checkBingo(box)!=False:
            print(winBox[0], call)
            finalScore = int(getWinningBoxScore(winBox[0])) * int(call)
            print(finalScore)
            end = True
            break
        if end == True: break

def getWinningBoxScore(box):
    totalPoints = 0
    for cell in np.nditer(box,op_flags=['readwrite']):
        if cell == 'X':pass
        else: totalPoints+=int(cell)
    return totalPoints

########################################################################
boxRowList = []
with open('input.txt') as inputDoc:
        callCheck=(inputDoc.readline()[:-1]).split(',')
        lines = inputDoc.readlines()
        for line in lines:
            if line == '\n':pass
            else:
                boxRow = line.split()
                boxRowList.append(boxRow)
#callCheck and BoxRowList populated

buildCount = 0
boxList = []
Startindex = 0
Endindex = 5
while buildCount != (len(boxRowList)/5):
    box = [] #Clear Box for build
    box.append(boxRowList[Startindex:Endindex]) #Get list of rows
    x = np.array(box)
    boxList.append(x)
    Startindex+=5
    Endindex+=5
    buildCount+=1
#boxList now populated.

for call in callCheck:
    crossNumber(call)
    if end == True:break

#part 1 = 58412