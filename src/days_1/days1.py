print("Merhaba Python!") # Mesajı ekrana yazdırır

# Değişkenler
sayi1 = 10
sayi2 = 5
toplam = sayi1 + sayi2
print("Toplam:", toplam) # Toplamı ekrana yazdırır

# string ifadesi
isim = "Ahmet"
soyisim = "Yılmaz"
tam_isim = isim + " " + soyisim
print("Tam İsim:", tam_isim) # Tam ismi ekrana yazdırır

# ondalık sayılar
pi = 3.14
yaricap = 5
cevre = 2 * pi * yaricap
print(f"Çevre: {cevre:.2f}") # Çevreyi ekrana yazdırır, 2 ondalık basamak gösterir

# boolean ifadeler
# if yazarken True veya False kullanılır
cevap = False

# karar verme
# büyük mü?
cevap = sayi1 > sayi2 # sayı1'in sayı2'den büyük olup olmadığını kontrol eder ve sonucu cevap değişkenine atar
print("Sayı1, Sayı2'den büyük mü?", cevap) # Karar sonucunu ekrana yazdırır

# küçük mü?
cevap = sayi1 < sayi2 # sayı1'in sayı2'den küçük olup olmadığını kontrol eder ve sonucu cevap değişkenine atar
print("Sayı1, Sayı2'den küçük mü?", cevap) # Karar sonucunu ekrana yazdırır

# eşit mi?
cevap = sayi1 == sayi2 # sayı1'in sayı2'ye eşit olup olmadığını kontrol eder ve sonucu cevap değişkenine atar
print("Sayı1, Sayı2'ye eşit mi?", cevap) # Karar sonucunu ekrana yazdırır

# kullanıcı adı şifre kontrolü
kullanici_adi = "admin"
sifre = "12345"

giris_kullanici_adi = input("Kullanıcı Adı: ") # Kullanıcıdan kullanıcı adı girmesini ister
giris_sifre = input("Şifre: ") # Kullanıcıdan şifre girmesini ister

cevap = (giris_kullanici_adi == kullanici_adi) and (giris_sifre == sifre) # Girilen kullanıcı adı ve şifrenin doğru olup olmadığını kontrol eder
print("Giriş Başarılı mı?", cevap) # Giriş sonucunu ekrana yazdırır

# if karar kontrol yapısı
if cevap: # Eğer cevap True ise
    print("Hoşgeldiniz!") 
else: # Eğer cevap False ise
    print("Giriş Başarısız!, Tekrar deneyin.")