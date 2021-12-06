inputDoc = open('input.txt').read()
if inputDoc[-1] == '\n':
    inputDoc = inputDoc[:-1]
inputList = inputDoc.split('\n')

distance = 0
depth = 0
for instruction in inputList:
    instructions = instruction.split()
    if instructions[0] == 'forward': distance += int(instructions[1])
    elif instructions[0] == 'up': depth -= int(instructions[1])
    elif instructions[0] == 'down': depth += int(instructions[1])
part1 = distance*depth
print(part1) #Completed

aim = 0
distance = 0
depth = 0
for instruction in inputList:
    instructions = instruction.split()
    if instructions[0] == 'forward': 
        distance += int(instructions[1])
        depth += aim*int(instructions[1])
    elif instructions[0] == 'up': aim -= int(instructions[1])
    elif instructions[0] == 'down': aim += int(instructions[1])
part2 = distance*depth
print(part2) #Completed