import os
import pandas as pd
from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)
app.jinja_env.cache = {}

# Configuración para la carpeta de carga
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'xls', 'xlsx'}
app.secret_key = 'your_secret_key'  # Para mensajes flash



# Ruta para la página de inicio
@app.route('/')
def home():


    return render_template("home.html")



# Función para verificar si el archivo tiene una extensión permitida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']



# Ruta para la página integracion
@app.route('/integration', methods=['GET', 'POST'])
def integration():
    return render_template("integration.html")

# Ruta para la página de subir archivo
@app.route('/uploadfile', methods=['GET', 'POST'])
def uploadfile():


 
    if request.method == 'POST':
    



        






        file = request.files['file']
                
        

                # Si el archivo es válido
        if file and allowed_file(file.filename):
                    # Guardar el archivo en la carpeta de uploads
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], "data.xmls")
            file.save(filepath)
            flash(f'Archivo "{file.filename}" cargado exitosamente!')
            return redirect(request.url)
        

        else:
            flash('Solo se permite archivos, xls, xlsx')
            return redirect(request.url)
        



    return render_template("integration.html")





@app.route('/analystfile', methods=['GET', 'POST'])
def analystfile():


 
    if request.method == 'POST':
    
        print("analisis realizado")


        data_clientes = os.path.join(app.config['UPLOAD_FOLDER'], "data.xmls")


        df = pd.read_excel(data_clientes)


        print(df)


        return render_template("integration.html")







if __name__ == "__main__":
    app.run(debug=False)
