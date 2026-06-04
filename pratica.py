# Verificador de login e senha

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

login_correto = "admin"
senha_correta = "123456"

if login == login_correto and senha == senha_correta:
    print("Login bem-sucedido!")
else:    print("Login ou senha incorretos. Tente novamente.")
