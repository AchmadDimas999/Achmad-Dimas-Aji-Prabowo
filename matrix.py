matriksC = [ [21, 22, 23, 24,20], 
             [5, 6, 7, 8, 19], 
             [9, 10, 11, 12, 18], 
             [13, 14, 15, 16, 17] ]

print(matriksC[2][2])

for baris in range(len(matriksC)): #4
    for kolom in range(len(matriksC[baris])): #5
        print(matriksC[baris][kolom], end=" ")
    print()

luastotal = 0
delta = 1
for x in range(1,4,1):
    t = -(x**2) + 5*x + 1
    luas = t * delta
    luastotal = luastotal + luas