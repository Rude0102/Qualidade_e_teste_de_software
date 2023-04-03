senha=("Digite uma senha que contenha a primeira letra maiúscula!,um caracter especial e um número: ")


def MinimoDeCaracter(senha):
   quantidade=len(senha)
   if quantidade>=6 and quantidade<=10:
      print("Possui os caracteres necessários")
   else:
      print("Não possui os caracteres necessários")



def LetraMaiúscula(senha):
    if senha[0].isupper():
        print("A primeira Letra é maiúscula!")
    else:
        print("A primeira letra não é maiúscula!")



def Numero(senha):
  if senha.isdigit():
    print("A senha possuí números")
  else:
    print("Não possui números")



def LetraMinuscula(senha):
  if senha.islower():
    print("Possui letra minuscula")
  else:
    print("Não possui letra minuscula")


def CaracterEspecial(senha):
   if senha.isalpha():
      print("A senha possuí caracter especial")
   else:
      print("A senha não possui caracter especial")

    

if __name__== "__main__":
    MinimoDeCaracter(senha)
    LetraMaiúscula(senha)
    Numero(senha)
    LetraMinuscula(senha)
    CaracterEspecial(senha)