#Se usa el comando: pip install flask 
#Importacion librerias

from flask import Flask, render_template
#Se declaro la variable "app" para crear una instancia, Flask es el nombre del modulo y "__name__" es de donde se sacaran
#los recursos

app = Flask(__name__)


#Creacion del Route para enlanzar paginas, en el caso que el request concuerde se lanzara la pagina
# index la hemos marcado como pagina principal por el ('/')
#index es el metodo que retorna el tipo de dato render_template (index.html)
@app.route('/')
def index():
    return render_template('pages/index.html') 

#Se aplica igual solo que ahora el route("/AcercaDeNosotros") sera la ruta para el html de sobreNosotros y retorna este
#Mismo archivo de HTML, asi con las demas o las que se vayan a crear
@app.route('/AcercaDeNosotros')
def sobreNosotros():
    return render_template('pages/sobreNosotros.html')

@app.route('/Facturacion')
def facturacion():
    return render_template('pages/facturacion.html')

@app.route('/Proveedores')
def proveedores():
    return render_template('pages/proveedores.html')

@app.route('/Departamentos/')
def Departamentos():
    return render_template('pages/departamentos.html')

@app.route('/Surcursales')
def Surcursales():
    return render_template('pages/surcursales.html')

@app.route('/Preguntas-Frecuentes')
def Preguntas():
    return render_template('pages/preguntasFrecuentes.html')

@app.route('/Contacto')
def Contacto():
    return render_template('pages/contacto.html')





# Este bloque es para asegurarnos si se esta corriendo y nos muestre en la terminal todo, se pone al final
if __name__ == '__main__':
    app.run(debug=True)
