class Calculadora:    
    # Suma entre dos numeros reales
    def suma(a,b):
        if isinstance(a,str) or isinstance(b,str) :
            return "Solo se permiten números"
        return a+b

    # Resta dos numeros reales
    def resta(a,b):
        return a-b

    # multiplicacion dos numeros reales
    def multiplicacion(a,b):
        return a*b

    # division dos numeros reales
    def division(numerador,denominador):
        if denominador == 0:
            return "la division por cero no esta permitida"
        return numerador/denominador

    # potencia dos numeros reales
    def potencia(base,exponente):
        return base**exponente

    # raiz dos numeros reales
    def raiz(a,b):
        if b == 0:
            return "la operacion no esta permitida"
        elif a < 0:
            return "no tiene solucion en los reales"
        return a**(1/b)



