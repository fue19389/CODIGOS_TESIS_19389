import os.path
import numpy as np
from matplotlib import pyplot as plt


# Listas de landmarks encontradas en: https://pythonrepo.com/repo/k-m-irfan-simplified_mediapipe_face_landmarks
lebw = [70,63,105,66,107,55,65,52,53,46]
rebw = [300,293,334,296,336,285,295,282,283,276]
le = [33,246,161,160,159,158,157,173,133,155,154,153,145,144,163,7]
re = [263,466,388,387,386,385,384,398,362,382,381,380,374,373,390,249]
ilip = [78,191,80,81,82,13,312,311,310,415,308,324,318,402,317,14,87,178,88,95]
olip = [61,185,40,39,37,0,267,269,270,409,291,375,321,405,314,17,84,181,91,146]
fcontour = [10,338,297,332,284,251,389,356,454,323,361,288,397,365,379,378,400,377,152,148,176,149,150,136,172,58,132,93,234,127,162,21,54,103,67,109]

admat = np.zeros((468, 468))

for i in lebw:
    for j in lebw:
        admat[i, j] = 1
        admat[j, i] = 1
for i in rebw:
    for j in rebw:
        admat[i, j] = 1
        admat[j, i] = 1
for i in le:
    for j in le:
        admat[i, j] = 1
        admat[j, i] = 1
for i in re:
    for j in re:
        admat[i, j] = 1
        admat[j, i] = 1
for i in ilip:
    for j in ilip:
        admat[i, j] = 1
        admat[j, i] = 1
for i in olip:
    for j in olip:
        admat[i, j] = 1
        admat[j, i] = 1
for i in fcontour:
    for j in fcontour:
        admat[i, j] = 1
        admat[j, i] = 1
print(admat)
plt.imshow(admat)
plt.ylim(0, 467)
plt.xlim(0, 467)
plt.show()

print(admatlip)
plt.imshow(admatlip)
plt.ylim(0, 51)
plt.xlim(0, 51)
plt.show()

expordir = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS'
expordir = os.path.join(expordir, 'admat')
np.save(expordir, admat)
expordir = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS'
expordir = os.path.join(expordir, 'admatlip')
np.save(expordir, admatlip)
print(admat.shape)
print(admatlip.shape)

