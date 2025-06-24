import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

function Search() {
  const navigate = useNavigate();
  const [query, setQuery] = useState('');
  const [filters, setFilters] = useState([]);
  const [country, setCountry] = useState('');
  const [aiResponse, setAiResponse] = useState('');
  const [results] = useState([
    { id: 1, title: 'Circular Básica Jurídica CE02914', details: 'Detalles de la circular...' },
  ]);

  useEffect(() => {
    if (!localStorage.getItem('isAuthenticated')) {
      navigate('/');
    }
  }, [navigate]);

  const handleSearch = async () => {
    try {
      const response = await axios.post('http://localhost:5000/api/search', { query });
      setAiResponse(response.data.response);
    } catch (error) {
      console.error('Error al consultar el asistente de IA:', error);
      setAiResponse('Error al conectar con el asistente de IA');
    }
  };

  const handleFilterChange = (filter) => {
    setFilters((prev) =>
      prev.includes(filter) ? prev.filter((f) => f !== filter) : [...prev, filter]
    );
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <h1 className="text-xl font-bold mb-4">Buscar Normativas</h1>
      <input
        type="text"
        placeholder="¿Qué deseas encontrar hoy? Ejemplo: Normas de ciberseguridad en Colombia 2023"
        className="w-full p-2 mb-4 border rounded"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button
        onClick={handleSearch}
        className="w-full bg-blue-500 text-white p-2 rounded mb-4 hover:bg-blue-600"
      >
        Enviar
      </button>
      {aiResponse && (
        <p className="mb-4 bg-yellow-100 p-2 rounded">Asistente de IA: {aiResponse}</p>
      )}
      <select
        className="w-full p-2 mb-4 border rounded"
        value={country}
        onChange={(e) => setCountry(e.target.value)}
      >
        <option value="">País</option>
        <option value="Colombia">Colombia</option>
        <option value="Internacional">Internacional</option>
        <option value="Otros">Otros</option>
      </select>
      {results.map((result) => (
        <div
          key={result.id}
          className="bg-white p-4 rounded-lg shadow mb-4 flex justify-between items-center"
        >
          <span>{result.title}</span>
          <button
            onClick={() => alert(result.details)}
            className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
          >
            Ver Detalles
          </button>
        </div>
      ))}
      <h2 className="text-lg font-semibold mb-2">Latest News</h2>
      <label className="flex items-center mb-2">
        <input
          type="checkbox"
          checked={filters.includes('Legislación nacional')}
          onChange={() => handleFilterChange('Legislación nacional')}
        />
        <span className="ml-2">Legislación nacional sobre ciberseguridad</span>
      </label>
    </div>
  );
}

export default Search;