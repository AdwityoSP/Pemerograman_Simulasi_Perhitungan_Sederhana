import random as ran
x=[]#angka acak bahan
y=[]#frekuensi
z=[]#probabilitas
xx=[]#probabilitas kumulatif
yy=[]#batas bawah
zz=[]#batas atas
xxx=[]#angka acak uji coba
yyy=[]#angka permintaan
zzz=[]#total prediksi
total=[]#total dana
aa=0#pengelompokan
bb=0#pengelompokan
cc=0#pengelompokan
dd=0#pengelompokan
ee=0#pengelompokan
print("Aplikasi Metode Prediksi Monte Carlo")
print("Adwityo S.P 1520180 Pemerograman Simulasi 2")
print("==========================================")
#n angka
n=int(input("masukan jumlah angka : "))
for i in range (0,n) :
    a=ran.randint(0,4)
    x.append(a)
print("data statistik : "+ str(x))
#n frekuensi
for i in range (0,n):
    if x[i] == 0 :
        aa+=1
    elif x[i] == 1 :
        bb+=1
    elif x[i] == 2 :
        cc+=1
    elif x[i] == 3 :
        dd+=1
    elif x[i] == 4 :
        ee+=1
y.append(aa)
y.append(bb)
y.append(cc)
y.append(dd)
y.append(ee)
print("frekuensi : "+ str(y))
#n prob  
for i in range (0,5):
    a=y[i]/n
    z.append(a)
print("probabilitas : "+ str(z))
#n prob kumulatif
a=z[0]
xx.append(a)
for i in range (0,4):
    b=xx[i]+z[i+1]
    xx.append(b)
print("probabilitas kumulatif : "+ str(xx))
#b.bawah
a=0
yy.append(a)
for i in range (0,4):
    a=xx[i]
    yy.append (a)
print("batas bawah kelas : "+ str(yy))
#b.atas
for i in range (0,4):
    a=xx[i]-0.01
    zz.append(a)
a=1
zz.append(a)
print("batas atas kelas : "+ str(zz))
#interval
for i in range (0,5):
    print("interval ke-"+str(i)+" : "+str(yy[i])+" - "+str(zz[i]))
#prediksi
wow=int(input("masukan jumlah data uji coba : "))
for i in range (0,wow) :
    a=round(ran.random(),4)
    xxx.append(a)
print("data uji : "+str(xxx))
#nilai
for i in range (0,wow) :
    if xxx[i]<zz[0] :
        a=0
    elif xxx[i]<zz[1]:
        a=1
    elif xxx[i]<zz[2]:
        a=2
    elif xxx[i]<zz[3]:
        a=3
    elif xxx[i]<zz[4]:
        a=4
    yyy.append(a)
print("prediksi permintaan : "+str(yyy))
#nilai prediksi
for i in range(0,wow):
    a= yyy[i]*2500000
    zzz.append(a)
print("prediksi biaya : "+str(zzz))
#total nilai
res=0
for i in range(0,wow):
    res=res+yyy[i]
print("prediksi permintaan total : "+str(res))
ren=0
for i in range(0,wow):
    ren=ren+zzz[i]
print("prediksi total biaya : "+str(ren))