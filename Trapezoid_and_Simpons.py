import numpy as np
import matplotlib.pyplot as plt


def func(x):
    Cme = 5*(10**(-4))
    a = 6.73*x+6.725*(10**(-8))+7.26*(10**(-4))*Cme
    b = 3.62*(10**(-12))*x+3.908*(10**(-8))*x*Cme
    return -a/b


def trapezoid(n, lower, upper):
    mul = (upper-lower)/(2*n)
    sum = func(upper)+func(lower)
    h = (upper-lower)/n
    for i in range(1, n, 1):
        sum += 2*func(lower+i*h)
    return sum*mul


def simpons(n, lower, upper):
    mul = (upper-lower)/(3*n)
    sum = func(upper)+func(lower)
    h = (upper-lower)/n
    for i in range(1, n, 2):
        sum += 4*func(lower+i*h)
    for i in range(2, n-1, 2):
        sum += 2*func(lower+i*h)
    return sum*mul


ini_oxy = 1.22*10**(-4)
in_n = int(input("No of segment: "))

print("\t\t Trapezoidal Rule ")
print("\t", "Result ", "\t\t", "Error")
for i in range(1, in_n+1, 1):
    curr = trapezoid(i, ini_oxy*0.75, ini_oxy*0.25)
    if i == 1:
        error = "No error calculation"
        print("n: ", i, "\t", curr, "\t", error)
    else:
        prv = trapezoid(i-1, ini_oxy*0.75, ini_oxy*0.25)
        error = abs(curr - prv)*100/curr
        print("n: ", i, "\t", curr, "\t", error, "%")

print("\t\t Simpons 1/3 Rule ")
print("\t", "Result ", "\t\t", "Error")
for i in range(2, 2*(in_n+1), 2):
    curr = simpons(i, ini_oxy*0.75, ini_oxy*0.25)
    if i == 2:
        error = "No error calculation"
        print("n: ", i, "\t", curr, "\t", error)
    else:
        prv = simpons(i-2, ini_oxy*0.75, ini_oxy*0.25)
        error = abs(curr - prv)*100/curr
        print("n: ", i, "\t", curr, "\t", error, "%")

x = np.array([1.22, 1.20, 1.0, 0.8, 0.6, 0.4, 0.2])*(10**-4)
y = []
for i in x:
    y.append(simpons(10, ini_oxy, i))
y = np.array(y)
plt.title("Time Vs Concentration")
plt.xlabel("Concentration")
plt.ylabel("Time")
plt.plot(x, y, "go")
plt.plot(x, y)
plt.grid()
plt.show()
