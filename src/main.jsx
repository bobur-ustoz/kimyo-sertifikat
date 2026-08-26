import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import Admin from './Admin.jsx'
import RecoveryGate from './RecoveryGate.jsx'

const screen = window.location.pathname.startsWith('/admin') ? <Admin/> : <App/>

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RecoveryGate>{screen}</RecoveryGate>
  </StrictMode>,
)
