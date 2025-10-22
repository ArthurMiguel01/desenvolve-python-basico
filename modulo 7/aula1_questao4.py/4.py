num = input("Digite o número: ")
if len(num) == 8:
    num = "9" + num
if len(num) == 9:
    num = num[:5] + "-" + num[5:]
print("Número completo:", num)
