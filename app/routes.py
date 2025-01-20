# app/routes.py
from flask import request, render_template,redirect,url_for,jsonify
from app import app

from modules.upload import handle_file_upload
from modules.analytic import analytic_data
from modules.downloader import downloader_file
from modules.clearfile import clear_file

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/integration', methods=['GET', 'POST'])
def integration():
    stcarga = request.args.get('stcarga')  # Recupera el parámetro de la URL
    return render_template("integration.html", stcarga=stcarga)


@app.route('/upload', methods=['GET', 'POST'])
def uploadfile():

    status=0

    if request.method == 'POST':
        status = handle_file_upload(request)

        response = {
            "status": status,
            "message": "Archivo cargado correctamente" if status == 1 else "Error en la carga del archivo"
        }

        return jsonify(response)
    
    else:
         return redirect(url_for('integration'))
    



@app.route('/analytic', methods=['GET', 'POST'])
def analystfile():

    status=0
    if request.method == 'POST':
        status = analytic_data(request)
        
        response = {
            "status": status,
            "message": "Archivo analizado exitosamente"
        }

        return jsonify(response)
    
    else:
    
        return render_template("home.html")




@app.route('/downloader',methods=['GET', 'POST'])
def downloaderfile():

    if request.method == 'POST':

        status = downloader_file(request)

        return status
    
    else:
    
        return render_template("home.html")
    






@app.route('/clearfile', methods=['GET', 'POST'])
def clearfile():

    if request.method == 'POST':

        status = clear_file(request)

        return render_template("integration.html")
    
    else:
    
        return render_template("home.html")






