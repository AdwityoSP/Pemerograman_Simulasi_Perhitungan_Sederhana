def mulai(pilih) :
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
    m = [ ] #(n.∑Xi^2)
    o = [ ] #array y^2
    p = [ ] #((∑Yi)(∑Xi^2))-((∑Xi)(∑XiYi))
    q = [ ] #((n.∑Xi^2)-((∑Xi)^2))
    r = [ ] #a = ((∑Yi)(∑Xi^2))-((∑Xi)(∑XiYi))/((n.∑Xi^2)-((∑Xi)^2))
    s = [ ] #(n.∑XiYi)
    t = [ ] #(∑Xi)(∑Yi)
    u = [ ] #(n(∑Xi))
    v = [ ] #((n.∑XiYi))-(∑Xi)(∑Yi))
    w = [ ] #((n(∑Xi))-(∑X(^2))
    z = [ ] #b = ((n.∑XiYi))-(∑Xi)(∑Yi))/((n(∑Xi))-(∑X(^2))
    aa = [ ] #∑Y^2
    bb = [ ] #∑X(^2)
    cc = [ ] #(n.∑Yi^2)
    dd = [ ] #(n.(∑Yi^2))-(∑Y(^2))
    ee = [ ] #((n.∑Xi^2)-(∑X(^2)*(n.(∑Yi^2)))-(∑Y(^2)))
    ff = [ ] #Rxy
    n = int(input("masukan jumlah n (minimal 2 titik): "))

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
        a = g[0]**2
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
            print("(n.(∑Xi^2)) ke- "+str(i+1)+" :"+str(a))
        

    def X10():
        a=k[0]-l[0]
        p.append(a)
        print("((∑Yi)(∑Xi^2))-((∑Xi)(∑XiYi)) "+str(a))

    def X11():
        for i in range(0,n):
            a=m[i]-h[0]
            q.append(a)
            print("((n.∑Xi^2)-(∑X(^2)) ke- "+str(i+1)+" :"+str(a))

    def X12():
        for i in range(0,n):
            a=float(p[0]/q[i])
            r.append(a)
            print("a ke-"+str(i+1) +":"+str(a))

    def X13():
        a=n*d[0]
        s.append(a)
        print("(n.∑XiYi) :"+str(a))

    def X14():
        a=g[0]*j[0]
        t.append(a)
        print("(∑Xi)(∑Yi) :"+str(a))

    def X15():
        a=n*g[0]
        u.append(a)
        print("n(∑Xi) :"+str(a))

    def X16():
            a=s[0]-t[0]
            v.append(a)
            print("((n.∑XiYi) - (∑Xi)(∑Yi))) :"+str(a))

    def X17():
        a=u[0]-h[0]
        w.append(a)
        print("((∑X(^2))-((∑Xi)^2)) :"+str(a))

    def X18():
        a=v[0]/w[0]
        z.append(a)
        print("b :"+str(a))

    def X19():
        if z[0]>0:
            a="+"
        else :
            a=""
        for i in range(0,n):    
            print("Y = "+str(r[i])+a+str(z[0])+"X")

    def X20():
        for i in range(0,n):
            a = y[i]**2
            o.append(a)
        b=sum(o)
        aa.append(b)
        print("∑Y^2 : "+str(b))

    def X21():
        for i in range(0,n):
            a = j[0]**2
            bb.append(a)
            print ("∑Y(^2) :"+str(a))

    def X22():
        for i in range(0,n):
            a=n*bb[i]
            cc.append(a)
            print("(n.(∑Yi^2)) ke- "+str(i+1)+" :"+str(a))

    def X23():
        for i in range(0,n):
            a=bb[0]-cc[i]
            dd.append(a)
            print("(n.(∑Yi^2))-(∑Y(^2))ke- "+str(i+1)+" :"+str(a))

    def X24():
        for i in range(0,n):
            a=q[i]-dd[i]
            ee.append(a)
            print("((n.∑Xi^2)-(∑X(^2)*(n.(∑Yi^2)))-(∑Y(^2))) ke- "+str(i+1)+" :"+str(a))

    def X25():
        for i in range(0,n):
            a=v[0]/ee[i]
            ff.append(a)
            print("Rxy ke- "+str(i+1)+" :"+str(a))


    def RL():
            X0()
            X1()
            X2()
            X3()
            X4()
            X5()
            X6()
            X7()
            X8()
            X10()
            X11()
            X12()
            X13()
            X14()
            X15()
            X16()
            X17()
            X18()
            X19()

    def KR() :
            X0()
            X1()
            X2()
            X3()
            X4()
            X5()
            X8()
            X11()
            X13()
            X14()
            X16()
            X20()
            X21()
            X22()
            X23()
            X24()
            X25()

    if pilih == '1' :
        RL()
    elif pilih == '2' :
        KR()
    else :
        print("nomor salah")

    print ("mulai lagi ?(Y/N)")
    lagi=str(input())
    if lagi==('Y'):
        pilihan()
        mulai(pilih)
    elif lagi==('N'):
        quit()

print("Aplikasi Regresi Linier & Korelasi Pearson")
print("Adwityo S.P 1520180Pemerograman Simulasi 1")
print("==========================================")
print("1.Regresi Linier")
print("2.Korelasi Pearson")
print("==========================================")

def pilihan():
    pilih = input("1/2 ?")
    return(pilih)

pilih=pilihan()
mulai(pilih)
