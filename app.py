import random
import math

# your code here

who = ['the dog','my granma','his turtle','my bird']
what = ['eat','pissed','crushed','broked']
when = ['before the class','right in time','when I finished','during my lunch','while I was praying']

def excuse (a,b,c):
    x = random.randint(0,len(a)-1)
    y = random.randint(0,len(b)-1)
    z = random.randint(0,len(c)-1)

    return a[x]+" "+b[y] + " "+c[z]

print(excuse(who,what,when))
