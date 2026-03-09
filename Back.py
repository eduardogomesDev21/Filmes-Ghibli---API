from flask import Flask, jsonify
from flask_cors import CORS
import requests

import os

app = Flask(__name__)
# Habilita CORS para permitir que o Front.html faça requisições para este servidor
CORS(app)

# Diretório base
BASE_DIR = os.path.dirname(os.path.abspath(__name__))

# Nota importante: A API original (ghibliapi.herokuapp.com) foi descontinuada.
# Esta é a URL substituta oficial da mesma API.
GHIBLI_API_URL = "https://ghibliapi.vercel.app/films"

@app.route('/')
def index():
    # Serve o arquivo HTML diretamente do mesmo diretório
    with open(os.path.join(BASE_DIR, 'Front.html'), 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/api/filmes', methods=['GET'])
def get_filmes():
    try:
        # Fazendo a requisição da API externa pelo backend
        response = requests.get(GHIBLI_API_URL, timeout=10)
        response.raise_for_status()
        filmes = response.json()
        
        # O backend repassa os filmes como JSON para o frontend
        return jsonify(filmes)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar os filmes: {e}")
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    print("="*50)
    print(" Servidor do Studio Ghibli rodando! ")
    print("="*50)
    print(" Acesse o site no seu navegador pelo link abaixo:")
    print(" http://127.0.0.1:5000")
    print("="*50)
    app.run(debug=True, port=5000)
