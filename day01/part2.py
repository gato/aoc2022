f = open('input.txt', 'r')
lines = f.readlines()

def proc_cal(curr_maxs, calories):
  pos = 3
  for i in [2, 1, 0]:
    if curr_maxs[i] > calories:
      break
    pos = i
  if pos < 3:
    curr_maxs = curr_maxs[:pos] + [calories] + curr_maxs[pos:]
    curr_maxs = curr_maxs[:3]
  return curr_maxs

cals = 0
top3 = [0, 0, 0]
for line in lines:
  line = line.strip()
  if len(line) == 0:
    top3 = proc_cal(top3, cals)
    cals = 0
  else:
    cals += int(line)
top3 = proc_cal(top3, cals)
print("Max calories: ", top3, sum(top3))
print("Answer is:", sum(top3))