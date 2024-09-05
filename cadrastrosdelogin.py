import os
import time
import getpass
email = []
senha = []


while True:
  print("************")
  print("Bem vindo ao sistema de login")
  print("1 - Cadastrar")
  print("2 - Ver logins salvos")
  print("3 - Limpar tela")
  print("4 - Sair")
  print("************")

  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    print("Digite seu email:")
    login = input("")
    email.append(login)

    print("Digite sua senha(obs: a senha estará oculta):")
    senha_digitada = getpass.getpass("")
    senha.append(senha_digitada)
    novamente = input("Deseja cadastrar outra conta? (s/n):")
    if novamente.lower() == "n":
      os.system('clear')
    elif novamente.lower() == "s":
      print("Digite seu email:")
      login = input("")
      email.append(login)

      print("Digite sua senha(obs: a senha estará oculta):")
      senha_digitada = getpass.getpass("")
      senha.append(senha_digitada)	
      print("senhas adicionadas com sucesso!")
      time.sleep(2)
      os.system('clear')
    else:
      print("*use apenas S ou N!*")
      time.sleep(2)
      os.system('clear')


  elif opcao == "2":
    os.system('clear')
    print("Emails cadastrados(Veja os números correspondentes):")
    for i, email in enumerate(email):
      print(f"{i+1}. {email}")
    print("Senhas cadastradas:")
    for i, senha in enumerate(senha):
      print(f"{i+1}. {senha}")
    print("****************")
  elif opcao == "3":
    os.system('clear')
  elif opcao == "4":
    print("tem certeza que deseja sair?Todos seus dados serão perdidos!")
    print("1 - sim")
    print("2 - não")
    
    decisao = input("Digite sua decisão? ")
    if decisao == "1":
      os.system('clear')
      break
      
    elif decisao == "2":
      os.system('clear')
    else:
      print("digite apenas 1 ou 2!")
      time.sleep(2)
      os.system('clear')

  else:
    print("Opção inválida. Tente novamente.")
    time.sleep(1)
    os.system('clear')




print("programa encerrado, obrigado por usar!")
