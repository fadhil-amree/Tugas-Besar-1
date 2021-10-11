#Program HitungJarak
#Menerima input kecepatan(m/s) dan waktu(s), lalu menghasilkan output jarak(m)

#KAMUS
# kecepatan, waktu, jarak : float

#ALGORITMA

kecepatan = float(input("Masukkan kecepatan(m/s): ")) #Input
waktu = float(input("Masukkan waktu(s): "))

jarak = kecepatan * waktu                             #Proses

print("Jarak yang ditempuh adalah:", jarak, "m")      #Output