f = open('26prog.1.txt')
s, n = map(int, f.readline().split())
a = sorted(int(x) for x in f)

b = []
while sum(b)<=s:
    b.append(a.pop(-1))
    b.append(a.pop(0))
if sum(b)>s:
    b.pop(-1)
print(len(b), b[-1])




f = open('26prog.2.txt')
n = int(f.readline())
a = [int(x) for x in f]
a.sort()

mx = []
mn = []
while len(a)>0:
    mx+=[a.pop(-1)]
    while sum(mx)>=sum(mn):
        mn+=[a.pop(0)]
print(len(mx),len(mn))




f = open('26prog.3.txt')
n, s = map(int, f.readline().split())
a = [int(x) for x in f]
a.sort(reverse=1)

count = 0
last = 0
s1 = 0

while len(a)>0:
    for i in range(len(a)):
        if s1+a[i]<=s:
            s1 += a[i]
            a[i] = 0
    a = [int(x) for x in a if x!=0]
    count+=1
    last = s1
    s1 = 0
print(count,last)


f = open('26prog.4.txt')
n = int(f.readline())
a = [int(x) for x in f]
a.sort()

ans = []
for i in range(n):
    for j in range(i+1,n):
        if (a[i]+a[j])%2==0:
            sr = (a[i]+a[j])//2
            if a[2499]<sr<a[3750]:
                ans.append(sr)
print(len(ans),min(ans))





f = open('26prog.5.txt')
n = int(f.readline())
a = [int(x) for x in f]
a.sort()
d = set(a)

ans = []
for i in range(n):
    for j in range(i+1,n):
        if a[i]%2!=a[j]%2 and a[i]+a[j] in d:
            ans.append(a[i]+a[j])
print(len(ans),max(ans))




f = open('26prog.6.txt')
n = int(f.readline())
a = [int(x) for x in f]


d = {x: a.count(x) for x in sorted(set(a),key=a.count) if a.count(x)!=0}
print(len(d), d)






f = open('26prog.6.txt')
n = int(f.readline())
a = [int(x) for x in f]
count = len(sorted(set(a)))
a.sort()

m=c=1
for i in range(1,n):
    if a[i-1]==a[i]:
        c+=1
        m = max(m,c)
    else:
        c=1
print(count,m)'''




f = open('26prog.7.txt')
n = int(f.readline())
a = [int(x) for x in f]






    
        
        
        

