from flask import Flask, request, make_response, redirect

# Variables globales
app = Flask (__name__)
edades = [5, 55, 42, 85, 41, 18, 27]

# Petición en el raiz para invocar "Hola"
@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip2', user_ip)

    return response

# Imprimir mensaje de hola
@app.route('/hello',methods=["GET"])
def hello():
    user_ip = request.cookies.get('user_ip2')
    leerEdades()
    return "Hello Jose, estas en el IP (cookie) {}. Tu edad es: ".format(user_ip) +str(leerEdad(1))
#    return "Hello Jose, estas en el IP (cookie) {}. Tu edad es: ".format(user_ip) +str(edades[2])

# Regresar edades
@app.route('/edades/<int:e>',methods=["GET"])
def getEdadporPosicion(e):
    lecturaEdad = edades[e]
    return "La edad es: " +str(lecturaEdad)
#    return "Hello Jose, estas en el IP (cookie) {}. Tu edad es: ".format(user_ip) +str(edades[2])

# Prueba para agregar edades
@app.route('/incluirEdades',methods=["POST"])
def setEdadporPosicion():
    return request.data
#    return "Hello Jose, estas en el IP (cookie) {}. Tu edad es: ".format(user_ip) +str(edades[2])

def leerEdad(i):
    return (edades[i])

def leerEdades():
    print (edades)