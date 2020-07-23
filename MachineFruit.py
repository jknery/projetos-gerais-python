'''
Programa Teste de Machine Learning
'''

from sklearn import tree
#lista de frutas
MAÇA = 1
LIMAO = 2
#lista de caracteristicas
LISA = 1
IRRG = 2

Pomar = [ [150, LISA], [130, LISA], [80, IRRG], [60, IRRG] ]

Resultado = [MAÇA, MAÇA, LIMAO, LIMAO]

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(Pomar, Resultado)

peso = input("Entre com o peso: ")
tipoSuperficie = input("Entre com a superficie: ")

fruta = classifier.predict([ [peso, tipoSuperficie] ])

if fruta == 1:
    print("É uma MAÇÃ!")
if fruta == 2 :
    print("É um LIMÃO!")
