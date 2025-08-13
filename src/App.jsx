import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import Search from './components/Search';

import Assistant from './components/Assistant';

function App() {
  return (
    <div>
      <h1>Bienvenida Karen 👋</h1>
      <Assistant />
    </div>
  );
}

export default App;