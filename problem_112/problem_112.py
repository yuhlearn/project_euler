from time import time

start = time()
n = 21780
no_bouncy = 21780*0.9

while no_bouncy/n < 0.99:
  n += 1
  N = str(n)
  decr = False
  incr = False
  for i in range(len(N)-1):
    if int(N[i]) > int(N[i+1]):
      decr = True
    elif int(N[i]) < int(N[i+1]):
      incr = True
    if decr and incr:
      break
  if decr and incr:
    no_bouncy += 1

print n, no_bouncy/n, time()-start
