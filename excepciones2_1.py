def divide():
    try:
        op1 = (float(input("Introduce el primer numero: ")))
        op2 = (float(input("Introduce el segundo numero: ")))

        print("La division es: "+ str(op1/op2))
8
    except ValueError:
        print("El valor introduccido es incorrecto")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

    finally:
        print("Calculo Finalizado")

divide()