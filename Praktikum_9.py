#### kegiatan 1

berkas = open("L200180153","w")
berkas.write("L200180153 \n")
berkas.write("02-01-2000 \n")
berkas.write("Anita Lusi Romadhon \n")
berkas.close()

#### Kegiatan 2.Membaca berkas teks
berkas = open('L200180153','r')
NIM = berkas.readline()
Tanggal = berkas.readline()
Nama = berkas.readline()
ttlmm = "01/02/2000 \n"
kota = "Sragen "
berkas.close()


berkas = open('L200180153','w')
berkas.write (Nama)
berkas.write (kota)
berkas.write (ttlmm)
berkas.write (NIM)
berkas.close()

## Kegiatan 3,4.

import shelve
C = open("L200180153","r")
D = shelve.open("anita.data")
D["berkas"] = C.read()
D.close()
C.close()

D = shelve.open("anita.data")
print(D["berkas"])
D.close()
