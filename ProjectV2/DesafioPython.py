menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


#Deposito 
def Deposito():
    global saldo
    global extrato
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

#Saque
def Saque():
    global saldo
    global extrato
    global numero_saques
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
         print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

#Extrato
def Extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

#CriarUsuario
def CriarUsuario(): 
    cpf = input('Informe o CPF(Somente número): ')
    usuario = filtrarusuario(cpf,usuario)

    if usuario:
        print('\n@@@ Há um usuario existente com as mesmas informações')
        return
        
    nome = input('Informe o nome completo: ')
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input('Informe o endereço(Logradouro,bairro - cidade)')

    usuario.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(" --- Usuário criado com sucesso! ---")


# Filtrar Usuário Função
def filtrarusuario(cpf,usuarios):
    usuario_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf] 
    return usuario_filtrados[0] if usuario_filtrados else None

while True:
    opcao = input(menu)
    if opcao == "d":
        Deposito()
    elif opcao == "s":
        Saque()
    elif opcao == "e":
        Extrato()
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
