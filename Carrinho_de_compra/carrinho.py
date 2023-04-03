import os
import unittest


produtos= [
    {'id':1,'nome':'Notebook','preco':2800},
    {'id':2,'nome':'Mouse','preco':38},
    {'id':3,'nome':'Teclado','preco':50},
    {'id':4,'nome':'Monitor','preco':850},
    ]



carrinho=[]

def Menorpreco(produtos):
    return min(produtos, key=lambda d:d['preco'])
    

desconto=Menorpreco(produtos)* 25/100
print(f"o valor do desconto no produto de menor valor é de {desconto}")

def exibirOpcoes():
    print('1 - adicionar Item')
    print('2 - Remover Item')
    print('3 - limpar Carrinho de compras')



def exibirProdutos():
    for i in produtos:
        print('Id: {0} - Nome:{1} - Preço: {2}\n'.format(i['id'],i['nome'],i['preco']))


opcao='1'


os.system('clear')
print('carrinho de Compras \n')

def obterNomeProduto(id):
    for i in produtos:
        if i['id'] == id:
            return['nome']


while opcao !='5':
    exibirOpcoes()
    opcao= input('Digite a opção: ')

    if(opcao == "1"):
        exibirProdutos()
        id = int(input("digite o identificador do produto: "))
        quantidade = int(input('Digite quantidade: '))
        carrinho.append({'id':id,'quantidade': quantidade})

    if opcao == '2':
        id = int(input('digite o identificador do produto: '))
        temp=[]
        for item in carrinho:
            if item['id']!= id:
                temp.append(item)

    if opcao== '3':
        print('\n\n')
        somatorio = 0
        for item in carrinho:
            for produto in produtos:
                if produto['id'] == item['id']:
                    somatorio = somatorio +\
                        (produto['preco']* item['quantidade'])
                    break

                print(
                'Nome: {0} - Quantidade: {1}'.format(obterNomeProduto(item['id']), item['quantidade']))
        print('Preço total: {0}'.format(somatorio))

    if opcao == '4':
        carrinho = []    




class TestCarrinho(unittest.TestCase):
    def setUp(self):
        self.carrinho = {}

    def test_adicionar_produto(self):
        adicionar_produto("Produto 1", 5)
        self.assertEqual(self.carrinho, {"Produto 1": 5})

    def test_adicionar_produto_existente(self):
        adicionar_produto("Produto 1", 5)
        adicionar_produto("Produto 1", 3)
        self.assertEqual(self.carrinho, {"Produto 1": 8})

    def test_remover_produto(self):
        adicionar_produto("Produto 1", 5)
        remover_produto("Produto 1", 3)
        self.assertEqual(self.carrinho, {"Produto 1": 2})

    def test_remover_produto_nao_existente(self):
        remover_produto("Produto 1", 3)
        self.assertEqual(self.carrinho, {})

    def test_calcular_subtotal(self):
        subtotal = calcular_subtotal("Produto 1", 5)
        self.assertEqual(subtotal, 37.5)

    def test_calcular_subtotal_desconto(self):
        subtotal = calcular_subtotal("Produto 1", 30)
        self.assertEqual(subtotal, 225)

if _name_ == '_main_':
    unittest.main()