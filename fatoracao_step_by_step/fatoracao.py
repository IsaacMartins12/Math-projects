numero = int(input('Seu número : '))
lista = []
cont = 1
print('\n')

while (numero!=1) :

    cont = cont + 1

    if numero % 2 == 0 :

      print(f'{numero:20} ',end=" ")
      numero = numero // 2
      divisores = 2
      lista.append(divisores)
      print(' | ',divisores)
      cont = cont - 1

    elif numero % (2*cont-1) == 0 :

      print(f'{numero:20} ',end=" ")
      
      numero = numero // (2*cont-1)
      divisores = 2*cont-1

      lista.append(divisores)

      print(' | ',divisores)

      cont = cont - 1

print(f'{1:20} ',end=" ")
print('\n\nForma fatorada = ', end = " ")

for i in range (0,len(lista)) :

 if i != len(lista) - 1 :
    print(lista[i] ,'*', end =  " ")
 else :
     print(lista[i])
     print('\n')