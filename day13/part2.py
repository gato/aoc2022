import functools

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
  index = 0
  while len(l1[index:]) > 0 and len(l2[index:]) > 0:
    i1 = l1[index]
    i2 = l2[index]
    index += 1
    if isinstance (i1,int) and isinstance(i2, int):
      if i1 == i2:
        continue
      return 1 if i2 < i1 else -1
    elif isinstance (i1, list) and isinstance(i2, list):
      return compare(i1, i2)
    else:
      i1 = i1 if isinstance (i1, list) else [i1]
      i2 = i2 if isinstance (i2, list) else [i2]
      return compare(i1, i2)
  return -1 if len(l1[index:]) <= len(l2[index:]) else 1

f = open('input.txt', 'r')
lines = list(map(lambda x: parse(x), filter(lambda x: len(x) > 0, map(lambda x: x.strip(), f.readlines()))))

lines.append([[2]])
lines.append([[6]])
lines.sort(key=functools.cmp_to_key(compare))
m1 = -1
m2 = -1
for index in range(len(lines)):
  if lines[index] == [[2]]:
    m1 = index+1
  elif lines[index] == [[6]]:
    m2 = index+1
print("Your answer is:", m1 * m2)
