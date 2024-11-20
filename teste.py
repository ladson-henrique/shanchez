
print("CALCULADORA")

ligar = input("Ligar (sim/não): ").strip().lower()

if ligar == "sim":
    print("Calculadora Ligada \n")
    while ligar == "sim":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("\n")


        print("Escolha uma Operação: \n")

        operacao = ""

        while operacao not in ["1", "2", "3", "4"]:
            print("Adição (1)")
            print("Subtração (2)")
            print("Multiplicação (3)")
            print("Divisão (4)")

            operacao = input("Escolha a operação: ").strip()
            print("\n")


            if operacao == '1':
                resultado = a + b
                print(f"O resultado da adição ({a} + {b}) é: {resultado}")
            elif operacao == '2':
                resultado = a - b
                print(f"O resultado da subtração ({a} - {b}) é: {resultado}")
            elif operacao == '3':
                resultado = a * b
                print(f"O resultado da multiplicação ({a} * {b}) é: {resultado}")
            elif operacao == '4':
                if b != 0:
                    resultado = a / b
                    print(f"O resultado da divisão ({a} / {b}) é: {resultado}")
                else:
                    print("Erro: Não é possível dividir por zero.")
            else:
                print("Opção inválida! Por favor, escolha uma operação válida. \n")
    
        desligar =input("Deseja desligar a calculadora? (sim/não): ").strip().lower()
        print("\n")
        if desligar == "sim":
            print("Desligando a calculadora...")
            break
        else:
            print("Calculadora ligada. Pronta para a novas operações!")
else:
    print("Calculadora desligada. Até logo!")