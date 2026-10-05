a = int(input("Masukkan nilai A: "))
b = int(input("Masukkan nilai B: "))
operation = (input("Pilih Operasi *,/,+,-: "))

if operation == "+":
    penjumlahan = a+b
    print("Hasil Perhitungan: " + penjumlahan)
elif operation == "-":
    pengurangan = a-b
    print("Hasil Perhitungan: " + pengurangan)
elif operation == "*":
    perkalian = a*b
    print("Hasil Perhitungan: " + perkalian)
elif operation == "/":
    pembagian = a/b
    print("Hasil Perhitungan: " + pembagian)