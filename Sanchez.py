print("Bem vindo a Sanchez Barber Shop \n")

print("Selecione uma opção abaixo. \n")

opcao = ""

while opcao != ["1", "2", "3"]:

        print("1) Marcar horario")
        print("2) Reagendar horario")
        print("3) Cancelar marcação")
        print("4) Sair \n")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            nome = input("Digite seu nome: \n").strip()
            print("\n")
            numero = (input("Número de telemóvel: \n")).strip()
            print("\n")
            email = input("Digite seu E_mail: \n").strip()
            print("\n")
            dia = (input("Escolha uma Data: (formato: dd/mm) \n")).strip()
            print("\n")
            horario = (input("Escolha um horario: (formato: HH/MM) \n")).strip()
            print("\n")

            print("Seu horario foi marcado, vejo você em breve!:")

        elif opcao == '2':
            print("Digite seu nome:")
            nome = input("nome: \n").strip()

            print("Informe a nova data ?")
            dia = (input("Escolha um dia: (formato: dd/mm) \n")).strip()

            print("Qual horario você gostaria de marcar ?")
            horario = (input("Escolha um horario: (formato: HH/MM) \n")).strip()

            print("Seu horario foi remarcado, vejo você em breve!:")

        elif opcao == '3':
            print("informe seu nome:")
            nome = (input("nome: \n")).strip()
            print("Quer mesmo desmarcar seu horario ?")
            cancelar = (input("(sim/não) \n")).strip()

            if cancelar == 'sim':
                print("Marcação cancelada.")
            else:
                print("Marcação não cancelada, até logo!")
        elif opcao == '4':
            print("")
        else:
            print("Opção inválida, por favor escolha outra opção válida. \n")