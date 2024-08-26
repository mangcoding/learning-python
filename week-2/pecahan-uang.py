uang = float(input("Masukkan jumlah uang: "))

sisa_100ribu = uang%100_000
uang_pecahan_100ribu = uang // 100_000
sisa50ribu = uang%50_000
uang_pecahan_50ribu = sisa_100ribu // 50_000
sisa20ribu = sisa50ribu%20_000
uang_pecahan_20ribu = sisa50ribu // 20_000
sisa10ribu = sisa20ribu%10_000
uang_pecahan_10ribu = (sisa20ribu-sisa10ribu) / 10_000
sisa5ribu = sisa10ribu%5_000
uang_pecahan_5ribu = (sisa10ribu-sisa5ribu) / 5_000
sisa2ribu = sisa5ribu%2_000
uang_pecahan_2ribu = (sisa5ribu-sisa2ribu) / 2_000
sisa1ribu = sisa2ribu%1_000
uang_pecahan_1ribu = (sisa2ribu-sisa1ribu) / 1_000
sisa500 = sisa1ribu%500
uang_pecahan_500 = (sisa1ribu-sisa500) / 500

print("Uang",uang)
print("100.000: ", uang_pecahan_100ribu)
print("50.000: ", uang_pecahan_50ribu)
print("20.000: ", uang_pecahan_20ribu)
print("10.000: ", uang_pecahan_10ribu)
print("5.000: ", uang_pecahan_5ribu)
print("2.000: ", uang_pecahan_2ribu)
print("1.000: ", uang_pecahan_1ribu)
print("500: ", uang_pecahan_500)