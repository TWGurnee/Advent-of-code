import statistics

inputDoc = open('input.txt').read()
if inputDoc[-1] == '\n':
    inputDoc = inputDoc[:-1]
inputList = inputDoc.split('\n')


elem1, elem2, elem3, elem4, elem5, elem6, elem7, elem8, elem9, elem10, elem11, elem12 = [],[],[],[],[],[],[],[],[],[],[],[]
list_of_elemLists = [elem1, elem2, elem3, elem4, elem5, elem6, elem7, elem8, elem9, elem10, elem11, elem12]
gammaList, epsilonList= [],[]
for bit in inputList:
    counter = 0
    lineList = bit.split('\n')
    for elem in lineList[0]:#Grab each elem and put into new list (essentially list of columns)
        if counter == 0:elem1.append(str(elem))
        elif counter == 1:elem2.append(str(elem))
        elif counter == 2:elem3.append(str(elem))
        elif counter == 3:elem4.append(str(elem))
        elif counter == 4:elem5.append(str(elem))
        elif counter == 5:elem6.append(str(elem))
        elif counter == 6:elem7.append(str(elem))
        elif counter == 7:elem8.append(str(elem))
        elif counter == 8:elem9.append(str(elem))
        elif counter == 9:elem10.append(str(elem))
        elif counter == 10:elem11.append(str(elem))
        elif counter == 11:elem12.append(str(elem))
        counter+=1

for list in list_of_elemLists:
    gammaList.append(str(statistics.mode(list)))
    if statistics.mode(list) == '1': epsilonList.append('0')
    elif statistics.mode(list) == '0': epsilonList.append('1')

gammaBit = ''.join(gammaList)
epsilonBit = ''.join(epsilonList)
gamma = int(gammaBit,2)
epsilon = int(epsilonBit,2)
print(gamma,epsilon)
powerConsumption = gamma*epsilon
print(powerConsumption) #Complete