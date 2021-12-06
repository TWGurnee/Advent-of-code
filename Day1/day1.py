inputDoc = open('input.txt').read()
if inputDoc[-1] == '\n':
    inputDoc = inputDoc[:-1]
inputList = inputDoc.split('\n')

count = 0
prevNum = 1000000000 #Large just so never fails first check.
for number in inputList:
    if int(number) > int(prevNum): count+=1
    prevNum = int(number)
print(count) # number of increases for part 1

#Calculate sum rolling window of size 3
size=3
windowSumList = []
for i in range(len(inputList)- size + 1):
    num = (inputList[i:i+size])
    #x=sum(num)
    x=int(num[0]) + int(num[1]) + int(num[2]) #this line required as sum(num) didnt seem to work (int + str)
    windowSumList.append(x)

newcount = 0
for number in windowSumList:
    if int(number) > int(prevNum): newcount+=1
    prevNum = int(number)
print(newcount)#Number of increases between sliding windows.