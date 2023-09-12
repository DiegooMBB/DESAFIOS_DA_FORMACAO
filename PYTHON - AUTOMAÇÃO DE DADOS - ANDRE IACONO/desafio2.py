enter=input('Digite seu primeiro nome e sua idade(separados por espaco): ')
nome, idade=enter.split()
idade=float(idade)
print(f'O seu nome é {nome} e voce tem {idade} anos.')