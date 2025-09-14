nome = []
num = []


print('\033[1m\033[36m=====================================')
print('|                                   |')
print('|    < GERENCIADOR DE CONTATOS >    |')
print('|                                   |')
print('=====================================\033[m')


def opcoes():
    opçoes = input('\n\033[1m[\033[1m\033[36m1\033[m\033[1m] Cadastrar' \
                    '\n\033[1m[\033[1m\033[32m2\033[m\033[1m] Listar\033[m' \
                    '\n\033[1m[\033[1m\033[36m3\033[m\033[1m] Atualizar\033[m' \
                    '\n\033[1m[\033[1m\033[32m4\033[m\033[1m] Excluir\033[m' \
                    '\n\033[1m[\033[1m\033[36m5\033[m\033[1m] Sair\033[m' \
                    '\n\033[1mQual você escolhe: ')
    
    while True:

        if opçoes == '1':
            print('=' * 20)
            c_nome = input("Qual seu nome: ")
            nome.append(c_nome)
            c_num = input("Qual seu numero: ")
            print('=' * 20)
            num.append(c_num)
            print("\n\033[32mCadastro realisado com sucesso!\033[m")
            break

        elif opçoes == '2':
            print(f'Nomes: {nome} | Número: {num}')
            break


        elif opçoes == '3':
            if len(nome) == 0:
                print('\n> Nenhum contato cadastrado <')
                break

            elif len(nome) > 0:
                for i in range(len(nome)):
                        print(f'[{i + 1}] Nome: {nome[i]} | Número: {num[num]}')
                
                at_contato = int(input('Digite a posição dos contatos para modificar: ')) -1

                if 0 <= at_contato < len(nome):
                    novo_nome = input('Digite um novo nome: ')
                    nome[at_contato] = novo_nome
                    novo_num = input('Digita o novo número: ')
                    num[at_contato] = novo_num

                else:
                    print('\n\033[31mPosição inválida\033[m')


        elif opçoes == '4':
            for i in range(len(nome)):
                        print(f'[{i + 1}] Nome: {nome[i]} | Número: {num[num]}')

            conta = int(input("Qual contato deseja excluir: ")) + 1
            if conta <= len(nome):
                nome.remove(nome[conta])
                num.remove(num[conta])
            else:
                print("\n\033[31mNão existe contato para excluir\033[m")


        elif opçoes == '5':
            print("\033[1m\033[32m================\033[m")
            print("\033[1m\033[32m |  Até Mais  |\033[m")
            print("\033[1m\033[32m================\033[m")
            exit()
        

        else:
            print('\n\033[31m>  Opção Inválida  <\033[m')            
            break
            

while True:
    opcoes()
