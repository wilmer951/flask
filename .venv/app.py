import os
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



# Ruta para la página de subir archivo
@app.route('/uploadfile', methods=['GET', 'POST'])
def uploadfile():

 
    if request.method == 'POST':
    


        folder_path = app.config['UPLOAD_FOLDER']
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
                flash('No hay archivos a procesar!')
                
                return redirect(request.url)






        file = request.files['file']
                
        

                # Si el archivo es válido
        if file and allowed_file(file.filename):
                    # Guardar el archivo en la carpeta de uploads
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            flash(f'Archivo "{file.filename}" cargado exitosamente!')
            return redirect(request.url)
        

        else:
            flash('Solo se permite archivos, xls, xlsx')
            return redirect(request.url)
        



    return render_template("uploadfile.html")

if __name__ == "__main__":
    app.run(debug=True)
