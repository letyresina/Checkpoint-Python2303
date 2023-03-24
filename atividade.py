"""
    Checkpoint 1 - 23/03/2023 
    Desenvolvido para as aulas de Computational Thinking - 1ESPH
    Alunas: 
        Camila Padalino - RM: 98316
        Leticia Resina - RM: 98069
 """

# Pedindo para o usuário digitar os números (enganando o usuário)
num1 = int(input("Informe um valor de número inteiro de 0 a 99: "))
num2 = int(input("Informe outro valor de numero inteiro de 0 a 99: "))

# Intervalo de 0 a 10 para pegar o 7 e transformar em 0
if (num1 >= 0 and num1 <= 9) or (num2 >= 0 and num2 <= 9):
    if num1 == 7:
        num1 = 0
    if num2 == 7:
        num2 = 0

# Condicional para quando o número que o usuário digitar for com 2 dígitos
if (num1 >= 10 and num1 <= 99) or (num2 >= 10 and num2 <= 99):
    #Separando os números de dois digitos do 1º número
    a1 = num1 // 10
    resto1 = num1 % 10
    b1 = resto1
     #Separando os números de dois digitos do 2º número
    a2 = num2 // 10 
    resto2 = num2 % 10
    b2 = resto2
    if (a1 == 7):
      a1 = 0
    if (b1 == 7):
      b1 = 0
    if (a2 == 7):
      a2 = 0
    if (b2 == 7):
      b2 = 0
    
    num1 = a1 * 10 + b1
    num2 = a2 * 10 + b2

# Realiza a operação
soma = num1 + num2

# Para descobrir se o valor possui 7 em algum momento
if (soma == 7):
    soma = 0
if (soma >= 8 and soma <= 198):
    a3 = soma // 10
    resto3 = soma % 10
    b3 = resto3
    if (a3 == 7):
        a3 = 0
    if (b3 == 7):
        b3 = 0
    soma = a3 * 10 + b3

# Mostrando o resultado final pro usuário com o vírus já funcionando
print(f"A soma entre esses dois números é: {soma}")
