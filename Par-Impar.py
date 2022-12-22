def ParImpar(n):
    if n % 2 == 0:
        print("El numero ",n," es par")
    else:
        print("El numero ",n," es impar")


n = int(input("Ingrese un número: "))
print(ParImpar(n))