'''a = set()    ###14
b = {3,6,9,12}
c = {1,3,5,7,9,11}

def f(x):
    A = x in a
    B = x in b
    C = x in c
    return (B <= (not C)) or A

for x in range(1000):
    if f(x)==0:
        a.add(x)
print(a)




###15
a = set()
b = {3,6,9,12}
c = {1,2,3,4,5,6}

def f(x):
    A = x in a
    B = x in b
    C = x in c
    return (not((not A) and B)) or (not(C))

for x in range(1,10001):
    if f(x)==0:
        a.add(x)
print(len(a))



###16
a = set(range(1,101))
p = {2,4,6,8,10,12,14,16,18,20}
q = {5,10,15,20,25,30,35,40,45,50}

def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (A <= P) and (Q <= (not (A)))

for x in range(1,101):
    if f(x)==0:
        a.remove(x)
print(a)


###17
a = set()
p = {2,4,6,8,10,12,14,16,18,20}
q = {3,6,9,12,15,18,21,24,27,30}
r = {12,24,36,48,60}

def f(x):
    A = x in a
    P = x in p
    Q = x in q
    R = x in r
    return (not A) <= ((P and Q) <= R)

for x in range(1,1001):
    if f(x)==0:
        a.add(x)
print(a)



###18
from itertools import *
def f(x):
    A = a1<=x<=a2
    D = 17<=x<=58
    C = 29<=x<=80
    return D <= (((not C) and (not A)) <= (not D))

Ox = [i/4 for i in range(16*4,81*4+1)]
ans = []

for a1,a2 in combinations(Ox,2):
    if all(f(x)==1 for x in Ox):
        ans.append(a2-a1)
print(min(ans))




from itertools import *
def f(x):
    P = 17<=x<=54
    Q = 37<=x<=83
    A = a1<=x<=a2
    return P <= ((Q and (not A)) <= (not P))

Ox = [i/4 for i in range(16*4,84*4)]
ans = []

for a1,a2 in combinations(Ox,2):
    if all(f(x)==1 for x in Ox):
        ans.append(a2-a1)
print(min(ans))'''





from itertools import *
def f(x):
    B = 18<=x<=52
    C = 16<=x<=41
    A = a1<=x<=a2
    return (B <= A) and ((not C) or A)

Ox = [i/4 for i in range(15*4,53*4+1)]
ans = []

for a1,a2 in combinations(Ox,2):
    if all(f(x)==1 for x in Ox):
        ans.append(a2-a1)
print(min(ans))
    
