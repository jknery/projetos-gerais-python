'''
BIBLIOTECA DE FUNÇÕES E REGRAS DE NEGÓCIO DO APLICATIVO

FACULDADE DE CIÊNCIAS SOCIAIS APLICADAS - UNIFACISA
SISTEMAS DE INFORMAÇÃO - NOTURNO
DISCIPLINA: PROGRAMAÇÃO 1 - PYTHON 3.7
GRUPO: JOSÉ IVO KOERICH NERY - 182.308.00-07
       ARTUR RENE DA SILVA - 182.308.00-05
'''

import json

#OPÇÃO 1
######################################################################
def listAlunos():

    Aluno = {}
    file = open("DBAlunos.json", "r")
    Aluno = json.load(file)
    file.close()

    if len(Aluno) == 0:
        print("Cadastro Vazio!!!")
    else:
        chaves = list(Aluno.keys())
        chaves.sort()
        cont_alunos = 1
        for alunos in chaves:
            notas_aluno = Aluno[alunos]
            nota1 = notas_aluno[0]
            nota2 = notas_aluno[1]
            nota3 = notas_aluno[2]
            media = ((nota1 + nota2 + nota3) / 3)
            print('Nº[%i]. %s. Notas: 1.[%.1f] | 2.[%.1f] | 3.[%.1f] | Média: %.1f' % (
            cont_alunos, alunos, nota1, nota2, nota3, media))
            cont_alunos += 1


# OPÇÃO 2
######################################################################
def createAluno():

    Aluno = {}
    file_read = open("DbAlunos.json", "r")
    Aluno = json.load(file_read)
    file_read.close()

    nome = input("Digite o Nome do Aluno a ser Adicionado: ").upper()

    chaves = list(Aluno.keys())

    if nome in chaves:
        print("O Aluno já existe")
    else:
        Aluno[nome] = [0.0, 0.0, 0.0]
        file_write = open("DBAlunos.json", "w")
        json.dump(Aluno,file_write)
        file_write.close()


#OPÇÃO 3
######################################################################
def addrNotaAluno():

    Aluno = {}
    file_read = open("DbAlunos.json", "r")
    Aluno = json.load(file_read)
    file_read.close()

    nome = input("Digite o Nome do Aluno para Adicionar as Notas Referentes: ").upper()
    chaves = list(Aluno.keys())

    if nome not in chaves:

        print("O Aluno não está Matriculado!!")

    else:

        lista_notas = Aluno[nome]

        if len(lista_notas) == 3 and lista_notas[0] > 0 and lista_notas[1] > 0 and lista_notas[2] > 0:
            print("Notas já colocadas!!")

        else:
            nota1 = float(input("Digite a nota 1: "))
            nota2 = float(input("Digite a nota 2: "))
            nota3 = float(input("Digite a nota 3: "))
            Aluno[nome] = [nota1, nota2, nota3]

            file_write = open("DBAlunos.json", "w")
            json.dump(Aluno, file_write)
            file_write.close()

#OPÇÃO 4
######################################################################
def deleteAluno():

    Aluno = {}
    file_read = open("DbAlunos.json", "r")
    Aluno = json.load(file_read)
    file_read.close()

    nome = input("Digite o Nome do Aluno a ser Removido: ").upper()
    chaves = list(Aluno.keys())

    if nome not in chaves:
        print("O Aluno não está Matriculado!!")
    else:
        print("O Aluno %s foi removido!" %nome)
        del Aluno[nome]
        file_write = open("DBAlunos.json", "w")
        json.dump(Aluno, file_write)
        file_write.close()

#OPÇÃO 5
###############################################################################################
def deleteNotaAluno():

    Aluno = {}
    file_read = open("DbAlunos.json", "r")
    Aluno = json.load(file_read)
    file_read.close()

    nome = input("Digite o Nome do Aluno para deletar as Notas Referentes: ").upper()
    chaves = list(Aluno.keys())

    if nome not in chaves or len(Aluno) == 0:
        print("O Aluno não está Matriculado!!")

    else:
        notaDel = int(input("Digite a nota a ser deletada (1ª, 2ª, 3ª ou 0 para limpar tudo): "))

        if notaDel == 1:
            del Aluno[nome][0]
            Aluno[nome].insert(0,0.0)
            file_write = open("DBAlunos.json", "w")
            json.dump(Aluno, file_write)
            file_write.close()

        elif notaDel == 2:
            del Aluno[nome][1]
            Aluno[nome].insert(1, 0.0)
            file_write = open("DBAlunos.json", "w")
            json.dump(Aluno, file_write)
            file_write.close()

        elif notaDel == 3:
            del Aluno[nome][2]
            Aluno[nome].insert(2, 0.0)
            file_write = open("DBAlunos.json", "w")
            json.dump(Aluno, file_write)
            file_write.close()

        elif 0 == notaDel:
            Aluno[nome].clear()
            Aluno[nome] = [0.0, 0.0, 0.0]
            file_write = open("DBAlunos.json", "w")
            json.dump(Aluno, file_write)
            file_write.close()

#OPÇÃO 6
###############################################################################################
def updateNomeAluno():

    Aluno = {}
    file_read = open("DbAlunos.json", "r")
    Aluno = json.load(file_read)
    file_read.close()

    aluno_deseja_editar = input('Digite o nome do aluno que deseja editar:').upper()
    if aluno_deseja_editar in Aluno:
        aluno_editar = input('Digite o novo nome do aluno:').upper()
        Aluno[aluno_editar] = Aluno.pop(aluno_deseja_editar)
        file_write = open("DBAlunos.json", "w")
        json.dump(Aluno, file_write)
        file_write.close()
    else:
        print('Nome do aluno não existe')


# OPÇÃO 7
###############################################################################################
def updateNotaAluno():

    Aluno = {}
    file_read = open("DbAlunos.json", "r")
    Aluno = json.load(file_read)
    file_read.close()

    editar_nota = input('Digite o nome do aluno que deseja alterar a nota:').upper()
    if editar_nota in Aluno:
        nota_alterar = input(
            'especifique se é a "PRIMEIRA", "SEGUNDA" ou "TERCEIRA" nota que deseja alterar e digite a nova nota:').split()

        if editar_nota in Aluno and nota_alterar[0].upper() == 'PRIMEIRA':
            Aluno[editar_nota][0] = float(nota_alterar[1])
            file_write = open("DBAlunos.json", "w")
            json.dump(Aluno, file_write)
            file_write.close()

        elif editar_nota in Aluno and nota_alterar[0].upper() == 'SEGUNDA':
            Aluno[editar_nota][1] = float(nota_alterar[1])
            file_write = open("DBAlunos.json", "w")
            json.dump(Aluno, file_write)
            file_write.close()

        elif editar_nota in Aluno and nota_alterar[0].upper() == 'TERCEIRA':
            Aluno[editar_nota][2] = float(nota_alterar[1])
            file_write = open("DBAlunos.json", "w")
            json.dump(Aluno, file_write)
            file_write.close()
    else:
        print("ALUNO NÃO EXISTE!")


# OPÇÃO 8
###############################################################################################
def pesquisaNome():

    Aluno = {}
    file_read = open("DbAlunos.json", "r")
    Aluno = json.load(file_read)
    file_read.close()

    result = 0
    nome = input("Digite o nome a ser pesquisado: ").upper()

    chaves = list(Aluno.keys())

    tam = len(nome)
    cont_alunos = 1

    for aluno in chaves:
        res = aluno[:tam]
        if res == nome:
            notas_aluno = Aluno[aluno]
            nota1 = notas_aluno[0]
            nota2 = notas_aluno[1]
            nota3 = notas_aluno[2]
            media = ((nota1 + nota2 + nota3) / 3)
            print('Nº[%i]. %s. Notas: 1.[%.1f] | 2.[%.1f] | 3.[%.1f] | Média: %.1f' % (
                cont_alunos, aluno, nota1, nota2, nota3, media))
            cont_alunos += 1
            result += 1

    if result == 0:
        print("Aluno não encontrado!")

#OPÇÃO 9
###############################################################################################
def mediaDaSala():

    Aluno = {}
    file_read = open("DbAlunos.json", "r")
    Aluno = json.load(file_read)
    file_read.close()

    media_alunos = 0
    media_total = 0
    for notas in Aluno:
        notas_aluno = Aluno[notas]
        nota1 = notas_aluno[0] if len(notas_aluno) >= 1 else 0
        nota2 = notas_aluno[1] if len(notas_aluno) >= 2 else 0
        nota3 = notas_aluno[2] if len(notas_aluno) >= 3 else 0
        media = (nota1 + nota2 + nota3) / 3
        media_alunos += media
    media_total = media_alunos / len(Aluno)
    print('A média da turma é {:.1f}'.format(media_total))


# OPÇÃO 10
###############################################################################################
def melhorAluno():

    Aluno = {}
    file_read = open("DbAlunos.json", "r")
    Aluno = json.load(file_read)
    file_read.close()

    mediaDecres = {}

    if len(Aluno) == 0:
        print("Cadastro Vazio!!!")
    else:
        chaves = list(Aluno.keys())
        chaves.sort()
        cont_alunos = 1
        for alunos in chaves:
            notas_aluno = Aluno[alunos]
            nota1 = notas_aluno[0]
            nota2 = notas_aluno[1]
            nota3 = notas_aluno[2]
            media = ((nota1 + nota2 + nota3) / 3)
            mediaDecres[media] = alunos

        medChave = list(mediaDecres.keys())
        medChave.sort(reverse=True)

        for mediass in medChave:
            print('Nº[%i]. %s. | Média: %.1f' % (cont_alunos, mediaDecres[mediass], mediass))
            cont_alunos += 1
            break

#OPÇÃO 11
###############################################################################################
def mediaDecrescente():

    Aluno = {}
    file_read = open("DbAlunos.json", "r")
    Aluno = json.load(file_read)
    file_read.close()

    mediaDecres = {}
    if len(Aluno) == 0:
        print("Cadastro Vazio!!!")
    else:
        chaves = list(Aluno.keys())
        chaves.sort()
        cont_alunos = 1
        for alunos in chaves:
            notas_aluno = Aluno[alunos]
            nota1 = notas_aluno[0]
            nota2 = notas_aluno[1]
            nota3 = notas_aluno[2]
            media = ((nota1 + nota2 + nota3) / 3)
            mediaDecres[media] = alunos

        medChave = list(mediaDecres.keys())
        medChave.sort(reverse = True)

        for mediass in medChave:
            print('Nº[%i]. %s. | Média: %.1f' %(cont_alunos, mediaDecres[mediass], mediass))
            cont_alunos += 1

#OPÇÃO 12
######################################################################
def aprovadosMedia():

    Aluno = {}
    file_read = open("DbAlunos.json", "r")
    Aluno = json.load(file_read)
    file_read.close()

    if len(Aluno) == 0:
        print("Cadastro Vazio!!!")
    else:
        chaves = list(Aluno.keys())
        chaves.sort()
        cont_alunos = 1
        for alunos in chaves:
            notas_aluno = Aluno[alunos]
            nota1 = notas_aluno[0]
            nota2 = notas_aluno[1]
            nota3 = notas_aluno[2]
            media = ((nota1 + nota2 + nota3) / 3)

            if media >= 7.0:
                print('Nº[%i]. %s. Notas: 1.[%.1f] | 2.[%.1f] | 3.[%.1f] | Média: %.1f' % (cont_alunos, alunos, nota1, nota2, nota3, media))
                cont_alunos += 1

#OPÇÃO 13
######################################################################
def final():

    Aluno = {}
    file_read = open("DbAlunos.json", "r")
    Aluno = json.load(file_read)
    file_read.close()

    if len(Aluno) == 0:
        print("Cadastro Vazio!!!")
    else:
        chaves = list(Aluno.keys())
        chaves.sort()
        cont_alunos = 1
        for alunos in chaves:
            notas_aluno = Aluno[alunos]
            nota1 = notas_aluno[0]
            nota2 = notas_aluno[1]
            nota3 = notas_aluno[2]
            media = ((nota1 + nota2 + nota3) / 3)

            if media <= 7.0 and media >= 4.0:
                print('Nº[%i]. %s. Notas: 1.[%.1f] | 2.[%.1f] | 3.[%.1f] | Média: %.1f' % (cont_alunos, alunos, nota1, nota2, nota3, media))
                cont_alunos += 1

#OPÇÃO 14
######################################################################
def reprovados():

    Aluno = {}
    file_read = open("DbAlunos.json", "r")
    Aluno = json.load(file_read)
    file_read.close()

    if len(Aluno) == 0:
        print("Cadastro Vazio!!!")
    else:
        chaves = list(Aluno.keys())
        chaves.sort()
        cont_alunos = 1
        for alunos in chaves:
            notas_aluno = Aluno[alunos]
            nota1 = notas_aluno[0]
            nota2 = notas_aluno[1]
            nota3 = notas_aluno[2]
            media = ((nota1 + nota2 + nota3) / 3)

            if media < 4.0:
                print('Nº[%i]. %s. Notas: 1.[%.1f] | 2.[%.1f] | 3.[%.1f] | Média: %.1f' % (cont_alunos, alunos, nota1, nota2, nota3, media))
                cont_alunos += 1
