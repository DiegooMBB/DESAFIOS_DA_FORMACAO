lista = []
continuar=True
while continuar:
    try:
        numero = float(input("Digite um número: "))
        lista.append(numero)
    except ValueError:
        print("Caractere errado. Digite um número.")

    teste = input('Deseja continuar? [S/N]').strip().lower()
    continuar = True if teste == 's' else False

lista.sort()
print(f'O menor número é {lista[0]} e o maior é {lista[-1]}')
