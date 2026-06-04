# Verificador de autorização para trabalho em construção

idade = int(input("Digite sua idade: "))
treinamento_em_dia = input("Você fez o treinamento de segurança?: ").lower() == "sim"
esta_com_epi = input("Você está usando os equipamentos de proteção individual (EPI)?: ").lower() == "sim"

if 18 <= idade <= 60 and treinamento_em_dia and esta_com_epi:
    print("Você está autorizado a trabalhar no local de construção.")

else:
    print("Você não está autorizado a trabalhar no local de construção.")

    if idade < 18 or idade > 60 :
        print("Requisito de idade não atendido.")
    if not treinamento_em_dia:
        print("Requisito de treinamento de segurança não atendido.")
    if not esta_com_epi:
        print("Requisito de uso de EPI não atendido.")