import random

cartas = [1,2,3,4,5,6,7,8,9,11]
jogador = "jogador"
dealer = "dealer"

resultado_jogador =  random.choice(cartas) + random.choice(cartas)
resultado_dealer = random.choice(cartas) + random.choice(cartas)

#Resultado
if resultado_jogador <= 21:
      print ("O jogador tem " + str(resultado_jogador) + " pontos")
      print ("O dealer tem " + str(resultado_dealer) + " pontos")
else: 
      print ("O jogador obteve " + str(resultado_jogador) + " pontos, rebentou e o dealer venceu.")

#Vencedor
if resultado_jogador > resultado_dealer:
      print("\nO jogador venceu!")
elif resultado_jogador == resultado_dealer:
      print("\nO jogo empatou.")
else:
      print("\nO dealer venceu!")


