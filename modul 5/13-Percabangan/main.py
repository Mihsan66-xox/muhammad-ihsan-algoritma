# percabangan 
# struktur
"""
1. if -nya
2. punya kondisi
3. punya aksi

"""
nama = input("masukan nama: ")

# percabangan inline (satu baris)
if nama == "isan" : print("selamat datang")
print("lembo ade")

# percabangan indentasi
if nama == "isan":
    print("selamat datang")
    print("tabee'")

# percabangan 1 kondisi dan 2 aksi
# pakai kata kunci else

if nama == "isan":
    print("selamat datang")
else:
    print(f'Anda {nama}, bukan adam')
    print("terimakasih")