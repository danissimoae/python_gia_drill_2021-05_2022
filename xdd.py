s  = '110010100011'###OLIMPUDA
k = ''
for i in range(1,10):
    if s[i]+s[i+1]+s[i+2] =='110':
        s = s.replace('110','100',1)
        k+='A'
    elif s[i]+s[i+1]+s[i+2]=='100':
        s = s.replace('100','010',1)
        k+='B'
    elif s[i]+s[i+1]+s[i+2]=='010':
        s = s.replace('010','110',1)
        k+='C'
print(k)
print(s)

print('x y w z')
for x in (0,1):
    for y in (0,1):
        for w in (0,1):
            for z in (0,1):
                f = (not(y<=w)) or (x==z) or x
                if f==0:
                    print(x,y,w,z)

for i in range(1,1001):
    s = i
    s = (s-21)//10
    n = 1
    while s > 0:
        n = n*2
        s = s-n
    if n==16:
        print(i)


from itertools import *
k=0
for x in product('ЕЛНОСЦ',repeat=5):
    s=''.join(x)
    k+=1
##    if s.count('Е')==1 and 'Л' not in s:
##        print(s,k)
##        break
    print(s)
    
    
s = 89*'8'
while '1111' in s or '8888' in s:
    if '1111' in s:
        s = s.replace('1111','8',1)
    else:
        s = s.replace('8888','11',1)
print(s)


x = 5*216**3031 + 4*36**3024 - 3*6*3053 - 3064
k=0
while x>0:
    k += x%6
    x = x//6
print(k)


def f(x,a):
    return ((x%2==0)<=(not(x%5==0)) or (x+a>=90))

for a in range(1,101):
    if all(f(x,a)==1 for x in range(1,10001)):
        print(a)


def f(n):
    if n<3: return 1
    if n>2 and n%2==0: return f(n-1)+n-1
    if n>2 and n%2!=0: return f(n-2)+2*n-2
print(f(31))



a = [int(x) for x in open('17_probnik_27_4_22.txt')]
s = (min(int(x) for x in a if x%6==0))
ans = []
for i in range(len(a)-1):
    if a[i]%s==0 and a[i+1]%s==0:
        ans.append(a[i]+a[i+1])
print(len(ans),max(ans))
print(ans)



def f(a,b,c,m):
    if a+b>=247: return c%2==m%2
    if c==m: return 0
    h = [f(a+1,b,c+1,m),f(a,b+1,c+1,m),f(a*2,b,c+1,m),f(a,b*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)

for b in range(1,230):
    for m in range(1,5):
        if f(17,b,0,m)==1:
            print(b,m)
            break

from functools import *
def m(h):
    a,b = h
    return (a+1,b), (a,b+1), (a*2,b), (a,b*2)

@lru_cache(None)
def g(h):
    a,b = h
    if a+b>=247: return 'w'
    if any(g(i)=='w' for i in m(h)): return 'p1'
    if all(g(i)=='p1' for i in m(h)): return 'v1'
    if any(g(i)=='v1' for i in m(h)): return 'p2'
    if all(g(i)=='p1' or g(i)=='p2' for i in m(h)): return 'v2'
    if any(g(i)=='v2' for i in m(h)): return 'p3'
    if all(g(i)=='p1' or g(i)=='p2' or g(i)=='p3' for i in m(h)): return 'v3'

for i in range(20,201):
    h = 17,i
    if g(h)=='v2':
        print(i, g(h))

for i in range(1,100001):
    x = i
    q = 7
    p = 10
    k1 = 0
    k2 = 0
    while x<=100:
        k1 = k1+1
        x = x+p
    while x>=q:
        k2 = k2+1
        x = x-q
    l = x+k1
    m = x+k2
    if l==11 and m==20:
        print(i)



def f(curr,end):
    if curr>end: return 0
    if curr==end: return 1
    if curr<end: return f(curr+2,end)+f(curr*2,end)
print(f(1,24)*f(24,50))
    

s = open('24_probnik_27_4_22.txt').readline()
c=m=s[0]
for i in range(1,len(s)):
    if s[i-1] + s[i]=='BA' or s[i-1]+s[i]=='DA':
        c+=s[i]
        m=max(c,m,key=len)
    else: c=s[i]
print(m,len(m))'''



x = 5*216**3031 + 4*36**3024 - 3*6*3053 - 3064
k=0
while x>0:
    k += x%6
    x = x//6
print(k)
