a = [int(x) for x in open('')]
ans = []

for i in range(len(a)):
    if a[i]%3==0:
        ans.append(a(i))
print(len(ans), max(ans))



a = [int(x) for x in open('')
ans = []

for i in range(len(a)-1):
    if abs(a[i])%10==7 or abs(a[i+1])%10==7:
        ans.append(a[i]+a[i+1])
print(len(ans), max(ans))


a = [int(x) for x in open('17.txt')]
ans= []

for i in range(len(a)):
    if a[i]%3==0 and not (a[i]%7==0\
    and a[i]%17==0 and a[i]%19==0 and a[i]%27==0):
        ans.append(a(i))
print(len(ans), max(ans))





#############
abs - когда модуль
while x>0:
    k=0
    if x%3==2:
        k+=1
        x//3
двузнач = 10<=x<=99
m = max(ans, key=sum)


a = [int(x) for x in open('')]
ans = []

for i in range(len(a-1)):
    if (a[i]**2 + a[i+1]**2)%2!=0 and (a[i]**2 + a[i+1]**2)<80:
        ans.append(a[i],a[i+1])



a = [int(x) for x in open('17.txt')]
ans = []

for i in range(len(a)):
    if a[i]%3==0 and a[i]%7!=0 and a[i]%17!=0\
    and a[i]%19!=0 and a[i]%27!=0:
        ans.append(a[i])
print(len(ans), max(ans))



a = [int(x) for x in open('17.2.txt')]###чел через перевод в символы решает....
ans = []

for i in range(len(a)):
    if (str(a[i])[-1]=='2' and a[i]%3==0 and a[i]%11==0)\
    or (str(a[i])[-1]=='7' and a[i]%3==0 and a[i]%11==0):
        ans.append(a[i])
print(len(ans),min(ans))



a = [int(x) for x in open('17.3.txt')]
ans = []

for i in range(len(a)):
    if (a[i]%10==5 and a[i]%9!=0 and a[i]%11!=0) or \
    (a[i]%10==7 and a[i]%9!=0 and a[i]%11!=0):
        ans.append(a[i])
print(len(ans),min(ans)+max(ans))




a = [int(x) for x in open('17.4.txt')]
ans = []

for i in range(len(a)):
    if a[i]%13==7 and a[i]%7!=0 and a[i]%11!=0:
        ans.append(a[i])
print(max(ans)-min(ans), len(ans))



a = [int(x) for x in open('17.5.txt')]
ans = []
            
for i in range(len(a)):
    if a[i]%16==11 and (a[i]%7==0 and a[i]%6!=0 \
    and a[i]%13!=0 and a[i]%19!=0):
        ans.append(a[i])
print(sum(ans),len(ans))



a = [int(x) for x in open('17.6.txt')]
ans = []

for i in range(len(a)-1):
    if (a[i]+a[i+1])%3==0 and (a[i]+a[i+1])%6!=0\
    and abs((a[i]*a[i+1]))%10==8:
        ans.append(a[i]+a[i+1])
print(len(ans), max(ans))



a = [int(x) for x in open('17.7.txt')]
ans = []

for i in range(len(a)-1):
    if ((a[i]*a[i+1])>0 and (a[i]+a[i+1])%7==0):
        ans.append(a[i]*a[i+1])
print(len(ans),min(ans))



a = [int(x) for x in open('17.8.txt')]
ans = []

for i in range(len(a)-2):
    if (a[i]*a[i+1]*a[i+2])%7==0 and (a[i]+a[i+1]+a[i+2])%10==5:
        ans.append(a[i]+a[i+1]+a[i+2])
print(len(ans),max(ans))



a = [int(x) for x in open('17.9.txt')]#если все числа делятся на три то их сум тоже
ans = []

for i in range(len(a)-2):
    if (a[i]%12==0 and a[i]%3==0 and a[i+1]%3==0 and a[i+2]%3==0)\
      or (a[i+1]%12==0 and a[i]%3==0 and a[i+1]%3==0 and a[i+2]%3==0)\
      or (a[i+2]%12==0 and a[i]%3==0 and a[i+1]%3==0 and a[i+2]%3==0):
        ans.append((a[i]+a[i+1]+a[i+2])//3)
print(len(ans), min(ans))



a = [int(x) for x in open('17.10.txt')]
ans = []

for i in range(len(a)-2):
    if a[i]%3==2 or a[i+1]%3==2 or a[i+2]%3==2:
        ans.append(min(a[i],a[i+1],a[i+2]))
print(len(ans),sum(ans))





a = [int(x) for x in open('17.11.txt')]
ans = []

for i in range(len(a)-3):
    if abs(a[i]-a[i+3])>1000 and a[i]>a[i+1]>a[i+2]>a[i+3]:
        ans.append(a[i]+a[i+1]+a[i+2]+a[i+3])
print(len(ans),min(ans))




a = [int(x) for x in open('17.12.txt')]
ans = []
for i in range(len(a)-1):
    if (a[i]+a[i+1]>=100 and (a[i]<0 or a[i+1]<0)) or\
       (a[i]+a[i+1]>=100 and (a[i]<0 and a[i+1]<0)):
        ans.append(a[i]*a[i+1])
print(len(ans),max(ans))




a = [int(x) for x in open('17.13.txt')]
ans = []
for i in range(len(a)-1):
    if 50<=(abs(a[i])+abs(a[i+1]))<=200:
        ans.append(min(a[i],a[i+1]))
print(len(ans),min(ans))


a = [int(x) for x in open('17.14.txt')]
ans = []
srz = sum(a)/len(a)

for i in range(len(a)-2):
    if (a[i]>srz and a[i+1]>srz) or (a[i]>srz and a[i+2]>srz)\
       or (a[i+1]>srz and a[i+2]>srz):
        ans.append(a[i]+a[i+1]+a[i+2])
print(len(ans),max(ans))




a = [int(x) for x in open('17.15.txt')]
ans = []
delimoe = []
for i in range(len(a)):
    if a[i]%19==0:
        delimoe.append(a[i])

for i in range(len(a)-1):
    if a[i]>max(delimoe) or a[i+1]>max(delimoe):
        ans.append(a[i]+a[i+1])
print(len(ans),min(ans))




a = [int(x) for x in open('17.16.txt')]
ans = []
kr11 = []
kr17 = []
for i in range(len(a)):
    if a[i]%11==0:
        kr11.append(a[i])
for i in range(len(a)):
    if a[i]%17==0:
        kr17.append(a[i])
if len(kr11)>len(kr17):
    print(len(kr11),min(kr11))
else:
    print(len(kr17),max(kr17))


a = [int(x) for x in open('17.16.txt')]###ТОЖЕ ЧТО И НАВЕРХУ
kr11 = [x for x in a if x%11==0]
kr17 = [x for x in a if x%17==0]
if len(kr11)>len(kr17):
    print(len(kr11),min(kr11))
else:
    print(len(kr17),max(kr17))



a = [int(x) for x in open('17.17.txt')]
usl = [x for x in a if x%10==4]
ans = []
znach = (min(usl)+max(usl))
for i in range(len(a)-1):
    if (a[i] + a[i+1]) < znach:
        ans.append(a[i]+a[i+1])
print(len(ans),max(ans))



a = [int(x) for x in open('17.18.txt')]
ans = []
for i in range(len(a)-1):
    if (a[i]%9==0 and a[i+1]%9!=0 and abs(a[i+1]%8==3)) + \
       (a[i]%9!=0 and a[i+1]%9==0 and abs(a[i]%8==3))==1:
        ans.append(max(a[i],a[i+1]))
print(len(ans),max(ans))




a = [int(x) for x in open('17.19.txt')]###ИНТЕРЕСНОЕ УСЛОВИЕ 19KOMPEGE
ans = []
for i in range(len(a)-2):
    if not(a[i]>0 and a[i]%10==9) and not(a[i+2]>0 and a[i+2]%10==9) \
       and a[i+1]>0 and a[i+1]%10==9:
        ans.append(a[i]+a[i+1]+a[i+2]), print(a[i+1])
print(len(ans),max(ans))




a = [int(x) for x in open('17.20.txt')]
ans = []
s = sum(int(i) for x in a if x%35==0 for i in str(x))###ПЕРЕВОД ЧИСЕЛ В ЦИФРЫ
for i in range(len(a)-1):
    if (a[i]>s and a[i+1]<=s and a[i+1]%16==15 and a[i+1]//16%16==14)\
       or (a[i]%16==15 and a[i]//16%16==14 and a[i]<=s and a[i+1]>s):
        ans.append(a[i]+a[i+1])
print(len(ans),min(ans))


a = [int(x) for x in open('17.5.txt')]
ans = []

for i in range(len(a)):
    if a[i]%16==11 and a[i]%7==0 and a[i]%6!=0 and a[i]%13!=0 and a[i]%19!=0:
        ans.append(a[i])
print(sum(ans),len(ans))

