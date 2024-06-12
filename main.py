import banco

clientes = [
    {"nconta": 1717, "titular": "SHURA"},
]

def login(nconta, titular):
    for cliente in clientes:
        if cliente["nconta"] == nconta and cliente["titular"] == titular:
            return True
    return False

while True:
    try:
        login_nconta = int(input('Digite o número da conta: '))
    except ValueError:
        print("Digite números inteiros")
    login_titular = input("Digite o nome do titular: ").upper()
    
    if login(login_nconta, login_titular):
        print(f"Bem vindo, {login_titular}")
        break
    else:
        print("Conta ou Titular inválidos")

cliente_validado = banco.ContaBancaria(login_nconta, login_titular)
while True:
    print('O que você deseja fazer?')
    print('1. Verificar saldo \n2. Depositar \n3. Sacar\n4. Sair ')
    
    menuop = input(" Digite o número da opção: ")
    if menuop == "1":
        saldo = cliente_validado.verificar_saldo()
        print(saldo)
    elif menuop == "2":
            try:
                valor = float(input("Digite o valor para depositar: "))
                cliente_validado.depositar(valor)
                print("Depósito realizado com sucesso!")
            except ValueError:
                print("Digite um valor válido.")
    elif menuop == "3":
            try:
                valor_saque = float(input("Digite o valor para sacar: "))
                try:
                    cliente_validado.sacar(valor_saque)
                    print("Saque realizado com sucesso!")
                except ValueError as e:
                    print(e)
            except ValueError:
                print("Digite um valor válido.")
    elif menuop == "4":
        print("Volte sempre!")
        break
    else:
        print("Opção inválida, tente novamente.")
