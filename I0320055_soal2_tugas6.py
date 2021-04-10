print("-----PROGRAM PENGHITUNG RATA-RATA-----")
banyak_data = int(input("Masukkan banyaknya data: "))
data = []
jumlah = 0
for i in range(0, banyak_data):
    nodata = int(input("Masukkan data ke-%d: " % (i+1)))
    data.append(nodata)
    jumlah += data[i]
    rata = float(jumlah/banyak_data)
print("Nilai rata-ratanya adalah: ", rata)