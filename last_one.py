#1 - 7
#2 - zxwy
#3 - 401600
#4 - 203360
#5 - 388
#6 - 28
#7 - 65536
#8 - 2963
#9 - 42
#10 - 1
#11 - 18
#12 - 882882
#13 - 11
#14 - 92
#15 - 17
#16 - 5158048
#17 - 147 10849
#18 - 4507 3066
#19 - 15
#20 - 7 14
#21 - 13
#22 - 9
#23 - 182
#24 - 2940
#25 - 800120 400062
#     800253 266754
#     800273 21666
#     800375 160080
#     800396 400200
#26 - 99 14


###2
print('x y w z')
for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = (not(z and (not w))) or ((z<=w)==(x<=y))
                if f == 0:
                    print(x,y,w,z)



###5
ans = []
for i in range(2,1000):
    n = bin(i)[2:]
    if int(n)%2==0: n = '1' + n +'0'
    else: n = '11' + n + '10'
    r = int(n,2)
    if sum(int(x) for x in str(r))>17:
        ans.append(r)
print(bin(sum(int(x) for x in str(min(ans))))[2:])


###6
for i in range(1,100000):
    s = i
    n = 5
    while s<110:
        s = s + n
        n = n + 1
    if n==15:
        print(i)





###8
from itertools import *
st = 0
for x in product('ВЕКНО',repeat = 5):
    s = ''.join(x)
    st+=1
    if s.count('Н')==2 and s.count('К')==2:
        print(st)



###12
s = 400 * '2'
while '8888' in s or '222' in s:
    if '222' in s:
        s = s.replace('222','88',1)
    else:
        s = s.replace('8888','22',1)
print(s)



###14
x = 5**94 + 25**49 - 130
k = 0
while x>0:
    if x%5==4:
        k+=1
    x = x//5
print(k)



###15
from itertools import *
def f(x):
     P = 17<=x<=54
     Q = 37<=x<=83
     A = a1<=x<=a2
     return P <= ((Q and (not A)) <= (not P))

Ox = [i/4 for i in range(16*4,84*4+1)]
ans = []

for a1,a2 in combinations(Ox,2):
    if all(f(x)==1 for x in Ox):
        ans.append(a2-a1)
print(min(ans))





###16
def f(n):
    if n<5: return 1+2*n
    if n>=5 and n%3==0: return 2*(n+1)*f(n-2)
    if n>=5 and n%3!=0: return 2*n+1+f(n-1)+2*f(n-2)
print(f(15))




###17
a = [int(x) for x in open('17.txt')]
mx = max(x for x in a if x%111==0)
ans = []
for i in range(len(a)-1):
    if (a[i]>mx or a[i+1]>mx) and (a[i]%10==7 or a[i+1]%10==7):
        ans.append(a[i]+a[i+1])
print(len(ans),min(ans))



###19
def f(a,b,c,m):
    if a*b>=63: return c%2==m%2
    if c==m: return 0
    h = [f(a+1,b,c+1,m),f(a,b+1,c+1,m),f(a*2,b,c+1,m),f(a,b*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)

for b in range(1,31+1):
    for m in range(1,5):
        if f(2,b,0,m)==1:
            print(b,m)
            break



###22
for i in range(6,100):
    x = i
    a = 3*x + 23
    b = 3*x - 17
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a==10:
        print(i)



###23
def f(curr,end):
    if curr>end or curr==30: return 0
    if curr==end: return 1
    if curr<end: return f(curr+1,end)+f(curr*3,end)+f(curr*4,end)
print(f(2,15)*f(15,100))



###24
s = open('24.txt').readline()
c = m = s[0]
for i in range(1,len(s)):
    if s[i-1]+s[i]!='PR' and s[i-1]+s[i]!='RP':
        c+=s[i]
        m = max(c,m,key=len)
    else:
        c=s[i]
print(len(m),m)




###25
def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(80_0001,80_1001):
    d = div(x)
    if len(d)>0:
        if (d[0]+d[-1])%138==0:
            print(x,d[0]+d[-1],d)



###5
ans = []
for i in range(2,1000):
    n = bin(i)[2:]
    if int(n)%2==0: n = '1' + n +'0'
    else: n = '11' + n + '10'
    r = int(n,2)
    if sum(int(x) for x in str(r))>17:
        ans.append(r)
print(bin(sum(int(x) for x in str(min(ans))))[2:])'''





###27
f = open('24.txt')
n = int(f.readline())
k = 0
for i in range(n):
    x = int(f.readline())
    if (a[i]+a[i+1])%39==0:
        
