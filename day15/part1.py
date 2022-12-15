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
ty = 2000000
count = 0
for x in range(left, right + 1):
  covered = False
  for s in sensors:
    dist = abs(s["sensor"][0] - x) + abs(s["sensor"][1] - ty)
    if s["distance"] >= dist and (x, ty) not in beacons:
      covered = True
      break
  if covered == True:
    count += 1
print("Your Answer is:", count)