from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain.llms import OpenAI

app = Flask(__name__)
CORS(app)

llm = OpenAI(api_key="tu_api_key_aquí")  # Reemplaza con tu API key de OpenAI

@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query', '')
    try:
        response = llm(f"Busca normativas relacionadas con: {query}")
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(port=5000)