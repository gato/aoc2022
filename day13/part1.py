f = open('input.txt', 'r')
lines = map(lambda x: x.strip(), f.readlines())

def parse(line):
  return _parse(line)[0][0] #unwrap result

def _parse(line):
  result = []
  digit = None
  while len(line) > 0:
    c, line = line[0], line[1:]
    if c == "[":
      (r, line) = _parse(line)
      result.append(r)
    elif c == "]":
      if digit != None:
        result.append(digit)
      return (result, line)
    elif c == ',':
      if digit != None:
        result.append(digit)
      digit = None
    else:
      digit = digit = int(c) if digit == None else (digit * 10) + int(c)
  return (result, line)

def compare(l1, l2):
  while len(l1) > 0 and len(l2) > 0:
    i1 = l1.pop(0)
    i2 = l2.pop(0)
    if isinstance (i1,int) and isinstance(i2, int):
      if i1 == i2:
        continue
      return False if i2 < i1 else True
    elif isinstance (i1, list) and isinstance(i2, list):
      return compare(i1, i2)
    else:
      i1 = i1 if isinstance (i1, list) else [i1]
      i2 = i2 if isinstance (i2, list) else [i2]
      return compare(i1, i2)
  return len(l1) <= len(l2)

pairs = []
in_order = 0
index = 0
for line in lines:
  if len(line) > 0:
    pairs.append(parse(line))
  else:
    index += 1
    if compare(pairs[0], pairs[1]):
      in_order += index
    pairs = []
if compare(pairs[0], pairs[1]):
  in_order += index+1

print("Your answer is:", in_order)
