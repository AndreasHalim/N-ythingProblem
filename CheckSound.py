import random

i = [[1,2,3], [2,3,4], [3,4,5], [4,5,6]]

tes = [(100, 200), (50, 400), (25, 800)]
x = [n for n in tes if n[0] >= 50]

state = [('R', 2, 6), ('Q', 4, 5), ('B', 4, 2), ('B', 5, 3)]
bidak = ('R', 2, 6)
x = [n for n in state if n != bidak]
print(x)


def cekNeg(angka):
    return (angka <= 0)

print(cekNeg(-1))
