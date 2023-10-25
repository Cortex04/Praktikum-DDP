print("1")

Kendaraan = ["zx25rr", "motor", "250cc", "Hijau", 2]
Kendaraan.append("125jt, Sport")
Kendaraan.insert(1, "Kawasaki")

print(Kendaraan)

print("2")

print("1. Menghitung Luas Persegi")
print("2. Menghitung Luas Lingkaran")
print("3. Menghitung Luas Segitiga")

Rumus = int(input ("Tentukan pilihan anda :"))

match Rumus:
        case 1:
            sisi = float(input("Masukkan panjang sisi persegi: "))
            luas = sisi * sisi
            print("Luas persegi adalah", luas)
        case 2:
            jari = float(input("Masukkan jari-jari lingkaran: "))
            luas = 3.14 * jari * jari
            print("Luas lingkaran adalah", luas)
        case 3:
            alas = float(input("Masukkan alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            luas = 0.5 * alas * tinggi
            print("Luas segitiga adalah", luas)
        case _:
            print("Pilihan tidak valid")