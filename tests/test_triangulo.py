import sys
sys.path.append('src/')
from triangulo import checaTriangulo 

class Test:
    #Valores iguais
    def teste1(self):
        assert checaTriangulo(4,4,4) == "Eh triangulo"
    #Dois lados iguais
    def teste2(self):
        assert checaTriangulo(4,4,10) == "Eh triangulo"
    #Um dos valores sendo 0.
    def teste3(self):
        assert checaTriangulo(5,0,5) == "Nao eh triangulo"
    #Valores diferentes
    def teste4(self):
        assert checaTriangulo(1,4,5) == "Eh triangulo"
    #Todos os valores 0
    def teste5(self):
        assert checaTriangulo(0,0,0) == "Nao eh triangulo"

