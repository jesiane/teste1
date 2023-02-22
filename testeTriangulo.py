v1 = float(input("Digite a medida do lado a: "))
v2 = float(input("Digite a medida do lado b: "))
v3 = float(input("Digite a medida do lado c: "))

if (v1 + v2 > v3 and v1 + v3 > v2 and v2 + v3 > v1):
    print("Os 3 lados formam um Triângulo")
    if (v1==v2 and v1==v3):
        print("É um Triângulo equilátero.")
    elif v1== v2 or v2 == v3 or v1== v3:
        print("É um Triângulo isósceles.")
    else:
        print("É um Triângulo Escaleno.")
else:
    print("Triângulo Invalido!")


