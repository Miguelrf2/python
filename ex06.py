# Exercício - sistema de perguntas e respostas
ask = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Option': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Option': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Option': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

correct = 0     #Correct Questions  
indice = 0
numCorrect = 2
for i in ask:
    print('Question: ', i['Pergunta'])
    options = i['Option']
    for j, option in enumerate(options):
        print(f'{j})', option)
    print()
    question = input()
    inInt = int(question)
    if inInt > j or inInt < 0:
        print("Error expected: You choosed a invalid number")
    else:
        if inInt == enumerate[option]:
            print('Acertou!! 😎😎')
            correct += 1
        else:
            print('Errou! ❌')
            print(i['Resposta'][indice])
print(f'You choosed {correct}/3 correct questions ')