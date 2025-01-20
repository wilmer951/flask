import os


class Config:
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    ALLOWED_EXTENSIONS = {'xls', 'xlsx'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB límite de tamaño de archivo
    SECRET_KEY = 'your_secret_key'  # Para mensajes flash
