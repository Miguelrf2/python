number = [1, 2, 2, 4, 5, 6, 7, 6]
inSet = set()
primeiroDulicado = -1

def find():
    for i in number:
        if i in inSet:
            primeiroDulicado = i
            break

        inSet.add(i)
    return primeiroDulicado 

print(number, find())