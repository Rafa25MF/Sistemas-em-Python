import time

def titulo():

    print('\033[32m--------------------------------------------------------------')
    print('  |                                                         |')
    print('  |                        PAY PROZ                         |')
    print('  |                                                         |')
    print('--------------------------------------------------------------')


    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡾⢿⣶⣤⣀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⠟⢋⣥⣴⣶⣤⣙⠛⠿⣶⣤⣀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⡾⠟⣋⣡⣶⣾⣿⣿⣿⣿⣿⣿⣿⣶⣬⣉⠻⢿⣶⣤⣀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⡾⠟⣋⣥⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣬⣙⠻⢿⣶⣤⡀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⡿⠟⣋⣥⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣬⣙⠻⢿⣶⣄⣀")
    print("⠀⠀⠀⠀⠀⣾⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣷")
    print("⠀⠀⠀⠀⠀⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿")
    print("⠀⠀⠀⠀⠀⠈⠉⢹⣿⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹⣿⠉⠁")
    print("⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⠿⠿⠿⠿⠿⠏")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⡆⠀⢰⣿⣿⣿⣿⣷⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⣾⣿⣿⣿⣿⡆⠀⢰⣿⣿⣿⣿⣷")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⠀⢀⣴⣿⣿⣿⣿⠿⠏⠈⠿⢿⣿⣿⣿⣦⡀⠀⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⢀⣾⣿⣿⣿⠋⢀⣠⡄⠀⣤⣀⣸⣿⣿⣿⣷⡄⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣾⣿⣿⣿⡏⠀⢸⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠘⠛⠃⠀⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⡇⠀⣿⡇⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⠋⠉⠛⠇⠀⠟⠃⠀⣾⣿⣿⣿⠇⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⠀⠙⣿⣿⣿⣷⣶⣤⡄⠀⣤⣤⣾⣿⣿⣿⠏⠀⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⠀⠀⠈⠛⢿⣿⣿⣿⣿⣾⣿⣿⣿⡿⠟⠁⠀⠀⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠁⠀⠈⠛⠛⠛⠛⠋⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀ ⠙⠛⠛⠛⠛⠁⠀⠈⠛⠛⠛⠛⠋")
    print("⠀⠀⠀⠀⠀⠀⢰⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⡆")
    print("⢀⣀⣀⣀⣀⣀⣸⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⣇⣀⣀⣀⣀⣀⡀")
    print("⣿⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢻⣿")
    print("⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿")
    print("⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁")

def cofre():
    print("⢀⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣄⣀⣀⡀")
    print("⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠈⠉⠉⠉⠑⠒⡆")
    print("⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⡇⠀⠀⠀⠀⠀⠀⡇")
    print("⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡷⠃⠀⡤⡤⡄⠀⠀⢱")
    print("⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⡟⡝⡇⠀⠀⢸")
    print("⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠿⠼⠇⠀⠀⢸")
    print("⢸⣿⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡠⠔⠊⢹⣿⣇⡀⠀⠀⠉⠾⠀⠀⢸")
    print("⢸⣿⠀⠀⠠⠬⠝⢛⡛⠒⠉⢉⣉⡱⣮⠕⠂⠀⠀⢸⣿⡇⡇⠀⠀⠀⠀⠀⠀⡎")
    print("⢸⣿⠉⢉⡩⠝⠊⠁⠱⡊⠉⠁⠀⠀⢀⣉⠉⠒⠒⢼⣿⡗⠁⠀⠀⠀⠀⠀⠀⡇")
    print("⠘⣿⣤⣭⣽⣭⣭⣵⣶⣷⣤⣴⣮⣭⣥⣤⣭⣦⣤⣼⣿⣃⣀⡠⠤⠤⠤⠔⠒⠃")
    print("⠀⠈⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠁")

    print("⢀⠖⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⣄")
    time.sleep(0.5)
    print("⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇")
    time.sleep(0.5)
    print("⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡟⡇")
    time.sleep(0.5)
    print("⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠒⠀⠀⠀⠀⠀⠀⠀⣿⡷⠃")
    time.sleep(0.5)
    print("⢸⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⢠⣶⠶⢶⣄⠀⠀⠀⠀⠀⣿⡇")
    time.sleep(0.5)
    print("⢸⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⢻⣧⣀⣨⡿⠀⠀⠀⠀⠀⣿⡇")
    time.sleep(0.5)
    print("⢸⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠉⡛⠉⠀⠈⠀⠀⠀⠀⣿⣇⡀")
    time.sleep(0.5)
    print("⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⣿⡇⡇")
    time.sleep(0.5)
    print("⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡗⠁")
    time.sleep(0.5)
    print("⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠃")
    time.sleep(0.5)
    print("⠀⠈⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠁")
    time.sleep(0.5)

def menu():

    nome_arm = []
    cpf_arm = []
    senha_arm = []

    chave_pix = [1234567890]

    while True:
        munu_1 = int(input("\n--- Bem-Vindo à Agencia PAY PROZ ---"
                            "\n[ 1 ] CRIAR CONTA"
                            "\n[ 2 ] FAZER LOGIN"
                            "\n[ 3 ] SAIR"
                            "\n> ESCOLHA: "))
        

        if munu_1 == 1:
            print('--- Faça seu Cadastro ---')

            nome_cad = input('Digite seu Nome: ')
            nome_arm.append(nome_cad)

            cpf_cad = input('Digite seu CPF: ')
            cpf_arm.append(cpf_cad)

            senha_cad = int(input('Digite sua senha (SOMENTE NÚMEROS): '))
            senha_arm.append(senha_cad)
            

        elif munu_1 == 2:

            print('--- Faça login ---')

            cpf_log = input('CPF: ')
            senha_log = int(input('SENHA: '))


            while True:
                if cpf_log == cpf_arm[0] and senha_log == senha_arm[0]:
                    print('Login Bem-Sucedido!')

                    saldo = 100.00

                    while True:
                        menu_2 = int(input("\n--- MENU ---"
                                        "\n[ 1 ] Ver Saldo"
                                        "\n[ 2 ] Depósito"
                                        "\n[ 3 ] Sacar"
                                        "\n[ 4 ] Pix"
                                        "\n[ 5 ] SAIR"
                                        "\n> ESCOLHA: "))

                        if menu_2 == 1:
                            print(f'Seu SALDO é de R${saldo}')

                        elif menu_2 == 2:
                            dep = float(input('Digite o valor para depósito: '))
                            saldo += dep
                            print('Depósito Realizado')
                            print(f'Seu saldo: R${saldo}')

                        elif menu_2 == 3:
                            print(f'Seu saldo atual: R${saldo}')
                            sacar_su = float(input('Quanto deseja sacar: '))
                            if sacar_su > saldo:
                                print('<! Saldo Insuficiente !>')
                            else:
                                saldo -= sacar_su
                                print('Saque Realizado')
                                print(f'Seu saldo: R${saldo}')

                        elif menu_2 == 4:
                            conta = int(input('Digite a chave PIX: '))

                            if conta == chave_pix[0]:
                                pix = float(input('Digite o valor do PIX: '))

                                if pix > saldo:
                                    print('<! Saldo Insuficiente !>')
                                else:
                                    saldo -= pix
                                    print('PIX Realizado com Sucesso!')
                                    print(f'Seu saldo: R${saldo}')

                            elif conta != chave_pix[0]:
                                print('=============================')
                                print('<  CHAVE PIX NÃO EXISTENTE  >')
                                print('=============================')

                        elif menu_2 == 5:
                            print('==================')
                            print('<  DESCONECTADO  >')
                            print('==================')
                            break

                        else:
                            print('===================================')
                            print('< Opção inválida. Tente novamente >')
                            print('===================================')


            else:
                print('=============================')
                print('<! CPF ou SENHA incorretos !>')
                print('=============================')
                


       
        elif munu_1 == 3:
            print('==================')
            print('< Banco Trancado >')
            print('==================')

            cofre()
            break

        else:
            print('====================')
            print('<! Opção Inválida !>')
            print('====================')


titulo()
menu()
