N = 4
K = 3
C = 0
a = 0

for i in range(0, K):
    if i > 0:
        a = (a + 1)*2
    for j in range(1, N + 1):
        if i + j == N:
            C = C + a + 1
print(C)