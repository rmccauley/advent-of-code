f1 = open('day-3-a.txt', 'r')
Lines = f1.readlines()

for x in range(len(Lines)):
  Lines[x] = Lines[x].strip()


def treePlow(r, d):
  lineLen = len(Lines[0])
  listLen = len(Lines)
  currentRow = 0
  currentPos = 0
  treesHit = 0

  for x in range(len(Lines)):
    currentRow += d

    if currentPos+r > lineLen-1:
      currentPos = currentPos+r-lineLen
    else:
      currentPos += r

    if currentRow >= listLen:
      return treesHit

    if Lines[currentRow][currentPos] == '#':
      treesHit += 1
  exit(1)

print(treePlow(1,1))
print(treePlow(3,1))
print(treePlow(5,1))
print(treePlow(7,1))
print(treePlow(1,2))

print(treePlow(1,1)*treePlow(3,1)*treePlow(5,1)*treePlow(7,1)*treePlow(1,2))

# Answer: 7560370818