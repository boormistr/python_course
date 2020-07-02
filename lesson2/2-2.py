swapping = list(input().split())
n = len(swapping) - len(swapping) % 2
print(swapping)
for i in range(0, n, 2):
    swapping[i], swapping[i+1] = swapping[i+1], swapping[i]
print(swapping)