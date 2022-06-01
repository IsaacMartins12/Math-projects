def valida_expressao(exp4) :

 caracteres = {' ','%','$','!','@','¨','=','§','|','_'}
 cont=0
 
 if (exp4.count(')') != exp4.count('(')):  ## uso de parenteses
   print('\nErro com o número de parenteses, revise sua expressao !')
   return False
 if (exp4.count('[') != exp4.count(']')): ## uso de colchetes
   print('\nErro com o número de colchetes, revise sua expressao !')
   return False
 if (exp4.count('{') != exp4.count('}')): ## uso de chaves
   print('\nErro com o número de chaves, revise sua expressao !')
   return False

 if (('0' in exp4 and '/' in exp4 ) and (exp4.index('0') == exp4.index('/') + 1)) : ## divisao por zero
    print('\nDivisoes por zero nao podem ser executada, revise sua expressao !')
    return False

 for i in range(0,len(exp4),1) :

   if exp4[i] in caracteres :  ## caracteres invalidos
     print('\nVocê inseriu caracteres inválidos, revise sua expressao !')
     return False

   if float(exp4[i].isnumeric()) : ##Conta os números da conta
     cont+=1

 if cont == len(exp4) :
   print('\nAcrescente operadores, revise sua expressao !')
   return False

 if exp4[0] == " " or exp4[len(exp4)-1] ==" ":
  print('\nNao comece ou termine com espaço !')
  return False


 return True
