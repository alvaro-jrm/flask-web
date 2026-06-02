# Importamos la herramienta Flask. 'render_template' sirve para mostrar HTML.
from flask import Flask, render_template

# Creamos nuestra aplicación web y la guardamos en la variable 'app'
app = Flask(__name__)

# Le decimos a Flask qué hacer cuando alguien entra a la página principal ("/")
@app.route('/')
def inicio():
    # Cuando alguien entra, Flask le devuelve el archivo index.html
    return render_template('index.html')

# Esta parte enciende el servidor en tu computadora cuando ejecutas el archivo
if __name__ == '__main__':
    # debug=True nos permite ver los errores en pantalla si nos equivocamos
    app.run(debug=True)