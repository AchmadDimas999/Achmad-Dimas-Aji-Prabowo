luastotal = 0
for x in range(100000):
    delta = 4 / 100000
    t1 = -((1+x*delta)**2) + 5*(1+x*delta) + 1
    t2 = -((1+(x+1)*delta)**2) + 5*(1+(x+1)*delta) + 1
    lebar = t2 - t1
    luas = lebar * t2
    luastotal = luastotal + luas

print("Total luas: ", luastotal)