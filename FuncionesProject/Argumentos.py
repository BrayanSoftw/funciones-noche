#Ejemplo de argumentos PREDETERMINADOS
from statistics import multimode


def my_function(country = 'Colombia'):
    print('I am from '+country)

#Invocar la funcion
my_function('Sweden')
my_function('India')
my_function()
my_function('Brazil')

#ARGUMENTOS ARBITARIOS
def mostrarEstudiantes(*args):
    print('El estudiante: '+ args[1])

mostrarEstudiantes('Emil','Tobias','Linus')

#ARGUMENTOS CLAVE=VALOR
def mostrarCarros(carro1,carro2,carro3):
    print('El carro es: '+carro2)

mostrarCarros(carro1 = 'BMW', carro2='Ferrari',carro3='Ford')

#ARGUMENTO ARBITRARIO **Kwargs
def mostrarCliente(**Kwargs):
    print('Su apellido es: '+Kwargs['apellido'])

mostrarCliente(nombre = 'Tobias', apellido = 'refsnes')