f = open('27B.txt')
n = int(f.readline())
count = 0
k7 = 0
k = 0
for i in range(n):
    x = int(f.readline())
    if x%7==0: count+=k
    if x%7!=0: count+=k7

    k+=1
    if x%7==0: k7+=1
print(count)'''



'''f = open('27B.txt')
n = int(f.readline())
k65,k5,k13,k,count = 0,0,0,0,0
for i in range(n):
    x = int(f.readline())
    if x%65==0: count+=k
    elif x%13==0: count+=k5
    elif x%5==0: count+=k13
    else: count+=k65

    k+=1
    if x%65==0: k65+=1
    if x%5==0: k5+=1
    if x%13==0: k13+=1
print(count)




f = open('27A.txt')
n = int(f.readline())
k1,k0,k51,k50 = 0,0,0,0
for i in range(n):
    x = int(f.readline())
    if x%5==0 and x%2==0: k50+=1
    if x%5!=0 and x%2==0: k0+=1
    if x%5==0 and x%2!=0: k51+=1
    if x%5!=0 and x%2!=0: k1+=1
print(k50*k51 + k50*k1 + k51*k0)




f = open('27B.txt')
n = int(f.readline())
k = [0]*131
count = 0

for i in range(n):
    x = int(f.readline())
    ost = 0 if x%131==0 else 131-x%131
    count += k[ost]

    k[x%131]+=1
print(count)




f = open('27A.txt')
n = int(f.readline())
a = [0]*80
b = [0]*80
for i in range(n):
    x = int(f.readline())
    if x>50_000: b[x%80]+=1
    else: a[x%80]+=1

count = 0
count += b[0]*(b[0]-1)//2 + b[40]*(b[40]-1)//2
for i in range(1,39+1):
    count+=b[i]*b[80-i]

count+= b[0]*a[0] + b[40]*a[40]
for i in range(1,39+1):
    count += b[i]*a[80-i]
    count += a[i]*b[80-i]

print(count)'''
    
    


f = open('27A.txt')
n = int(f.readline())
m = -10**15

m = []
m2 = []
for i in range(n):
    x = int(f.readline())
    if x%2==0: m2+=[x]
    else: m+=[x]

print(max(m)+max(m2))






    
