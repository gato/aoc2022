f = open('input.txt', 'r')
lines = list(map(lambda x: x.strip(), f.readlines()))

w = len(lines)
h = len(lines[0])

def view_score(i, j):
  tree = lines[j][i]
  view_score = 1
  
  #check north
  trees = 0
  for k in range (j-1, -1, -1):
    trees += 1
    if lines[k][i] >= tree:
      break
  view_score *= trees
  
  #check south
  trees = 0
  for k in range (j+1, h):
    trees += 1
    if lines[k][i] >= tree:
      break
  view_score *= trees
  
  #check west
  trees = 0
  for k in range (i-1, -1, -1):
    trees += 1
    if lines[j][k] >= tree:
      break
  view_score *= trees

  #check east
  trees = 0
  for k in range (i+1, w):
    trees += 1
    if lines[j][k] >= tree:
      break
  view_score *= trees
  return view_score

max_view = 0
for i in range(1, w -1):
  for j in range(1, h-1):
    curr_view = view_score(i, j)
    max_view = max(max_view, curr_view)
print("Answer is:", max_view)
