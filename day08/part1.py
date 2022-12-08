f = open('input.txt', 'r')
lines = list(map(lambda x: x.strip(), f.readlines()))

w = len(lines)
h = len(lines[0])
visible = (2 * w) + ((h-2) *2) # edge trees

print (h, w, visible)

def is_visible(i, j):
  tree = lines[j][i]
  v = True
  #check north
  for k in range (0, j):
    if lines[k][i] >= tree:
      v = False
      break
  if v == True:
    return True
  #check south
  v = True
  for k in range (j+1, h):
    if lines[k][i] >= tree:
      v = False
      break
  if v == True:
    return True
  #check west
  v = True
  for k in range (0, i):
    if lines[j][k] >= tree:
      v = False
      break
  if v == True:
    return True
  #check east
  v = True
  for k in range (i+1, w):
    if lines[j][k] >= tree:
      v = False
      break
  return v

for i in range(1, w -1):
  for j in range(1, h-1):
    if is_visible(i, j):
      visible += 1

print("Answer is:", visible)
