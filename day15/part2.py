import re
def parse_line(line):
  p = re.split(r':|,|=', line)
  sx = int(p[1])
  sy = int(p[3])
  bx = int(p[5])
  by = int(p[7])
  return { "sensor" : (sx, sy), "beacon": (bx, by), "distance": abs(sx - bx ) + abs (sy - by)}

f = open('input.txt', 'r')
sensors = list(map(lambda x: parse_line(x.strip()), f.readlines()))

top = 0
left = 100000000
right = -100000000
bottom = 0
beacons = set()

for s in sensors:
  left = min(left, s["sensor"][0]-s["distance"], s["beacon"][0])
  right = max(right, s["sensor"][0]+s["distance"], s["beacon"][0])
  bottom = max(bottom, s["sensor"][1]+s["distance"], s["beacon"][1])
  beacons.add(s["beacon"])
print (top, left, bottom, right)

y = 0
while y < 4000000:
  #print(y)
  x = 0
  while x < 4000000:
    for s in sensors:
      covered = False
      dist = abs(s["sensor"][0] - x) + abs(s["sensor"][1] - y)
      if s["distance"] >= dist:
        covered = True
        x = s["sensor"][0] + s["distance"] - abs(y - s["sensor"][1]) + 1
        break
    if not covered:
      print("Your Answer is:", x, y, (x*4000000)+ y)
      exit(0)
  y += 1