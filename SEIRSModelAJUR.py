import matplotlib.pyplot as plt

uq = 0
bmin = 0.05
bmax = 0.25

def beta(uv):
    return (uv*(bmin - bmax))+bmax
# (+ *bmax* (* u (- *bmin* *bmax*))))

def interaction(I,S,beta,uv,uq):
    return round((beta(uv)*S*((1- 0.03)*I))/((S+I)*1.02))
    #return round((beta(uv)*S*((1- 0.05) * I)*(1-uv)*(1-uq))/((S+I)*1.02))

def Iplus(I,S,beta,gamma,uv,uq):
    return round(I+interaction(I,S,beta,uv,uq)-gamma*((1 - 0.03) *I) - uq*I - 0.13 * ((1- 0.03) * I))

def Splus(I,S,beta,uv,uq):
    return round(S-interaction(I,S,beta,uv,uq) + 0.13*((1 - 0.03) * I))

def objective(uv,uq,I,S,beta,gamma,CI,Cq):
    return round(interaction(I,S,beta,uv,uq)*CI + uv*(((I+S)*1.02)/(I+1)))

def opt(I,S,nbuv,nbuq,beta,gamma,CI,Cq):
    best=None
    for uv in [i*(0.2/nbuv) for i in range(nbuv+1)]:
        for uq in [i*(0.0/nbuq) for i in range(nbuq+1)]:
            v=objective(uv,uq,I,S,beta,gamma,CI,Cq)
            if best is None or v<best:
                best = v
                uvopt = uv
                uqopt = uq
    return [best,uvopt,uqopt]

def dp(I0=100,S0=400,T=60,gamma=0.05,CI=0.85,Cq=0):
    V=[0]
    I=[I0]
    S=[S0]
    Uv=[]
    Uq=[]
    nbuv,nbuq = 1,1
    for i in range(1,T+1):
        [v,uv,uq] = opt(I[i-1],S[i-1],nbuv,nbuq,beta,gamma,CI,Cq)
        V.append(V[i-1]+v)
        Uv.append(uv)
        I.append(Iplus(I[i-1],S[i-1],beta,gamma,uv,uq))
        S.append(Splus(I[i-1],S[i-1],beta,uv,uq))
    return [V,I,S,Uv,Uq]

[V,I,S,Uv,Uq]=dp()
print("T, V, I, S, uv")
for i in range(60):
    print("{0:2d}, {1:6.1f}, {2:6.2f}, {3:6.2f}, {4:6.2f}".format(i,V[i],I[i],S[i],Uv[i]))

x = list(range(0,60))
y = Uv[0:60]
y2 = I[0:60]
plt.plot(x, y)
plt.show()

SNQ = S

INQ = I

