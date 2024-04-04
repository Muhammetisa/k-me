import numpy as np
import pandas as pd

# Verilen örnekler
veriler = np.array([15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65])

# Başlangıç küme merkezleri
c1 = 16
c2 = 22

# İterasyon sayısı
iterasyon_sayısı = 4

# Tablo oluşturma
tablo = []

# Her iterasyonda işlem yapma
for iterasyon in range(iterasyon_sayısı):
    # Örneklerin hangi kümelere ait olduğunu belirleme
    kume1 = []
    kume2 = []
    for veri in veriler:
        distance1 = abs(veri - c1)
        distance2 = abs(veri - c2)
        if distance1 < distance2:
            kume1.append(veri)
        else:
            kume2.append(veri)
    
    # Yeni küme merkezlerini hesaplama
    yeni_c1 = np.mean(kume1)
    yeni_c2 = np.mean(kume2)
    
    # Tabloyu güncelleme
    tablo.append([c1, c2, kume1, kume2])
    
    # Yeni küme merkezlerini atama
    c1 = yeni_c1
    c2 = yeni_c2

# Sonuçları DataFrame'e yükleme
df = pd.DataFrame(tablo, columns=['c1', 'c2', 'Küme 1', 'Küme 2'])

# DataFrame'i ekrana yazdırma
print(df)
