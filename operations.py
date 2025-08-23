def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    
    return a / b  

def power(a, b):
    return a ^ b  

def square_root(x):
    import math
    return math.sqrt(x)

def average(list):
    return sum(list) / len(list)

def maximum(list):
    return min(list) 


if __name__ == "__main__":

    print("start test")

    print("hola")

    print("end test")

    print("add(2,3)", add(2,3), "esperado: 5")

    print("subtract(5,3)", subtract(5,3), "esperado: 2")

    print("multiply(4,6)", multiply(4,6), "esperado: 24")

    print("divide(10,2)", divide(10,2), "esperado: 5")

    print("square_root(4)", square_root(4), "esperado: 2")

    print("maximum([3,7,1])", maximum([3,7,1]), "esperado: 7") 

   # add(a, b) sumar
print("add('2','3') =>", add('2','3'))          # Esperado: 5 (suma numérica) | Obtenido: '23'
print("add([1],[2]) =>", add([1],[2]))          # Esperado: error por tipos no numéricos | Obtenido: [1, 2]

# subtract(a, b) — restar
try:
    print("subtract('5','2') =>", subtract('5','2'))  # Esperado: 3 o rechazo claro
except Exception as e:
    print("subtract('5','2') lanzó:", type(e).__name__, e)

try:
    print("subtract(None,1) =>", subtract(None,1))  
except Exception as e:
    print("subtract(None,1) lanzó:", type(e).__name__, e)

# multiply(a, b) multiplicar

print("multiply('a',3) =>", multiply('a',3))          # 
print("multiply(1e308,1e308) =>", multiply(1e308,1e308))  #

# divide(a, b) dividir
try:
    print("divide(5,0) =>", divide(5,0))            
except Exception as e:
    print("divide(5,0) lanzó:", type(e).__name__, e)


try:
    print("divide('10',2) =>", divide('10',2))        
except Exception as e:
    print("divide('10',2) lanzó:", type(e).__name__, e)

# potencia” (a^b esperado)
print("power(2,3) =>", power(2,3))                    # Esperado: 8 | Obtenido: 1 (usa XOR ^)

print("power(5,0) =>", power(5,0))                    # Esperado: 1 | Obtenido: 5 (a ^ 0 = a)

# square_root(x)raíz cuadrada
try:
    print("square_root(-4) =>", square_root(-4))      #
except Exception as e:
    print("square_root(-4) lanzó:", type(e).__name__, e)

try:
    print("square_root('9') =>", square_root('9'))    # Esperado: rechazo claro por tipo
except Exception as e:
    print("square_root('9') lanzó:", type(e).__name__, e)

# average(lista)
try:
    print("average([]) =>", average([]))              # Esperado: manejo definido (no ZeroDivisionError)
except Exception as e:
    print("average([]) lanzó:", type(e).__name__, e)


try:
    print("average([1,'2',3]) =>", average([1,'2',3]))  # validación/mensaje claro
except Exception as e:
    print("average([1,'2',3]) lanzó:", type(e).__name__, e)

# maximum(lista)
print("maximum([1,5,3]) =>", maximum([1,5,3]))        # Esperado: 5 | Obtenido: 1 (usa min)




    





    
