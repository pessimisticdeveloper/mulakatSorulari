def program(cumle):
  #cümlenin noktalama işaretleri çıkardım
  cumle = cumle.replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "")
  kelimeler = cumle.split(" ") #cumlenin kelimelerini ayırdım
  toplamUzunluk = 0   # kelimelerin uzunluklarını topladım
  for kelime in kelimeler: # kelimeleri gezdim
    toplamUzunluk += len(kelime)
  ortUzunluk = toplamUzunluk / len(kelimeler) # ortalama kelime uzunluklarını hesapladım
  return ortUzunluk #$sonra dönderdim

# Örnek

cumle = "muz, kivi, şeftali"
ortUzunluk = program(cumle)
print("Cevap: ",ortUzunluk)  #4.666666666666667

