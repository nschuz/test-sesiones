class FileContext:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Uso del contexto para abrir y cerrar un archivo
with FileContext('archivo.txt', 'w') as file:
    file.write('Hola, mundo')
# El archivo se cierra automáticamente al salir del contexto

# Aquí el archivo ya está cerrado
