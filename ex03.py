import random
def criaCpf():
    inStr = ''
    for i in range(0, 11):
        cpf = random.randint(0,9)
        inStr += str(cpf)
        toList = list(inStr)
    simbol = toList.insert(3, '-')
    simbol = toList.insert(7, '-')
    simbol = toList.insert(11, '.')
    cpfCompleto = ''
    for item in toList:
        cpfCompleto += item 
        try: 
            len(cpfCompleto) > 11 or len(cpfCompleto) <= 0
        except ValueError:
            print('Error expected: Max lenght = 11 numbers')

    return cpfCompleto

criarCpf = criaCpf()
print(criarCpf)
