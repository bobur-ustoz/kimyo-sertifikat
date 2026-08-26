import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import Admin from './Admin.jsx'
import ResetPassword, { RESET_PATH } from './ResetPassword.jsx'

const path = window.location.pathname

const screen =
  path.startsWith(RESET_PATH) ? <ResetPassword/> :
  path.startsWith('/admin')   ? <Admin/> :
                                <App/>

createRoot(document.getElementById('root')).render(
  <StrictMode>{screen}</StrictMode>,
)
