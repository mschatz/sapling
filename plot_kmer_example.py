import matplotlib.pyplot as plt
import operator

s = 'CATATAGA'

n = len(s)

ss = [s[i:] for i in range(0, n)]
ss = sorted(ss)
sa = [0 for i in range(0, n)]
for i in range(0, n):
    sa[n - len(ss[i])] = i

k = 3

points = []

for i in range(0, n - k + 1):
    kmer = 0
    for j in range(0, k):
        kmer *= 4
        c = s[i+j]
        if c == 'A':
            kmer += 0
        if c == 'C':
            kmer += 1
        if c == 'G':
            kmer += 2
        if c == 'T':
            kmer += 3
    points.append((kmer, sa[i]))
print(points)
points.sort(key=lambda x: x[1])
print(points)
xs = [x[0] for x in points]
ys = [x[1] for x in points]
plt.plot(xs, ys)
plt.savefig('kmer_example.png')
            
