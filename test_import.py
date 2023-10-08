"""
   test file for imports and partial imports
   
   PyCon Latam 2023
   
"""
print("Hola desde test_import.py!")
for x in range(1_000_000):
    y = x ** 3
print(f"calculated {x+1} cubes, highest was {y}")


def foo_4(parameter=[]):
    test_var = "test"
    print(parameter)
    parameter.append("test")
    return parameter

"""
def foo_5(parameter=None):
    return parameter
"""

# codigo que refiere al objeto (función) foo_4 creado encima
print(f"Object creado {foo_4}, con id de {id(foo_4)}")
