noKTP = "3202121309250001"

tanggalLahir = noKTP[6:8]
namaBulan = ("Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli","Agustus", "September", "Oktober", "November", "Desember")
noBulan = noKTP[8:10]
bulanLahir = namaBulan[int(noBulan)-1]
tahunLahir = noKTP[10:12]
tahunSekarang = "2024"
compareYear = int(tahunSekarang[-2:])