from classes import Person, Rent, Renter, User
from os import system as st


""" Samuel = Renter()
casa = Rent()
number      = 514
casa.description = "Localizado em frente a Universidade Federal, ótimo vista da cidade"
casa.street = "Cícero Duarte"
casa.number = 338
casa.situation   = True
casa.complement  = 'em frente à UFPI'
casa.cep         = '64600054'
casa.price       = 5000
casa.quality     = 4.8

Samuel.name      = 'Samuel Lelis'
Samuel.cpf       = '01937470300'
Samuel.telephone = '86999722699'
Samuel.email     = 'samuellelis88@gmail.com'

Samuel.printPerson()
casa.printRent() """

def addLocatario(LisLoc):
    loc = Renter()
    loc.name = input('Nome do Locatário >>')
    loc.cpf = input('CPF do Locatário >> ')
    loc.telephone = input('Telefone do Locatário >> ')
    loc.email = input('E-mail do Locatário >> ')
    print('<< Agora digite as informações sobre o Imóvel >>')
    loc.rent = Rent()
    loc.rent.number = int(input("Digite o número do imóvel >> "))
    loc.rent.description = input("Descreva o imóvel >> ")
    loc.rent.street = input('Nome da rua >> ')
    loc.rent.situation   = True
    loc.rent.complement  = input("Complemento >> ")
    loc.rent.cep         = input('CEP do Imóvel >>')
    loc.rent.price       = float(input("Preço do aluguel > "))
    loc.rent.quality     = 0
    LisLoc.append(loc)
    st("clear || cls")

Lista_de_locatarios = []
Lista_de_usuarios = []

def Menu():
    print(" _______________________________________")
    print("|                                       |")
    print("|  [0] - << Sair >>                     |")
    print("|  [1] - << Adicionar Locatário >>      |")
    print("|  [2] - << Adicionar Locador >>        |")
    print("|  [3] - << Visualizar Ímóveis >>       |")
    print("|_______________________________________|")

    return int(input('Escolha uma opção >> '))

while True:
    op = Menu()
    if op == 1:
        addLocatario(Lista_de_locatarios)
    elif op == 3:
        print()
        for x in Lista_de_locatarios:
            x.printPerson()
            x.rent.printRent()
    if op == 0:
        break


print("Success")
print("Success")