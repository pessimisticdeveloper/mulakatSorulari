def program(list):
  sonucListesi = [] #bir liste oluşturdum sonuçları eklemek için
  oncekiNone = None #none atadım
  for i in list: # verdiğim listeyi gezdim
    if i is not None: # içerde none varsA
      sonucListesi.append(i) #SONUC listesine ekledim
      oncekiNone = i #BİR sonraki değere atadım
    else:
      sonucListesi.append(oncekiNone)
  return sonucListesi #listeyi dönderdim

# Örnek

list = [3, None, 40, None, None, True, False, None, 10]
yeniListe = program(list)
print("Cevap: ", yeniListe)  # [3, 3, 40, 40, 40, True, False, False, 10]
