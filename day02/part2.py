file1 = open('input.txt', 'r')
lines = file1.readlines()

decode_oponent = { 'A' : 'Rock', 'B': 'Paper', 'C': 'Scissors'}
decode_result = {'X' : 'Lost', 'Y': 'Draw', 'Z': 'Win' }
shape_points = { 'Rock': 1, 'Paper': 2, 'Scissors': 3 }
match_points = { 'Lost': 0, 'Draw': 3, 'Win': 6 }
win_shape = {'Rock':'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock' }
lose_shape = dict(map(lambda item: (item[1], item[0]), win_shape.items()))

print(win_shape)
print(lose_shape)

def get_shape(oponent, result):
  if result == 'Draw':
    return oponent
  if result == 'Win':
    return win_shape[oponent]
  return lose_shape[oponent]

total_score = 0
for line in lines:
  line = line.strip()
  parts = line.split(" ")
  oponent = decode_oponent[parts[0]]
  result = decode_result[parts[1]]
  myself = get_shape(oponent, result)
  score = shape_points[myself] + match_points[result]
  total_score += score
  print(oponent, myself, result, score)

print(total_score)
