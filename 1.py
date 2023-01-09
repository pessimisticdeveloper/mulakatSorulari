def program():
    toplam = 0 # toplamı 0 eşitledim
    for i in range(0, 1000000): # 1 milyondan küçük sayılar için döngü başlattım. doğal sayı dediği için 0'da aldım.
      if all(i % j > 0 for j in [2, 3, 5]):  # i'nin asal çarpanlar 2,3 ve 5 ten oluştuğu için if ile kontrol ettim
        toplam += i # i'yi toplama ekledim
    return toplam # toplamı return ettim

print("Cevap: ",program()) # 133332666668