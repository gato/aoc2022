f = open('input.txt', 'r')
lines = f.readlines()

def parse_crane_matrix(cranes):
  stacks = {}
  for i in range(0, len(cranes[0])-1, 4):
    stack = []
    for j in range(len(cranes)-2, -1, -1):
      if cranes[j][i:i+4].strip() == "":
        break
      stack.append(cranes[j][i+1])
    stacks[cranes[-1][i+1]]=stack
  return stacks

def parse_moves(moves):
  ops = []
  for move in moves:
    move = move.strip().split()
    t = (int(move[1]), move[3], move[5])
    ops.append(t)
  return ops

def cranes_ops(lines):
  cranes = []
  ops = []
  sl = 0
  for line in lines:
    if len(line) == 1:
      break
    sl += 1
  cranes = parse_crane_matrix(lines[:sl])
  ops = parse_moves(lines[sl+1:])
  return (cranes, ops)

cranes, ops = cranes_ops(lines)

for op in ops:
  q, source, dest = op
  items = cranes[source][-q:]
  cranes[source] = cranes[source][:-q]
  cranes[dest] = cranes[dest] + items

str = ""
for k in cranes.keys():
  str += cranes[k][-1]
print("Answer is:", str)