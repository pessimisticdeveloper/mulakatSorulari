def program(basamakSayisi):
    x = 0       # x burada en büyük palindroma sayısına eşit
    for i in range(100, 1000):      # 3 basamaklı dediği için sm lg arasında döngü açtım.
        for j in range(100, 1000):
            carpim = i * j      #sayının çarpımını hesapladım.
            if str(carpim) == str(carpim)[::-1] and carpim > x: #çarpım palindrom ise ve en büyük palindromdan daha büyük ise
                x = carpim  #en büyük palindromu güncelledim.
    return x #ve dönderdim

print("Cevap: ",program(3)) # 906609
