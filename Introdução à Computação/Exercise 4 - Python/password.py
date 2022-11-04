import re

while True:
    password = input("Coloca a tua password: ")
    if len(password) <= 5:
        print("A tua password deve conter 6 ou mais carácteres")
    elif len(password) >= 16:
        print("A tua password não deve conter mais que 16 caracteres")
    elif re.search("[0-9]",password) is None:
        print("A tua password deve conter pelo menos um número")
    elif re.search('[a-z]',password) is None: 
        print("A tua password deve conter pelo menos uma letra minuscula")
    elif re.search('[A-Z]',password) is None: 
        print("A tua password deve conter pelo menos uma letra maiúscula")
    elif re.search('[$,#,@]',password) is None: 
        print("A tua password deve conter pelo menos um caracter especial")
    else:
        print("A tua password está ótima!")
