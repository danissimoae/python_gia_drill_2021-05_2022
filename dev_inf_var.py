print('x y w z')
for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = z or ((w or (not y)) == (x<=z))
                if f == 0:
                    print(x,y,w,z)

for i in range(112,125):
    n = bin(i)[2:]
    if sum(int(x) for x in n)%2==0:
        n = n + '00'
    else:
        n = n + '10'
    r = int(n,2)
    if r>452:
        print(r,i)


for i in range(1,10000):
    s = i
    n = 1
    while s>= 5:
        s = s - 15
        n = n * 2
    if n == 2048:
        print(i)


from itertools import *
k = 0
for x in product('ЛЕГКО',repeat = 6):
    s = ''.join(x)
    if s.count('О')<=1 and s[0]!= 'Г' and s[-1] not in 'ЕО':
        k+=1
print(k)


s = '1' + 105*'0'
while '1' in s:
    if '100' in s:
        s = s.replace('100','0001',1)
    else:
        s = s.replace('1','00',1)
print(s.count('0'))



x = 9**11 * 3**20 - 3**9 - 27
k = 0
while x>0:
    if x%3==2:
        k+=1
    x = x//3
print(k)


def f(x,y):
    return ((x*y)>a) or (x>y) or (74>x)

for a in range(1,10001):
    if all(f(x,y)==1 for x in range(1,100) for y in range(1,100)):
        print(a)


def f(n):
    if n<=2: return 2
    if n>2: return f(n-1) - 2*f(n-2)
print(f(37))


a = [int(x) for x in open('17_std.txt')]
mx = max(x for x in a if x%22==0)
ans = []
for i in range(1,len(a)):
    if (a[i-1]>mx or a[i]>mx) or (a[i-1]>mx and a[i]>mx):
        ans.append(a[i-1]+a[i])
print(len(ans),min(ans))



def f(a,b,c,m):
    if a+b>=150: return c%2==m%2
    if c==m: return 0
    h = [f(a+1,b,c+1,m),f(a,b+1,c+1,m),f(a+2,b,c+1,m),f(a,b+2,c+1,m),f(a+b,b,c+1,m),f(a,b+a,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
for b in range(1,89):
    for m in range(1,5):
        if f(61,b,0,m)==1:
            if m==4:print(b,m)
            break



for i in range(150,10001):
    x = i
    l = 0
    m = 0
    while x>0:
        m = m+1
        if x%2!=0:
            l = l+1
        x = x//2
    if l==7 and m==8:
        print(i)


def f(curr,end):
    if curr<end: return 0
    if curr==end: return 1
    if curr>end: return f(curr-2,end)+f(curr-5,end)
print(f(24,3))


f=open('24_std.txt').readline().strip().replace('R', ' ').split()
mx=0
for x in f:
    if x.count('A')<=3:
        mx=max(mx, len(x))
    else:
        s=x.split('A')
        for i in range(len(s)-3):
            ss='A'.join(s[i:i+4])
            mx=max(len(ss), mx)
print(mx)
    


for i in '0123456789':
    for j in '0123456789':
        d = int(f'12345{i}7{j}8')
        if d%68==0:
            print(d,d//68)'''

#1 - 57          xD 88 БАЛЛОВ
#2 - zyxw
#3 - 1341
#4 - 17
#5 - 456
#6 - 169
#7 - 3
#8 - 5376
#9 -
#10 - 24
#11 - 13504
#12 - 159
#13 - 18
#14 - 38
#15 - 5475
#16 - 388798
#17 - 58 1017
#18 - 2337 1275
#19 - 27
#20 - 9 26
#21 - 24
#22 - 191
#23 - 29
#24 - 151
#25 - 123452708 1815481
#     123453728 1815496
#     123454748 1815511
#     123455768 1815526
#     123456788 1815541
#26 - 24566 91982
