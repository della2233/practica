from hashlib import new


class Persona:

# se definen las variables con su tipo de dato, para ingresarlo despues.

    nombre: str
    apellido_materno: str
    apellido_paterno: str
    edad: int
    genero: str 
    estatura: float 
    peso: float
    estado_civil: str 
    grado_estudio: str

#se crea un metodo(se le nombro atributo al azar), para poder llamarlo cuando sea necesario

    def __init__(self, atributo):
        preguntar_datos()

    def preguntar_datos():
        #se pide al usuario ingresar los datos con input.
        nombre = str(input("Escribe tu nombre: "))
        apellido_paterno = str(input("Escribe tu apellido paterno: "))
        apellido_materno = str(input("Escribe tu apellido materno: "))
        edad = int(input("Escribe tu edad: "))
        genero = str(input("Escribe tu genero: "))
        estatura = float(input("Escribe tu altura: "))
        peso = float(input("Escribe tu peso: "))
        estado_civil = str(input("Escribe tu estado civil: "))
        grado_estudio = str(input("Escribe tu grado de estudios: "))

        nueva_persona= new Persona(nombre, apellido_materno, edad, genero, estatura, peso, estado_civil, grado_estudio)

        #se imprimen en pantalla los datos dados haciendo concatenaciones, los datos de tipo int o float se 
        #convierten a str con str(atributo).

        print("\nEl nombre es: " + nueva_persona.nombre + "\nEl apellido paterno es: " + nueva_persona.apellido_paterno +
            "\nEl apellido materno es: " + nueva_persona.apellido_materno + "\nLa edad es: " + nueva_persona.str(edad) +
            "\nEl genero es: " + nueva_persona.genero + "\nLa estatura es: " + nueva_persona.str(estatura) +
            "\nEl peso es: " + str(peso) + "\nEl estado civil es: " + estado_civil +
                "\nEl grado de estudios es: " + nueva_persona.grado_estudio)