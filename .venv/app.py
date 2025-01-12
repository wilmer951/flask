import os
import pandas as pd
from openpyxl import load_workbook


from flask import Flask, request, render_template, flash, redirect, url_for,send_from_directory

app = Flask(__name__)
app.jinja_env.cache = {}

# Configuración para la carpeta de carga
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
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

    status=0
 
    if request.method == 'POST':
    



        






        file = request.files['file']
                
        

                # Si el archivo es válido
        if file and allowed_file(file.filename):
                    # Guardar el archivo en la carpeta de uploads
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], "data.xlsx")
            file.save(filepath)
            flash(f'Archivo "{file.filename}" cargado exitosamente!')

            status=1
            return render_template("integration.html", stcarga=status)
          

        else:
            flash('Solo se permite archivos, xls, xlsx')
            status=0
            return render_template("integration.html", stcarga=status)
        

    







@app.route('/analystfile', methods=['GET', 'POST'])
def analystfile():

    status=0
 
    if request.method == 'POST':

        data_file=os.path.join(app.config['UPLOAD_FOLDER'], "data.xlsx")
    
        # Abrir el archivo de Excel con openpyxl
        wb = load_workbook(data_file)
        ws = wb.active

        # Obtener las filas visibles (comprobando si están ocultas por el filtro)
        visible_rows = []
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
            if not ws.row_dimensions[row[0].row].hidden:  # Si la fila no está oculta
                visible_rows.append([cell.value for cell in row])

        # Crear un DataFrame con las filas visibles
        columns = [cell.value for cell in ws[1]]
        df_visible = pd.DataFrame(visible_rows, columns=columns)

        # Asignar las columnas 'HOMBRE' y 'MUJER'
        df_visible['HOMBRE'] = ''
        df_visible['MUJER'] = ''

        df_visible['CONTRIBUTIVO'] = ''
        df_visible['SUBSIDIADO'] = ''

        df_visible['CATEGORIA'] = ''
        df_visible['SINCATEGORIA'] = ''


        # Asegurarse de que no haya espacios en blanco ni diferencias de mayúsculas/minúsculas
        df_visible['VICTIMA DE CONFLICTO'] = df_visible['VICTIMA DE CONFLICTO'].str.strip(
        ).str.upper()
        df_visible['MIGRANTE'] = df_visible['MIGRANTE'].str.strip().str.upper()
        df_visible['CARCELARIO'] = df_visible['CARCELARIO'].str.strip().str.upper()
        df_visible['EN ESTADO DE GESTACION'] = df_visible['EN ESTADO DE GESTACION'].str.strip(
        ).str.upper()
        df_visible['OTRO'] = df_visible['OTRO'].str.strip().str.upper()
        df_visible['DESPLAZADO'] = df_visible['DESPLAZADO'].str.strip().str.upper()


        # Asignar la edad a 'hombres' si el sexo es 'M' (masculino), o a 'mujeres' si el sexo es 'F' (femenino)
        df_visible.loc[df_visible['SEXO'] == 'M',
                    'HOMBRE'] = df_visible['EDAD'].astype(int)
        df_visible.loc[df_visible['SEXO'] == 'F',
                    'MUJER'] = df_visible['EDAD'].astype(int)

        df_visible.loc[df_visible['REGIMEN'] == 'Contributivo', 'CONTRIBUTIVO'] = 'X'
        df_visible.loc[df_visible['REGIMEN'] == 'Subsidiado', 'SUBSIDIADO'] = 'X'

        for index, row in df_visible.iterrows():
            if (row['VICTIMA DE CONFLICTO'] == 'SI' or
                row['MIGRANTE'] == 'SI' or
                row['CARCELARIO'] == 'SI' or
                row['EN ESTADO DE GESTACION'] == 'SI' or
                row['OTRO'] == 'SI' or
                    row['DESPLAZADO'] == 'SI'):
                df_visible.at[index, 'CATEGORIA'] = 'X'

            else:
                df_visible.at[index, 'SINCATEGORIA'] = 'X'


        # Obtener la fecha y hora actual en formato 'YYYYMMDD_HHMMSS'


        # Guardar el DataFrame modificado en un nuevo archivo de Excel
    
 
        output_file = os.path.join(app.config['UPLOAD_FOLDER'], "datamodficado.xlsx")
        


        df_visible.to_excel(output_file, index=False)
        
        status=1
    


       

        return render_template("integration.html",stdf=status)



@app.route('/downloaderfile', methods=['POST'])
def downloaderfile():
    
    if request.method == 'POST':
        file_name = "datamodficado.xlsx"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)

        # Verificar si el archivo existe
        if os.path.exists(file_path):
            return send_from_directory(app.config['UPLOAD_FOLDER'], file_name, as_attachment=True)
        else:
            return f"Archivo no encontrado: {file_path}", 404
            
        


if __name__ == "__main__":
    app.run(debug=False)
