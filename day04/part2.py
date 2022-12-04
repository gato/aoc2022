f = open('input.txt', 'r')
lines = f.readlines()

def get_pairs(str):
  e1, e2 = str.split(",")
  return [
    list(map(lambda x: int(x), e1.split("-"))), 
    list(map(lambda x: int(x), e2.split("-")))]

def overlaps(e1, e2):
  (e1, e2) = (e1, e2) if e1[0] <= e2[0] else (e2, e1)
  if e1[1] >= e2[0]:
    return True
  return False

acc = 0
for line in lines:
  line = line.strip()
  e1, e2 = get_pairs(line)
  ov = overlaps(e1, e2)
  acc += 1 if ov else 0
  print(e1, e2, ov , acc)
print("Answer is:", acc)
