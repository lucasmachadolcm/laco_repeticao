def calcular_reajuste(salario_atual):
    if salario_atual <= 280:
        percentual_aumento = 20
    elif 280 < salario_atual <= 700:
        percentual_aumento = 15
    elif 700 < salario_atual <= 1500:
        percentual_aumento = 10
    else:
        percentual_aumento = 5

    aumento = salario_atual * (percentual_aumento / 100)
    novo_salario = salario_atual + aumento
    inflacao = 3.8 / 100
    aumento_real = aumento - (novo_salario * inflacao)

    return (salario_atual, percentual_aumento, aumento, novo_salario, aumento_real)

# Laço de repetição para entrada múltipla
while True:
    try:
        print("Digite o salário atual do colaborador ")
        print("Ou digite 0 para sair")
        salario = float(input("R$: "))
        if salario == 0:
            break
        resultado = calcular_reajuste(salario)
        print(f"\nSalário antes do reajuste: R$ {resultado[0]:.2f}")
        print(f"Percentual de aumento aplicado: {resultado[1]}%")
        print(f"Valor do aumento: R$ {resultado[2]:.2f}")
        print(f"Novo salário, após o aumento: R$ {resultado[3]:.2f}")
        print(f"Valor do aumento real, descontado a inflação: R$ {resultado[4]:.2f}\n")
    except ValueError:
        print("Por favor, insira um valor numérico válido.")
