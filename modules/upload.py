import os
from flask import flash
from app import app  # Importar la instancia de app correctamente
from app.utils import allowed_file, file_origen

def handle_file_upload(request):
    status = 0
    file = request.files['file']
    if file and allowed_file(file.filename):
        # Aquí se usa la configuración UPLOAD_FOLDER de app.config
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file_origen)
        file.save(filepath)
        status = 1
        return status
    else:
        
        return status