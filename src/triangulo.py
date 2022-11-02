def checaTriangulo(a, b, c):
    if (a < b + c and b < a + c and c < b + c):
        if a == b and a == c and b == c:
            return "Eh triangulo"
        else:
            if (a == b or a == c or b == c):
                return "Eh triangulo"
            else:
                if (a != b and a != c and b != c):
                    return "Eh triangulo"
    else:
        return "Nao eh triangulo"