import random
import time

def defesa() :
  if matriz[0][0] == matriz[0][1] == "X" and matriz[0][2] == " ":
    matriz[0][2] = "O"
    return 1
  if matriz[0][0] == matriz[0][2] == "X" and matriz[0][1] == " ":
    matriz[0][1] = "O"
    return 1
  if matriz[0][1] == matriz[0][2] == "X" and matriz[0][0] == " ":
    matriz[0][0] = "O"
    return 1
          ## CHECALINHA 2
  if matriz[1][0] == matriz[1][1] == "X" and matriz[1][2] == " ":
    matriz[1][2] = "O"
    return 1
  if matriz[1][0] == matriz[1][2] == "X" and matriz[1][1] == " ":
    matriz[1][1] = "O"
    return 1
  if matriz[1][1] == matriz[1][2] == "X" and matriz[1][0] == " ":
    matriz[1][0] = "O"
    return 1
           ## CHECALINHA 3
  if matriz[2][0] == matriz[2][1] == "X" and matriz[2][2] == " ":
    matriz[2][2] = "O"
    return 1
  if matriz[2][0] == matriz[2][2] == "X" and matriz[2][1] == " ":
    matriz[2][1] = "O"
    return 1
  if matriz[2][1] == matriz[2][2] == "X" and matriz[2][0] == " ":
    matriz[2][0] = "O"
    return 1
        ## CHECA COLUNA 1

  if matriz[0][0] == matriz[1][0] == "X" and matriz[2][0] == " ":
    matriz[2][0] = "O" 
    return 1
  if matriz[0][0] == matriz[2][0] == "X" and matriz[1][0] == " ":
    matriz[1][0] = "O" 
    return 1
  if matriz[2][0] == matriz[1][0] == "X" and matriz[0][0] == " ":
    matriz[0][0] = "O" 
    return 1

         ## CHECA COLUNA 2

  if matriz[0][1] == matriz[1][1] == "X" and matriz[2][1] == " ":
    matriz[2][1] = "O" 
    return 1
  if matriz[0][1] == matriz[2][1] == "X" and matriz[1][1] == " ":
    matriz[1][1] = "O" 
    return 1
  if matriz[2][1] == matriz[1][1] == "X" and matriz[0][1] == " ":
    matriz[0][1] = "O" 
    return 1
         ## CHECA COLUNA 3
  if matriz[0][2] == matriz[1][2] == "X" and matriz[2][2] == " ":
    matriz[2][2] = "O" 
    return 1
  if matriz[0][2] == matriz[2][2] == "X" and matriz[1][2] == " ":
    matriz[1][2] = "O" 
    return 1
  if matriz[2][2] == matriz[1][2] == "X" and matriz[0][2] == " ":
    matriz[0][2] = "O" 
    return 1
        ## CHECA DIAGONAIS
  if matriz[0][2] == matriz[1][1] == "X" and matriz[2][0] == " " :
    matriz[2][0] = "O"
    return 
  if matriz[0][2] == matriz[2][0] == "X" and matriz[1][1] == " "  :
    matriz[1][1] = "O" 
    return 1
  if matriz[0][0] == matriz[1][1] == "X" and matriz[2][2] == " " :
    matriz[2][2] = "O" 
    return 1
  if matriz[0][0] == matriz[2][2] == "X" and matriz[1][1] == " " :
    matriz[1][1] = "O" 
    return 1
  if matriz[2][0] == matriz[1][1] == "X" and matriz[0][2] == " " :
    matriz[0][2] = "O" 
    return 1
  if matriz[2][2] == matriz[1][1] == "X" and matriz[0][0] == " " :
    matriz[0][0] = "O" 
    return 1
  return 0

def testa_vencedor() :
 if matriz[0][0] == matriz[0][1] == matriz[0][2] != " "  :
     mostra_tabuleiro()
     return 1
 if matriz[1][0] == matriz[1][1] == matriz[1][2]  != " " :
     mostra_tabuleiro()
     return 1
 if matriz[2][0] == matriz[2][1] == matriz[2][2]  != " " :
     mostra_tabuleiro()
     return 1
 if matriz[0][0] == matriz[1][0] == matriz[2][0]  != " " :
     mostra_tabuleiro()
     return 1
 if matriz[0][1] == matriz[1][1] == matriz[2][1]  != " " :
     mostra_tabuleiro()
     return 1
 if matriz[0][2] == matriz[1][2] == matriz[2][2]  != " " :
     mostra_tabuleiro()
     return 1
 if matriz[0][0] == matriz[1][1] == matriz[2][2]  != " " :
     mostra_tabuleiro()
     return 1
 if matriz[0][2] == matriz[1][1] == matriz[2][0]  != " " :
     mostra_tabuleiro()
     return 1
def mostra_tabuleiro() :
 print("\n")
 print(" 1     2     3  (colunas)\n")
 print(" |     |     | \n")
 for i in range(0,3,1) :
  for j in range(0,3,1) :
    if j!=2 :
     print(f' {matriz[i][j]} ' + ' | ' ,end='')
    else :
     print(f' {matriz[i][j]}  --> (linha {i+1})' ,end='')
  print("\n")
  if i!=2 :
   print("-"*15)

rodada=a=0
matriz = [[' ',' ',' '] , [' ',' ',' '] , [' ',' ',' ']]  
op = int(input("\n[1] - 1x1 \n[2] - x COMPUTADOR\n\nESCOLHA SUA OPCAO : "))
if op == 1 :
 while (True) :
    print("\t\t\t\t\t\tJOGO DA VELHA ")
    mostra_tabuleiro()
    if rodada == 9 :
        print ("\nDEU VELHA !! \n\n")
        break
    if rodada%2 ==0 :
     print(f'\n Jogador {rodada%2+1} faca sua jogada ! (X)\n')
    else :
     print(f'\n Jogador {rodada%2+1} faca sua jogada ! (O)\n')
    while (True) :
     linha = int(input("Informe a linha : "))
     coluna = int(input("Informe a coluna : "))
     if (linha>=1 and linha<=3) and (coluna>=1 and coluna <=3) and (matriz[linha-1][coluna-1] ==' '): 
        break
     else :
        print("\n Coordenadas inválidas ou posição já preenchida !!\n")
    if rodada%2==0 :
     (matriz[linha-1][coluna-1]) = 'X'
    else :
     (matriz[linha-1][coluna-1]) = 'O'
    if (testa_vencedor()) :
         if rodada%2==0 :
          print("\n\n JOGADOR 1 VENCEU !!\n")
          break
         else :
          print("\n\n JOGADOR 2 VENCEU !!\n")
          break  
    rodada+=1
    print("\n\n\n\n\n\n\n\n")

if op == 2 :
 nivel = int(input("\n[1] - FACIL\n[2] - DIFÍCIL\n\nESCOLHA SEU NIVEL : "))
 while (True) :
  print("\t\t\t\t\t\tJ O G O  D A  V E L H A  ")
  mostra_tabuleiro()
  if rodada == 9 :
        print ("\nDEU VELHA !! \n\n")
        break
  if rodada%2 ==0 :
     print(f'\nFaça sua jogada ! (X)\n')
  while (True) :
    if rodada%2==0 :
       linha = int(input("Informe a linha : "))
       coluna = int(input("Informe a coluna : "))
       if (linha>=1 and linha<=3) and (coluna>=1 and coluna <=3) and (matriz[linha-1][coluna-1] ==' '): 
         (matriz[linha-1][coluna-1]) = 'X'
         break
       else : 
         print("\n Coordenadas inválidas ou posição já preenchida !!\n")
    else :
        if nivel==1 :
          while(1) :
           linha = random.randint(1,3)
           coluna = random.randint(1,3)
           if matriz[linha-1][coluna-1] ==" " :
            matriz[linha-1][coluna-1] = "O"
            break
        if nivel==2:
         while (1) :
          linha = random.randint(1,3)
          coluna = random.randint(1,3)
          a = defesa()
          if a==0 and matriz[linha-1][coluna-1] ==' ':
           matriz[linha-1][coluna-1] = "O"
           break
          else :
           break
        print("\nO COMPUTADOR ESTA JOGANDO....\n")
        time.sleep(3)
        break
  if (testa_vencedor()) :
          if rodada%2==0 :
              print("\n\n VOCE VENCEU !!\n")
              break
          else :
           print("\n\n O COMPUTADOR VENCEU !!\n")
           break  
  rodada+=1 
  print("\n\n\n\n\n\n\n\n")
