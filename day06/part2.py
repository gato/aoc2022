f = open('input.txt', 'r')
lines = f.readlines()
line = lines[0].strip()

for i in range(14, len(line)):
  if len(set(line[i-14:i])) == 14:
    print("Answer is:", i)
    break