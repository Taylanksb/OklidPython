import math

# Adım 1: Noktaları tanımla
noktalar = [(1, 2), (4, 6), (5, 3)]  # Örnek noktalar

# Adım 2: Öklid mesafesini hesaplayan bir fonksiyon yaz
def oklidMesafesi(nokta1, nokta2):
    return math.sqrt((nokta2[0] - nokta1[0]) ** 2 + (nokta2[1] - nokta1[1]) ** 2)

# Adım 3: Tüm nokta çiftleri arasındaki mesafeleri hesapla
mesafeler = []
for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):
        mesafe = oklidMesafesi(noktalar[i], noktalar[j])
        mesafeler.append(mesafe)

# Adım 4: Minimum mesafeyi bul ve yazdır
min_mesafe = min(mesafeler)
print(f"Minimum Öklid mesafesi: {min_mesafe}")