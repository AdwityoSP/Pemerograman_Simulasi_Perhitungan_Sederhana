import random as rn
x=[]#jarak antar kota
y=[]#invers jarak
z=2#nilai beta
xx=0.9#Q0
yy=[]#phenomon awal tiap kota
zz=[]#Q random kota
xxx=[]#temporary
yyy=()#sum temporary
zzz=()#probabilitas
xxxx=()#nilai maks
n=int(input("masukan jumlah pos : "))
for i in range(0,n):
    a=rn.randint(1,100)
    x.append(a)
print (x)
for i in range(0,n):
    a=1/x[i]
    y.append(round(a,4))
print(y)
for i in range (0,n):
    a=0.0001
    yy.append(a)
print(yy)
for i in range(0,n):
    a=round(rn.random(),4)
    zz.append(a)
print(zz)
for i in range(0,n):
    a=round(yy[i]*(y[i]**(z)),10)
    xxx.append(a)
print(xxx)
for i in range(0,n):
    a=a+xxx[i]
yyy=a
print(yyy)
zzz=round(xxx[1]/yyy,4)
print(zzz)
for i in range(0,n):
    if (zz[i]<=xx) :
        xxxx=xxx
        break
    else : 
        xxxx=zzz
print(xxxx)