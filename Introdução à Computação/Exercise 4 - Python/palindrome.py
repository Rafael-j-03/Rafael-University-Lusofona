string=input(("Introduz uma palavara para verificar se é um palíndromo: "))

if(string==string[::-1]):
      print("Esta palavra é um palíndromo.")
else:
      print("Esta palavra não é um palíndromo.")