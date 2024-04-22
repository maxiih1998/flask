from flask import Flask, render_template, request
import os
from docx import Document

app = Flask(__name__)

# Lista de empresas
empresas = [
    "Hogar de Cristo",
    "Canal 13",
    "Desafio Levantemos Chile",
    "Zapping",
    "AMSA",
    "DRS",
    "Transearch",
    "AquaChile",
    "Total Energies",
    "Codelco",
]

@app.route('/', methods=['GET', 'POST'])
def index():
    mensaje = None
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        
        file = request.files['file']
        
        if file.filename == '':
            return 'No selected file'
        
        if file:
            # Leer el contenido del archivo de Word
            doc = Document(file)
            content = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
            
            # Verificar si alguna empresa aparece en el contenido del archivo
            empresa_encontrada = None
            for empresa in empresas:
                if empresa in content:
                    empresa_encontrada = empresa
                    break
            
            # Generar el texto de respuesta
            if empresa_encontrada:
                mensaje = f"La empresa asociada a la denuncia es {empresa_encontrada}"
            else:
                mensaje = "La empresa asociada a la denuncia es Otros"
            
    return render_template('index.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)
