f1 = open('day-2-a.txt', 'r')
Lines = f1.readlines()

validPasswords = 0
for line in Lines:
  parsed = line.split(' ')
  minReq = int(parsed[0].split('-')[0])
  maxReq = int(parsed[0].split('-')[1])
  charReq = parsed[1][0]
  password = parsed[2]

  reqCharCount = 0
  for char in password:
    if char == charReq:
      reqCharCount += 1

  if reqCharCount >= minReq and reqCharCount <= maxReq:
    validPasswords += 1

print(validPasswords)

#Answer: 477