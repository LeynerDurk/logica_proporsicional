# Función para imprimir la tabla de verdad de la compuerta NOT
def tabla_verdad_not():
    print("A | NOT A")
    print("---------")
    for A in [0, 1]:
        resultado = not A
        print(f"{A} |   {int(resultado)}")

# Llamar a la función
tabla_verdad_not()
