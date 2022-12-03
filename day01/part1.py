file1 = open('input.txt', 'r')
Lines = file1.readlines()

max_cal = 0
cals = 0
for line in Lines:
  line = line.strip()
  if len(line) == 0:
    if cals > max_cal:
      max_cal = cals
    cals = 0
  else:
    cals += int(line)
if cals > max_cal:
  max_cal = cals

print("Max calories: ", max_cal)