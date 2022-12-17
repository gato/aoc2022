import random
def parse_line(line):
  [node, edges] = line.split(";")
  node = {
    "name": node[6:8],
    "rate": int(node.split("=")[1]),
    "nodes": list(map(lambda x: x if len(x) == 2 else x[-2:] , edges.split(", ")))
  }
  return node

f = open('input.txt', 'r')
parsed = list(map(lambda x: parse_line(x.strip()), f.readlines()))
nodes = {x["name"]: x for x in parsed}
open_valves = [n for n in nodes if nodes[n]["rate"]>0]

dist_cache = {}

def dist(origin, valve):
  if (origin["name"], valve["name"]) in dist_cache:
   return dist_cache[(origin["name"], valve["name"])]
  visited = set()
  queue = [(origin, 0)]
  visited.add(origin["name"])
  while len(queue) > 0:
    (node, d) = queue.pop(0)
    for name in node["nodes"]:
      n = nodes[name]
      if n == valve:
        dist_cache[(origin["name"], valve["name"])] = d + 1
        return d + 1
      if not name in visited:
        visited.add(name)
        queue.append((n, d+1))
  return None

def solve(start, remaining, minutes):
  path = [start["name"]]
  if minutes == 0:
    return (0, path)
  if remaining == []:
    return (0, path)
  max_volume = 0
  for i in range(len(remaining)):
    n = nodes[remaining[i]]
    d = dist(start, n)
    cost = d + 1
    if cost < minutes:
      vol = (minutes - cost) * n["rate"]
      res = solve(n, remaining[:i]+remaining[i+1:], minutes - cost)
      calc = vol + res[0]
      if max_volume < calc:
        max_volume = calc
        path = [start["name"]] + res[1]
  return (max_volume, path)

print()
print("Your answer is", solve(nodes['AA'], open_valves, 30))

