# Função responsável por exibir o menu principal e capturar a escolha do usuário
def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Criar conta
    [u] Criar usuáio
    [q] Sair
    => """
    return input(menu)


#============================================================================
# DEPOSITAR
# Requisitos: A funçãp depósito deve receber os argumentos apenas por posição (Positional only). Sugestão de argumentos: saldo, valor, extrato.
## Sugestão de retorno : saldo e extrato. 
### Implementações: A variável valor estava dentro da função desitar, foi retidada e passada para o bloco main, antes da chamada da função.
### Foi incluido a / no final, que em python significa que todos os argumentos antes da barra são obrigatoriamente posicionais.
#============================================================================
# Função que gerencia o depósito de valores na conta
def depositar(valor, saldo, extrato, /):
    try:
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


#============================================================================
# SACAR
# Requisitos: A função saque deve receber os argumentos apenas por nome (Keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques,
# limite_saques.
## Sugestão de retorno: saldo e extrato
### Implementações: ###
### . A variável valor estava dentro da função desitar, foi retidada e passada para o bloco main, antes da chamada da função, assim atendendo o requisito de Positional Only.
### . variável limite_saque era Global e agora é local
### . Foi incluido o * antes de todos os agumentos, indicando que todos os argumentos após o * são nomeados
#============================================================================
# Função que gerencia o saque de valores da conta
def sacar(*, saldo, valor, limite, extrato, numero_saques, limite_saque):
    try:
        # Verifica se o saque é válido
        if valor <= 0:
            print("Erro: O valor do saque deve ser maior que zero.")
        elif valor > saldo:
            print("Erro: Saldo insuficiente.")
        elif valor > limite:
            print("Erro: O valor do saque excede o limite permitido.")
        elif numero_saques >= limite_saque:
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


#============================================================================
# EXTRATO
# Requisitos: A função extrato deve receber os argumentos por posição e nome (positional onlye e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato
### Implementações: Incluído a / indicando que todos os argumentos antes da barra são posicionais e o * indicando que todos os argumentos após ele são nomeados
#============================================================================
# Função para exibir o extrato completo e o saldo atual
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    
    # Exibe mensagem caso não haja movimentações
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        print(extrato)
    
    # Exibe o saldo atual
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("========================================")


#============================================================================
# NOVAS FUNÇÕES: criar_usuario, criar_conta_corrente
#============================================================================

#============================================================================
# CRIAR_USUARIO
# Requisitos: O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string
# com formato: logradouro, nro - bairro - cidade/UF. Deve ser armazenado somente os númerosdo CPF. Não podemos cadastrar 2 usuários  com o mesmo cpf (Unique)
#============================================================================
# Lista para armazenar os usuários
usuarios = []

# Função para criar um novo usuário
def criar_usuario():
    # Coleta de informações do usuário
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    
    # Validação do CPF (apenas números)
    while True:
        cpf = input("Digite o CPF (apenas números): ").strip()
        if len(cpf) == 11 and cpf.isdigit():
            break
        print("CPF inválido. O CPF deve conter 11 números.")
    
    # Verifica se o CPF já foi cadastrado
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: Usuário com este CPF já está cadastrado.")
            return
    
    # Coleta do endereço
    endereco = input("Digite o endereço no formato 'logradouro, nro - bairro - cidade/UF': ")
    
    # Cria um dicionário com os dados do usuário
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    
    # Adiciona o usuário à lista de usuários
    usuarios.append(usuario)
    print(f"Usuário {nome} criado com sucesso!")


#============================================================================
# CRIAR_CONTA_CORRENTE
# Requisitos: O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, inicial
# em 1. O número da agência é fixo: 0001. O usuário pode ter mais de uma conta, mas uma conta pertence somente à um usuario (um para muitos a relação)
#============================================================================
# Lista para armazenar as contas
contas = []
# Contador sequencial para os números das contas
numero_conta = 1

# Função para criar uma nova conta corrente
def criar_conta_corrente():
    global numero_conta
    
    # Exibe os usuários cadastrados
    if not usuarios:
        print("Erro: Nenhum usuário encontrado. Crie um usuário primeiro.")
        return
    
    print("\nLista de usuários:")
    for i, usuario in enumerate(usuarios):
        print(f"{i + 1}. {usuario['nome']} (CPF: {usuario['cpf']})")
    
    # Seleciona o usuário para associar à conta
    while True:
        try:
            opcao = int(input("\nSelecione o número do usuário para associar à conta: "))
            if 1 <= opcao <= len(usuarios):
                usuario_selecionado = usuarios[opcao - 1]
                break
            else:
                print("Erro: Número inválido. Tente novamente.")
        except ValueError:
            print("Erro: Digite um número válido.")
    
    # Define os dados da conta corrente
    conta = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': usuario_selecionado
    }
    
    # Incrementa o número sequencial da conta
    numero_conta += 1
    
    # Adiciona a conta à lista de contas
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}\n")



# Função principal que gerencia a interação do usuário com o sistema bancário
def main():
    saldo = 0  # Saldo inicial da conta
    extrato = ""  # Extrato de movimentações
    numero_saques = 0 # Inicializa fora do loop

    # Loop principal do sistema bancário
    while True:
        # Exibe o menu e captura a escolha do usuário
        opcao = exibir_menu()

        # Condicional para as operações baseadas na escolha do usuário
        if opcao == "d":
            ### Implementações: Agora a chamada da função é posicional e a variável valor é passada antes da chamada da função
            # Solicita o valor do depósito ao usuário
            valor = float(input("Informe o valor do depósito: R$ "))
            # Executa o depósito
            saldo, extrato = depositar(valor, saldo, extrato)
        elif opcao == "s":
            ### Implementações: Agora a chamada da função é nomeada e a variável valor é passada antes da chamada da função
            # Solicita o valor do saque ao usuário
            valor = float(input("Informe o valor do saque: R$ "))
            limite = 500  # Limite de saque diário
            limite_saque= 3  # Limite de saques diários permitidos
            
            # Executa o saque
            saldo, extrato, numero_saques = sacar(
                saldo = saldo, 
                valor = valor, 
                limite = limite, 
                extrato = extrato, 
                numero_saques = numero_saques, 
                limite_saque = limite_saque
            )
        elif opcao == "e":
            # Exibe o extrato completo
            exibir_extrato(
                saldo, 
                extrato = extrato
            )
        elif opcao == "u": 
            criar_usuario()
        elif opcao == "c":
            criar_conta_corrente()
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
