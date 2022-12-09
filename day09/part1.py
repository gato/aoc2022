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
    self.head = (0, 0)
    self.tail = (0, 0)
    self.visited = set()

  def hasToMove(self):
    return abs(self.head[0] - self.tail[0]) > 1 or abs(self.head[1] - self.tail[1]) > 1

  def moveTail(self):
    if self.head[0] == self.tail[0]:
      self.tail = (self.tail[0], self.tail[1]+1 if self.head[1] > self.tail[1] else self.tail[1]-1)
    elif self.head[1] == self.tail[1]:
      self.tail = (self.tail[0]+1 if self.head[0] > self.tail[0] else self.tail[0]-1, self.tail[1])
    else:
      self.tail = (self.tail[0]+1 if self.head[0] > self.tail[0] else self.tail[0]-1, self.tail[1]+1 if self.head[1] > self.tail[1] else self.tail[1]-1)

  def move(self, direction, q):
    for i in range(q):
      # move head
      m = movements[direction]
      self.head = (self.head[0]+m[0], self.head[1]+m[1])
      # update t
      if (self.hasToMove()):
        self.moveTail()
      self.visited.add(self.tail)

r = Rope()
for op in ops:
  r.move(op[0], int(op[1]))
print("Answer is:", len(r.visited))