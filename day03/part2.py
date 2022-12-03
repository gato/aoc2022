f = open('input.txt', 'r')
lines = f.readlines()

def findBadge(group):

  firstElf = {}
  for c in group[0]:
    firstElf[c] = True

  secondElf = {}
  for c in group[1]:
    secondElf[c] = True

  for c in group[2]:
    if c in firstElf and c in secondElf:
      return c
  return None

def getPriority(c):
  asc = ord(c)
  if (asc >= ord('a') and asc <= ord('z')):
    return asc - ord('a') + 1
  return asc - ord('A') + 27

acc = 0
group = []
for line in lines:
  line = line.strip()
  group.append(line)
  if len(group) == 3:  
    b = findBadge(group)
    prio = getPriority(b)
    acc += prio
    print(group, " -> ", b, prio, acc)
    group = []
