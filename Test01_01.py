#sdnfs,dmfns,fnsm

g = 'aaaabbcaa' #input()
gl = g.lower()
i = 0
s = 0
x = 0
res = ''

while s < len(gl):
    j = gl[s]
    while (len(gl) > i) and  (j == gl[i]):
        i+=1
    res += j + str(i-s)
    s = i 
print(res)
print(len(gl))