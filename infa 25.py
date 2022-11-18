#база
'''def p(x):
    return x>1 and all(x%i!=0 for i in range(2, int(x**0.5)+1))

def div(x):
    d = set()
    for i in range(1, int(x**0,5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)


for x in range(,+1): #generatori yuzat nado []
    d = div(x)
    if len(d)==:
        print(d[], d[])

#простота: x>1, нет делителей на [2;x**0,5]

def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(174457, 174505+1):
    d = div(x)
    if len(d)==2:
        print(*d)



def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(150001, 151001):
    d = div(x)
    s = sum(d)
    if s%13==10:
        print(x, s)
        


def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(250201, 251000):
    d = div(x)
    if len(d)>=2 and min(d) + max(d) % 123 == 17:
        print(x, min(d) + max(d)) 
        

def divisors(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(400000001, 400010001):
    d = divisors(x)
    if len(d)>=5:
        p = d[0]*d[1]*d[2]*d[3]*d[4]
        if p%100==17 and p<=x:
            print(p, d[4])


def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(1204300, 1204380+1):
    d = div(x)
    if d%2==0 and d%10==0:


def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(220001, 220501):
    d = div(x)
    if len(d)>0:
        s = min(d)+max(d)
        if s%10==4:
            print(x, s)




def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(174457, 174505+1):
    d = div(x)
    if len(d)==2:
        print(x,d)



def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(81234,134689+1):
    d = div(x)
    if len(d)==3:
        print(d)
        


def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
...
for x in range(1204300, 1204380+1):
    d = div(x)
    s = (sum(int(x) for x in d if x%2==0))
    if s!=0 and s%10==0:
        print(x,s)

        

def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(500001,500102):
    d = div(x)
    s = [i for i in d if i%10==8 and i!=8]
    if len(s)>0:
        print(x,s[0])




def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(3_000_00, 3_009_00):
    d = div(x)
    s = [i for i in d if i%3==0]
    if len(s)>0 and len(s)==5:
        print(x,s[-1])



def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(550_000, 551_001):
    d = div(x)
    s = [i for i in d if i%10==7]
    if len(s)>0 and len(s)==3:
        print(x,s[-1])





def div(x):
    d = set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(6_080_068, 6_080_176+1):
    d = div(x)
    s = [i for i in d]
    if len(s)==2:
        print(x)'''




def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

def prime(x):
    return x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))

for x in range(25317,51238):
    d = div(x)
    s = [i for i in d if prime(i)]
    if len(s)>=6:
        print(x,s[-1])



