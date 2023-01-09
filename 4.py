def program(n):
  asalSayilar = [] #bir tane liste oluşturdum asal sayıları barındıracak
  sayi = 2    # en küçük asal sayı 2 olduğu için
  while len(asalSayilar) <= n: # asal sayılar listesinde kaç elemean varsa n'e eşit veya küçükse n kadar dön
    if all(sayi % i != 0 for i in range(2, sayi)): #asal sayı kontrolu
      asalSayilar.append(sayi) #Asal sayı ise listeye ekle
    sayi += 1
  return asalSayilar[-1] # son elemanı döndür bana

print(program(10101)) # 105967
