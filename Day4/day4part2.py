#input list contains line of number called and boxes
import numpy as np

def remove(array, arrays): # taken from http://stackoverflow.com/questions/3157374/how-do-you-remove-a-numpy-array-from-a-list-of-numpy-arrays
    """
    Remove the `array` from the `list` of `arrays`
    Returns list with remaining arrays by keeping the order.

    :param array: `np.ndarray`
    :param arrays: `list:np.ndarray`
    :return: `list:np.ndarray`
    """

    assert isinstance(arrays, list), f'Expected a list, got {type(arrays)} instead'
    assert isinstance(array, np.ndarray), f'Expected a numpy.ndarray, got {type(array)} instead'
    for a in arrays:
        assert isinstance(a, np.ndarray), f'Expected a numpy.ndarray instances in arrays, found {type(a)} instead'

    # We use np.allclose for comparing arrays, this will work even if there are
    # floating point representation differences.
    # The idea is to create a boolean mask of the same lenght as the input arrays.
    # Then we loop over the arrays-elements and the mask-elements and skip the
    # flagged elements
    mask = [np.allclose(a, array) for a in arrays]
    return [a for a, skip in zip(arrays, mask) if not skip]


winBox = []
def checkBingo(box): #box is np.arrays from boxList.
    win =['X','X','X','X','X']
    global winBox
    boxL=box.tolist()
    colList = list(zip(*boxL[0]))
    for col in colList:
        if col == ('X','X','X','X','X'):return True
    for row in boxL[0]:
        if win == row:return True
    else: return False

end, finalCheckStartIndex = False, int

def crossNumber(x):#Take call as arg and find in each box, then replace that index with str 'X'
    global boxList
    global end
    boxCount = 0
    for box in boxList:
        for cell in np.nditer(box,op_flags=['readwrite']):
            if cell == str(x):
                cell[...] = 'X'
        if checkBingo(box)!=False: #if bingo is found, can delete box at that index from list as we don't want it.
            del boxList[boxCount] 
            boxCount-=1 # as length has decreased by one the next index would be the same number.
            if len(boxList) == 1: #When only one box left we know this will be last to win.
                end = True
                print('Last box found\n', boxList[0])
                print(((getWinningBoxScore(boxList[0])-int(x))*int(x)), 'Is the last box winning score')#
                break
        if end == True:
            print('stopping checking, last call = ',x) #Currently continuing to print until last call 80 which conveiently is last call to win last box.
            break
        boxCount+=1

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

# However nice above looks when calls 29,30,10,and finally 80 are made the sqaure looks as below
#  ['67' 'X' 'X' 'X' 'X']
#  ['X' 'X' '38' '90' '77']
#  ['X' 'X' 'X' '94' 'X']
#  ['X' 'X' '85' 'X' 'X']
#  ['X' 'X' '47' '12' 'X']
total_of_remainder = 67+38+90+77+94+85+47+12
finalCall = 80
print(total_of_remainder*finalCall)
