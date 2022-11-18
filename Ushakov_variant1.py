print('x y w z')
for x in (0,1):
    for y in (0,1):
        for z in (0,1):
            for w in (0,1):
                f = (w and z) or (not y) or ((not x) == (not w))
                if f == 0:
                    print(x,y,w,z)

for i in range(1,1001):
    k = 0
    s = i
    while s<205:
        s = s + 10
        k = k + 8
    if k==72:
        print(i)


for i in range(20,50):
    s = bin(i)[2:]
    if i%2==0:
        s+='01'
    else:
        s+='10'
    s = int(s,2)
    if s>81:
        print(s)


from itertools import *
k = 0
for x in product('АЕНПСТ',repeat=4):
    s=''.join(x)
    if s.count('Т')==1:
        k+=1
print(k)



s = 83 * '7'
while '77777' in s or '222' in s:
    if '77777' in s:
        s = s.replace('77777','22',1)
    else: s = s.replace('222','2')
print(s)


x = 9**200+3**100-7
k=0
while x>0:
    if x%6==2:
        k=k+1
    x = x//6
print(k)


def f(x):
    return ((not(x%12==0)) or (not(x%18==0))) <= (not(x%a==0))

for a in range(1,1001):
    if all(f(x)==1 for x in range(1,10001)):
        print(a)


def f(n):
    if n==1: return 1
    if n==2: return 2
    if n>2: return f(n-1)+f(n-2)
print(f(17))


ans = []
for i in range(1316,9965):
    if i%5==0 and i%3!=0 and i%7!=0 and i%11!=0 and i%25!=0:
        ans.append(i)
print(len(ans),max(ans))


def f(a,b,c,m):
    if a+b>=61: return c%2==m%2
    if c==m: return 0
    h = [f(a+1,b,c+1,m),f(a,b+1,c+1,m),f(a*2,b,c+1,m),f(a,b*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)

for b in range(1,54):
    for m in range(1,5):
        if f(7,b,0,m)==1:
            print(b,m)
            break


for i in range(1,1001):
    x = i
    l = 94
    m = 0
    while l>=x:
        m = m + 1
        l = l - x
    if m < l:
        x = m
        m = l
        l = x
    if l==3 and m == 7:
        print(i)


def f(curr,end):
    if curr>end: return 0
    if curr==end: return 1
    if curr<end: return f(curr+1,end)+f(curr*2,end)
print(f(1,18)*f(18,45))



s = open('USHAKOV/24/24-01.txt').readline()
k=0
c=0
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        k+=1
        c=max(k,c)
    else:
        k==1
print(c)



def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)'''

s = open('USHAKOV/24/24-01.txt').readline()
c = k = 0
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        k+=1
        c=max(c,k)
    else:
        k=1
print(c)
        
