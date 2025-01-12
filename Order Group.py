def gen(a,b):
  s = set(range(0,a))
  g = set()
  for i in s:
    g.add((i*b)%a)
  return g
a = int(input('a :' )) #order of Z, e.g Z4, Z5, etc...
s = set(range(0,a))
for i in s:
  if(gen(a,i) == s):
    print(i)