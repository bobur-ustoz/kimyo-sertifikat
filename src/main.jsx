import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import Admin from './Admin.jsx'
import RecoveryGate from './RecoveryGate.jsx'
import XatoChegara from './XatoChegara.jsx'
import { xatoKuzat } from './lib/xato.js'

xatoKuzat()

const screen = window.location.pathname.startsWith('/admin') ? <Admin/> : <App/>

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <XatoChegara><RecoveryGate>{screen}</RecoveryGate></XatoChegara>
  </StrictMode>,
)
