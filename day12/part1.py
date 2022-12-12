f = open('input.txt', 'r')
matrix = list(map(lambda x: x.strip(), f.readlines()))
w = len(matrix[0])
h = len(matrix)
start, end = (-1,-1), (-1, -1)
for i in range(h):
  for j in range(w):
    if matrix[i][j] == 'E':
      end = (j, i)
      matrix[i] = matrix[i][0:j] + "z" + matrix[i][j+1:]
    elif matrix[i][j] == 'S':
      start = (j, i)
      matrix[i] = matrix[i][0:j] + "a" + matrix[i][j+1:]

queue = []
queued = set()
queue.append((start[0], start[1], 0))

while len(queue) > 0:
  node = queue.pop(0)
  if (node[0], node[1]) == end:
    print("Answer is", node[2])
    break 
  value = ord(matrix[node[1]][node[0]])
  if node[0] > 0 and ord(matrix[node[1]][node[0]-1]) <= value + 1:
    if not (node[0]-1, node[1]) in queued:
      queue.append((node[0]-1, node[1], node[2] + 1))
      queued.add((node[0]-1, node[1]) )
  if node[1] < h - 1 and ord(matrix[node[1]+1][node[0]]) <= value + 1:
    if not (node[0], node[1]+1) in queued:
      queue.append((node[0], node[1]+1, node[2] + 1))
      queued.add((node[0], node[1]+1))
  if node[0] < w - 1 and ord(matrix[node[1]][node[0]+1]) <= value + 1:
    if not (node[0]+1, node[1]) in queued:
      queue.append((node[0]+1, node[1], node[2] + 1))
      queued.add((node[0]+1, node[1]))
  if node[1] > 0 and ord(matrix[node[1]-1][node[0]]) <= value + 1:
    if not (node[0], node[1]-1) in queued:
      queue.append((node[0], node[1]-1, node[2] + 1))
      queued.add((node[0], node[1]-1))