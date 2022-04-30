import unittest
from calculadora import Calculadora

# ejecutar pruebas
# python -m unittest discover 
class test_calculadora(unittest.TestCase):
  
    def test_suma(self):
        # sumando enteros positivos
        self.assertEqual(Calculadora.suma(1,5),6)
        # sumando con uno de los numeros negativos
        self.assertEqual(Calculadora.suma(-1,5),4)
        # sumando con el modulo
        self.assertEqual(Calculadora.suma(0,5),5)
        # sumando decimales
        self.assertEqual(Calculadora.suma(1,5.5),6.5)
        # sumando con fracionarios
        self.assertEqual(Calculadora.suma(1/2,5/5),1.5)

    def test_division(self):
        # dividiendo enteros positivos
        self.assertEqual(Calculadora.division(4,2),2)
        # dividiendo enteros positivos resultado decimal
        self.assertEqual(Calculadora.division(1,2),0.5)
        # Dividiendo por decimales
        self.assertEqual(Calculadora.division(3.5,0.5),7)
        # division por 0 numerador
        self.assertEqual(Calculadora.division(0,5),0)
        # division por 0 denominador
        self.assertEqual(Calculadora.division(0,0),"la division por cero no esta permitida")

    def test_raiz(self):
        # raiz a y b positivos
        self.assertEqual(Calculadora.raiz(4,2),2)
        # raiz a negativo 
        self.assertEqual(Calculadora.raiz(-4,2), "no tiene solucion en los reales")
        # raiz b negativo 
        self.assertEqual(Calculadora.raiz(4,-2), 0.5)
        # raiz b decimal
        self.assertEqual(Calculadora.raiz(4,0.5), 16)
        # raiz b = 0
        self.assertEqual(Calculadora.raiz(4,0), "la operacion no esta permitida")
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)