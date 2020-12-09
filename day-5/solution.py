import math

f1 = open('input.txt', 'r')
Lines = f1.readlines()
highestSeatId = 0
seatIdList = []

for line in Lines:
  minRow = 0
  maxRow = 127
  minSeat = 0
  maxSeat = 7

  currentRow = 0
  currentSeat = 0
  currentSeatId = 0

  x = 0
  while x < len(line):
    if line[x] == 'B': # upper
      minRow = math.ceil((maxRow - minRow)/2)+minRow
    elif line[x] == 'F': #lower
      maxRow = math.floor((maxRow - minRow)/2)+minRow
    elif line[x] == 'L': #lower
      maxSeat = math.floor((maxSeat - minSeat)/2)+minSeat
    elif line[x] == 'R': #upper
      minSeat = math.ceil((maxSeat - minSeat)/2)+minSeat

    if minRow == maxRow:
      currentRow = minRow
    if minSeat == maxSeat:
      currentSeat = minSeat

    currentSeatId = (currentRow * 8) + currentSeat
    if currentSeatId > highestSeatId:
      highestSeatId = currentSeatId

    x+=1

  seatIdList.append(currentSeatId)

print('Highest Seat Id ' + str(highestSeatId))

seatIdList.sort()
y = 0
while y < len(seatIdList):
  if y - 1 > 0 and y + 1 < len(seatIdList):
    if seatIdList[y] + 1 < seatIdList[y+1]:
      print('My Seat Id ' + str(seatIdList[y] +1))
      break;
  y+=1

# Answer A: 822
# Answer B: 705