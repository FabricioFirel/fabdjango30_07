def adicionar():
    print("\n=== Adicionar Item ===\n")
    chave = input("Digite o nome do item: ")
    valor = int(input("Digite a quantidade do item: "))

    if chave in estoque:
        print("Item já existe no estoque.")
        return
    else:
        estoque[chave] = valor
        return

def main():
    estoque={"Caneta": 10, "Caderno": 5, "Lápis": 20}

    while True:
        print("Menu:")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Listar")
        print("4. Sair")
        

        op = input("Escolha uma opção: ")



        match op:
            case "1":
                adicionar(estoque)
             case "2":
                print("Option 2 selected")
            case "3":
                print("Option 3 selected")    
            case "4":
                print("Option 4 selected")          
            case _:
                print("Invalid option selected")