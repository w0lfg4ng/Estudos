from math import factorial
##FUNÇÕES##
def arranjos():
    print("De acordo com a fórmula A = n!/(n-p)!, defina n e p")
    print("n = Quantidade de elementos a serem distribuidos entre o conjunto")
    print("p = Quantidade de elementos distintos tomados em um conjunto")
    print("Insira o valor de P")
    p = int(input())
    print("Insira o valor de n")
    n = int(input())
    facn = factorial(n)
    nMenosP = n-p
    facNMenosP = factorial(nMenosP)
    print('O número de arranjos A =', facn/facNMenosP)

def combinações():
   print("De acordo com a fórmula C = n!/p!(n-p)!")

print("Olá! Gostaria de começar a estudar análise combinatória?")
answer = input("Digite S para Sim e N para Não:")
if answer == "S" or answer == 's':
  print("Vamos começar!")
  print("Qual assunto você gostaria de estudar?")
  print("1 - Arranjos")
  print("2 - Combinações")
  print("3 - Permutações")
  print("5 - Princípio Fundamental de Contagem")
  answer01 = input()
  if(answer01 == "1"):
    arranjos()

        

elif answer == "N":
  print("Ok, até a próxima!")

