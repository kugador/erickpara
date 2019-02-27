#El módulo 'os' nos permitirá consultar si un archivo existe.
import os



def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
    return mensaje

def mostrar_mensaje(origen, destinatario, mensaje):
    print("--------------------------------------------------")
    if destinatario == None:
        print(origen, "dice:", mensaje)
    else:
        print(origen, "dice:", "@"+destinatario, mensaje)
    print("--------------------------------------------------")

#Muestra los mensajes recibidos
def mostrar_muro(muro):
     print("------ MURO ("+str(len(muro))+" mensajes) ---------")
     for mensaje in muro:
         print(mensaje)
     print("--------------------------------------------------")

#Publica un mensaje en el timeline personal y en el de los amigos
def existe_archivo(ruta):
    return os.path.isfile(ruta)

def leer_usuario(nombre):
    archivo_usuario = open(nombre+".user","r")
    nombre = archivo_usuario.readline().rstrip()
    edad = int(archivo_usuario.readline())
    estatura = float(archivo_usuario.readline())
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*100 )
    sexo = archivo_usuario.readline().rstrip()
    pais = archivo_usuario.readline().rstrip()
    amigos = archivo_usuario.readline().rstrip().split(",")
    estado = archivo_usuario.readline().rstrip()
    #Lee el 'muro'. Esto es, todos los mensajes que han sido publicados en el timeline del usuario.
    muro = []
    mensaje = archivo_usuario.readline().rstrip()
    while mensaje != "":
        muro.append(mensaje)
        mensaje = archivo_usuario.readline().rstrip()
    #Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()
    return(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado, muro)

def escribir_usuario(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado, muro):
    archivo_usuario = open(nombre+".user","w")
    archivo_usuario.write(nombre+"\n")
    archivo_usuario.write(str(edad)+"\n")
    archivo_usuario.write(str(estatura_m + estatura_cm/100)+"\n")
    archivo_usuario.write(sexo+"\n")
    archivo_usuario.write(pais+"\n")
    archivo_usuario.write(",".join(amigos)+"\n")
    archivo_usuario.write(estado+"\n")
    #Escribe el 'timeline' en el archivo, a continuación del último estado
    for mensaje in muro:
        archivo_usuario.write(mensaje+"\n")
    #Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
    archivo_usuario.close()
