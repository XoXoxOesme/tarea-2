
class persona:

    def inicializar(self,nombre,nota):
      self.nombre=nombre
      self.nota=nota

    def imprimir(self):
      print("nombre",self.nombre)
      print("nota",self.nota)

    def mostrar_edad(self):
      if self.nota>=18:
        print("es mayor de edad")
      else:
          print("no es mayor de edad")

#bloque principal
persona1=persona()
persona1.inicializar("Gismara", 12)
persona1.imprimir()
persona1.mostrar_edad()

persona2=persona()
persona2.inicializar("Pepe",23)
persona2.imprimir()
persona2.mostrar_edad()

class triangulo:

   def __init__(self,lado1,lado2,lado3):
      self.lado1=lado1
      self.lado2=lado2
      self.lado3=lado3

   def lado_mayor(self):
      lados=[self.lado1 , self.lado2 , self.lado3]
      lado_mayor=max(lados)
      return lado_mayor

   def es_equilatero(self):
    return self.lado1==self.lado2==self.lado3

lado1=float(input("ingrese el primer lado del triangulo:"))
lado2=float(input("ingrese el segundo lado del triangulo:"))
lado3=float(input("ingrese el tercer lado del triangulo:"))
triangulo=triangulo(lado1,lado2,lado3)
print("el lado mayor del triangulo es:")
print(triangulo.lado_mayor())

if triangulo.es_equilatero():
   print("el triangulo es equilatero")
else:
   print("el triangulo no es equilatero")

class alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("nombre:",self.nombre)
        print("nombre:",self.nota)

    def mostrar_estado(self):
        if self.nota>=4:
           print("regular")
        else:
            print("libre")

#bloque principal

alumno1=alumno()
alumno1.inicializar("diego",21)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=alumno()
alumno2.inicializar("ana",10)
alumno2.imprimir()
alumno2.mostrar_estado()

class Persona:

    def inicializar(self,nom):
        self.nombre=nom

    def imprimir(self):
        print("Nombre",self.nombre)


# bloque principal

persona1=Persona()
persona1.inicializar("Pedro")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Carla")
persona2.imprimir()