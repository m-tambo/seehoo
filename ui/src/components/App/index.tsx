import { Outlet } from 'react-router';

import Header from 'components/Header';

const App = () => (
  <body>
    <Header />
    <main>
      <Outlet />
    </main>
  </body>
)

export default App
