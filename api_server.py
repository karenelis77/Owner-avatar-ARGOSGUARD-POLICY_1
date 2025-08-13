<<<<<<< HEAD
import sqlite3
from typing import List, Tuple, Dict, Any
=======
>>>>>>> 068294a (Actualización del README y manual)
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
<<<<<<< HEAD
CORS(app)  # Permitir solicitudes desde el frontend

def get_db_connection() -> sqlite3.Connection:
    """Connect to the SQLite database."""
    try:
        conn = sqlite3.connect('policies.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        raise RuntimeError(f"Database connection failed: {e}")

# Initialize the database
def init_db() -> None:
    """Initialize the database with users and policies tables."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS policies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT
            )
        ''')
        # Insert a default user for testing
        cursor.execute(
            'INSERT OR IGNORE INTO users (email, password) VALUES (?, ?)',
            ('admin@example.com', 'password123')
        )
        conn.commit()

@app.route('/api/login', methods=['POST'])
def login() -> Dict[str, Any]:
    """Handle user login."""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM users WHERE email = ? AND password = ?',
            (email, password)
        )
        user = cursor.fetchone()

    if user:
        return jsonify({'success': True})
    return jsonify({'success': False}), 401

@app.route('/api/policies', methods=['GET'])
def get_policies() -> List[Dict[str, Any]]:
    """Retrieve all policies."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM policies')
        policies = cursor.fetchall()
    return jsonify([dict(policy) for policy in policies])

@app.route('/api/policies', methods=['POST'])
def create_policy() -> Dict[str, Any]:
    """Create a new policy."""
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO policies (name, description) VALUES (?, ?)',
            (name, description)
        )
        conn.commit()
        policy_id = cursor.lastrowid
    return jsonify({'id': policy_id, 'name': name, 'description': description}), 201

@app.route('/api/policies/<int:id>', methods=['PUT'])
def update_policy(id: int) -> Dict[str, Any]:
    """Update a policy by ID."""
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE policies SET name = ?, description = ? WHERE id = ?',
            (name, description, id)
        )
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Policy not found'}), 404
    return jsonify({'id': id, 'name': name, 'description': description})

@app.route('/api/policies/<int:id>', methods=['DELETE'])
def delete_policy(id: int) -> Dict[str, Any]:
    """Delete a policy by ID."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM policies WHERE id = ?', (id,))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Policy not found'}), 404
    return jsonify({'message': 'Policy deleted'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
=======
# Configura CORS para permitir solicitudes desde http://localhost:5173
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5173"]}}, supports_credentials=True)

@app.route('/api/assistant', methods=['POST'])
def assistant():
    data = request.get_json()
    print("Consulta recibida:", data)
    query = data.get('query', '').lower()  # Usar 'query' en lugar de 'pregunta'

    # Lista de respuestas (puedes modificarla para procesar 'query')
    respuestas = [
        {"titulo": "Política Nacional de Seguridad Digital", "detalle": "Ver Detalles"},
        {"titulo": "Ley de Protección de Datos (Habeas Data)", "detalle": "Ver Detalles"},
    ]

    # Devolver la lista de respuestas
    return jsonify({"respuesta": respuestas})

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
>>>>>>> 068294a (Actualización del README y manual)
