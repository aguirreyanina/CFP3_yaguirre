# def suma_infinita(*args):
#      resultado = 0
#      for numeros in args:
#          resultado += numeros
#      return resultado
# resultado = suma_infinita(3,5,6,2500,56,88,77,9)
# print(resultado)

def masa_corporal(peso, altura):
    return peso / (altura ** 2)
peso = int(input("Ingrese su peso en Kilogramos: "))
altura = float(input("Ingrese su estatura en metros: "))
resultado = masa_corporal(peso,altura)
print(resultado)



