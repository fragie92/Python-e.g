# # #  Largest Prime Factor  # # #
# https://projecteuler.net/problem=3 cevabı


a = int(input())
b = 2
while (a > b):
    if a % b == 0:
        a = a / b
        b = 2
    else:
        b += 1
print(f"En Büyük Asal Bölen: {b}")