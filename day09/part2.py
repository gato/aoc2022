f = open('input.txt', 'r')
ops = map(lambda x: x.strip().split(), f.readlines())

movements = {
  "U": (1, 0),
  "D": (-1, 0),
  "R": (0, 1),
  "L": (0, -1)
}

class Rope:
  def __init__(self):
    self.knots = [(0, 0) for i in range(10)]
    self.visited = set()

  def hasToMove(self, h, t):
    head = self.knots[h]
    tail = self.knots[t]
    return abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1

  def moveTail(self, h, t):
    head = self.knots[h]
    tail = self.knots[t]
    if head[0] == tail[0]:
      tail = (tail[0], tail[1]+1 if head[1] > tail[1] else tail[1]-1)
    elif head[1] == tail[1]:
      tail = (tail[0]+1 if head[0] > tail[0] else tail[0]-1, tail[1])
    else:
      tail = (tail[0]+1 if head[0] > tail[0] else tail[0]-1, tail[1]+1 if head[1] > tail[1] else tail[1]-1)
    self.knots[t]=tail

  def move(self, direction, q):
    for i in range(q):
      # move head
      m = movements[direction]
      self.knots[0]= (self.knots[0][0]+m[0], self.knots[0][1]+m[1])
      # update t
      for j in range(1, 10, 1):
        if (self.hasToMove(j-1, j)):
          self.moveTail(j-1, j)
      self.visited.add(self.knots[9])

r = Rope()
for op in ops:
  r.move(op[0], int(op[1]))
print("Answer is:", len(r.visited))