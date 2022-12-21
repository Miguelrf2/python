import random

for i in range(100):
    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0,9))
    print(cpf)