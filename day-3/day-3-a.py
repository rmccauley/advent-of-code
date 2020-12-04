f1 = open('day-3-a.txt', 'r')
Lines = f1.readlines()

for x in range(len(Lines)):
  Lines[x] = Lines[x].strip()

lineLen = len(Lines[0])
listLen = len(Lines)
currentRow = 0
currentPos = 0
treesHit = 0

for x in range(len(Lines)):
  currentRow += 1

  if currentPos+3 > lineLen-1:
    currentPos = currentPos+3-lineLen
  else:
    currentPos += 3

  if currentRow >= listLen:
    print(treesHit)
    exit(0)

  if Lines[currentRow][currentPos] == '#':
    treesHit += 1

print(treesHit)

# Answer: 169