from flask import flash, send_from_directory
import os


file_origen = "data.xlsx"
file_end = "dataend.xlsx"


def allowed_file(filename, allowed_extensions={'xls', 'xlsx'}):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
