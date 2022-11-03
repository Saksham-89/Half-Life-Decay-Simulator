import numpy as np
import matplotlib.pyplot as plt   #dependencies

thalf = int(input("input your half life "))             #half life
lam = np.log(2)/thalf  #from equation
dp = lam               #decay probability
sp = 1 - dp            #survival probability

eq = "the equation is: "

N = int(input("inital number of atoms "))           #initial number of atomrs
time = int(input('time '))

def decay(N):
    count = []
    for t in range(time):
        r = np.random.random(N)
        survive = np.sum(r < sp)    #numver of atoms survived
        count.append(survive)
        N = survive                 #updated for next lop
    return count

print(eq + str(N)+" x "+"Ni "+"e^"+"-"+str(lam)+" x "+str(time))
print("Lambda is " + str(lam))

plt.plot(range(time), decay(N))
plt.show()



