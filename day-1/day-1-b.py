f1 = open('day-1-a.txt', 'r')
Lines = f1.readlines()
for x in range(0, len(Lines)):
  for y in range(1, len(Lines)):
    for z in range(2, len(Lines)):
      valX, valY, valZ = int(Lines[x]), int(Lines[y]), int(Lines[z])
      if x != y and x != z and y != z and valX + valY + valZ == 2020:
        print(int(Lines[x]) * int(Lines[y]) * int(Lines[z]))
        exit(0)