#1 - 19          88 баллов
#2 - wzyx
#3 - 2059 -
#4 - 20
#5 - 402
#6 - 280
#7 - 2
#8 - 883
#9 - 2559
#10 - 20
#11 - 368
#12 - 17
#13 - 8
#14 - 205
#15 - 35
#16 - 24
#17 - 86 10184
#18 - 2437 1654
#19 - 19
#20 - 15 18
#21 - 14
#22 - 39
#23 - 400
#24 - 20
#25 - 12325677 72933
#     12385672 73288
#     123165679 728791
#     123225674 729146
#     123515678 730862
#     123575673 731217
#     123865677 732933
#     123925672 733288








###2
print('x y w z')
for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = (not w) and ((y or z) <= (y and (not x)))
                if f == 1:
                    print(x,y,w,z)



###5
for i in range(90,110):
    n = bin(i)[2:]
    if n.count('1')%2==0: n = n + '0'
    else: n = n + '1'
    if n.count('1')%2==0: n = n + '0'
    else: n = n + '1'
    r = int(n,2)
    if r>=396:
        print(r,n)




###6
for i in range(1,1001):
    n = 34
    s = i
    while n <= 170:
        s = s + 120
        n = n + 23
    if s>999:
        print(i,s)



###8
from itertools import *
k = 0
st = 0
r = ['АА','ЕЕ','ПП','СС','ТТ','УУ','ХХ']
for x in product('АЕПСТУХ', repeat=4):
    s = ''.join(x)
    st += 1
    if all(x not in s for x in r) and st>1000:
        k+=1
print(k)



###14
x = 6*512**180 + 7*64**181 + 3*8**184 + 5*8**125 - 65
k = 0
while x>0:
    if x%64==0:
        k+=1
    x = x//64
print(k)


###15
def f(x,y,a):
    return (x<a) and (y<a) and ((x*y)>1200)

for a in range(1,200):
    if all(f(x,y,a)==0 for x in range(1,1001) for y in range(1,1001)):
        print(a)


###16
def f(n):
    if n<2: return n
    if n>=2 and n%2==0: return f(n/2)+1
    if n>=2 and n%2!=0: return f(3*n+1)+1

k = 0
for i in range(1,100001):
    d = f(i)
    if d==16:
        k+=1
print(k)




###17
a = [int(x) for x in open('17.txt')]
srz = ((sum(int(x) for x in a))/len(a))
ans = []
for i in range(1,len(a)):
    if (a[i-1]<srz and a[i]<srz) and (a[i-1]%10==9 or a[i]%10==9):
        ans.append(a[i-1]+a[i])
print(len(ans),max(ans))



###19
def f(a,c,m):
    if a>=40: return c%2==m%2
    if c==m: return 0
    h = [f(a+1,c+1,m),f(a+4,c+1,m),f(a*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)

for a in range(1,39+1):
    for m in range(1,5):
        if f(a,0,m)==1:
            if m==4: print(a,m)
            break



###22
for i in range(1,10001):
    x = i
    a = 0
    b = 0
    while x>0:
        if x%2==0:
            a+=1
        else:
            b+=x%6
        x = x//6
    if a==1  and b==4:
        print(i)



###23
def f(curr,end):
    if curr>end or curr==11 or curr==18: return 0
    if curr==end: return 1
    if curr<end: return f(curr+1,end)+f(curr+2,end)+f(curr*3,end)
print(f(4,8)*f(8,23))



###24
s = open('24.txt').readline()
for j in set(s):
    s = s.replace(f'X{j}Y','*')
    s = s.replace(f'Z{j}Y','*')
c=m=''
for i in range(len(s)):
    if s[i]=='*':
        c+=s[i]
        m = max(c,m,key=len)
    else:
        m = max(c,m,key=len)
        c=''
print(len(m))




s = open('24.txt').readline()
for i in set(s):
    s = s.replace(f'X{i}Y','*')
    s = s.replace(f'Z{i}Y','*')
for i in set(s) - {'*'}:
    s = s.replace(i,' ')
print(max(map(len,s.split())))'''



###25
from itertools import *
digits = '0123456789'
r = []

for d1 in digits:
    for i in range(3):
        for x in product(digits,repeat = i):
            n = int('123' + ''.join(x) + '567' + d1)
            if n%169==0 and n<10**9:
                r.append(n)
for x in sorted(r):
    print(x,x//169)








    
    
    

