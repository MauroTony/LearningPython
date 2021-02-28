from random import randint
if __name__ == '__main__':
    cpf = str(randint(100000000, 999999999))
    while cpf == (cpf[0] * 9):
        cpf = str(randint(100000000, 999999999))
    countCPF = 0
    soma1digito = 0
    for count in range(10, 1, -1):
        soma1digito += count * int(cpf[countCPF])
        if count == 2:
            temp = (11 - (soma1digito % 11))
            primeiroDigito = temp if temp <= 9 else 0
        countCPF += 1
    countCPF = 0
    soma2digito = 0
    for count in range(11, 1, -1):
        if count == 2:
            soma2digito += 2 * primeiroDigito
            temp = (11 - (soma2digito % 11))
            segundoDigito = temp if temp <= 9 else 0
            break
        soma2digito += count * int(cpf[countCPF])
        countCPF += 1
    novoCPF = cpf[:9] + str(primeiroDigito) + str(segundoDigito)
    print(novoCPF)
