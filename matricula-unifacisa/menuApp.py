'''
FUNÇÃO DE MENU DO APLICATIVO

FACULDADE DE CIÊNCIAS SOCIAIS APLICADAS - UNIFACISA
SISTEMAS DE INFORMAÇÃO - NOTURNO
DISCIPLINA: PROGRAMAÇÃO 1 - PYTHON 3.7
GRUPO: JOSÉ IVO KOERICH NERY - 182.308.00-07
       ARTUR RENE DA SILVA 182.308.00-06
'''

def menuPrincipal():

        print()
        print("############################################")
        print("#           Sistema de Matrícula           #")
        print("############################################")
        print("# 01 - Listar Alunos Em Ordem Alfabética!  #")
        print("# 02 - Adicionar Alunos                    #")
        print("# 03 - Adicionar Nota                      #")
        print("# 04 - Remover Aluno                       #")
        print("# 05 - Remover Nota                        #")
        print("# 06 - Editar Nome Aluno                   #")
        print("# 07 - Editar Nota Aluno                   #")
        print("# 08 - Buscar Aluno Por Nome               #")
        print("# 09 - Calcular Média da turma             #")
        print("# 10 - Exibir Melhor Aluno                 #")
        print("# 11 - Exibir Aluno Por Ordenados Por Nota #")
        print("# 12 - Exibir alunos aprovados por média   #")
        print("# 13 - Exibir Alunos Na Final              #")
        print("# 14 - Exibir Alunos Reprovados            #")
        print("# 15 - Encerra o Programa                  #")
        print("############################################")
        opcao = int(input("Digite a Opção escolhida: "))
        print()
        return opcao
