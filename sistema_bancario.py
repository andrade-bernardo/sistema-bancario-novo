import textwrap

# Usuários e contas são armazenados em listas
usuarios = []
contas = []

# Função para encontrar usuário por CPF
def filtrar_usuario(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

# Função para criar novo usuário
def criar_usuario():
    cpf = input("Informe o CPF (somente número): ")
    if filtrar_usuario(cpf):
        print("⚠️ Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })

    print("✅ Usuário criado com sucesso!")

# Função para criar nova conta
def criar_conta(agencia="0001"):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf)

    if usuario:
        numero_conta = len(contas) + 1
        contas.append({
            "agencia": agencia,
            "numero": numero_conta,
            "usuario": usuario,
            "saldo": 0,
            "extrato": "",
            "limite": 500,
            "saques": 0,
            "LIMITE_SAQUES": 3
        })
        print("✅ Conta criada com sucesso!")
    else:
        print("❌ Usuário não encontrado.")

# Função para listar contas
def listar_contas():
    for conta in contas:
        linha = f"""\
            Agência: {conta['agencia']}
            Conta: {conta['numero']}
            Titular: {conta['usuario']['nome']}
        """
        print("=" * 30)
        print(textwrap.dedent(linha))

# Função de depósito
def depositar(conta):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print("✅ Depósito realizado com sucesso!")
    else:
        print("❌ Valor inválido.")

# Função de saque
def sacar(conta):
    valor = float(input("Informe o valor do saque: "))

    if valor <= 0:
        print("❌ Valor inválido.")
    elif valor > conta["saldo"]:
        print("❌ Saldo insuficiente.")
    elif valor > conta["limite"]:
        print("❌ Valor excede o limite por saque.")
    elif conta["saques"] >= conta["LIMITE_SAQUES"]:
        print("❌ Número máximo de saques atingido.")
    else:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["saques"] += 1
        print("✅ Saque realizado com sucesso!")

# Função de extrato
def exibir_extrato(conta):
    print("\n========== EXTRATO ==========")
    print(conta["extrato"] if conta["extrato"] else "Não foram realizadas movimentações.")
    print(f"Saldo: R$ {conta['saldo']:.2f}")
    print("=" * 28)

# Função principal
def menu():
    while True:
        print("""
        ========== MENU ==========
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nc] Nova conta
        [lc] Listar contas
        [nu] Novo usuário
        [q] Sair
        ==========================
        """)

        opcao = input("Escolha uma opção: ")

        if opcao == "d":
            numero = int(input("Informe o número da conta: "))
            conta = next((c for c in contas if c["numero"] == numero), None)
            if conta:
                depositar(conta)
            else:
                print("❌ Conta não encontrada.")

        elif opcao == "s":
            numero = int(input("Informe o número da conta: "))
            conta = next((c for c in contas if c["numero"] == numero), None)
            if conta:
                sacar(conta)
            else:
                print("❌ Conta não encontrada.")

        elif opcao == "e":
            numero = int(input("Informe o número da conta: "))
            conta = next((c for c in contas if c["numero"] == numero), None)
            if conta:
                exibir_extrato(conta)
            else:
                print("❌ Conta não encontrada.")

        elif opcao == "nu":
            criar_usuario()

        elif opcao == "nc":
            criar_conta()

        elif opcao == "lc":
            listar_contas()

        elif opcao == "q":
            print("👋 Saindo do sistema...")
            break

        else:
            print("❌ Opção inválida.")

# Executa o programa
menu()
