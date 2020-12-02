f1 = open('day-2-b.txt', 'r')
Lines = f1.readlines()

validPasswords = 0
for line in Lines:
  parsed = line.split(' ')
  posOne = int(parsed[0].split('-')[0])-1
  posTwo = int(parsed[0].split('-')[1])-1
  charReq = parsed[1][0]
  password = parsed[2]

  if (password[posOne] == charReq and password[posTwo] != charReq) or (password[posOne] != charReq and password[posTwo] == charReq):
    validPasswords += 1

print(validPasswords)

# Answer: 686