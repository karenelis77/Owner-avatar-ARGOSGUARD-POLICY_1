import { useState } from 'react';

function Assistant() {
  const [input, setInput] = useState('');
  const [respuesta, setRespuesta] = useState(null); // Cambiado a null para manejar listas

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      console.log("Enviando al servidor:", { query: input });
      const res = await fetch('http://127.0.0.1:5000/api/assistant', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: input }),
      });

      if (!res.ok) {
        throw new Error(`Error en la solicitud: ${res.status}`);
      }


      const data = await res.json();
      console.log("Respuesta:", data)
      setRespuesta(data.respuesta); // Guardar la lista de respuestas
    } catch (err) {
      console.error('Error:', err);
      setRespuesta([{ titulo: 'Error', detalle: 'No se pudo conectar con el servidor.' }]);
    }
  };

  return (
    <div>
      <h2>Asistente Inteligente</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Haz tu pregunta"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button type="submit">Enviar</button>
      </form>
      {respuesta && (
        <div style={{ marginTop: '10px' }}>
          <strong>Respuesta:</strong>
          <ul>
            {respuesta.map((item, index) => (
              <li key={index}>
                <strong>{item.titulo}</strong>: {item.detalle}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default Assistant;