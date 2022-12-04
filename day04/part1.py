f = open('input.txt', 'r')
lines = f.readlines()

def get_pairs(str):
  e1, e2 = str.split(",")
  return [
    list(map(lambda x: int(x), e1.split("-"))), 
    list(map(lambda x: int(x), e2.split("-")))]

def fully_contains(e1, e2):
  if e1[0]<= e2[0] and e1[1] >= e2[1]:
    return True
  if e2[0]<= e1[0] and e2[1] >= e1[1]:
    return True
  return False

acc = 0
for line in lines:
  line = line.strip()
  e1, e2 = get_pairs(line)
  fc = fully_contains(e1, e2)
  acc += 1 if fc else 0
  print(e1, e2, fc, acc)
print("Answer is:", acc)
