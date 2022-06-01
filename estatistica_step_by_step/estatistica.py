import calculo  ## script responsável por apresentar o step by step das operações realizadas

def media() :   ## Apresenta o step by step de como encontrar a média aritmética de uma sequencia

  soma = 0
  sequencia = input('Sua sequencia -- > ').split(' ')  
  print('\n')

  init()
  
  print('\n')
  print('(' , soma , ')' , '/' , len(sequencia))
  print('\nSua média é : ' , round(resposta_media,3),'\n')


def mediana() :  ## Apresenta o step by step de como encontrar a média aritmética de uma sequencia

  ordem = []
  sequencia = input('Sua sequencia -- > ').split(' ')
  print('\nSua sequencia ->',end=" ")
  for i in range (0,len(sequencia)):
    print(sequencia[i],end=" ")

  for i in range(len(sequencia)) :

   ordem.append(float(sequencia[i]))

  print('\n')
  print(f'Sua sequencia ordenada -> {sorted(ordem)}')
 

  for i in range (0,len(sequencia)) :
    sequencia[i]=float(sequencia[i])
    

  sequencia = sorted(sequencia)
  if len(sequencia)%2==0 :
     
    mediana = ( (sequencia[len(sequencia)//2] + sequencia[len(sequencia)//2-1]) ) / 2
   
  else :

    mediana = (sequencia[len(sequencia)//2])
     

  print('A mediana dessa sequencia vale : ', mediana,'\n')



def moda() :  ## Apresenta a moda de uma sequencia " 2 3 4 5 7 8 1 1 "

  
  quantidade = []
  modas = []
  sequencia = input('Sua sequencia -- > ').split(' ')
  print('\nSua sequencia -> ',sequencia,'\n')
  
  for i in range (0,len(sequencia)) :

    cont = 0
  
    for j in range (0,len(sequencia)) :

      if (float(sequencia[i]==sequencia[j])) :
        cont +=1 

    quantidade.append(cont)

  maior = max(quantidade)

  if maior > 1 :

    for i in range(0,len(quantidade)) :
        if (maior == quantidade[i] and sequencia[i] not in modas) :
          modas.append(sequencia[i])
    
    print('A(s) moda(s) da sequencia : ',end= " ")

    for i in range(0,len(modas)) :
      print(modas[i],end=" ")
    print('\n')
  else :  print('Nao existe moda nessa sequencia porque nenhum elemento se repete ! \n',end= " ")



def desviopadrao () :    ## Apresenta o step by step de como encontrar o desvio padrão de uma sequencia

  soma = 0
  sequencia = input('Sua sequencia -- > ').split(' ')
  print('\n')

  for i in range (0,len(sequencia)) :
    if i == 0 :
      print('(' , sequencia[i] , '+' , end = " ")

    if i == len(sequencia)-1 :
      print(sequencia[i] , ')' , '/' , len(sequencia), end = " ")

    if i!=0 and i!= len(sequencia)-1 :
      print(sequencia[i] , '+' , end = " ")

  for i in range (0,len(sequencia)) :
    soma += float(sequencia[i])
    resposta_media = soma/len(sequencia)
  
  print('\n')
  print('(' , soma , ')' , '/' , len(sequencia))
  print('\nSua média é : ' , round(resposta_media,3),'\n')

  conta = []

  for i in range (0,len(sequencia)) :

     if i == 0 :
      conta.append('[')
      conta.append('(')
      conta.append(float(sequencia[i]) - round(float(resposta_media),3))
      conta.append(')')
      conta.append('^')
      conta.append(2)
      conta.append('+')

      print('[ (', sequencia[i],'-',round(resposta_media,3),') ^ 2 + ', end='')

     if i != len(sequencia)-1 and i!=0:

      conta.append('(')
      conta.append(float(sequencia[i]) - round(float(resposta_media),3))
      conta.append(')')
      conta.append('^')
      conta.append(2)
      conta.append('+')

      print('(', sequencia[i],'-',round(resposta_media,3),') ^ 2 + ', end='')

     if i == len(sequencia)-1 :
      
      conta.append('(')
      conta.append(float(sequencia[i]) - round(float(resposta_media),3))
      conta.append(')')
      conta.append('^')
      conta.append(2)
      conta.append(']')
      conta.append('/')
      conta.append(i+1)

      
      print('(', sequencia[i],'-',round(resposta_media,3),') ^ 2 ] / ',i+1, end='')
      print('\n')

  for i in range (0,len(conta))  :
   print(conta[i] , end=" ")
  print('\n')
  resposta = calculo.calcula1(conta)

  print('O desvio padrao vale : √ (',resposta,') = ',round(float(resposta)**0.5,3))
  print('\n')


def variancia () :   ## Shows the step by step of how to find the variance of a sequence

  soma = 0
  sequencia = input('Sua sequencia -- > ').split(' ')
  print('\n')

  for i in range (0,len(sequencia)) :
    if i == 0 :
      print('(' , sequencia[i] , '+' , end = " ")

    if i == len(sequencia)-1 :
      print(sequencia[i] , ')' , '/' , len(sequencia), end = " ")

    if i!=0 and i!= len(sequencia)-1 :
      print(sequencia[i] , '+' , end = " ")

  for i in range (0,len(sequencia)) :
    soma += float(sequencia[i])
    resposta_media = soma/len(sequencia)
  
  print('\n')
  print('(' , soma , ')' , '/' , len(sequencia))
  print('\nSua média é : ' , round(resposta_media,3),'\n')

  conta = []

  for i in range (0,len(sequencia)) :

     if i == 0 :
      conta.append('[')
      conta.append('(')
      conta.append(float(sequencia[i]) - round(float(resposta_media),3))
      conta.append(')')
      conta.append('^')
      conta.append(2)
      conta.append('+')

      print('[ (', sequencia[i],'-',round(resposta_media,3),') ^ 2 + ', end='')

     if i != len(sequencia)-1 and i!=0:

      conta.append('(')
      conta.append(float(sequencia[i]) - round(float(resposta_media),3))
      conta.append(')')
      conta.append('^')
      conta.append(2)
      conta.append('+')

      print('(', sequencia[i],'-',round(resposta_media,3),') ^ 2 + ', end='')

     if i == len(sequencia)-1 :
      
      conta.append('(')
      conta.append(float(sequencia[i]) - round(float(resposta_media),3))
      conta.append(')')
      conta.append('^')
      conta.append(2)
      conta.append(']')
      conta.append('/')
      conta.append(i+1)

      
      print('(', sequencia[i],'-',round(resposta_media,3),') ^ 2 ] / ',i+1, end='')
      print('\n')

  for i in range (0,len(conta))  :
   print(conta[i] , end=" ")
  print('\n')

  resposta = calculo.calcula1(conta)

  print('A variância vale : ',round(float(resposta),3))
  print('\n')
  

## Main Program

print('1 - Média ')
print('2 - Mediana ')
print('3 - Moda')
print('4 - Desvio padrao')
print('5 - Variancia')

opcao = int(input('Your option : '))

# Call the methods

if opcao == 1 : media()
if opcao == 2 : mediana()
if opcao == 3 : moda()
if opcao == 4 : desviopadrao()
if opcao == 5 : variancia()