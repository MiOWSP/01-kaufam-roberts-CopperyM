def calc_x(V,M,a,t):
    x=[1]*(V+1)
    for n in range (1,V+1):
        sum=0
        for i in range (0,M):
            if n>=t[i]:
                sum+=a[i]*t[i]*x[n-t[i]]
        x[n]=sum/n
    i = 0
    for item in x:
        print("x{}={}".format(i,item))
        i +=1
    return x

def calc_po(x):
    sum=0
    for item in x:
        sum+=item
    return 1/sum

def calc_pn(x,V,M,a,t):
    p=[1]*(V+1)
    p[0]=calc_po(x)
    for n in range (1,V+1):
        sum=0
        for i in range (0,M):
            if n>=t[i]:
                sum+=a[i]*t[i]*p[n-t[i]]
        p[n]=sum/n
    i=0
    for item in p:
        print("p{}={}".format(i,item))
        i +=1
    print("b0={}".format(p[len(p)-1]))
    return p
    
def calc_b(V,P,t,i=1):
    sum=0
    for n in range(V-t[i-1]+1,V+1):
        sum+=P[n]
    print("b1={}".format(sum))
    return sum

def run_all():
    a=[]
    t=[]
    V=int(input("Podaj V: "))
    M=int(input("Podaj M: "))
    for x in range(0,2):
        print("Podaj wartosc a{}:".format(x), end='')
        p = float(input())
        a.append(p)
    for x in range(0,2):
        print("Podaj wartosc t{}:".format(x), end='')
        p = int(input())
        t.append(p)
    x=calc_x(V,M,a,t)
    calc_po(x)
    P=calc_pn(x,V,M,a,t)
    calc_b(V,P,t,2)

run_all()