def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Erro: Não é possível dividir por zero."
    except TypeError:
        return "Erro: Digite apenas números."
    else:
        return f"Resultado da divisão: {resultado}"
    finally:
        print("Operação finalizada (com ou sem erro).")

# Exemplo de uso interativo
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(dividir(num1, num2))  # Agora imprime o resultado ou erro
except ValueError:
    print("Você deve digitar apenas números válidos.")
