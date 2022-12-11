
def op_body(op, arg):
  if op == "*":
    return lambda x : x * (x if arg == "old" else int(arg))
  return lambda x : x + (x if arg == "old" else int(arg))

def parse():
  monkeys = []
  f = open('input.txt', 'r')
  lines = map(lambda x: x.strip(), f.readlines())
  monkey = None
  for line in lines:
    if line.startswith("Monkey"):
      #change monkey
      if monkey != None:
        monkeys.append(monkey)
      monkey = {
        "inspected": 0
      }
    elif "Starting" in line:
      items = line.split(":")[1]
      monkey["items"]=list(map(lambda x: int(x.strip()), items.split(",")))
    elif "Operation" in line:
      operation = line.split("=")
      op = operation[1][5]
      arg = operation[1][7:]
      monkey["operation"] = op_body(op, arg)
    elif "Test" in line:
      monkey["mod"] = int(line.split()[-1])
    elif "If true" in line:
      monkey["true"] = int(line.split()[-1])
    elif "If false" in line:
      monkey["false"] = int(line.split()[-1])
  if monkey != None:
    monkeys.append(monkey)
  return monkeys

monkeys = parse()
for r in range(20):
  for monkey in monkeys:
    for item in monkey["items"]:
      #inspect
      item = monkey["operation"](item)
      # decrese 
      item = item // 3
      # throw
      dest = monkey["true"] if item % monkey["mod"] == 0 else monkey["false"]
      monkeys[dest]["items"].append(item)
      monkey["inspected"] += 1
    monkey["items"] = []
inspections = sorted(map(lambda x: x["inspected"], monkeys), reverse=True)
print("Answer is:", inspections[0] * inspections[1])
