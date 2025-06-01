import numpy as np


def GaussianElimination(A, B, pivot=True, showall=True):
    n = len(B)
    x = np.zeros(n, float)
    # pertial pivoting
    if pivot == True:
        for i in range(n):
            sw = i
            # for j in range(i+1, n):
            #     if abs(A[i][i]) < abs(A[j][i]):
            #         A[[i, j]] = A[[j, i]]
            #         B[i], B[j] = B[j], B[i]
            for j in range(i+1, n):
                if abs(A[sw][i]) < abs(A[j][i]):
                    sw = j
            A[[i, sw]] = A[[sw, i]]
            B[i], B[sw] = B[sw], B[i]
    # forward elemination
    for i in range(n-1):
        for j in range(i+1, n):
            if A[j, i] == 0:
                continue
            factor = A[j, i]/A[i, i]
            A[j] = A[j]-A[i]*factor
            B[j] = B[j]-B[i]*factor
        if showall == True:
            print(A)
            print(B)
    # determinant of the coefficient matrix A
    if showall == True:
        print("%.4f" % np.linalg.det(A))
    # back substitution
    x[n-1] = B[n-1]/A[n-1, n-1]
    for i in range(n-2, -1, -1):
        sum = B[i]
        for j in range(n-1, i, -1):
            sum -= A[i, j]*x[j]
        x[i] = sum/A[i, i]
    return x


n = int(input())
arr = np.array([[0]*n]*n, float)
for i in range(n):
    a = input()
    a = a.split()
    for j in range(n):
        arr[i, j] = a[j]

brr = np.array([0]*n, float)
for i in range(n):
    a = float(input())
    brr[i] = a
if np.linalg.det(arr) == 0:
    print("No solution or infinite solution")
else:
    x = GaussianElimination(arr, brr, True, False)
    for i in range(n):
        print("%.4f" % x[i])
