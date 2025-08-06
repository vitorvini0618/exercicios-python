import os

mensagens = []

nome1 = input('Nome da Pessoa 1: ')
nome2 = input('Nome da Pessoa 2: ')

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  

    if mensagens:
        print(" HISTÓRICO DO CHAT")
        for m in mensagens:
            print(f"{m['nome']}: {m['texto']}")
        print('------------------------\n')

    texto1 = input(f"{nome1}, sua mensagem (ou 'fim' pra sair): ")
    if texto1.lower() == 'fim':
        break
    mensagens.append({"nome": nome1, "texto": texto1})

    os.system('cls' if os.name == 'nt' else 'clear')  

    print(" HISTÓRICO DO CHAT")
    for m in mensagens:
        print(f"{m['nome']}: {m['texto']}")
    print('------------------------\n')

    texto2 = input(f"{nome2}, sua mensagem (ou 'fim' pra sair): ")
    if texto2.lower() == 'fim':
        break
    mensagens.append({"nome": nome2, "texto": texto2})

