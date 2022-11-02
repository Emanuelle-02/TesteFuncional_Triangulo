def ehTriangulo(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "Nao eh triangulo"
    elif (a < b + c and b < a + c and c < b + c):
        return "Eh triangulo"
    else:
        return "Nao eh triangulo"

def ehEscaleno(a, b, c):
        if a != b and a != c and b != c:
            return "Eh triangulo"
        else:
            return "Nao eh triangulo"

def ehIsosceles(a, b, c):
    if a == b:
        return "Eh triangulo"
    elif a == c:
        return "Eh triangulo"
    elif b == c:
        return "Eh triangulo"
    else:
        return "Nao eh triangulo"

def ehEquilatero(a, b, c):
    if a == b and a == c and b == c:
        return "Eh triangulo"
    else:
        return "Nao eh triangulo"

def checaTriangulo(a, b, c):
    if ehTriangulo(a, b, c) == "Eh triangulo" and ehEscaleno(a, b, c) or ehTriangulo(a, b, c) == "Eh triangulo" and ehIsosceles(a, b, c) or ehTriangulo(a, b, c) == "Eh triangulo" and ehEquilatero(a, b, c):
        return "Eh triangulo"
    else:
        return "Nao eh triangulo"
        