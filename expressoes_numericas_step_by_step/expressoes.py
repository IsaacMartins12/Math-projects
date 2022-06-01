import operacoes_exp
import validacao_exp


def apresenta_menu() :

    exp = []
    exp = input("\nSua expressao : ").split(" ") 
    print("\n")
    return exp

def conta_especial(exp1,indice) :        ## Realiza conta que tenham elementos especiais
 
   op = 1

   if '(' in exp1 and ')' in exp1 : aux = exp1[exp1.index('(')+1:exp1.index(')')]
   elif '[' in exp1 and ']' in exp1 : aux = exp1[exp1.index('[')+1:exp1.index(']')]
   elif '{' in exp1 and '}' in exp1 : aux = exp1[exp1.index('{')+1:exp1.index('}')]

   while(True) :

     if '*' in aux and '/' in aux :

      if aux.index("*") < aux.index("/") :
          if '^' in aux : valor = operacoes_exp.potencia(exp1,indice,aux,op) 
          if '*' in aux : valor = operacoes_exp.multiplicar(exp1,indice,aux,op)
          if '/' in aux : valor = operacoes_exp.dividir(exp1,indice,aux,op)

      else : 

        if '^' in aux : valor = operacoes_exp.potencia(exp1,indice,aux,op) 
        if '/' in aux :valor  =  operacoes_exp.dividir(exp1,indice,aux,op)
        elif '*' in aux : valor = operacoes_exp.multiplicar(exp1,indice,aux,op)

     else :

      if '^' in aux : valor = operacoes_exp.potencia(exp1,indice,aux,op)
      elif '/' in aux : valor = operacoes_exp.dividir(exp1,indice,aux,op)
      elif '*' in aux : valor = operacoes_exp.multiplicar(exp1,indice,aux,op)
      elif '-' in aux :  valor = operacoes_exp.subtrair(exp1,indice,aux,op)
      elif '+' in aux : valor = operacoes_exp.somar(exp1,indice,aux,op)
      
      if len(aux) == 1 : return(aux[0]) 

def calcula(exp) :  ## Realiza conta que nao tenham elementos especiais

 expressao = exp
 valor = paren = 0 
 while (True) :

  if '(' in expressao and ')' in expressao :

   paren = expressao.index('(')
   resposta = conta_especial(expressao,paren+1)
   del(expressao[paren:expressao.index(')')+1])
   expressao.insert(paren,resposta)

  else : break

 while (True) :
  if '[' in expressao and ']' in expressao :

   paren = expressao.index('[')
   resposta = conta_especial(expressao,paren+1)
   del(expressao[paren:expressao.index(']')+1])
   expressao.insert(paren,resposta)

  else : break 

 while (True) :

  if '{' in expressao and '}' in expressao :
   paren = expressao.index('{')
   resposta = conta_especial(expressao,paren+1)
   del(expressao[paren:expressao.index('}')+1])
   expressao.insert(paren,resposta)
  else : break 
 
 op = 0


 while(True) :           ## Realiza a sequencia de operacoes
  try :  
   if '*' in expressao and '/' in expressao :

    if expressao.index("*") < expressao.index("/") :

        if '^' in expressao :  valor = operacoes_exp.potencia(expressao,1,1,op)
        if '*' in expressao :  valor = operacoes_exp.multiplicar(expressao,1,1,op)
        if '/' in expressao :  valor = operacoes_exp.dividir(expressao,1,1,op)

    else : 

      if '^' in expressao :  valor = operacoes_exp.potencia(expressao,1,1,op)
      if '/' in expressao :  valor = operacoes_exp.dividir(expressao,1,1,op)
      elif '*' in expressao :  valor =  operacoes_exp.multiplicar(expressao,1,1,op)

   else : 

    if '^' in expressao : valor = operacoes_exp.potencia(expressao,1,1,op)
    elif '/' in expressao : valor =  operacoes_exp.dividir(expressao,1,1,op)
    elif '*' in expressao : valor = operacoes_exp.multiplicar(expressao,1,1,op)
    elif '-' in expressao : valor =  operacoes_exp.subtrair(expressao,1,1,op)
    elif '+' in expressao : valor = operacoes_exp.somar (expressao,1,1,op)
    elif len(expressao) == 1 : return(expressao[0]) 

  except :

    print('\nExpressao incorreta !')
    return 1

print ('\n\n'+'='*30 + ' CALCULADORA DE EXPRESSOES NUMÉRICAS  ' + '='*30) 
print ('\n (*) - multiplicação entre 2 e 5 --> exemplo : 2 * 5 ')
print ('\n (/) - divisao entre 2 e 5 --> exemplo : 2 / 5  , se for uma fração use assim --> ( 2 / 5 )')
print ('\n (^) - potenciação - 2 elevado a 5 --> exemplo : 2 ^ 5 ')
print ('\n (+) - adição entre 2 e 5 --> exemplo : 2 + 5 ')
print ('\n (-) - Subtração entre 2 e 5 --> exemplo : 2 - 5 ')
print('\nOBSERVACAO : Todo digito do teclado deve ser separado por espaço -- > 2-4 - 2  NAO é uma expressao válida\n')
print("\n\n Exemplo de expressao válida : { 2 * 5 + 4 - [ ( 2 + 9 ) ] + 2 } \n\n")

while (True) :
 exp = apresenta_menu()
 if (validacao_exp.valida_expressao(exp) and calcula(exp)!=1):
    print(f'\n\nO valor da sua expressao é {round(calcula(exp),3)} \n')
    novamente = input(('\n\nQuer colocar outra expressao ? [S/N] : '))
    if novamente.upper() == 'N' :
      break
    
  