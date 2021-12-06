import statistics

inputDoc = open('input.txt').read()
if inputDoc[-1] == '\n':
    inputDoc = inputDoc[:-1]
O2List = inputDoc.split('\n')
listIndex = 0

def getSplit(bit):
    x = [int(a) for a in str(bit)]
    return x

stop = False
while stop == False: #O2 check
    if len(O2List) == 1 or listIndex ==11 : stop = True #Breakpoint
    checkmodeList = []
    o2 = []
    for bit in O2List: #This function adds chosen elem into list to grab MODE.
        splitBit= getSplit(bit)
        checkmodeList.append(splitBit[listIndex])
    
    #Below required as couldnt work out how to get statistics.mode to work with equality edge case. 
    count1 = 0
    count0 = 0
    for num in checkmodeList: 
        if num == 1:count1+=1
        if num == 0:count0+=1
    if count1>count0:O2scrub=1
    elif count1<count0:O2scrub=0
    elif count1==count0:O2scrub=1
    
    #Below to iterate through ever shortening list.
    for bit in O2List:
        splitBit= getSplit(bit)
        if splitBit[listIndex] == O2scrub:
            o2.append(bit) #If matches scrub check then add to new list.
    O2List = o2 #allows check for next iteration.
    listIndex += 1 #Iteration/index count.


inputDoc = open('input.txt').read()
if inputDoc[-1] == '\n':
    inputDoc = inputDoc[:-1]
CO2List = inputDoc.split('\n') #Repopulating list with new name to make it clear.

stop=False
listIndex = 0
while stop == False: #CO2 Check
    CO2scrub=0#binary addition baseline, resets each loop.
    if len(CO2List) == 1 or listIndex == 11 : stop = True #Breakpoint
    checkmodeList = [] #now emptylist.
    co2L = []
    for bit in CO2List: #This function adds chosen elem into list to grab mode.
        splitBit= getSplit(bit) #get list of bit
        checkmodeList.append(splitBit[listIndex]) #adds each indexed number to the list which you can then check number of each.
    count1 = 0 #reset from prev iter.
    count0 = 0
    for num in checkmodeList: #compare numbers of 1s and 0s
        if num == 1:count1+=1
        if num == 0:count0+=1
    if count1>count0:CO2scrub=0 #assigning scrubber
    elif count1<count0:CO2scrub=1
    elif count1==count0:CO2scrub=0
    for bit in CO2List:
        splitBit= getSplit(bit)
        if splitBit[listIndex] == CO2scrub:
            co2L.append(bit)
    CO2List = co2L
    if len(CO2List) == 1: stop = True
    listIndex += 1 

#Checks and Conversions
print(O2List, CO2List) #Check how many elements.
oxyGen = int(O2List[0],2) #Converting from bit to int.
CO2Scrubber = int(CO2List[0],2)
lifeSupportRating = oxyGen*CO2Scrubber
print(lifeSupportRating)#6085575