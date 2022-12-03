f = open('input.txt', 'r')
lines = f.readlines()

def findDup(rucksack):
  half = len(rucksack) // 2
  compartments = [rucksack[:half], rucksack[half:]]
  seen = {}
  for c in compartments[0]:
    seen[c] = True

  for c in compartments[1]:
    if c in seen:
      return c
  return None

def getPriority(c):
  asc = ord(c)
  if (asc >= ord('a') and asc <= ord('z')):
    return asc - ord('a') + 1
  return asc - ord('A') + 27

acc = 0
for line in lines:
  line = line.strip()
  dup = findDup(line)
  prio = getPriority(dup)
  acc += prio
  print(len(line), line, " -> ", dup, prio, acc)

print("Answer is:", acc)
