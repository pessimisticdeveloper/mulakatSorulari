import requests

url = "https://gist.githubusercontent.com/akarca/fd99fea898db82dc39c41d03d68c93b8/raw/db67136bf7431be047a2faaef95eff5bd5df2f03/isimler"
x = requests.get(url)
isimListesi = x.text.split("\n") #adresteki isim listesini indirdim ve atadım

def program(arr): # quicksort algoritmasını kulladım. ve sıraladım
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]
  return program(left) + middle + program(right)

siralanmisIsimListesi = program(isimListesi)
isimListesi = list(dict.fromkeys(siralanmisIsimListesi)) #tekrar eden isimleri sildim

#print(isimListesi)

def anaProgram(isimListesi):
  skorToplami = 0 #skor toplamını 0'a atadım
  for i, isim in enumerate(isimListesi):  #enumerate metodu ile index ve kendini aldım (satır sırasını aldım)
    skor = (i+1) * sum([ord(harf) - ord('A') + 1 for harf in isim]) #burada satır sırası ile harf sırası toplanı çarptım.
    skorToplami += skor # skor toplamı ile topladım
  return skorToplami #döndürdüm

print("Cevap: ",anaProgram(isimListesi)) # 173502153