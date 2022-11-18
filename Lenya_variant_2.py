#1 - 30                88 баллов
#2 - zywx
#3 - 50
#4 - 20
#5 - 49
#6 - 26
#7 - 11
#8 - 4352
#9 - 2585
#10 - 26
#11 - 11008
#12 - 717
#13 - 36
#14 - 6
#15 - 80
#16 - 2072
#17 - 731 990
#18 - 2145 1145 - balll
#19 - 18
#20 - 31 34
#21 - 30
#22 - 46
#23 - 30
#24 - 284
#25 - 220004 110004
#     220023 73344
#     220024 110014
#     220033 20014
#     220043 1044



###2
print('x y w z')
for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = (x<=y) or (not(w<=z))
                if f == 0:
                    print(x,y,w,z)




###5
for i in range(1,101):
    n = bin(i)[2:]
    if n.count('1')==n.count('0'):
        n = n + n[-1]
    elif n.count('1')>n.count('0'):
        n = n + '0'
    else:
        n = n + '1'
    if n.count('1')==n.count('0'):
        n = n + n[-1]
    elif n.count('1')>n.count('0'):
        n = n + '0'
    else:
        n = n + '1'
    if n.count('1')==n.count('0'):
        n = n + n[-1]
    elif n.count('1')>n.count('0'):
        n = n + '0'
    else:
        n = n + '1'
    r = int(n,2)
    if r%4==0 and r%8!=0:
        print(i,r)



###6
for i in range(1,1000001):
    s = i
    n = 1
    while s<47:
        s = s+4
        n = n*2
    if n == 64:
        print(i)



###8
from itertools import *
k = 0
for x in product('ВИШНЯ',repeat = 6):
    s = ''.join(x)
    if s.count('В')<=1 and s[0]!='Ш' and s[-1] not in 'ИЯ':
        k+=1
print(k)




###12
s = 95*'1' + 31 * '7'
while '1111' in s:
    s = s.replace('1111','7',1)
    s = s.replace('77','1',1)
print(s)



###14
for i in range(5,10):
    if int('132',i) + int('13',8) == int('124',i+1):
        print(i)


###15
def f(x,a):
    return ((x%2==0) <= (x%5!=0)) or ((x+a)>=90)

for a in range(1,100):
    if all(f(x,a)==1 for x in range(1,1001)):
        print(a)



###16
def f(n):
    if n==1: return 1
    if n%2==0: return n+f(n-1)
    if n>1 and n%2!=0: return 2*f(n-2)
print(f(24))




###17
a = [int(x) for x in open('17.txt')]
mx = max(x for x in a if x%11==0)
ans = []
for i in range(1,len(a)):
    if (a[i-1]%11==0 or a[i]%11==0) and ((a[i-1]+a[i])<=mx):
        ans.append(a[i-1]+a[i])
print(len(ans),max(ans))





###19-21
def f(a,b,c,m):
    if a+b>=77: return c%2==m%2
    if c==m: return 0
    h = [f(a+1,b,c+1,m),f(a,b+1,c+1,m),f(a*2,b,c+1,m),f(a,b*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)

for b in range(1,69+1):
    for m in range(1,5):
        if f(7,b,0,m)==1:
            if m==4:print(b,m)
            break



###22
for i in range(1,100001):
    x = i
    a,b = 0,0
    while x>0:
        c = x%10
        a = a+c
        if b<c:
            b=c
        x = x//10
    if a==10 and b==6:
        print(i)



###23
def f(curr,end):
    if curr>end or curr==15: return 0
    if curr==end: return 1
    if curr<end: return f(curr+1,end)+f(curr*2,end)
print(f(2,12)*f(12,32))



###24
s = open('24.txt').readline().split('.')
print(max(len(x) for x in s if s.count('A')>=3))

s = open('24.txt').readline().split('.')
m = 0
for x in s:
    if x.count('A')>=3:
        m = max(m,len(x))
print(m)




###25
def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(220_000,221_001):
    d = div(x)
    if len(d)>1 and (min(d) + max(d)) % 10 == 4:
        print(x,min(d)+max(d))'''




        
        
