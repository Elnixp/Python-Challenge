import random
aluno1 = input('Qual o nome do primeiro aluno?: ')
aluno2 = input('Qual o nome do segundo aluno?: ')
aluno3 = input('Qual o nome do terceiro aluno?: ')
aluno4 = input('Qual o nome do quarto aluno?: ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)
print('Os alunos são {}, {}, {}, {}. O escolhido para apagar o quadro hoje é {}.'.format(aluno1, aluno2, aluno3, aluno4,
                                                                                         sorteio))
