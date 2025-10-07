from lib import cuadrado, triangulo, rectangulo, circunferencia
print("Proyecto Figuras")
print(cuadrado.get_identificador())
lado = 4
print(f"El área de un cuadrado de lado {lado} es: {cuadrado.get_area(lado)}")

base=3
altura=5
print(f"El área de un {triangulo.get_identificador()} de base \
      {base} y altura {altura} es: {triangulo.get_area(base, altura)} \
        y su perímetro es: {triangulo.get_perimetro(base, altura)}")

base=4
altura=2
print(rectangulo.get_identificador())
print(f"El área de un rectángulo de base {base} \
      y altura {altura} es: {rectangulo.get_area(base, altura)} \
        y su perímetro es: {rectangulo.get_perimetro(base, altura)}")

radio=3
print(circunferencia.get_identificador())
print(f"El área de una circunferencia de radio {radio} es: {circunferencia.get_area(radio)}")
