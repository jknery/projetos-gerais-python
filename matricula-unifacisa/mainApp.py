'''
PROGRAMA TESTE DO SISTEMA DE MATRÍCULA EM PYTHON 3 COM USO DE JSON COMO REPOSITÓRIO

FACULDADE DE CIÊNCIAS SOCIAIS APLICADAS - UNIFACISA
SISTEMAS DE INFORMAÇÃO - NOTURNO
DISCIPLINA: PROGRAMAÇÃO 1 - PYTHON 3.7
GRUPO: JOSÉ IVO KOERICH NERY - 182.308.00-07
       ARTUR RENE DA SILVA - 182.308.00-06
'''
import menuApp
import serviceApp

Status = 0

while Status != 15:
    Status = menuApp.menuPrincipal()
    if Status == 1:
        serviceApp.listAlunos()
    elif Status == 2:
        serviceApp.createAluno()
    elif Status == 3:
        serviceApp.addrNotaAluno()
    elif Status == 4:
        serviceApp.deleteAluno()
    elif Status == 5:
        serviceApp.deleteNotaAluno()
    elif Status == 6:
        serviceApp.updateNomeAluno()
    elif Status == 7:
        serviceApp.updateNotaAluno()
    elif Status == 8:
        serviceApp.pesquisaNome()
    elif Status == 9:
        serviceApp.mediaDaSala()
    elif Status == 10:
        serviceApp.melhorAluno()
    elif Status == 11:
        serviceApp.mediaDecrescente()
    elif Status == 12:
        serviceApp.aprovadosMedia()
    elif Status == 13:
        serviceApp.final()
    elif Status == 14:
        serviceApp.reprovados()
    elif Status == 15:
        print("Bye Bye - Até a Próxima!!")
