f = open('input.txt', 'r')
lines = f.readlines()

decode = { 'A' : 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X' : 'Rock', 'Y': 'Paper', 'Z': 'Scissors' }
shape_points = { 'Rock': 1, 'Paper': 2, 'Scissors': 3 }
match_points = { 'Lost': 0, 'Draw': 3, 'Win': 6 }

def match_result(a, b):
  if a == b:
    return 'Draw'
  if b == 'Rock':
    return 'Win' if a == 'Scissors' else 'Lost'
  if b == 'Paper':
    return 'Win' if a == 'Rock' else 'Lost'
  return 'Win' if a == 'Paper' else 'Lost'

total_score = 0
for line in lines:
  line = line.strip()
  parts = line.split(" ")
  [oponent, myself] = map( lambda x : decode[x], parts)
  result = match_result(oponent, myself)
  score = shape_points[myself] + match_points[result]
  total_score += score
  print(oponent, myself, result, score)

print("Answer is:", total_score)