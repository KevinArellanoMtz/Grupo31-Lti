separador = ("*" * 20) + "\n"
Alumnos = []
Materia=[]
Calificacion=[]

n=int(input("¿Cuantos alumnos?"))
for i in range(n):
    Alumno=input("Nombre del Alumno?:")
    idalumno=input("ID del alumno?:")
    Alumnos.append("/ " + idalumno + " .- "  + Alumno + " /")

print(separador *2)
print(Alumnos)

print(separador *2)
print ("Selecciona una opción" + " ")
print ("1.- LISTA DE ALUMNOS")
print ("2.- CAPTURA DE CALIFICACIONES")
print ("3.-MOSTRAR ESTADISTICAS")
print ("4.-CAPTURA DE MATERIAS")
print ("5.-SALIR")

opcion = int(input("DIGITE UNA OPCIÓN VÁLIDA"+ " "))

if opcion == 1:
   print("LISTA DE ALUMNOS REGISTRADOS")
   print(Alumnos)
if opcion == 2:
    c=int(input("Cuantas calificaciones quiere registrar?"))
    for i in range(c):
        print ("CAPTURA DE CALIFICACIONES")
        materia=input("¿De que materia desea registrar?")
        calificaciones=input("¿Cual sera la calificacion asignada?")
        idalumno2=input("Dime el id del alumno que le daras la calificacion:")
        Calificacion.append(idalumno2 + " .- " + materia + "-"   + calificaciones + " /")
    
       
       
   