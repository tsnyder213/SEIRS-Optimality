import matplotlib.pyplot as plt
import numpy as np

bmin = 0.05
bmax = 0.25
mu=0.97
tau=0.13
gamma=0.05

def beta(ut):
    return (ut*(bmin - bmax))+bmax

def interaction(I,S,E,beta,ut):
    return round((beta(ut)*S*I)/(S+I+E))

def Iplus(I,S,E,beta,gamma,ut):
    return I+round(mu*E)-round(gamma*I)-round(tau*I)

def Splus(I,S,E,beta,ut):
    return S-round(interaction(I,S,E,beta,ut)) + round(tau*I)

def Eplus(I,S,E,beta,ut):
    return E + round(interaction(I,S,E,beta,ut)) - round(mu*E)

def objective(ut,I,S,E,beta,gamma,CI):
    return interaction(I,S,E,beta,ut)*CI + (ut*((I+S+E)/(I+1)))

def opt(I,S,E,nbut,beta,gamma,CI):
    best=None
    for ut in [i*(0.20/nbut) for i in range(nbut+1)]:
        v=objective(ut,I,S,E,beta,gamma,CI)
        if best is None or v<best:
            best = v
            utopt = ut
    return [best,utopt]

def dp(I0=100,S0=395,T=60,gamma=0.05,CI=0.85,E0=5):
    V=[0]
    I=[I0]
    S=[S0]
    E=[E0]
    Ut=[]
    nbut = 1
    for i in range(1,T+1):
        [t,ut] = opt(I[i-1],S[i-1],E[i-1],nbut,beta,gamma,CI)
        V.append(V[i-1]+t)
        Ut.append(ut)
        I.append(Iplus(I[i-1],S[i-1],E[i-1],beta,gamma,ut))
        S.append(Splus(I[i-1],S[i-1],E[i-1],beta,ut))
        E.append(Eplus(I[i-1],S[i-1],E[i-1],beta,ut))
    return [V,I,S,E,Ut]

[V,I,S,E,Ut]=dp()
print("T, V, I, S, E, ut")
for i in range(60):
    print("{0:2d}, {1:6.1f}, {2:6.2f}, {3:6.2f}, {4:6.2f}, {5:6.2f}".format(i,V[i],I[i],S[i],E[i],Ut[i]))

x = list(range(0,60))
y = Ut[0:60]
y2 = I[0:60]

plt.figure()
plt.xticks(np.arange(min(x), max(x)+5, 5.0))
plt.yticks(np.arange(0, max(y)+1, 0.02))
plt.step(x, y)
plt.ylabel('Rate of Vaccination')
plt.xlabel('Time Steps')
plt.figure()
plt.xticks(np.arange(min(x), max(x)+5, 5.0))
plt.yticks(np.arange(0, max(y2)+1, 5.0))
plt.step(x, y2)
plt.ylabel('Infected Individuals')
plt.xlabel('Time Steps')
plt.show()

SNQ = S

INQ = I
