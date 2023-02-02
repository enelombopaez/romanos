"""
I - Uno
V - Cinco
X - Diez
L - Cincuenta
C - Cien
D - Quinientos
M - Mil
"""

def convertir_en_romano(numero):

    if not isinstance(numero, int):
        return "ERROR: No has introducido un número entero"

    if numero < 1 or numero > 3999:
        return "ERROR: debe ser un valor entre 1 y 3999 (incluidos)"

    divisores = [1000, 100, 10, 1]
    indices = []

    for divisor in divisores:
        indices.append(numero // divisor)
        numero = numero % divisor

    millares = ["", "M", "MM", "MMM"]
    centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    resultado = millares[indices[0]] + \
        centenas[indices[1]] + \
        decenas[indices[2]] + \
        unidades[indices[3]]

    return resultado


"""
print(convertir_en_romano("56t"))
print(convertir_en_romano("56"))
print(convertir_en_romano(-3))
print(convertir_en_romano(4000))
print(convertir_en_romano(1123))
print(convertir_en_romano(2746))
print(convertir_en_romano(11))
"""

def convertir_en_numero(romano):
    """
    MCXXIII: 1123
        - de izquierda a derecha
        M+C+X+X+I+I+I = 1000 + 100 + 10 + 10 + 1 + 1 + 1
    """

    digitos_romanos = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    if not isinstance(romano, str):
        return "ERROR: tiene que ser un número romano en formato cadena"

    resultado = 0
    puntero = 0
    previa = ""
    for letra in romano:
        if letra not in digitos_romanos:
            return f"ERROR: {letra} no es un dígito romano válido (I, V, X, L, C, D, M)"
        # rescatar el valor
        resultado = resultado + digitos_romanos.get(letra)

    return resultado

print(convertir_en_romano(49))