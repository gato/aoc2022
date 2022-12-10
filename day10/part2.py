f = open('input.txt', 'r')
ops = list(map(lambda x: x.strip().split(), f.readlines()))

at_end = {}
cicle = 0
for op in ops:
  to_add = 0
  if op[0] == "noop":
    cicle += 1
  else:
    cicle += 2
    to_add = int(op[1])
  at_end[cicle]=to_add

def pixel_value(pos, register):
  crt = (pos % 40)
  return "#" if register -1 <= crt <= register +1 else "."

register = 1
pixels = ""
for i in range(1, 261, 1):
  pixels += pixel_value(i-1, register)
  register += at_end[i] if i in at_end else 0

print("your Answer is:")
for i in range(0, 201, 40):
  print(pixels[i:i+40])