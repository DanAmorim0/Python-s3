#ATIVIDADE I - 05/02/2025

# Criar uma programa de um Zoológico com os atributos nome, localização e lista de animais.
# Um método que adiciona animais na lista e outro que imprime a lista de animais.
# Um método que abre e fecha o zoológico. Um método que imprime o status do zoológico
# (aberto ou fechado). Um outro método que imprime o nome e a localização do zoológico. E outro método que imprime o nome e a espécie de cada animal.

class Zoologico:
    def __init__(self, nome, localizacao ):
        self.nome = nome
        self.localizacao = localizacao
        self.lista_animal = []
        self.aberto = False

    def adicionar(self):
        nome = input("Digite o nome do animal:")
        especie= input("digite o nome da espécie:")
        self.lista_animal.append({"Nome:":nome, "especie:":especie})
        print(f"o {nome} foi adicionado ao zoologico")
    
        
    def imprimirlista(self):
        print("*****Lista de animais do zoologico*****")
        print(self.lista_animal)
    
    def abertura(self):
        print("deseja abrir ou fechar o zoologico?")
        abrefecha = input("fechar/abrir\n").strip().lower()
        if abrefecha == "fechar":
            self.aberto = False
            print("o zoologico esta fechado")
        elif abrefecha=="abrir":
            self.aberto = True
            print("o zoologico esta aberto")
        else:
            print("tente com um valor valido")
            
    def imprimir_status(self):
        if self.aberto == False:
            print("o zoologico esta fechado")
        else:
            print("o zoologico esta aberto")
            
    def imprimir_info(self):
        print(f"Nome do Zoologico: {self.nome}")
        print(f"localizacao do Zoologico: {self.localizacao}")
        
    def imprimir_animais(self):
        print("-----Lista de animais do zoologico------")
        #for animal in self.lista_animal:
        #   print(f"{animal['nome']} - {animal['especie']}")


nome_zoologico = input("digite o nome do zoologico:")
localizacao_zoologico = input("digite a cidade do zoologico")

nome_loc = Zoologico(nome_zoologico, localizacao_zoologico) 

while True:
    print("\nEscolha uma opção:")
    print("1 - Adicionar animal")
    print("2 - Listar animais")
    print("3 - Abrir ou Fechar o Zoológico")
    print("4 - Mostrar status do Zoológico")
    print("5 - Mostrar informações do Zoológico")
    print("6 - imprimir nome e especie dos animais, NAO ESTA RODANDO")
    print("7- sair do programa")
    
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        nome_loc.adicionar()
    elif opcao == "2":
        nome_loc.imprimirlista()
    elif opcao == "3":
        nome_loc.abertura()
    elif opcao == "4":
        nome_loc.imprimir_status()
    elif opcao == "5":
        nome_loc.imprimir_info()
    elif opcao == "6":
        nome_loc.imprimir_animais()
    elif opcao == "7":
         print("Saindo do programa...")
         break
    else:
        print("Opção inválida! Tente novamente.")