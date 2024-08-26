gajiPokok = float(input("Masukkan gaji pokok: "))
uangTransportPerHari= float(input("Masukkan Uang Transport per hari: "))
uangMakanPerHari= float(input("Masukkan Uang Makan per hari: "))
tunjanganJabatan= float(input("Masukkan Tunj. Jabatan: "))
hariKerja= int(input("Masukkan hari kerja: "))
jamLembur1_5x= int(input("Masukkan jam lembur pertama: "))
jamLembur2_x= int(input("Masukkan jam lembur extra: "))

honorTransport = uangTransportPerHari*hariKerja
uangMakan = uangMakanPerHari*hariKerja
honorPerjam = 1/173*gajiPokok
honorLembur1_5 = jamLembur1_5x*1.5*honorPerjam 
honorLembur2_x = jamLembur2_x*2*honorPerjam
uangTransport = uangTransportPerHari*hariKerja
honorLembur = honorLembur1_5+honorLembur2_x

totalGaji = gajiPokok+uangTransport+uangMakan+tunjanganJabatan+honorLembur

totalGaji = 10000000
print("Total Gaji: ", totalGaji)