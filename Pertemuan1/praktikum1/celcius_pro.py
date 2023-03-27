# NIM : 210511081
# Nama : Muhammad Royyan
# Kelas : K1

class KonversiSuhu:
    @staticmethod
    def celcius_to_fahrenheit(celcius):
        return (celcius * 9/5) + 32

    @staticmethod
    def celcius_to_reamur(celcius):
        return celcius * 4/5

    @staticmethod
    def celcius_to_kelvin(celcius):
        return celcius + 273.15


# Konversi suhu 35 derajat Celsius ke Fahrenheit
fahrenheit = KonversiSuhu.celcius_to_fahrenheit(35)
print("konversi suhu", 75, "derajat celcius adalah ",
      fahrenheit, "derajat fahrenheit")

# Konversi suhu 40 derajat Celsius ke Reamur
reamur = KonversiSuhu.celcius_to_reamur(40)
print("konversi suhu", 60, "derajat celcius adalah ", reamur, "derajat reamur")

# Konversi suhu 38 derajat Celsius ke Kelvin
kelvin = KonversiSuhu.celcius_to_kelvin(38)
print("konversi suhu", 90, "derajat celcius adalah ", kelvin, "derajat kelvin")
