from collections import UserString
import random
import os

os.system('clear')

cartas = [1,2,3,4,5,6,7,8,9,11]

resultado_jogador =  random.choice(cartas) + random.choice(cartas)
resultado_dealer = random.choice(cartas) + random.choice(cartas)

#Vencedor
def Vencedor():
 if resultado_jogador > resultado_dealer:
      print("\nO jogador venceu!")
 elif resultado_jogador == resultado_dealer:
      print("\nO jogo empatou, logo o dealer venceu.")
 elif (resultado_dealer > 21):
       print ("\nO dealer rebentou, o jogador venceu.")
 else:
      print("\nO dealer venceu!")

def resultado():
       print ("\nO jogador tem " + str(resultado_jogador) + " pontos")
       print ("O dealer tem " + str(resultado_dealer) + " pontos")
       Vencedor()
if (resultado_jogador > 21): 
       print ("O jogador obteve " + str(resultado_jogador) + " pontos, rebentou e o dealer venceu.")

#Resultado
while resultado_dealer <= 16:
      resultado_dealer = resultado_dealer + random.choice(cartas)


while resultado_jogador < 21:
      print("A sua pontuação atual é de " + str(resultado_jogador) + " gostaria de tirar mais uma carta? (S/N)")
      escolha = input()
      if (escolha == "S"):
            resultado_jogador = resultado_jogador + random.choice(cartas)
            if (resultado_jogador > 21):
                   print ("\nO jogador obteve " + str(resultado_jogador) + " pontos, rebentou e o dealer venceu.")
            elif (resultado_jogador == 21):
                  print ("\nVocê fez blackjack!")
                  resultado()
      elif (escolha == "N"):
            resultado()
            break
      else:
            print ("Escolha (S) para sim e (N) para não.")




