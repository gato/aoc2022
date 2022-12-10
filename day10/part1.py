f = open('input.txt', 'r')
ops = map(lambda x: x.strip().split(), f.readlines())

register = 1
cicles = 0

every = range(20, 221, 40)
signal_strengths = []

for op in ops:
  prev_reg = register
  prev_cicles = cicles
  if (op[0] == "noop"):
    cicles += 1
  else:
    cicles += 2
    register += int(op[1])
  mark = every[0]
  if (prev_cicles < mark and cicles >= mark):
    signal_strengths.append(mark*prev_reg)
    every = every[1:]
    if len(every) == 0:
      break
print("Answer is:", sum(signal_strengths))