def descuento(total, descuento):
    print("el total con descuento aplicado es " + (total - descuento))


def total(unidades, precio):
    return unidades * precio


def total(unidades, precio, iva):  # sobrecarga o sobreecritura? dos metodos iguales con diferentes argumentos
    return unidades * precio * (1 + iva)
