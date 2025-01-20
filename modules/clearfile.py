    
from app import app
import os
from flask import flash
from app.utils import file_origen,file_end


def clear_file(request):
    
    status=0
    
    files_to_remove = [file_origen, file_end]
    upload_folder = app.config['UPLOAD_FOLDER']
    files_deleted = False  # Flag para saber si se eliminaron archivos

    for file_name in files_to_remove:
        output_file = os.path.join(upload_folder, file_name)
        if os.path.exists(output_file):
            os.remove(output_file)
            files_deleted = True  # Marcar que al menos un archivo fue eliminado

        if files_deleted:
            # Solo mostrar este mensaje si se eliminaron archivos
            flash('Limpieza exitosa.')
            status=1

            

    flash('No hay datos que limpiar.')

                
            
        
    return status

    

    
