import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function Dashboard() {
  const navigate = useNavigate();

  useEffect(() => {
    if (!localStorage.getItem('isAuthenticated')) {
      navigate('/');
    }
  }, [navigate]);

  const normativas = [
    { id: 1, title: 'Circular Básica Jurídica CE02914', details: 'Detalles de la circular...' },
    { id: 2, title: 'Ley 1273 de 2009', details: 'Detalles de la ley...' },
  ];

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <h1 className="text-xl font-bold mb-4">ArgosGuardPolicy - Panel Principal</h1>
      <p className="mb-4">Bienvenido, Aleja Ruiz</p>
      <div className="space-y-4">
        {normativas.map((normativa) => (
          <div
            key={normativa.id}
            className="bg-white p-4 rounded-lg shadow flex justify-between items-center"
          >
            <span>{normativa.title}</span>
            <button
              onClick={() => alert(normativa.details)}
              className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
            >
              Ver Detalles
            </button>
          </div>
        ))}
        <p>3 nuevas normativas esta semana</p>
      </div>
      <button
        onClick={() => navigate('/search')}
        className="mt-4 bg-gray-500 text-white p-2 rounded hover:bg-gray-600"
      >
        Ir a Búsqueda
      </button>
    </div>
  );
}

export default Dashboard;