class Persona():

    nombre: str
    apellido_materno: str
    apellido_paterno: str
    edad: int
    genero: str 
    estatura: float 
    peso: float
    estado_civil: str 
    grado_estudio: str

    #self para englobar los atributos al metodo
    def __init_(self):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.edad = edad
        self.genero = genero
        self.estatura = estatura
        self.peso = peso
        self.estado_civil = estado_civil
        self.grado_estudio = grado_estudio

#imput para pedir datos, antes de el poner tipo de dato(str no es necesario ponerlo)

    nombre = str(input("escribe tu nombre: "))
    apellido_paterno = str(input("Escribe tu apellido paterno: "))
    apellido_materno = str(input("Escribe tu apellido materno: "))
    edad = int(input("Escribe tu edad: "))
    genero = str(input("Escribe tu genero: "))
    estatura = float(input("Escribe tu altura: "))
    peso = float(input("Escribe tu peso: "))
    estado_civil = str(input("Escribe tu estado civil: "))
    grado_estudio = str(input("Escribe tu grado de estudios: "))

# para instanciar los dartos a un objeto(nuevapersona) creamos el objeto(nuevaperona) y lo relacionamos con la clase
nuevaPersona = Persona()
print("\nEl nombre es: " + nuevaPersona.nombre + "\nEl apellido paterno es: " + nuevaPersona.apellido_paterno +
     "\nEl apellido materno es: " + nuevaPersona.apellido_materno + "\nLa edad es: " + str(nuevaPersona.edad) +
      "\nEl genero es: " + nuevaPersona.genero + "\nLa estatura es: " + str(nuevaPersona.estatura) +
       "\nEl peso es: " + str(nuevaPersona.peso) + "\nEl estado civil es: " + nuevaPersona.estado_civil +
        "\nEl grado de estudios es: " + nuevaPersona.grado_estudio)

