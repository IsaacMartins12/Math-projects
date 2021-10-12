def deletar (aux,pos,exp3,indice,valor) :

     del(aux[pos-1:pos+2])
     del(exp3[pos-1+indice:indice+pos+2])
     aux.insert(pos-1, valor)
     exp3.insert(pos-1+indice, valor)
     for i in range (0,len(exp3)) :
       print(exp3[i] , end = ' ') 
     print('\n')

def somar (exp3,indice,aux,op) :  
          if op ==1 :
            pos = aux.index('+')
            valor = round((float(aux[pos-1]) + float(aux[pos+1])),3)
            deletar(aux,pos,exp3,indice,valor)
            return valor
          else :
             pos = exp3.index('+')
             valor = round((float(exp3[pos-1]) + float(exp3[pos+1])),3)
             del(exp3[pos-1:pos+2])
             exp3.insert(pos-1, valor)
             for i in range (0,len(exp3)) :
                print(exp3[i] , end = ' ')
             print('\n')
             return valor
def subtrair (exp3,indice,aux,op) :
          if op == 1 :
            pos = aux.index('-')
            valor = round((float(aux[pos-1]) - float(aux[pos+1])),3)
            deletar(aux,pos,exp3,indice,valor) 
            return valor
          else : 
             pos = exp3.index('-')
             valor = round((float(exp3[pos-1]) - float(exp3[pos+1])),3)
             del(exp3[pos-1:pos+2])
             exp3.insert(pos-1, valor)
             for i in range (0,len(exp3)) :
                print(exp3[i] , end = ' ')
             print('\n')
             return valor

def multiplicar (exp3,indice,aux,op) :

          if op == 1 :
            pos = aux.index('*')
            valor = round((float(aux[pos-1]) * float(aux[pos+1])),3)
            deletar(aux,pos,exp3,indice,valor) 
            return valor
          else :
             pos = exp3.index('*')
             valor = round((float(exp3[pos-1]) * float(exp3[pos+1])),3)
             del(exp3[pos-1:pos+2])
             exp3.insert(pos-1, valor)
             for i in range (0,len(exp3)) :
                print(exp3[i] , end = ' ')
             print('\n')

def dividir (exp3,indice,aux,op) :

          if op == 1 :
            pos = aux.index('/')
            valor = round((float(aux[pos-1]) / float(aux[pos+1])),3)
            deletar(aux,pos,exp3,indice,valor) 
            return valor
          else : 
             pos = exp3.index('/')
             valor = round((float(exp3[pos-1]) / float(exp3[pos+1])),3)
             del(exp3[pos-1:pos+2])
             exp3.insert(pos-1, valor)
             for i in range (0,len(exp3)) :
                print(exp3[i] , end = ' ')
             print('\n')
             return valor

def potencia (exp3,indice,aux,op) :

          if op == 1 :
            pos = aux.index('^')
            valor = round((float(aux[pos-1]) ** float(aux[pos+1])),3)
            deletar(aux,pos,exp3,indice,valor) 
            return valor
          else : 
             pos = exp3.index('^')
             valor = round((float(exp3[pos-1]) ** float(exp3[pos+1])),3)
             del(exp3[pos-1:pos+2])
             exp3.insert(pos-1, valor)
             for i in range (0,len(exp3)) :
                print(exp3[i] , end = ' ')
             print('\n')
             return valor

def conta_especial(exp1,indice) :
 op = 1
 if '(' in exp1 and ')' in exp1 : aux = exp1[exp1.index('(')+1:exp1.index(')')]
 elif '[' in exp1 and ']' in exp1 : aux = exp1[exp1.index('[')+1:exp1.index(']')]
 elif '{' in exp1 and '}' in exp1 : aux = exp1[exp1.index('{')+1:exp1.index('}')]
 while(True) :
   if '*' in aux and '/' in aux :
    if aux.index("*") < aux.index("/") :
        if '^' in aux : valor = potencia(exp1,indice,aux,op) 
        if '*' in aux : valor = multiplicar(exp1,indice,aux,op)
        if '/' in aux : valor = dividir(exp1,indice,aux,op)
    else : 
      if '^' in aux : valor = potencia(exp1,indice,aux,op) 
      if '/' in aux :valor  =  dividir(exp1,indice,aux,op)
      elif '*' in aux : valor = multiplicar(exp1,indice,aux,op)
   else :
    if '^' in aux : valor = potencia(exp1,indice,aux,op)
    elif '/' in aux : valor = dividir(exp1,indice,aux,op)
    elif '*' in aux : valor = multiplicar(exp1,indice,aux,op)
    elif '-' in aux :  valor = subtrair(exp1,indice,aux,op)
    elif '+' in aux : valor = somar(exp1,indice,aux,op)
    if len(aux) == 1 : return(aux[0]) 
  
def calcula(exp) :
 expressao = exp.split()
 valor = 0 
 while (True) :
  if '('in expressao and ')' in expressao :
   paren = expressao.index('(')
   resposta = conta_especial(expressao,paren+1)
   del(expressao[paren:expressao.index(')')+1])
   expressao.insert(paren,resposta)
  else : break
 while (True) :
  if '['in expressao and ']' in expressao :
   paren = expressao.index('[')
   resposta = conta_especial(expressao,paren+1)
   del(expressao[paren:expressao.index(']')+1])
   expressao.insert(paren,resposta)
  else : break 
 while (True) :
  if '{'in expressao and '}' in expressao :
   paren = expressao.index('{')
   resposta = conta_especial(expressao,paren+1)
   del(expressao[paren:expressao.index('}')+1])
   expressao.insert(paren,resposta)
  else : break 
 op = 0
 while(True) :

   if '*' in expressao and '/' in expressao :
    if expressao.index("*") < expressao.index("/") :
        if '^' in expressao :  valor = potencia(expressao,1,1,op)
        if '*' in expressao :  valor = multiplicar(expressao,1,1,op)
        if '/' in expressao :  valor = dividir(expressao,1,1,op)
    else : 
      if '^' in expressao :  valor = potencia(expressao,1,1,op)
      if '/' in expressao :  valor = dividir(expressao,1,1,op)
      elif '*' in expressao :  valor =  multiplicar(expressao,1,1,op)
   else : 
    if '^' in expressao : valor = potencia(expressao,1,1,op)
    elif '/' in expressao : valor =  dividir(expressao,1,1,op)
    elif '*' in expressao : valor = multiplicar(expressao,1,1,op)
    elif '-' in expressao : valor =  subtrair(expressao,1,1,op)
    elif '+' in expressao : valor = somar (expressao,1,1,op)
    elif len(expressao) == 1 : return(expressao[0]) 

while (True) :
 print ('\n\n'+'='*30 + ' CALCULADORA DE EXPRESSOES NUMÉRICAS  ' + '='*30)
 print ('\n (*) - multiplicação entre 2 e 5 --> exemplo : 2 * 5 ')
 print ('\n (/) - divisao entre 2 e 5 --> exemplo : 2 / 5  , se for uma fração use assim --> ( 2 / 5 )')
 print ('\n (^) - potenciação - 2 elevado a 5 --> exemplo : 2 ^ 5 ')
 print ('\n (+) - adição entre 2 e 5 --> exemplo : 2 + 5 ')
 print ('\n (-) - Subtração entre 2 e 5 --> exemplo : 2 - 5 ')
 print('\nOBSERVACAO : Todo digito do teclado deve ser separado por espaço -- > 2-4 - 2  NAO é uma expressao válida\n')
 print("\n\n Exemplo de expressao válida : { 2 * 5 + 4 - [ ( 2 + 9 ) ] + 2 } ")
 exp = []
 exp = input("\nSua expressao : ") 
 print("\n\n")
 print(exp,'\n')
 print(f'\n\nO valor da sua expressao é {round(calcula(exp),3)} \n')
 novamente = input(('\n\nQuer colocar outra expressao ? [S/N] : '))
 if novamente == 'N' :
    break