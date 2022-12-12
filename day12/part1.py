f = open('input.txt', 'r')
matrix = list(map(lambda x: [ord(c) for c in x.strip()], f.readlines()))
w = len(matrix[0])
h = len(matrix)
start, end = (-1,-1), (-1, -1)
for i in range(h):
  for j in range(w):
    if matrix[i][j] == ord('E'):
      end = (j, i)
      matrix[i][j] = ord('z')
    elif matrix[i][j] == ord('S'):
      start = (j, i)
      matrix[i][j] = ord('a')

queue = []
queued = set()
queue.append((start[0], start[1], 0))

def proc_node(x, y, dist, value):
  if x < 0 or x >= w or y < 0 or y >= h:
    return
  if matrix[y][x] > value + 1:
    return
  if (x, y) in queued:
    return
  queue.append((x, y, dist + 1))
  queued.add((x, y))

while len(queue) > 0:
  node = queue.pop(0)
  if (node[0], node[1]) == end:
    print("Answer is", node[2])
    break 
  value = matrix[node[1]][node[0]]
  proc_node(node[0] -1, node[1]   , node[2], value)
  proc_node(node[0]   , node[1] +1, node[2], value)
  proc_node(node[0] +1, node[1]   , node[2], value)
  proc_node(node[0]   , node[1] -1, node[2], value)
