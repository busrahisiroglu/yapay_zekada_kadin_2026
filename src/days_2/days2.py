# diziler
sehir1 = "Edirne"
sehir2 = "Istanbul"
sehir3 = "Bursa"
sehir4 = "Tekirdağ"
sehir5 = "Kırklareli"
sehir6 = "Çanakkale"

# dizi ile şehirler
nufuslar = [419913, 15029231, 3056120, 1107819, 348020, 540000, 5503985]
plakalar = [22, 34, 16, 59, 39, 17, 6]
sehirler = ["Edirne", "Istanbul", "Bursa", "Tekirdağ", "Kırklareli", "Çanakkale", "Ankara"]
kisiler = ["Ahmet", "Mehmet", "Ayşe", "Fatma", "Ali", "Veli", "Zehra"]
#şehirler sorted() fonksiyonu ile sıralanır
# sirali_sehirler = sorted(sehirler)

# dizilerdeki elemanlara erişim
# index numarası 0'dan başlar
print( sehirler[0] )
print( kisiler[0] )

print("================================")
# for loop ile dizilerdeki elemanlara erişim
for sehir in sehirler:
    print(sehir)
print("================================")

for sehir in sehirler:
    if sehir == "Bursa":
        print("Bursa bulundu!")
        
print("================================")
tireKisiler = []
for kisi in kisiler:
    kisi = "-" + kisi
    tireKisiler.append(kisi) # append() fonksiyonu ile tireKisiler dizisine eklenir
print(tireKisiler)

print("================================")
# kisiler dizindeki her bir elemanı büyük harfe çevirir ve yeni bir dizi oluşturur
buyukKisiler = []
for kisi in kisiler:
    kisi = kisi.upper()
    buyukKisiler.append(kisi)
print(buyukKisiler)

print("================================")
# kisiler dizindeki her bir elemanın yanında karakter sayısını ekler ve yeni bir dizi oluşturur
kisilerKarakter = []
for kisi in kisiler:
    kisi = kisi + " (" + str(len(kisi)) + " karakter)"
    kisilerKarakter.append(kisi)
print(kisilerKarakter)

print("================================")
# sehirler dizindeki her bir elemanın yanında nufus ve plaka bilgilerini ekler
sehirBilgileri = []
for i in range(len(sehirler)):
    bilgi = sehirler[i] + " (Nüfus: " + str(nufuslar[i]) + ", Plaka: " + str(plakalar[i]) + ")"
    sehirBilgileri.append(bilgi)
print(sehirBilgileri)

print("================================")

# Dizi özellikleri
# dizi içindeki eleman sayısı
print("Sehirler dizisinin uzunluğu: ", len(sehirler))
# Bir dizi elamanın değerini değiştirme
sehirler[0] = "Zonguldak"
print(sehirler)

print("================================")
# dizi sıralaması utf-8 karakter sıralamasına göre sıralanır, türkçe karakteri dikkate alarak sırlamayı yap
import locale
locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')
sirali_sehirler = sorted(sehirler, key=locale.strxfrm, reverse=False)
print(sirali_sehirler)

print("================================")
# index numarası ile eleman ekleme
sehirler.insert(2, "Sakarya")
print(sehirler)

print("================================")
# karadeniz bölgesi şehirleri
karadeniz_sehirleri = ["Trabzon", "Rize", "Samsun", "Ordu", "Giresun"]
# sehirler dizisine karadeniz bölgesi şehirlerini ekleme
sehirler.extend(karadeniz_sehirleri)
sehirler.sort(key=locale.strxfrm)
print(sehirler)

print("================================")
# bir dizi elemanını silme
# sehirler.remove("Sakarya")
# print(sehirler)

silinecek_sehir = ["Sakarya", "Rize", "Ankara"]
for sehir in silinecek_sehir:
    if sehir in sehirler:
        sehirler.remove(sehir)
print(sehirler)

print("================================")
sehirler.clear() # sehirler dizisini temizler
print(sehirler)
