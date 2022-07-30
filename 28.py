f = open("27_B (1).txt")
n=int(f.readline())
l=1000000000
m=0
s=0
k=43

first = [-1]*k
firstsum = [-1]*k
firstsum[0] = 0
first[0] = -1

for i in range(n):
    s += int(f.readline())
    r=s%k
    if firstsum[r] < 0:
        firstsum[r] = s
        first[r] = i
    else:
        mym = s - firstsum[r]
        myl = i - first[r]

        if mym > m:
            m=mym
            l=myl
        elif mym == m:
            if myl < l:
                l = myl

print(l)

