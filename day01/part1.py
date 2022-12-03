f = open('input.txt', 'r')
lines = f.readlines()

max_cal = 0
cals = 0
for line in lines:
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