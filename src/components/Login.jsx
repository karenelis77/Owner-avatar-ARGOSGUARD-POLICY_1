import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      if (!response.ok) {
        throw new Error('Invalid email or password');
      }

      const data = await response.json();
      if (data.success) {
        navigate('/dashboard');
      } else {
        setError('Login failed. Please try again.');
      }
    } catch (err) {
      setError(err.message);
    }
  };

  const handleHelp = () => {
    alert('Para ayuda, contacta a soporte: soporte@argosguardpolicy.com');
  };

  const handleClose = () => {
    if (window.confirm('¿Estás seguro de que quieres cerrar la aplicación?')) {
      window.close();
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 relative">
      <div className="absolute top-4 right-4 flex gap-2">
        <button
          onClick={handleHelp}
          className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition duration-200"
        >
          Ayuda
        </button>
        <button
          onClick={handleClose}
          className="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600 transition duration-200"
        >
          Cerrar
        </button>
      </div>

      <div className="bg-white p-8 rounded-lg shadow-lg w-full max-w-sm">
        <div className="flex justify-center mb-6">
          <img
            src="/LOGO/LOGO.png" // Ruta al logo en public/LOGO
            alt="ArgoSGuardPolicy Logo"
            className="w-32 h-32"
          />
        </div>
        <h2 className="text-2xl font-bold text-center mb-4">Argosguardpolicy</h2>
        <h3 className="text-xl font-semibold text-center mb-6">Sign In</h3>
        {error && <p className="text-red-500 text-center mb-4">{error}</p>}
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="email" className="block text-gray-700 mb-2">
              Email
            </label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full p-3 rounded bg-green-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-green-500"
              required
            />
          </div>
          <div className="mb-6">
            <label htmlFor="password" className="block text-gray-700 mb-2">
              Password
            </label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full p-3 rounded bg-green-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-green-500"
              required
            />
          </div>
          <button
            type="submit"
            className="w-full p-3 bg-gray-500 text-white rounded hover:bg-gray-600 transition duration-200"
          >
            Sign in
          </button>
        </form>
        <div className="flex justify-between mt-4 text-sm">
          <a href="/forgot-password" className="text-gray-500 hover:underline">
            Forget password
          </a>
          <a href="/signup" className="text-gray-500 hover:underline">
            Sign up
          </a>
        </div>
      </div>
    </div>
  );
}

export default Login;