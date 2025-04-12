import { Link } from 'react-router'

import Logo from 'components/Logo'

const Header = () => (
  <header>
    <Link to="/">
      <Logo />
    </Link>
  </header>
)

export default Header 
