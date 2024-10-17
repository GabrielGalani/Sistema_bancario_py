# Função responsável por exibir o menu principal e capturar a escolha do usuário
def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """
    return input(menu)

# Função que gerencia o depósito de valores na conta
def depositar(saldo, extrato):
    try:
        # Solicita o valor do depósito ao usuário
        valor = float(input("Informe o valor do depósito: R$ "))
        
        # Verifica se o valor é válido (maior que zero)
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
        else:
            print("Erro: O valor do depósito deve ser maior que zero.")
    except ValueError:
        # Captura erro caso o valor inserido não seja um número válido
        print("Erro: Valor inválido. Por favor, insira um número válido.")
    
    # Retorna o saldo atualizado e o extrato com a nova movimentação
    return saldo, extrato

# Função que gerencia o saque de valores da conta
def sacar(saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    try:
        # Solicita o valor do saque ao usuário
        valor = float(input("Informe o valor do saque: R$ "))
        
        # Verifica se o saque é válido
        if valor <= 0:
            print("Erro: O valor do saque deve ser maior que zero.")
        elif valor > saldo:
            print("Erro: Saldo insuficiente.")
        elif valor > limite:
            print("Erro: O valor do saque excede o limite permitido.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Erro: Número máximo de saques diários excedido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
    except ValueError:
        # Captura erro caso o valor inserido não seja um número válido
        print("Erro: Valor inválido. Por favor, insira um número válido.")
    
    # Retorna o saldo atualizado, extrato e número de saques realizados
    return saldo, extrato, numero_saques

# Função para exibir o extrato completo e o saldo atual
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    
    # Exibe mensagem caso não haja movimentações
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        print(extrato)
    
    # Exibe o saldo atual
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("========================================")

# Função principal que gerencia a interação do usuário com o sistema bancário
def main():
    saldo = 0  # Saldo inicial da conta
    limite = 500  # Limite de saque diário
    extrato = ""  # Extrato de movimentações
    numero_saques = 0  # Número de saques realizados
    LIMITE_SAQUES = 3  # Limite de saques diários permitidos

    # Loop principal do sistema bancário
    while True:
        # Exibe o menu e captura a escolha do usuário
        opcao = exibir_menu()

        # Condicional para as operações baseadas na escolha do usuário
        if opcao == "d":
            # Executa o depósito
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            # Executa o saque
            saldo, extrato, numero_saques = sacar(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)
        elif opcao == "e":
            # Exibe o extrato completo
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            # Sai do sistema
            print("Saindo... Obrigado por utilizar o sistema.")
            break
        else:
            # Caso o usuário escolha uma opção inválida
            print("Erro: Opção inválida. Por favor, escolha uma opção válida.")

# Executa o código principal caso o script seja executado diretamente
if __name__ == "__main__":
    main()
