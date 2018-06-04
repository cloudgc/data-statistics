import numpy as np

ndarry = np.array([[35, 20, 66], [23, 67, 89], [13, 244, 67]], np.int32)

print(ndarry.shape, ndarry.size)
print(ndarry.dtype)
print(ndarry[1:2, 1:2])

sdarry = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(sdarry[1, 2])
print(sdarry[:, 2])
print(sdarry[2, :])

print(sdarry.mean(), sdarry.mean(axis=1), sdarry.mean(axis=0))

print(sdarry[0, :].mean())
