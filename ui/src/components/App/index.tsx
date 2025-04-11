import { PropsWithChildren, StrictMode } from 'react'

import Header from 'components/Header';

function App() {

  const DevWrapper: React.FC<PropsWithChildren> = ({ children }) => (
    process.env.NODE_ENV === 'development' ? <StrictMode>{children}</StrictMode> : <>{children}</>
  )

  return (
    <DevWrapper>
      <div className="App">
        <Header />
      </div>
    </DevWrapper>
  );
}

export default App;
