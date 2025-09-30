from lib import cuadrado, rectangulo
print("Proyecto Figuras")
print(cuadrado.get_identificador())
lado = 4
print(f"El área de un cuadrado de lado {lado} es: {cuadrado.get_area(lado)} \
      y su perímetro es: {cuadrado.get_perimetro(lado)}")

base=4
altura=2
print(rectangulo.get_identificador())
print(f"El área de un rectángulo de base {base} \
      y altura {altura} es: {rectangulo.get_area(base, altura)} \
        y su perímetro es: {rectangulo.get_perimetro(base, altura)}")