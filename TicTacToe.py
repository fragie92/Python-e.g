# Listler konusunu pekiştirmek adına yazdığım XOX oyunu.
# Oyun tam anlamıyla bitmiş bir versiyon değil
# Örneğin input değerlerinde int karşılığı olmayan bir değer girilmediğinde hata veriyor.
# Fakat bunları önemsemedim burda amacım listleri kullanmak ve özellikle;
# [z for z in i if z in o_durumu] gibi for döngüsüyle listeleri nasıl oluşturacağımı anlamak kavramaktı.
# Keyifli bir öğrenme, pekiştirme süreci geçirdim...


tahta = [["___", "___", "___"],
         ["___", "___", "___"],
         ["___", "___", "___"]]

for i in tahta:
    print("\t".expandtabs(30), *i, end="\n"*2)

kazanma_olcutleri = [[[0, 0], [1, 0], [2, 0]],
                     [[0, 1], [1, 1], [2, 1]],
                     [[0, 2], [1, 2], [2, 2]],
                     [[0, 0], [0, 1], [0, 2]],
                     [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]],
                     [[0, 0], [1, 1], [2, 2]],
                     [[0, 2], [1, 1], [2, 0]]]

x_durumu = []
o_durumu = []

sira = 1
while True:
    if sira % 2 == 0:
        isaret = "X".center(3)
    else:
        isaret = "O".center(3)


    print(f"İŞARET: {isaret}\n")
    x = int(input("Soldan Sağa [1, 2, 3,]: ".ljust(30)))
    y = int(input("Yukarıdan Aşağıya [1, 2, 3,]: ".ljust(30)))

    x -= 1
    y -= 1

    if tahta[x][y] == "___":
        tahta[x][y] = isaret
        if isaret == "X".center(3):
            x_durumu += [[x, y]]
        elif isaret == "O".center(3):
            o_durumu += [[x, y]]
        sira += 1
    else:
        print("\nORASI DOLU! TEKRAR DENEYİN\n")


    for i in tahta:
        print("\t".expandtabs(30), *i, end="\n" * 2)

    for i in kazanma_olcutleri:
        o = [z for z in i if z in o_durumu]
        x = [z for z in i if z in x_durumu]
        if len(o) == len(i):
            print("O KAZANDI!")
            quit()
        if len(x) == len(i):
            print("X KAZANDI!")
            quit()
