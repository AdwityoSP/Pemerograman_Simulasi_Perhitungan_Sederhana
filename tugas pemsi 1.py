x = [ ] #array x
y = [ ] #array Y
c = [ ] #array x*y
d = [ ] #∑x*y
e = [ ] #array x^2
f = [ ] #∑X^2
g = [ ] #∑X
h = [ ] #∑X(^2)
j = [ ] #∑Y
k = [ ] #(∑Yi)(∑Xi^2)
l = [ ] #(∑Xi)(∑XiYi)
m = [ ] #(n ∑Xi^2)
o = [ ] #(∑Xi)^2
p = [ ] #((∑Yi)(∑Xi^2))-((∑Xi)(∑XiYi))
q = [ ] #((n ∑Xi^2)-((∑Xi)^2))
r = [ ] #hasil

n = int(input("masukan jumlah n : "))

def X0() :
     
    for i in range(0, n): 
        a = int(input("masukan jumlah x ke-"+str(i+1)+" :")) 
        x.append(a)
        b = int(input("masukan jumlah y ke-"+str(i+1)+" :")) 
        y.append(b) 

def X1():
    print("X : "+str(x))
    print("Y : "+str(y))    
    print("n : "+str(n))

def X2():
    a=sum(x)
    b=sum(y)
    print("∑X : "+str(a))
    print("∑Y : "+str(b))
    g.append(a)
    j.append(b)

    
def X3():
    for i in range(0,n):
        a = x[i]*y[i] 
        c.append(a)
    b=sum(c)
    d.append(b)
    print("∑XY : "+str(b))

def X4():
    for i in range(0,n):
        a = x[i]**2
        e.append(a)
    b=sum(e)
    f.append(b)
    print("∑X^2 : "+str(b))    

def X5():
    a = g[0]*g[0]
    h.append(a)
    print ("∑X(^2) :"+str(a))

def X6():
    a=j[0]*f[0]
    k.append(a)
    print ("(∑Yi)(∑Xi^2) : "+str(a))

def X7():
    a=g[0]*d[0]
    l.append(a)
    print ("(∑Xi)(∑XiYi) : "+str(a))

def X8():
    for i in range(0,n):
        a=n*e[i]
        m.append(a)
        print("n.(∑Xi^2) : "+str(a))
    

def X9():
    a=g[0]**2
    o.append(a)
    print("(∑Xi)^2 : "+str(a))

def X10():
    a=k[0]-l[0]
    p.append(a)
    print("((∑Yi)(∑Xi^2))-((∑Xi)(∑XiYi)) : "+str(a))

def X11():
    for i in range(0,n):
        a=m[i]-o[0]
        q.append(a)
        print("((n ∑Xi^2)-((∑Xi)^2)) : "+str(a))

def X12():
    for i in range(0,n):
        a=float(p[0]/q[i])
        r.append(a)
        print("a ke-"+str(i+1) +":"+str(a))

X0()
X1()
X2()
X3()
X4()
X5()
X6()
X7()
X8()
X9()
X10()
X11()
X12()