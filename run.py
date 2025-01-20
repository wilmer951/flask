from app import app  # Importa la app desde __init__.py

if __name__ == "__main__":
    app.run(debug=True)  # Llama a run sobre la instancia app, no el módulo
