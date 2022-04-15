import random   # importa a biblioteca que sorteia números

def usou() :   # função que checa as letras que ja foram usadas
 print ("LETRAS QUE JÁ USOU : " ,end=" ")
 for i in range(0,len(showletter),1) :
   print(showletter[i] , end=" ")

def linhas() :     #função que mostras as linhas , preenchidas ou nao
  for i in range(0,word_size,1) :
   print(compare_word[i] , end=" ")
  print("\n")

def mostrafase1() :
 print ("--"*5)
 print ("|"+" "*8 + "|")
 print ("|" + " "*8 + "O")
 print ("|\n"*4)
 usou()
 print ("\n\n")
 print (" "*3 )
 linhas()
 read1 = str(input('\n Informe sua letra :')).strip()
 print("\n" *15 )
 return(read1)

def mostrafase2():
 print ("--"*5)
 print ("|"+" "*8 + "|")
 print ("|" + " "*8 + "O")
 print ("|" + " "*8 + "|")
 print ("|\n"*3)
 usou()
 print ("\n\n")
 print (" "*3 )
 linhas()
 read2 = str(input('\n Informe sua letra :')).strip()
 print("\n" *15 )
 return(read2)

def mostrafase3():
 print ("--"*5)
 print ("|" + " "*8 + "|")
 print ("|" + " "*8 + "O")
 print ("|" + " "*8 + "|")
 print ("|" + " "*7 + "/")
 print ("|\n"*3)
 usou()
 print ("\n\n")
 print (" "*3 )
 linhas()
 read3 = str(input('\n Informe sua letra :')).strip()
 print("\n" *15 )
 return(read3)

def mostrafase4():
    print ("--"*5)
    print ("|" + " "*8 + "|")
    print ("|" + " "*8 + "O")
    print ("|" + " "*8 + "|")
    print ("|" + " "*7 + "/ " + "\\")
    print ("|" + " "*8 )
    print ("|\n"*3)
    usou()
    print ("\n\n")
    print (" "*3 )
    linhas()
    read4 = str(input('\n Informe sua letra :')).strip()
    print("\n" *15 )
    return(read4)

def mostrafase5():
    print ("--"*5)
    print ("|" + " "*8 + "|")
    print ("|" + " "*8 + "O")
    print ("|" + " "*7 + "/" + "|")
    print ("|" + " "*7 + "/ " + "\\")
    print ("|" + " "*8 )
    print ("|\n"*3)
    print ("\n\n")
    usou()
    print ("\n\n")
    print (" "*3 )
    linhas()
    read5 = str(input('\n Informe sua letra :')).strip()
    print("\n" *15 )
    return(read5)

def mostrafase6():
    print ("--"*5)
    print ("|" + " "*8 + "|")
    print ("|" + " "*8 + "O")
    print ("|" + " "*7 + "/" + "|" + "\\")
    print ("|" + " "*7 + "/ " + "\\")
    print ("|" + " "*8 )
    print ("|\n"*3)
    usou()
    print ("\n\n")
    print (" "*3 )
    print("---> ",end="")
    linhas()
    print("\n")

def mostrafase0():
 print ("--"*5 )
 print ("|"+" "*8 + "|")
 print ("|\n"*5)
 usou()
 print ("\n\n" + " "*3)
 linhas()
 read = str(input('\n Informe sua letra :')).strip()
 print("\n" *15 )
 return(read)

showletter=[]
word_choice=[]
compare_word = []

gameover=acertou=0
print('[1] ANIMAIS \n[2] PAÍSES  ')
op = int(input('ESCOLHA A CATEGORIA : '))
if (op==1) :
 words = ['macaco','arara','urso','peixe','cachorro','gato','pelicano','tubarao','avestruz','tartaruga','jabuti', 'orangotango','camarao','cavalo','tigre','onça','foca','baleia','rinoceronte','gaivota','hamster']
if (op==2) :
   words = ['alemanha','portugal','brasil','argentina','chile','uruguai','peru','marrocos','turquia','arzebaijao','mexico', 'espanha','italia','finlandia','franca','holanda','nigeria','cuba','india','china','japao']
if (op==1 or op==2) :
 word_index = random.randint(0,21)   #sorteia um indice da lista
 word_size = len(words[word_index])  #pega o tamanho da palavra escohida
 word_choice = words[word_index]    #pega a palavra escolhida
 for i in range (0,word_size,1) :
  compare_word += "_"
 while (True) :
  if acertou==word_size : break 
  if gameover == 0 :   readletter = mostrafase0().lower()
  if gameover == 1 :   readletter = mostrafase1().lower()
  if gameover == 2 :   readletter = mostrafase2().lower()
  if gameover == 3 :   readletter = mostrafase3().lower()
  if gameover == 4 :   readletter = mostrafase4().lower()
  if gameover == 5 :   readletter = mostrafase5().lower()
  if gameover == 6 :   break
  showletter += [readletter]
  if readletter in word_choice :  # Checa se a letra escolhida está na palavra
      for i in range (0,word_size,1) :
       if compare_word[i] =='_' and readletter in word_choice[i] :  # Se a letra estiver em um espaço vazio
         compare_word[i] = readletter # preenche o espaço vazio
         acertou+=1  
  else : gameover += 1
if gameover == 6 :
  print(f'VOCE ERROU ! A PALAVRA ERA {word_choice.upper()}\n\n')
  mostrafase6()
else : print(f'VOCE ACERTOU ! A PALAVRA ERA ---> {word_choice.title()}\n\n')
