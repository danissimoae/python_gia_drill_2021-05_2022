#1 - 20 +
#2 - yzx +
#3 - 14? -
#4 - 11<- / 011 +
#5 - BCDE -
#6 - 141 +
#7 - 3 - 
#8 - 1458 +
#9 - 190 -
#10 - 16 +
#11 - 5 -
#12 - 77 +
#13 - 75 +
#14 - 26 +
#15 - 19 +
#16 - 292 +
#17 - 5555 1254 +
#18 - 2627 833 -
#19 - 17 +
#20 - 31 33 +
#21 - 30 +
#22 - 316 +- 
#23 - 70 +
#24 - 22 +
#25 - 155925 51975 +
#     176715 58905
#     184275 61425
#     187425 62475
#     190575 63525
#     197505 65835
#26 - 609 31303 2+
#27A - 199578306 -
print('x y z')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = z and (y or (not x))
            if f == 1:
                print(x,y,z)


for i in range(1,10001):
    k = 2
    s = i
    while s<= 500:
        s = s + 20
        k = k + 5
    if k==92:
        print(i)


from itertools import product
k = 0
for x in product('ИВАН', repeat = 6):
    s = ''.join(x)
    if s.count("А")==1:
        k+=1
        print(s)
print(k)


s = '7'*62
while '5555' in s or '7777' in s:
    if '5555' in s: s = s.replace('5555','77',1)
    else: s = s.replace('7777','55',1)
print(s)



x = 49**10 * 7**9 - 7**7 - 49
k = 0
while x>0:
    if x%7==6:
        k+=1
    x = x//7
print(k)



def f(x,y,a):
    return (x+2*y!=60) or (a<y) or (y<x)

for a in range(10001):
    if all(f(x,y,a)==1 for x in range(1001) for y in range(1001)):
        print(a)



def f(n):
    if n==1: return 2
    if n>1 and n%3==0: return f(n-1) + f(n/3)
    if n>1 and n%3!=0: return f(n-1) + 1
print(f(50))



ans = []
for i in range(1240,9875+1):
    if i%3==0 and i%5!=0 and i%9!=0 and i%13!=0 and i%23!=0:
        ans.append(i)
print((sum(ans)/len(ans)), min(ans))



def f(a,b,c,m):
    if a+b>=73: return c%2==m%2
    if c==m: return 0
    h = [f(a+1,b,c+1,m),f(a,b+1,c+1,m),f(a*2,b,c+1,m),f(a,b*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)

for b in range(1,67+1):
    for m in range(1,5):
      if f(5,b,0,m)==1:
          print(b,m)
          break



for i in range(1,10001):
    x = i
    a = 0; b = 0
    while x>0:
        if x%2==0:
            a = a + 1
        b = b + x % 6
        x = x // 6
    if a==3 and b==1:
        print(i)


def f(curr,end):
    if curr>end: return 0
    if curr==end: return 1
    if curr<end: return f(curr+1,end)+f(curr*2,end)
print(f(2,12)*f(12,34))



s = open('Новая папка/USHAKOV/24/24-02.txt').readline()
s = s.replace('A',' ')
m = max(s.split(),key = len)
print(m,len(m))



def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(150_000,200_001):
    d = div(x)
    s = [int(x) for x in d if x%2!=0]
    if len(s)>=50:
        print(x,s[-1])


f = open('Новая папка/USHAKOV/26/26-02.txt')
s, n = map(int, f.readline())
a = [int(x) for x in f]'''



f = open('Новая папка/USHAKOV/27/27-02A.txt')
n = int(f.readline())
a = [int(x) for x in f]
ans = []
for i in range(n):
    for j in range(i+1,n):
        if a[i]-a[j]>=5:
            ans.append(a[i]+a[j])
print(max(ans))



