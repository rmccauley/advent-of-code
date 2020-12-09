import re

f1 = open('day-4-a.txt', 'r')
Lines = f1.readlines()

passports = []
newPassport = []
validPassports = 0
allRequiredFieldsPresent = 0

for line in Lines:
  if line != '\n':
    for x in line.split(' '):
      newPassport.append(x[:].strip())
  else:
    passports.append(newPassport[:])
    newPassport = []
# Append the last passport
passports.append(newPassport[:])

for passport in passports:
  hasByr, hasIyr, hasEyr, hasHgt, hasHcl, hasEcl, hasPid, hasCid = False, False, False, False, False, False, False, False
  validByr, validIyr, validEyr, validHgt, validHcl, validEcl, validPid, validCid = False, False, False, False, False, False, False, True

  for passportField in passport:
    splitField = passportField.split(':')
    m = False

    if splitField[0] == 'byr':
      hasByr = True
      validByr = int(splitField[1]) >= 1920 and int(splitField[1]) <= 2002
    elif splitField[0] == 'iyr':
      hasIyr = True
      validIyr = int(splitField[1]) >= 2010 and int(splitField[1]) <= 2020
    elif splitField[0] == 'eyr':
      hasEyr = True
      validEyr = int(splitField[1]) >= 2020 and int(splitField[1]) <= 2030
    elif splitField[0] == 'hgt':
      hasHgt = True
      m = re.search('[0-9]{3}cm|[0-9]{2}in', splitField[1])
      if m:
        validHgt = True
    elif splitField[0] == 'hcl':
      hasHcl = True
      m = re.search('#[0-9a-f]{6}', splitField[1])
      if m:
        validHcl = True
    elif splitField[0] == 'ecl':
      hasEcl = True
      m = re.search('^(amb|blu|brn|gry|grn|hzl|oth){1}$', splitField[1])
      if m:
          validEcl = True
    elif splitField[0] == 'pid':
      hasPid = True
      m = re.search('^[0-9]{9}$', splitField[1])
      if m:
        validPid = True
    elif splitField[0] == 'cid':
      hasCid = True

  if (hasByr and hasIyr and hasEyr and hasHgt and hasHcl and hasEcl and hasPid):
    allRequiredFieldsPresent += 1

  if (validByr and validIyr and validEyr and validHgt and validHcl and validEcl and validPid):
      validPassports += 1

print(allRequiredFieldsPresent) # Answer: 242
print(validPassports) # Answer: 186 (less one than prints somehow..)