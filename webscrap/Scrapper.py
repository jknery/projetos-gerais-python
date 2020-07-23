'''
UNIFACISA - FACULDADE DE CIÊNCIAS SOCIAS APLICADAS
PROJETO DE INTELIGÊNCIA ARTIFICIAL
PROFª ORIENTADORA: VERA L. C. DE MEDEIROS
CLASSES QUE REALIZAM SCRAPPER EM SITES DE MUSICAS
ALUNOS: MATHEUS JORDAN PAZ | JOSÉ IVO KOERICH NERY
'''
import requests
from bs4 import *
import lxml
import html5lib

#Classe Pai
class Scrapper:

    #Retornar um objeto BeautfulSoup da página html ou html5
    def makeRequest(self, url = "/"):
        url = self.url + url
        req = requests.get(url)
        soap = BeautifulSoup(req.content, 'lxml')
        return soap

    def setUrl(self, url):
        self.url = url

    def getUrl():
        return self.url
    

class BetFair:
    def __init__(self):
        self.url
