from lib import cuadrado, triangulo
print("Proyecto Figuras")
print(cuadrado.get_identificador())
lado = 4
print(f"El área de un cuadrado de lado {lado} es: {cuadrado.get_area(lado)}")

base=3
altura=5
print(f"El área de un {triangulo.get_identificador()} de base \
      {base} y altura {altura} es: {triangulo.get_area(base, altura)} \
        y su perímetro es: {triangulo.get_perimetro(base, altura)}")