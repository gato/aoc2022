def to_tuple(s):
  arr = s.split(',')
  return (int(arr[0]), int(arr[1])); 

f = open('input.txt', 'r')
lines = map(lambda x: x.strip().split(" -> "), f.readlines())

cave = {}
top = 0
left = 10000000
right = 0
bottom = 0

def print_cave():
  for y in range(bottom+1):
    row = ""
    for x in range(left, right+1, 1):
      row += cave[(x, y)] if (x, y) in cave else "."
    print(row)
  print("\n")

for line in lines:
  line = list(map(to_tuple, line))
  for i in range(1, len(line)):
    f = line[i-1]
    t = line[i]
    left = min(left, f[0], t[0])
    right = max(right, f[0], t[0])
    bottom = max(bottom, f[1], t[1])
    if f[0]==t[0]:
      #horizontal
      delta = 1 if f[1] < t[1] else -1
      for j in range(f[1], t[1]+delta, delta):
        cave[(f[0], j)]="#"
    else:
      #vertical
      delta = 1 if f[0] < t[0] else -1
      for j in range(f[0], t[0]+delta, delta):
        cave[(j, f[1])]="#"
#adjust
bottom = bottom + 2
right = max(right, 500 + (bottom +1 // 2))
left = min(left, 500 - (bottom +1 // 2))
for i in range(left-1, right+1, 1):
  cave[(i, bottom)]="#"

print_cave()
source = (500, 0)
units = 0
full = False
while not full:
  # drop sand
  sand = (source[0], source[1])
  while True:
    if sand[0] > right or sand[0] < left or sand[1] > bottom:
      flowing = True
      break
    if (sand[0], sand[1]+1) not in cave:
      sand = (sand[0], sand[1] + 1)
      continue
    elif (sand[0]-1, sand[1]+1) not in cave:
      sand = (sand[0]-1, sand[1]+1)
      continue
    elif (sand[0]+1, sand[1]+1) not in cave:
      sand = (sand[0]+1, sand[1]+1)
      continue
    else:
      cave[sand]="o"
      units += 1
      if sand == source:
        full = True
      break
print_cave()
print("Your answer is:", units)