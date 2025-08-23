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





    





    
