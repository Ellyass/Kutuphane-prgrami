import time

from kütüphane import *

print("""
*************************************
Kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Kitapları Göster 

2. Kitapları Sorgulama

3. Kitap EKle

4. Kitap Sil

5.Baskı Yükselt

Çıkmak için 'q' ya basın.
*************************************
""")

kutuphane = Kutuphane()

while True:
    islem = input("Yapacağınız işlemi seçiniz:")


    if islem == "q":
        print("Program Sonlanıyor")
        print("Yine Bekleriz")
        break

    elif islem == "1":
        kutuphane.kitaplari_goster()

    elif islem == "2":
        isim = input("Hangi Kitabı istiyorsunuz :")
        print("Kitap Sorgulanıyor...")
        time.sleep(2)

        kutuphane.kitap_sorgula(isim)

    elif islem == "3":
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayinevi = input("Yayınevi:")
        tur = input("Tür:")
        baski = int(input("Baskı:"))

        yeni_kitap = Kitap(isim, yazar, yayinevi, tur, baski)

        print("Kitap ekleniyor...")
        time.sleep(2)

        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap Eklendi...")

    elif islem == "4":
        isim = input("Hangi Kitabı silmek istiyorsunuz :")

        cevap = input("Emin misiniz ??? (E/H):")

        if cevap == "E" or cevap == "e":
            print("Kitap Sİliniyor")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap Silindi....")

    elif islem == "5":
        isim = input("Hangi Kitabın baskısını yükseltmek istiyorsunuz :")
        print("Baskı Yükseltiliyor....")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        print("Baskı Yükseltildi.")
    else:
        print("Geçersiz İşlem....")
