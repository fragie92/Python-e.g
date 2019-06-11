# 2 boyutlu bir tablo olarak, ekrana çarpım tablosunu hesaplayıp yazan kodu yazınız.

# Ekran çıktısı 5 x 5 boyutları için örnek olarak verilmiştir, isterseniz boyutları
# klavyeden okuyup istenen boyutlara göre ekrana basan bir kod yazabilirsiniz.

# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25"""

x = int(input("Bir sayı giriniz: "))

for i in range(1,x+1):
    print(i, end="\t")

    for j in range(2,x+1):
        print(j*i , end="\t")
    print("\n")