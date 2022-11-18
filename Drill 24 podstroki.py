###1
s = open('24.txt').readline()
print(s.count('XVIII'))



###2
s = open('24.txt').readline()
cnt = 0
for i in range(len(s)-3):
    if s[i]+s[i+1]+s[i+2]=='TIK' or s[i]+s[i+1]+s[i+2]=='TOK':
        cnt +=1
print(cnt)


s = open('24.txt').readline()
print(s.count('TIK')+s.count('TOK'))




###3
s = open('24.txt').readline()
print(s.count('OCK')-s.count('STOCK'))


s = open('24.txt').readline()
k = 0
r = 0
for i in range(len(s)-2):
    if s[i]+s[i+1]+s[i+2]=='OCK':
        k+=1
for i in range(len(s)-5):
    if s[i]+s[i+1]+s[i+2]+s[i+3]+s[i+4]=='STOCK':
        r+=1
print(k-r)





###4
s = open('24.txt').readline()
print(s.count('BOSS')-s.count('JBOSS')-s.count('BOSSJ')+s.count('JBOSSJ'))


s = open('24.txt').readline()
k = 0
r = 0
for i in range(len(s)-3):
    if s[i]+s[i+1]+s[i+2]+s[i+3]=='BOSS':
        k+=1
for i in range(len(s)-4):
    if s[i]+s[i+1]+s[i+2]+s[i+3]+s[i+4]=='JBOSS' or s[i]+s[i+1]+s[i+2]+s[i+3]+s[i+4]=='BOSSJ':
        r+=1
for i in range(len(s)-5):
    if s[i]+s[i+1]+s[i+2]+s[i+3]+s[i+4]+s[i+5]=='JBOSSJ':
        r-=1
print(k-r)



###5
s = open('24.txt').readline()
while 'XIXIX' in s:
    s = s.replace('XIXIX','XIX XIX')
print(s.count('XIX'))


s = open('24.txt').readline()
k = 0
for i in range(len(s)-2):
    if s[i]+s[i+1]+s[i+2]=='XIX':
        k+=1
print(k)
