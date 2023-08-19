class Asiento:
    
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        if color == "amarillo" or color == "rojo" or color == "verde" or color == "negro" or color == "blanco":
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo

class Auto:
    
    cantidadCreados = 0
    
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        contador = 0
        for i in self.asientos:
            if type(i) == Asiento:
                contador += 1
        return(contador)
    
    def verificarIntegridad(self):
        x = self.registro
        f = False
        for i in self.asientos:
            if type(i) == Asiento:
                if i.registro == x:
                    f = True
                else:
                    f = False
                    break
        if x == self.motor.registro and f == True:
            return("Auto original")
        else:
            return("Las piezas no son originales")