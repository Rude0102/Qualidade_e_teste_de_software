Nome=input(str('Digite nome completo: '))


def main(Nome):
    if Nome.isspace():
        print("O nome só contem espaços")
    else:
        print("Tudo certo")
        

def NomeEspaco(Nome):
    if Nome.rstrip(" "):
       print("Seu nome contém dois espaços")
    else:
        print('Tudo certo')
        

def NomeEspaco(Nome):
    if Nome.lstrip(" "):
       print("Seu nome contém dois espaços")        
    else:
        print('Tudo certo')
        
if __name__== "__main__":
    main(Nome)
    NomeEspaco(Nome)


