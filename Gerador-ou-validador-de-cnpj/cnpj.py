import re
from random import randint


def remove_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def gera_primeiro_digito(cnpj):
    multiplicadores = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum([x * int(y) for x, y in zip(multiplicadores, cnpj)])
    digito = 11 - (soma % 11)
    primeiroDigito = str(digito) if digito <= 9 else '0'
    return cnpj[:12] + primeiroDigito

def gera_segundo_digito(cnpj):
    multiplicadores = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum([x * int(y) for x, y in zip(multiplicadores, cnpj)])
    digito = 11 - (soma % 11)
    segundoDigito = str(digito) if digito <= 9 else '0'
    return cnpj + segundoDigito


def valida(cnpj):
    cnpj = remove_caracteres(cnpj)
    if len(cnpj) == 14 and cnpj != cnpj[0] * 14:
        cnpj_new = gera_primeiro_digito(cnpj)
        cnpj_new = gera_segundo_digito(cnpj_new)
        cnpj_new = ''.join(cnpj_new)
        if cnpj == cnpj_new:
            return True
        else:
            return False
    else:
        return False


def gera_um_novo_cnpj():
    cnpj = str(randint(10000000, 99999999))
    cnpj = cnpj + '0001'
    cnpj = gera_primeiro_digito(cnpj)
    cnpj = gera_segundo_digito(cnpj)
    cnpj = ''.join(cnpj)
    cnpj = cnpj[:2] + '.' + cnpj[2:5] + '.' + cnpj[5:8] + '/' + cnpj[8:12] + '-' + cnpj[12:14]
    return cnpj
