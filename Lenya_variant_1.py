#1 - 22
#2 - ywxz
#3 - 123_900
#4 - 111
#5 - 123
#6 - 77
#7 - 10
#8 - 2676053
#9 - 67
#10 - 65
#11 - 100
#12 - 88881
#13 - 11
#14 - 1484
#15 - 17
#16 - 1444
#17 - 147 10849
#18 - 761 579
#19 - 49
#20 - 88 96
#21 - 87
#22 - 143
#23 - 29
#24 - 28
#25 - 123450668 7261804
#     123451688 7261864
#     123456618 7262154
#     123457638 7262214
#     123458658 7262274
#     123459678 7262334
#26 - 99 14



###2
print('x y w z')
for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = (x <= (y and (not z))) or w
                if f == 0:
                    print(x,y,w,z)

###5
list = []
for i in range(1,35):
    n = bin(i)[2:]
    if int(n)%2==0:
        n = '11' + n + '11'
    else:
        n = '1' + n + '0'
    r = int(n,2)
    if r<=126:
        list.append(r)
print(sorted(list))


###6
for i in range(1,100001):
    d = i
    n = 3
    s = 57
    while s<=1200:
        s = s + d
        n = n + 4
    if n==63:
        print(i)



###7 16777216/(1024*1536) = 10.666666666666666


###8
from itertools import *
k = 0
r = ['000','111','222','333','444','555','666','777','888']
for x in product('012345678',repeat = 7):
    s = ''.join(x)
    if s[-1]!='3' and s[-1]!='4' and s[-1]!='7' and s[0]!='0'\
    and all(x not in s for x in r):
        k+=1
print(k)



###12
s = 81* '1'
while '1111' in s or '88888' in s:
    if '1111' in s:
        s = s.replace('1111','888',1)
    else:
        s = s.replace('88888','888',1)
print(s)




###14
x = 5**2004 - 5**1016 - 25**508 - 5**400 + 25**250 - 27
k = 0
while x>0:
    if x%5==4:
        k=k+1
    x = x//5
print(k)





###15
from itertools import combinations
def f(x):
    P = 17<=x<=54
    Q = 37<=x<=83
    A = a1<=x<=a2
    return P <= ((Q and (not A)) <= (not P))

ox = [i/4 for i in range(16*4,83*4+1)]
m = []

for a1,a2 in combinations(ox,2):
    if all(f(x)==1 for x in ox):
        m.append(a2-a1)
print(min(m))




###16
def f(n):
    if n==1: return 1
    if n>1 and n%2!=0: return 3*n+f(n-2)
    if n>1 and n%2==0: return 4*f(n/2)
print(f(42))





###17
a = [int(x) for x in open('17.txt')]
ans = []
mx = max(x for x in a if x%111==0)
for i in range(1,len(a)):
    if (a[i-1]>mx or a[i]>mx) and (a[i-1]%10==7 or a[i]%10==7)>0:
        ans.append(a[i-1]+a[i])
print(len(ans),min(ans))




###19 - 21
def f(a,b,c,m):
    if a+b>=211: return c%2==m%2
    if c==m: return 0
    h = [f(a+1,b,c+1,m),f(a,b+1,c+1,m),f(a*2,b,c+1,m),f(a,b*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)

for b in range(1,193+1):
    for m in range(1,5):
        if f(17,b,0,m)==1:
            if m==4:print(b,m)
            break



###22
for i in range(120,10000):
    x = i
    l = 0
    m = 0
    while x>0:
        m = m +1
        if x % 2 != 0:
            l = l+1
        x = x//2
    if l==5 and m==8:
        print(i)




###23
def f(curr,end):
    if curr<end: return 0
    if curr==end: return 1
    if curr>end: return f(curr-2,end)+f(curr-5,end)
print(f(23,2))



###24
s = open('24.txt').readline()
s = s.replace('ZXY','*').replace('ZYX','*')
c = m = ''
for i in range(1,len(s)):
    if s[i]=='*':
        c+=s[i]
        m = max(c,m,key=len)
    else:
        c=''
print(m,len(m))'''




###25
ans = []
for i in '0123456789':
    for j in '0123456789':
        d = int(f'12345{i}6{j}8')
        if d%17==0:
            print(d,d//17)




###27
a = open('27-11A.txt').readline()


