import math

limit = 1000000
out = 0
i = 1
while i < limit:
   a = 1/(i**2)
   i+=1
   out = out + a

pi_aproximate = math.sqrt(out*6)
print(pi_aproximate)
print(math.pi)


