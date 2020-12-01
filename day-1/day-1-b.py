f1 = open('day-1-a.txt', 'r')
Lines = f1.readlines()

for line1 in Lines:
  line1int = int(line1)

  for line2 in Lines:
    line2int = int(line2)

    for line3 in Lines:
      line3int = int(line3)
      if line1int + line2int + line3int == 2020:
        print(line1int*line2int*line3int)
        break
    else:
      continue
    break
  else:
    continue
  break