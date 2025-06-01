import matplotlib.pyplot as plt
import numpy as np


def func(x):
    return x ** 3 - 18 * x ** 2 + 475.2


def devfunc(x):
    return 3*x**2 - 36*x


def bisection(lower_bound, upper_bound, approximation_error, max_iteration):
    middle = (lower_bound+upper_bound)/2
    old_middle = middle
    if func(lower_bound)*func(middle) > 0:
        lower_bound = middle
    elif func(upper_bound)*func(middle) > 0:
        upper_bound = middle
    else:
        return middle
    for i in range(max_iteration-1):
        middle = (lower_bound+upper_bound)/2
        print("Percentage of Error in ", i+1, " iteration ",
              abs(middle-old_middle)*100/middle)
        if func(lower_bound)*func(middle) > 0:
            lower_bound = middle
        elif func(upper_bound)*func(middle) > 0:
            upper_bound = middle
        else:
            return middle
        if abs(middle-old_middle)*100/middle <= approximation_error:
            break
        old_middle = middle
    return middle

print("Using bisection method")
print("Answer: ", bisection(0, 12, 0.5, 20))


def newtonrapson(initial_guess, approximation_error, max_iteration):
    for i in range(max_iteration):
        answer = initial_guess - \
            func(initial_guess)/devfunc(initial_guess)
        print("Percentage of Error in ", i+1, " iteration ",
              abs(answer-initial_guess)*100/answer)
        if abs(answer-initial_guess)*100/answer <= approximation_error:
            break
        initial_guess = answer
    return answer

print("Using Newton-Rapson method")
print("Answer: ", newtonrapson(6, 0.5, 20))

x = np.linspace(0, 12, 100)
y = func(x)
plt.plot(x, y)
plt.yticks([0])
plt.grid()
plt.show()
