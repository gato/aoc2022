f = open('input.txt', 'r')

class FileTree:

  def __init__(self):
    self.root = {}
    self.wd=[]

  def cd(self, dir):
    if dir == "/":
      self.wd = []
    elif dir == "..":
      self.wd = self.wd[0:-1]
    else:
      self.wd.append(dir)
    return self.wd 

  def ls(self):
    pass

  def command(self, parts):
    if parts[1] == "cd":
      self.cd(parts[2])
    else:
      self.ls()

  def find_dirs(self, name, curr_dir, found):
    size=0
    for k in curr_dir.keys():
      if type(curr_dir[k]) is dict:
        size += self.find_dirs(k, curr_dir[k], found)
      else:
        size += curr_dir[k]
    if (size <= 100000):
      t = (name, size)
      found.append(t)
    return size

  def add_file(self, filename, size):
    curr_dir = self.root
    for d in self.wd:
      if not d in curr_dir:
        curr_dir[d]={}
      curr_dir = curr_dir[d]
    curr_dir[filename]=size

lines = f.readlines()
ft = FileTree()
for line in lines:
  parts = line.strip().split()
  if parts[0] == "$":
    ft.command(parts)
  elif parts[0] == "dir":
    pass
  else:
    ft.add_file(parts[1], int(parts[0]))
found = []
total = ft.find_dirs("/", ft.root, found)
print("total used space:", total)
acc = 0
for t in found:
  acc += t[1]
print("Answer is:", acc)