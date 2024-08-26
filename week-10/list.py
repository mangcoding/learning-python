listmahasiswa = []

mahasiswaA = {
    "nama": "Budi",
    "nomer_hp": "08123456789",
    "email": "budi@nusaputra.ac.id",
    "alamat": "Jl. Kebon Jeruk No. 123",
}

mahasiswaB = {
    "name": "Jojo",
    "nomer_hp": "08123457779",
    "email": "jojo@nusaputra.ac.id",
    "alamat": {
        "jalan": "Jl. Kebon Jeruk No. 123",
        "kota": "Jakarta",
        "provinsi": "DKI Jakarta",
    },
}

listmahasiswa.append(mahasiswaA)
listmahasiswa.append(mahasiswaB)

print(listmahasiswa[-1]["alamat"])