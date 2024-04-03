import textwrap

def menu():
  menu = """
  [d]\tDepositar
  [s]\tSacar
  [e]\tExtrato
  [nc]\tNova conta
  [nu]\tNovo usuário
  [lc]\tListar contas
  [q] Sair
  => """
  return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
  if valor > 0:
    saldo += valor
    extrato += f"Depósito R$ {valor:.2f} \n"
    print("Operação realizada com sucesso.")
  else: 
    print("Operação falhou: O valor informado é inválido.")
  return saldo, extrato

def sacar(*, saldo, valor, extrato, numero_saques, limite, limite_saques):
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_saques == limite_saques

  if excedeu_saldo:
    print("Operação falhou: Você não tem saldo suficiente para realizar esse saque.")
  elif excedeu_limite:
    print("Operação falhou: O valor desejado para saque é maior que o seu valor de limite.")
  elif excedeu_saques:
    print("Operação falhou: Você atingiu o número de saques diários permitidos.")
  elif valor <= 0:
    print("Operação falhou: O valor informado é inválido.")
  else:
    saldo -= valor
    numero_saques += 1
    extrato += f"Saque R$ {valor:.2f} \n"
    print("Operação realizada com sucesso.")

  return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
  print("Extrato")
  print("Não foram realizadas movimentações." if not extrato else extrato)
  print(f"\nSaldo atual: R$ {saldo:.2f}")

def procurar_usuario(cpf, usuarios):
  usuarios_localizados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuarios_localizados[0] if usuarios_localizados else None

def criar_usuario(usuarios):
  cpf = input("Informe o CPF (somente números):")
  usuario = procurar_usuario(cpf, usuarios)

  if usuario:
    print("Operação falhou: Já existe um usuário com esse CPF.")
    return

  nome = input("Informe o nome completo:")
  data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa):")
  endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/uf):")

  usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
  print("Operação realizada com sucesso.")
  return usuarios

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente números):")
    usuario = procurar_usuario(cpf, usuarios)

    if usuario:
      print("Operação realizada com sucesso.")
      return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
      print("Operação falhou: Usuário não encontrado com este CPF.")

def listar_contas(contas):
  print("Contas")
  print("=" * 100)
  if not contas:
    print("Nenhuma conta localizada.")
  else:
    for conta in contas:
      linha = f"""
        Agência:\t{conta["agencia"]}
        C/C:\t{conta["numero_conta"]}
        Titular:\t{conta["usuario"]["nome"]}
      """  
      print("=" * 100)
      print(textwrap.dedent(linha))
      a
def main():
  saldo = 0
  extrato = ""
  numero_saques = 0
  LIMITE = 500
  LIMITE_SAQUES = 3
  AGENCIA = "0001"
  usuarios = []
  contas = []

  while True:
    opcao = menu()
    if opcao == "d":
      print("Depósito")
      valor = float(input("Informe o valor a ser depositado: "))
      saldo, extrato = depositar(saldo, valor, extrato)    

    elif opcao == "s":
      print("Saque")
      valor = float(input("Informe o valor a ser sacado: "))
      saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, numero_saques=numero_saques, limite=LIMITE, limite_saques=LIMITE_SAQUES)     

    elif opcao == "e":
      exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
      criar_usuario(usuarios)

    elif opcao == "nc":
      numero_conta = len(contas) + 1
      conta = criar_conta(AGENCIA, numero_conta, usuarios)
      if conta:
        contas.append(conta)
    
    elif opcao == "lc":
      listar_contas(f
                    f)

    elif opcao == "q":
      break

    else:
      print("Operação inválida, por favor selecione novamente a operação desejada.")

main()