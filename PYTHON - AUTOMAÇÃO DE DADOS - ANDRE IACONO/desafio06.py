lista=['uva', 2, True, 'maca']
frutas=[]
for i in lista:
    if isinstance(i,str):
        frutas.append(i)
print(frutas)