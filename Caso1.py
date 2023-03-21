import matplotlib.pyplot as plt
import datetime

# Clase base para todos los empleados
class Empleado:
    def __init__(self, num_empleado, nombre, apellidos, fecha_nacimiento, num_seguro_social, sueldo_base, antiguedad):
        self.num_empleado = num_empleado
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.num_seguro_social = num_seguro_social
        self.sueldo_base = sueldo_base
        self.antiguedad = antiguedad

    def get_num_empleado(self):                     # Función getter 
        return self.num_empleado

    def set_num_empleado(self, num_empleado):       # Función setter
        try:
            self.num_empleado = int(num_empleado)
        except ValueError:
            print("Error: El número de empleado debe de ser un número entero")   # Reglas para no tener errores en la ejecución del código

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellidos(self):
        return self.apellidos

    def set_apellidos(self, apellidos):
        self.apellidos = apellidos

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        try:
            datetime.datetime.strptime(value, '%d/%m/%Y')
            self._fecha_nacimiento = value
        except ValueError:
            raise ValueError("La fecha de nacimiento debe tener el formato DD/MM/YYYY")     # Reglas para no tener errores en la ejecución del código

    def get_num_seguro_social(self):
        return self.num_seguro_social

    def set_num_seguro_social(self, num_seguro_social):
        self.num_seguro_social = num_seguro_social

    def get_sueldo_base(self):
        return self.sueldo_base

    def set_sueldo_base(self, sueldo_base):
        try:
            self.sueldo_base = float(sueldo_base)
        except ValueError:
            print("Error: El sueldo base debe ser un número.")                          # Reglas para no tener errores en la ejecución del código

    def get_antiguedad(self):
        return self.antiguedad

    def set_antiguedad(self, antiguedad):
        try:
            self.antiguedad = int(antiguedad)
        except ValueError:
            print("Error: La antigüedad debe de ingresarse como un número entero.")     # Reglas para no tener errores en la ejecución del código

    def mostrar_ficha(self):
        print(f"Número de empleado: {self.num_empleado}")
        print(f"Nombre completo: {self.nombre} {self.apellidos}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Número de seguro social: {self.num_seguro_social}")
        print(f"Sueldo base: {self.sueldo_base}")
        print(f"Años de antigüedad: {self.antiguedad}")


# Clases derivadas para cada tipo de empleado
class EmpleadoAdministrativo(Empleado):
    def __init__(self, num_empleado, nombre, apellidos, fecha_nacimiento, num_seguro_social, sueldo_base, antiguedad, puesto):
        super().__init__(num_empleado, nombre, apellidos, fecha_nacimiento, num_seguro_social, sueldo_base, antiguedad)
        self.puesto = puesto
  
    def get_puesto(self):               # Funcion get 
        return self.puesto

    def set_puesto(self, puesto):       # Funcion set
        self.puesto = puesto


class EmpleadoVentas(Empleado):
    def __init__(self, num_empleado, nombre, apellidos, fecha_nacimiento, num_seguro_social, sueldo_base, antiguedad, datosVentas):
        super().__init__(num_empleado, nombre, apellidos, fecha_nacimiento, num_seguro_social, sueldo_base, antiguedad)
        self.datosVentas = []

    def get_datosVentas(self):         # Funcion get
        return self.datosVentas

    def setDatosVentas(self, datosVentas):  # Funcion set
        self.datosVentas = datosVentas

    def graficarVentas(self):
        meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
        ventasSeisMeses = self.datosVentas[:6]
        try:
            plt.plot(meses, ventasSeisMeses)
            plt.title(f"Ventas de {self.nombre} {self.apellidos} durante el año")
            plt.xlabel("Meses")
            plt.ylabel("Ventas")
            plt.show()
        except:
            print("Error: No hay datos de ventas registrados para este empleado.")         # Reglas para no tener errores en la ejecución del código


class EmpleadoSupervisor(Empleado):
    def __init__(self, num_empleado, nombre, apellidos, fecha_nacimiento, num_seguro_social, sueldo_base, antiguedad, departamento):
        super().__init__(num_empleado, nombre, apellidos, fecha_nacimiento, num_seguro_social, sueldo_base, antiguedad)
        self.departamento = departamento

    def get_depto(self):                        # Funcion get
        return self.departamento
    
    def set_depto(self, departamento):          # Funcion set
        self.departamento = departamento


class Gerente(EmpleadoAdministrativo):
    def __init__(self, num_empleado, nombre, apellidos,):
        super().__init__(num_empleado, nombre, apellidos, None, None, None, None)

    def get_nombre_gerente(self):               # Funcion get
        return self.nombre
    
    def set_nombre_gerente(self, nombre):       # Funcion set
        self.nombre = nombre
    
    def get_apellidos_gerente(self):
        return self.apellidos
    
    def set_apellidos_gerente(self,apellidos):
        self.apellidos = apellidos

    def mostrar_ficha(self):
        print(f"Número de empleado: {self.num_empleado}")
        print(f"Nombre completo: {self.nombre} {self.apellidos}")