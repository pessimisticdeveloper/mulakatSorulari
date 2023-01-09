def program(milyon):
    x, y = 0, 1     # ilk iki fibonnaci sayısını aldım
    toplam = 0      # toplamı 0'a eşitledim.
    while y < milyon:   # 5 milyondan küçük tüm fibonnaci sayıları için döngü açtım
        if y % 3 == 0:      # eğer 3 bölünüyorsa,
            toplam += y     # y'yi toplama ekledim
        x, y = y, x + y     # burada ilk iki fibonnaci sayısını güncelledim
    return toplam       #toplamı döndürdüm.

print("Cevap: ",program(5000000)) # 2550408
