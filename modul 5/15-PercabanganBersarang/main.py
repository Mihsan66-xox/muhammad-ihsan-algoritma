# percabangan bersarang / NESTED IF

# kalkulator
# +,-,x,/,mod,//,pangkat(exponen)

print(20*"=")
print("Kalkulator Sederhana")
print(20*"=")

angka_1 = float(input("masukan bilangan 1 = "))
operator = input("operator (+,-,x,/,mod,//,pangkat) = ")
print(f'hasilnya adalah = {angka_1}')

angka_2 = float(input("masukan bilangan  2 = "))
operator = input("operator (+,-,x,/,mod,//,pangkat) = ")
print(f'hasilnya adalah = {angka_2}')

# operator

if operator == '+':
    hasil = angka_1 + angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '-':
    hasil = angka_1 - angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == 'x':
    hasil = angka_1 * angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '/' :
    hasil = angka_1 / angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '%' or operator == 'mod':
    hasil = angka_1 % angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '//':
    hasil = angka_1 // angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '**':
    hasil = angka_1 ** angka_2
    print(f'hasilnya adalah = {hasil}')
