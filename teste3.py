def eh_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

numero = 19
if eh_par(numero):
    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar")

