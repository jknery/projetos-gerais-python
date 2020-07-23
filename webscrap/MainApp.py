from Vagalume import Vagalume
from CifraClub import CifraClub
from LetrasMus import LetrasMus

#Objetos Instanciados
cifraClub = CifraClub("https://www.cifraclub.com.br")
vagalume = Vagalume("https://www.vagalume.com.br")
letrasMus = LetrasMus("https://www.letras.mus.br")

teste = cifraClub.getArtistaPorLetra("A")

print(teste)

input()
