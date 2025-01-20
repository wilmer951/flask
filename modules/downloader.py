from app import app
from flask import flash,send_from_directory
import os
from app.utils import file_end



def downloader_file(request):

    status=0
    

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_end)

        # Verificar si el archivo existe
    if os.path.exists(file_path):

        
            # Enviamos el archivo para su descarga
        
        return send_from_directory(app.config['UPLOAD_FOLDER'], file_end, as_attachment=True)

    else:
        flash('Se presento un error comuniquese con su administrador ')
            
        return status
    


    