import { PropsWithChildren, StrictMode } from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter } from 'react-router'

import Routes from 'routes'
import './index.scss'

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

const DevWrapper: React.FC<PropsWithChildren> = ({ children }) => (
  process.env.NODE_ENV === 'development' ? <StrictMode>{children}</StrictMode> : <>{children}</>
)

root.render(
  <DevWrapper>
    <BrowserRouter>
      <Routes />
    </BrowserRouter>
  </DevWrapper>
)
