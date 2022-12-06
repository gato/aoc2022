f = open('input.txt', 'r')
lines = f.readlines()
line = lines[0].strip()

for i in range(4, len(line)):
  if len(set(line[i-4:i])) == 4:
    print("Answer is:", i)
    break