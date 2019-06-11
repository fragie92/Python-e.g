#Fibonacci serisinin ilk iki elemanı 1'dir ve diğer elemanları, kendisinden önce gelen son iki elemanın toplamıdır. '
#'Klavyeden bir sayı okuyarak, girilen sayı kadar fibonacci serisinin elemanını ekrana bastıran kodu yazınız.

# 1 1 2 3 5 8 13 21 34 55 ...
#   a b c

a = 1
b = 1
c = ""
n = int(input("Bir sayı giriniz: "))
for i in range(1, n):
    c = a + b
    a, b = b, a
    b = c
    print(a)