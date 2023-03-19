### Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
###

class Persona:

    __nombre:str
    __edad:int
    __dni:str

    def __init__(self, nombre:str =None, edad:int =None , dni:str =None):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        try:
            if nombre.isalpha() is not True:
                raise Exception("Se debe ingresar una cadena de texto")
            self.__nombre = nombre
        except Exception as e:
            print(e)

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        try:
            if type(edad) != int or edad < 0 :
                raise Exception("Se debe ingresar un número entero positivo")
            self.__edad = edad
        except Exception as e:
            print(e)
        
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, dni):
        try:
            if len(dni) < 7 or not dni.isdigit() :
                raise Exception("Se debe ingresar un número de siete digitos como mínimo")
            self.__dni = dni
        except Exception as e:
            print(e)
        

    def mostrar(self):
        print(f"Nombre: {self.__nombre} Edad: {self.__edad} DNI: {self.__dni} ")
    
    def es_mayor_de_edad(self):
        return self.__edad >= 18


#ejercicio 7
# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales).
# El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero. 
# mostrar(): Muestra los datos de la cuenta. 
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Cuenta:

    __titular: Persona
    __cantidad: float

    def __init__(self, titular: Persona = None, cantidad: float = None):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print(f"Titular: {self.__titular} Cantidad: {self.__cantidad}")

    def ingresar(self, cantidad):
        if cantidad < 0:
            pass
        else:    
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad
        if self.__cantidad < 0:
            print(f"Usted adeuda la cantidad de:  + {self.__cantidad * -1} ")



# Ejercicio 8
# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada
# en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará 
# expresada en tanto por ciento. Crear los siguientes métodos para la clase:
#  Un constructor.
# Los setters y getters para el nuevo atributo. 
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un
# método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario. 
# Además, la retirada de dinero sólo se podrá hacer si el titular es válido. 
# El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

class CuentaJoven(Cuenta):

    __bonificacion: int 

    def __init__(self, titular=None, cantidad=None, bonificacion=None):
        if self.es_titular_valido():
            super().__init__(titular, cantidad)
            self.__bonificacion = bonificacion
        else:
            print("No cumple los requisitos para crear una cuenta joven")

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def es_titular_valido(self):
        return (self.__titular.es_mayor_de_edad() and self.__titular.edad < 25)
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            self.__cantidad -= cantidad
        else:
            print("No es un titular válido para efectuar el retiro de dinero") 

    def mostrar(self):
        print(f"Cuenta Joven con una bonificación de {self.__bonificacion}%") 

