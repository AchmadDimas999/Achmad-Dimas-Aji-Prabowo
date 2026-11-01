
nama_tamu = ["Fikri", "Afif", "Fadhil"]
nama_tamu.append('Rafel')

print('Saya hanya bisa mengundang dua orang untuk makan malam.')
while len(nama_tamu) > 2:
    tamu = nama_tamu.pop()
    print(f'Maaf {tamu}, saya tidak bisa mengundang Anda untuk makan malam.')

for tamu in nama_tamu:
    print(f'{tamu}, Anda tetap diundang untuk makan malam.')

del nama_tamu[0:2]
print(nama_tamu)
